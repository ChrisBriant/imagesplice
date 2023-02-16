
import os,sys, random
from PIL import Image, ImageDraw


class GridSizeException(Exception):
    pass

def main ():
    args = sys.argv
    cwd = os.getcwd()

    try:
        #Get the grid dimensions
        grid_x = int(args[1].split('x')[0])
        grid_y = int(args[1].split('x')[1])

        #Get the folder list
        folder_list = args[2].split('folders=')[1].split(',')

        #get the image dimensions for individual images
        width = int(args[3])
        height = int(args[4])

        #The output file name
        outfile = args[5]
    except Exception as e:
        print('Unable to read the arguments passed. The format is gridsize folders=<comma seperatedlist> imagewidth imageheight filename')
        return

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

    #Create image object
    spliced_image = Image.new(mode='RGB', size=(grid_x*width, grid_y*height))
    for y in range(0,grid_y):
        for x in range(0,grid_x):
            image_index = (y*grid_x)+x
            with Image.open(selected_files[image_index]) as img:
                img = img.resize((width, height), resample=Image.LANCZOS)
                img_x = x * width
                img_y = y * height
                spliced_image.paste(img, (img_x, img_y)) 
    #Draw lines between the images to form a grid
    draw = ImageDraw.Draw(spliced_image)
    draw.line((0, height, spliced_image.width, height), fill='black')
    draw.line((0, 2*height, spliced_image.width, 2*height), fill='black')
    draw.line((width, 0, width, spliced_image.height), fill='black')
    draw.line((2*width, 0, 2*width, spliced_image.height), fill='black')

    # Save the spliced and resized image to the output path
    spliced_image.save(outfile)

if __name__ == '__main__':
    main()