__author__ = 'yuli'

import numpy
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def largest_insc_rect(mask, label):
    # The function returns max_area inscribed in label
    # area_max[0]= maximum area
    # area_max[1] = 2 coords: (top, left, right, bottom)

    nrows = mask.shape[0]
    ncols = mask.shape[1]

    area_max = (0, [])

    #a = numpy.fromstring(s, dtype=int, sep=' ').reshape(nrows, ncols)
    w = numpy.zeros(dtype=int, shape=mask.shape)
    h = numpy.zeros(dtype=int, shape=mask.shape)
    for r in range(nrows):
        for c in range(ncols):
            if mask[r][c] != label:
                continue
            if r == label:
                h[r][c] = 1
            else:
                h[r][c] = h[r-1][c]+1
            if c == label:
                w[r][c] = 1
            else:
                w[r][c] = w[r][c-1]+1
            minw = w[r][c]
            for dh in range(h[r][c]):
                minw = min(minw, w[r-dh][c])
                area = (dh+1)*minw
                if area > area_max[0]:
                    area_max = (area, [(r-dh, c-minw+1, r, c)])
            y0, x0, H, W = (r-dh), (c-minw+1), dh, (minw-1)
    print 'max area: ', area_max[0]
    return area_max

def show_insc_rect():
    mask = numpy.load("/home/omer/core/largest_ins_rect/mask.npy")
    max_area = largest_insc_rect(mask, label=8)
    max_area_coord =  max_area[1][0]

    fig = plt.figure()
    plt.imshow(mask)
    currentAxis = plt.gca()
     # Rectangle(top, left, w, h)     x ,y , w, h
    currentAxis.add_patch(Rectangle((max_area_coord[1]- .5,  max_area_coord[0] - .5),
                                    max_area_coord[3]-max_area_coord[1], max_area_coord[2]-max_area_coord[0], facecolor="none"))
    plt.show()


if __name__ == "__main__":

    # EXAMPLE USAGE:
    show_insc_rect()


