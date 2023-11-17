# Description: Generate a dataset of simple grayscale rectangles

# Import the necessary libraries
import random
from PIL import Image, ImageDraw
import pandas as pd

# Set the size of the image
width = 20
height = 20

# Create a list to store the coordinates and the pixel values of the rectangles
coordinates = [] # This will store 4 coordinates for each rectangle
pixels = [] # This will store 50x50 = 2500 pixels
pixels_all = [] # This will store all the pixels for all the images

# Generate 100 images
for i in range(100):
    # Create a new image
    image = Image.new("RGB", (width, height))

    # Set the rectangle's color
    rect_gray = random.randint(0,255)
    rect_color = (rect_gray, rect_gray, rect_gray)

    # Set the background color
    bg_gray = random.randint(rect_gray, 255)
    bg_color = (bg_gray, bg_gray, bg_gray)

    # Set the coordinates of the rectangle
    x1 = random.randint(0, width)
    y1 = random.randint(0, height)
    x2 = random.randint(0, width)
    y2 = random.randint(0, height)

    # Save the coordinates of the rectangle
    coordinates.append([x1, y1, x2, y2])

    # Set the image pixels
    for y in range(height):  
        for x in range(width):
            if x >= x1 and x <= x2 and y >= y1 and y <= y2:
                image.putpixel((x, y), rect_color)
                pixels.append(rect_gray)
            else:
                image.putpixel((x, y), bg_color)
                pixels.append(bg_gray)
        pixels_all.append(coordinates[i])
        pixels = [] # Reset the pixels list

    # Create a new drawing object
    draw = ImageDraw.Draw(image)

    # Save the image with a different filename for each image
    image.save(f"dataset_img/simple_rectangle_sample_{i}.png")

# Print the x1 coordinates of the rectangles
print(coordinates[:][0])


# Create a dictionary to store the pixel values and the coordinates
dataset_dict = {'x1': coordinates[:][0], 'y1': coordinates[:][0], 'x2': coordinates[:][2], 'y2': coordinates[:][3], 'pixelVals': pixels_all}




# Save the coordinates of the rectangles in a csv file
#pd.DataFrame(dataset_dict).to_csv('dataset.csv', index=False)

# Print a message to indicate that the dataset was generated successfully
print("Dataset generated successfully!")
