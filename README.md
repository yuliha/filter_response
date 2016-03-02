
## Filter response
filter response for texture classification

___
The code is designed for texture classification of clothing.

#####The repository contains:

1. main code: MR8filterresponse.py
 - input: loads an image and mask
 - output: MR8 filter responses for a given sampled square size, from a given clothing label. spatially averaged
          and ravelled to give a 1d final vector.

2. code for the filters

3. code for parsing the largest inscribed rectangle from the desired item label

4. an image file im.npy of a woman wearing a dress

5. a mask file mask.npy - 2d array of the labels for the different items of cloth


