import cv2
import numpy as np

################################################################
#Gray Scale Image

image = cv2.imread('image.png')

height, width, other_dimension = image.shape

grayscale_image = 255 * np.ones((height, width), dtype=int)

for y in range(0, height):
    for x in range(0, width):
        blue, green, red = image[y, x]
        grayscale_image[y, x] = int(0.299 * red + 0.587 * green + 0.114 * blue)

cv2.imwrite('gray image.png', grayscale_image)

################################################################
#Gray Scale Image Scaled

height, width = grayscale_image.shape
new_height = int(height / 2)
new_width = int(width / 2)

scaled_image = np.zeros((new_height, new_width), dtype=np.uint8)

for i in range(0, new_height):
    for j in range(0, new_width):
        scaled_image[i, j] = grayscale_image[i * 2, j * 2]

cv2.imwrite("gray image scaled.png", scaled_image)

################################################################
#Gray Scale Image Translated

height, width = grayscale_image.shape
   
translated_image = np.zeros((height, width), dtype=np.uint8)

for y in range(height):
    for x in range(width):
        if 0 <= x + 50 < width and 0 <= y + 50 < height:
            translated_image[y+50, x+50] = grayscale_image[y, x]

cv2.imwrite("gray image translated.png", translated_image)

################################################################
#Gray Scale Image Flip Horizontal

height, width = grayscale_image.shape
   
flip_image = np.zeros((height, width), dtype=np.uint8)

for y in range(height):
    for x in range(width):
        flip_image[y, width-x-1] = grayscale_image[y, x]

cv2.imwrite("gray image flip horizontal.png", flip_image)

################################################################
#Gray Scale Image Flip Vertical

height, width = grayscale_image.shape
   
flip_image = np.zeros((height, width), dtype=np.uint8)

for y in range(height):
    for x in range(width):
        flip_image[height-y-1, x] = grayscale_image[y, x]

cv2.imwrite("gray image flip vertical.png", flip_image)

################################################################
#Gray Scale Image Invert

height, width = grayscale_image.shape
   
invert_image = np.zeros((height, width), dtype=np.uint8)

for y in range(height):
    for x in range(width):
        invert_image[y, x] = 255 - grayscale_image[y, x]

cv2.imwrite("gray image inversion.png", invert_image)

################################################################
#Gray Scale Image Rotate 45

rotate_45 = np.zeros_like(grayscale_image)
h, w = grayscale_image.shape

def center_rotate_45(x, y, new_x, new_y):
    x2 = int((x - new_x) * np.cos(np.deg2rad(-45))
                 - 
                 (y - new_y) * np.sin(np.deg2rad(-45)) + new_x)
        
    y2 = int((x - new_x) * np.sin(np.deg2rad(-45)) 
                 + 
                 (y - new_y) * np.cos(np.deg2rad(-45)) + new_y)
    return (x2, y2)

new_x = w // 2
new_y = h // 2

for y in range(h):
    for x in range(w):
        x2, y2 = center_rotate_45(x, y, new_x, new_y)
        if (0 <= x2 < w) and (0 <= y2 < h):
            rotate_45[y, x] = grayscale_image[y2, x2]

cv2.imwrite('gray image rotated.png', rotate_45)

################################################################
#Image Scale (Bonus)

height, width, breadth = image.shape
new_height = int(height / 2)
new_width = int(width / 2)

scaled_image = np.zeros((new_height, new_width, breadth), dtype=np.uint8)

for i in range(0, new_height):
    for j in range(0, new_width):
        for k in range(0, breadth):
            scaled_image[i, j, k] = image[i * 2, j * 2, k]

cv2.imwrite("image scaled.png", scaled_image)

################################################################
#Image Translate (Bonus)

height, width, breadth = image.shape
   
translated_image = np.zeros((height, width, breadth), dtype=np.uint8)

for y in range(height):
    for x in range(width):
        for k in range(breadth):
            if 0 <= x + 50 < width and 0 <= y + 50 < height:
                translated_image[y+50, x+50, k] = image[y, x, k]

cv2.imwrite("image translated.png", translated_image)

################################################################
#Image Flip Horizontal (Bonus)

height, width, breadth = image.shape
   
flip_image = np.zeros((height, width, breadth), dtype=np.uint8)

for y in range(height):
    for x in range(width):
        for k in range(breadth):
            flip_image[y, width-x-1, k] = image[y, x, k]

cv2.imwrite("image flip horizontal.png", flip_image)

################################################################
#Image Flip Vertical (Bonus)

height, width, breadth = image.shape
   
flip_image = np.zeros((height, width, breadth), dtype=np.uint8)

for y in range(height):
    for x in range(width):
        for k in range(breadth):
            flip_image[height - y - 1, x, k] = image[y, x, k]

cv2.imwrite("image flip vertical.png", flip_image)