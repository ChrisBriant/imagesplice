#IMAGE SPLICE

Python script to splice images together in a grid.

To run

python3 image_splice.py <grid_dimensions> <folders=<comma seperated list of folders>> <image_height> <image_width> <output_filename>

Exmaple:

python3 image_splice.py 2x3 folders=bathroom,bedroom,housepics,bedroom,kitchen,lounge 400 400 out.jpg

To prepare:

place the directories containing the images under the root.

The folder list must match the product of the grid size, you can specify the same folder more than once. It takes a random image from each folder and adds it to the grid. For example.

2x2 grid, dir1, dir2, dir3, dir4

Places image from dir1 into 0,0, image 3 would go in 0,1.
