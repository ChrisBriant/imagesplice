
import os,sys, random
import wand.image
from wand.drawing import Drawing
from wand.color import Color
from PIL import Image


class GridSizeException(Exception):
    pass

def main ():
    width = 200
    height = 200

    args = sys.argv
    cwd = os.getcwd()

    try:
        #Get the grid dimensions
        grid_x = int(args[1].split('x')[0])
        grid_y = int(args[1].split('x')[1])

        #Get the folder list
        folder_list = args[2].split('folders=')[1].split(',')
    except Exception as e:
        print('Unable to read the arguments passed. The format is "gridsize", "folders=<comma seperatedlist>" ')
        return

    print('arguments', grid_x,grid_y,folder_list, grid_x * grid_y, len(folder_list))

    #Product of the grid size must match the size of the folder list
    if(not grid_x * grid_y == len(folder_list)):
        raise GridSizeException('Grid size does not match file list. The product of the grid size must match the number of folders passed in the list.')

    selected_files = []

    #Read the files in each directory
    for folder in folder_list:
        # Get a list of all files in the directory
        try:
            curr_directory = cwd+'/'+folder
            file_list = [ os.path.join(curr_directory,f) for f in os.listdir(curr_directory) if os.path.isfile(os.path.join(curr_directory, f))]
            selected_files.append(random.sample(file_list,1)[0])
        except Exception as e:
            print('There was a problem reading from one of the directories, please check the folder names and try again.')
            return

    # Print the list of files
    #print(selected_files, len(selected_files))
    # Create a new ImageMagick wand to hold the spliced images
    #with wand.image.Image() as spliced_image:
    for y in range(0,grid_y):
        for x in range(0,grid_x):
            image_index = (y*grid_x)+x 
            print(image_index)

            try:
                with Image.open(selected_files[image_index]) as img:
                    # Image opened successfully
                    print(f"{selected_files[image_index]} is an image")
            except Exception as e:
                # Image failed to open
                print(f"{selected_files[image_index]} is not an image: {e}")

                # try:
                #     print('tring image',selected_files[image_index])
                #     with wand.image.Image(filename=selected_files[image_index]) as img:
                #         img.resize(width, height)
                #         img_x = x * width
                #         img_y = y * height
                #         spliced_image.composite(img, left=x, top=y)
                # except Exception as e:
                #     print(e)
                #     print("There was a problem reading the file. Please check that each directory only contains image files.")
                #     return
    
    # #Create the image
    # # Draw lines between the images to form a grid
    # with Drawing() as draw:
    #     draw.stroke_color = Color('black')
    #     draw.stroke_width = 1
    #     draw.line((0, height), (spliced_image.width, height))
    #     draw.line((0, 2*height), (spliced_image.width, 2*height))
    #     draw.line((width, 0), (width, spliced_image.height))
    #     draw.line((2*width, 0), (2*width, spliced_image.height))
    #     draw(spliced_image)

    # # Save the spliced and resized image to the output path
    # spliced_image.save(filename='out.png')

if __name__ == '__main__':
    main()