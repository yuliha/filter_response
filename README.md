
## filter response
filter response for texture classification


The code is designed for texture classification of clothing.

##The repository contains:

1- an image file im.npy of a woman

2- a mask file mask.npy - 2d array of the labels for the different items of cloth

3- main code: MR8filterresponse.py

  input: image and mask
  
  output: specially averaged "MR8" responses, for a given sample size, from a given clothing label.
          and ravelled to give a 1-d final vector.

4- code for the filters

5- code for parsing the largest inscribed rectangle from the desired item label


