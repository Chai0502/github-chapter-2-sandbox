import imageio.v3 as iio
from PIL import Image
import numpy as np

filenames = ['SkyHigh_198.jpg', 'SkyHigh_199.jpg', 'SkyHigh_200.jpg', 
             'SkyHigh_201.jpg', 'SkyHigh_203.jpg', 'SkyHigh_204.jpg']

# Step 1: Get target size from the first image
first_image = Image.open(filenames[0])
target_size = first_image.size  

# Step 2: Resize and convert all images to numpy arrays
images = []
for filename in filenames:
    img = Image.open(filename).resize(target_size)
    images.append(np.array(img))  

# Step 3: Save as a GIF
iio.imwrite('Frisbee.gif', images, duration=500, loop=0)