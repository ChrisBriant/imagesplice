import os
from PIL import Image, ImageDraw

# Define the file paths for the input images and the output image
input_paths = ['/path/to/image1.jpg', '/path/to/image2.jpg', '/path/to/image3.jpg', '/path/to/image4.jpg', '/path/to/image5.jpg', '/path/to/image6.jpg']
output_path = '/path/to/output.jpg'

# Define the desired dimensions for the resized images
width = 400
height = None  # Setting height to None maintains aspect ratio

# Create a new PIL Image to hold the spliced images
spliced_image = Image.new(mode='RGB', size=(3*width, 2*height))

# Resize each input image and add it to the spliced image
for i, path in enumerate(input_paths):
    with Image.open(path) as img:
        img = img.resize((width, height), resample=Image.LANCZOS)
        x = i % 3 * width
        y = i // 3 * height
        spliced_image.paste(img, (x, y))

# Draw lines between the images to form a grid
draw = ImageDraw.Draw(spliced_image)
draw.line((0, height, spliced_image.width, height), fill='black')
draw.line((0, 2*height, spliced_image.width, 2*height), fill='black')
draw.line((width, 0, width, spliced_image.height), fill='black')
draw.line((2*width, 0, 2*width, spliced_image.height), fill='black')

# Save the spliced and resized image to the output path
spliced_image.save(output_path)
