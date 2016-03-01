
## Filter response
filter response for texture classification

___
The code is designed for texture classification of clothing.

#####The repository contains:

1. an image file im.npy of a woman wearing a dress

2. a mask file mask.npy - 2d array of the labels for the different items of cloth

3. main code: MR8filterresponse.py
 - input: loads an image and mask
 - output: spatially averaged "MR8" filter responses, for a given sample size, from a given clothing label.
          and ravelled to give a 1-d final vector.

4. code for the filters

5. code for parsing the largest inscribed rectangle from the desired item label


