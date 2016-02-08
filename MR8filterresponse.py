__author__ = 'yuli'

import cv2
import numpy as np
import pickle
import matplotlib.pyplot as plt


def trimm_img(image, mask, label):
    # mask - mask to trimm
    # label - the inscribed rectangle should be taken from this label
    import inscribed_rect

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    coord = inscribed_rect.largest_insc_rect(mask, label)[1][0]
    trimmed_img = gray_image[coord[0]:coord[2], coord[1]:coord[3]]
    #fig = plt.figure()
    #plt.imshow(trimmed_img)
    #plt.show()
    return trimmed_img



def MR8response(trimmed , size):
    from itertools import product, chain
    import MR8filters

    centy = trimmed.shape[0]/2 ; centx = trimmed.shape[1]/2
    sample = trimmed[ centy-size/2:centy+size/2, centx-size/2:centx+size/2]
    print "sample shape= ", sample.shape

    # Make MR8 filters
    edge, bar, rot = MR8filters.makeRFSfilters()
    sample = sample.astype(np.float)

    # Normalize sample
    sample = (sample - np.mean(sample))/np.std(sample)

    # apply filters
    filterbank = chain(edge, bar, rot)
    n_filters = len(edge) + len(bar) + len(rot)
    response = MR8filters.apply_filterbank(sample, filterbank)


    # plot filters
    n_sigmas = 3
    n_orientations = 6
    # 2 is for bar / edge, + 1 for rot
    fig, ax = plt.subplots(n_sigmas * 2 + 1, n_orientations)
    for k, filters in enumerate([bar, edge]):
        for i, j in product(xrange(n_sigmas), xrange(n_orientations)):
            row = i + k * n_sigmas
            ax[row, j].imshow(filters[i, j, :, :], cmap=plt.cm.gray)
            ax[row, j].set_xticks(())
            ax[row, j].set_yticks(())
    ax[-1, 0].imshow(rot[0, 0], cmap=plt.cm.gray)
    ax[-1, 0].set_xticks(())
    ax[-1, 0].set_yticks(())
    ax[-1, 1].imshow(rot[1, 0], cmap=plt.cm.gray)
    ax[-1, 1].set_xticks(())
    ax[-1, 1].set_yticks(())
    for i in xrange(2, n_orientations):
        ax[-1, i].set_visible(False)


   # plot responses
    fig2, ax2 = plt.subplots(3, 3)
    for axes, res in zip(ax2.ravel(), response):
        axes.imshow(res, cmap=plt.cm.gray)
        axes.set_xticks(())
        axes.set_yticks(())
    plt.subplot(3, 3, 9)
    plt.imshow(sample, cmap=plt.cm.gray)
    #plt.savefig(path+'MR8'+name)
    #plt.format_coord = format_coord
    ax2[-1, -1].set_visible(False)
#    plt.show()

    return response

def blockshaped(arr, nrows, ncols):
    """
    Return an array of shape (n, nrows, ncols) where
    n * nrows * ncols = arr.size

    If arr is a 2D array, the returned array should look like n subblocks with
    each subblock preserving the "physical" layout of arr.
    """
    h, w = arr.shape
    return (arr.reshape(h//nrows, nrows, -1, ncols)
               .swapaxes(1,2)
               .reshape(-1, nrows, ncols))


def mean_std_pooling(response, s):
    # response dimentions should be mod(s)
    block_shaped = blockshaped(response, s, s)
    print "block_shaped shape: ", block_shaped.shape
    result = np.asarray(())
    for block in block_shaped:
        result= np.concatenate(( result, np.asarray([np.mean(block)]) ))
        result= np.concatenate(( result, np.asarray([np.std(block)]) ))
        if np.isnan(np.mean(block)) == True:
            print 'mean isNaN !!'
        if np.isnan(np.std(block)) == True:
            print 'std isNaN !!'
    return result


if __name__ == "__main__":

    samp_size = 42
    img = np.load("im.npy")
    mask = np.load("mask.npy")
    label = 8
    s = 6

    trimmed_img = trimm_img(img, mask, label)

    response = MR8response(trimmed_img, samp_size )
    ms_response = np.asarray(())
    for val in response:
        ms_response = np.concatenate((ms_response, mean_std_pooling(val, s)))

    np.save('MR8response.npy', ms_response)










