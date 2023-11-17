# Description: Generate a dataset of simple grayscale rectangles

# Import the necessary libraries
import random
from PIL import Image, ImageDraw
import pandas as pd

# Set the size of the image
width = 20
height = 20

# Create a list to store the coordinates and the pixel values of the rectangles
dataset = [] # Store the coordinates and the pixel values of the rectangles for each image
dataset_all = [] # Store the coordinates and the pixel values of the rectangles for all images


# Generate 100 images
for i in range(1000):
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
    x2 = random.randint(x1, width)
    y2 = random.randint(y1, height)

    # Save the coordinates of the rectangle
    dataset.append(x1)
    dataset.append(y1)
    dataset.append(x2)
    dataset.append(y2)

    # Set the image pixels
    for y in range(height):  
        for x in range(width):
            if x >= x1 and x <= x2 and y >= y1 and y <= y2:
                image.putpixel((x, y), rect_color)
                dataset.append(rect_gray)
            else:
                image.putpixel((x, y), bg_color)
                dataset.append(bg_gray)

    dataset_all.append(dataset) # Save the dataset for this image
    dataset = [] # Reset the dataset list

    # Create a new drawing object
    draw = ImageDraw.Draw(image)

    # Save the image with a different filename for each image
    image.save(f"dataset_img/simple_rectangle_sample_{i}.png")


# Save the coordinates of the rectangles in a csv file
pd.DataFrame(dataset_all).to_csv('dataset.csv', index=False)

# Print a message to indicate that the dataset was generated successfully
print("Dataset generated successfully!")
