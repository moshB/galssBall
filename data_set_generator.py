import math

import cv2
import numpy as np
import matplotlib
import os
import matplotlib.font_manager as font_manager

# Get a list of system fonts
# fonts = font_manager.findSystemFonts()

# Print the list of fonts (might be very long)
# print(fonts[:10])  # Print only the first 10 fonts for illustration


# Specify Matplotlib backend
matplotlib.use('TkAgg')  # Change to another backend if needed


def generate_bubble(image_size):
    img = np.zeros((image_size, image_size), dtype=np.uint8)
    center = (np.random.randint(20, image_size - 20), np.random.randint(20, image_size - 20))
    axes = (np.random.randint(10, 20), np.random.randint(5, 15))
    cv2.ellipse(img, center, axes, 0, 0, 360, 255, -1)
    return img


def generate_scratch(image_size):
    img = np.zeros((image_size, image_size), dtype=np.uint8)

    # Randomly choose start and end points for the line
    start_point = (np.random.randint(10, image_size - 20), np.random.randint(10, image_size - 20))
    end_point = (np.random.randint(10, image_size - 20), np.random.randint(10, image_size - 20))

    # Draw the line
    cv2.line(img, start_point, end_point, 255, 3)

    return img


def generate_dirt_stain(image_size):
    img = np.zeros((image_size, image_size), dtype=np.uint8)

    # Ensure that the center, radius, and frequency are valid
    center = (np.random.randint(20, image_size - 20), np.random.randint(20, image_size - 20))
    num_ellipses = np.random.randint(3, 5)  # Randomly choose the number of ellipses

    for _ in range(num_ellipses):
        # Randomly determine the size and orientation of each ellipse
        major_axis = np.random.randint(5, 15)
        minor_axis = np.random.randint(3, 8)
        angle = np.random.uniform(0, 2 * np.pi)

        # Randomly determine the position of each ellipse
        offset_x = np.random.randint(-5, 5)
        offset_y = np.random.randint(-5, 5)

        # Calculate the ellipse parameters
        ellipse_center = (center[0] + offset_x, center[1] + offset_y)
        ellipse_axes = (major_axis, minor_axis)

        # Draw the ellipse
        cv2.ellipse(img, ellipse_center, ellipse_axes, angle, 0, 360, 255, -1)

    return img

#
# def generate_dataset(num_images, image_size):
#     dataset = []
#     labels = []
#
#     for _ in range(num_images):
#         defect_type = np.random.choice(['bubble', 'scratch', 'dirt_stain'])
#         if defect_type == 'bubble':
#             img = generate_bubble(image_size)
#             label = 0  # 0 represents bubble
#         elif defect_type == 'scratch':
#             img = generate_scratch(image_size)
#             label = 1  # 1 represents scratch
#         else:
#             img = generate_dirt_stain(image_size)
#             label = 2  # 2 represents dirt stain
#
#         dataset.append(img)
#         labels.append(label)
#
#     return np.array(dataset), np.array(labels)
#

import cv2
import numpy as np

#
# def generate_number_one(image_size, thickness=2, font_scale=2):
#   """
#   Generates an image of the number "1".
#
#   Args:
#       image_size: The size (width and height) of the desired image.
#       thickness: Thickness of the number outline (default 2).
#       font_scale: Scale factor for the font size (default 2).
#
#   Returns:
#       A NumPy array representing the black and white image of number "1".
#   """
#   # Create a black image
#   img = np.zeros((image_size, image_size), dtype=np.uint8)
#   # Choose white for the text color
#   text_color = (255, 255, 255)
#
#   # Select a suitable font (replace if needed)
#   font = cv2.FONT_HERSHEY_SIMPLEX
#
#   # Calculate the text size
#   text_size, _ = cv2.getTextSize("1", font, font_scale, thickness)
#
#   # Calculate the center coordinates for positioning the text
#   text_x = int((image_size - text_size[0]) / 2)
#   text_y = int((image_size + text_size[1]) / 2)
#
#   # Add the text "1" on the image
#   cv2.putText(img, "1", (text_x, text_y), font, font_scale, text_color, thickness)
#
#   return img

import cv2
import numpy as np
import random


def generate_number_one(image_size, max_thickness_variation=2, max_font_scale_variation=0.5):
  """
  Generates an image of the number "1" with slight variations.

  Args:
      image_size: The size (width and height) of the desired image.
      max_thickness_variation: Maximum variation for the outline thickness (default 2).
      max_font_scale_variation: Maximum variation for the font scale (default 0.5).

  Returns:
      A NumPy array representing a black and white image of number "1" with slight variations.
  """
  # Create a black image
  img = np.zeros((image_size, image_size), dtype=np.uint8)
  # Choose white for the text color
  text_color = (255, 255, 255)

  # Select a suitable font (replace if needed)
  font = cv2.FONT_HERSHEY_SIMPLEX

  # Generate random variations within the specified ranges
  thickness = random.randint(2 - max_thickness_variation, 2 + max_thickness_variation)
  font_scale = 2 + random.uniform(-max_font_scale_variation, max_font_scale_variation)

  # Calculate the text size
  text_size, _ = cv2.getTextSize("1", font, font_scale, thickness)

  # Calculate the center coordinates for positioning the text
  text_x = int((image_size - text_size[0]) / 2)
  text_y = int((image_size + text_size[1]) / 2)

  # Add the text "1" on the image
  cv2.putText(img, "3", (text_x, text_y), font, font_scale, text_color, thickness)

  return img

def generate_number_2(image_size, max_thickness_variation=2, max_font_scale_variation=0.5):
  """
  Generates an image of the number "1" with slight variations.

  Args:
      image_size: The size (width and height) of the desired image.
      max_thickness_variation: Maximum variation for the outline thickness (default 2).
      max_font_scale_variation: Maximum variation for the font scale (default 0.5).

  Returns:
      A NumPy array representing a black and white image of number "1" with slight variations.
  """
  # Create a black image
  img = np.zeros((image_size, image_size), dtype=np.uint8)
  # Choose white for the text color
  text_color = (255, 255, 255)

  # Select a suitable font (replace if needed)
  font = cv2.FONT_HERSHEY_SIMPLEX

  # Generate random variations within the specified ranges
  thickness = random.randint(2 - max_thickness_variation, 2 + max_thickness_variation)
  font_scale = 2 + random.uniform(-max_font_scale_variation, max_font_scale_variation)

  # Calculate the text size
  text_size, _ = cv2.getTextSize("1", font, font_scale, thickness)

  # Calculate the center coordinates for positioning the text
  text_x = int((image_size - text_size[0]) / 2)
  text_y = int((image_size + text_size[1]) / 2)

  # Add the text "1" on the image
  cv2.putText(img, "2", (text_x, text_y), font, font_scale, text_color, thickness)

  return img

def generate_number_3(image_size, max_thickness_variation=2, max_font_scale_variation=0.5):
  """
  Generates an image of the number "1" with slight variations.

  Args:
      image_size: The size (width and height) of the desired image.
      max_thickness_variation: Maximum variation for the outline thickness (default 2).
      max_font_scale_variation: Maximum variation for the font scale (default 0.5).

  Returns:
      A NumPy array representing a black and white image of number "1" with slight variations.
  """
  # Create a black image
  img = np.zeros((image_size, image_size), dtype=np.uint8)
  # Choose white for the text color
  text_color = (255, 255, 255)

  # Select a suitable font (replace if needed)
  # font = cv2.FONT_HERSHEY_SIMPLEX
  fonts = font_manager.findSystemFonts()
  # l=len[fonts]
  i=np.random.randint(20)
  print(i)

  font = fonts[i]
  font = cv2.FONT_HERSHEY_SIMPLEX
  font = 3
  # print(cv2.getFontScaleFromHeight(1,12,4))


  # Generate random variations within the specified ranges
  thickness = random.randint(2 - max_thickness_variation, 2 + max_thickness_variation)
  font_scale = 2 + random.uniform(-max_font_scale_variation, max_font_scale_variation)

  # Calculate the text size
  text_size, _ = cv2.getTextSize("1", font, font_scale, thickness)

  # Calculate the center coordinates for positioning the text
  text_x = int((image_size - text_size[0]) / 2)
  text_y = int((image_size + text_size[1]) / 2)

  # Add the text "1" on the image
  cv2.putText(img, "3", (text_x, text_y), font, font_scale, text_color, thickness)

  return img


import cv2
import numpy as np


def show_image(image, title="Image"):
    cv2.imshow(title, image)
    cv2.waitKey(0)  # Wait for a key press to close the window
    cv2.destroyAllWindows()


# ... rest of your code ...
#
# After generating an image (e.g., in generate_bubble)
img = generate_number_3(500)
# show_image(img, title="Generated Bubble Image")
# img = generate_number_3(500)
# show_image(img, title="Generated Bubble Image")
# img = generate_number_3(500)
# show_image(img, title="Generated Bubble Image")
# img = generate_number_3(500)
# show_image(img, title="Generated Bubble Image")
#
# img = generate_number_one(500)
# show_image(img, title="Generated Bubble Image")
# img = generate_number_one(500)
# show_image(img, title="Generated Bubble Image")
# img = generate_number_one(500)
# show_image(img, title="Generated Bubble Image")

# img = generate_number_one(500)
# show_image(img, title="Generated Bubble Image")
# img = generate_number_one(500)
# show_image(img, title="Generated Bubble Image")
# img = generate_number_one(500)
# show_image(img, title="Generated Bubble Image")
# img = generate_number_one(500)
# show_image(img, title="Generated Bubble Image")
# img = generate_number_one(500)
# show_image(img, title="Generated Bubble Image")
# img = generate_number_one(500)
# show_image(img, title="Generated Bubble Image")
# img = generate_number_one(500)
# show_image(img, title="Generated Bubble Image")
# img = generate_number_one(500)
# show_image(img, title="Generated Bubble Image")
# img = generate_number_one(500)
# show_image(img, title="Generated Bubble Image")
# img = generate_number_one(500)
# show_image(img, title="Generated Bubble Image")
# img = generate_number_one(500)
# show_image(img, title="Generated Bubble Image")
#



def generate_dataset(num_images, image_size):
    dataset = []
    labels = []

    for _ in range(num_images):
        defect_type = np.random.choice(['bubble', 'scratch', 'dirt_stain'])
        if defect_type == 'bubble':
            img = generate_number_one(image_size)
            label = 0  # 0 represents bubble
        elif defect_type == 'scratch':
            img = generate_number_2(image_size)
            label = 1  # 1 represents scratch
        else:
            img = generate_number_3(image_size)
            label = 2  # 2 represents dirt stain

        dataset.append(img)
        labels.append(label)

    return np.array(dataset), np.array(labels)



