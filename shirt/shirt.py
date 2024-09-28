import sys
import os
from PIL import Image, ImageOps

def main():
    # check for correct number of command line arguments
    if len(sys.argv) != 3:
        print("Usage: python shirt.py <input_image> <output_image>")
        sys.exit("Too few command-line arguments" if len(sys.argv) < 3 else "Too many command-line arguments")

    input_image = sys.argv[1]
    output_image = sys.argv[2]

    # check for the correct file extensions
    valid_extensions = [".jpg" , ".jpeg" , ".png"]
    input_ext = os.path.splitext(input_image)[1].lower()
    output_ext = os.path.splitext(output_image)[1].lower()

    if input_ext not in valid_extensions or output_ext not in valid_extensions:
        sys.exit("Invalid output")

    if input_ext != output_ext:
        sys.exit("Input and output have different extensions")

    # check if the input exists
    if not os.path.isfile(input_image):
        sys.exit("Input does not exist")
    try:
        #open the input image
        photo = Image.open(input_image)
    except FileNotFoundError:
        sys.exit("Input does not exist")

    #open the shirt image
    shirt = Image.open("shirt.png")

    # resize & crop input image to match shirt.png
    size = shirt.size
    photo = ImageOps.fit(photo,size)

    # overlay shirt.png onto input image
    photo.paste(shirt, shirt)

    # save result
    photo.save(output_image)

if __name__ == "__main__":
    main()
