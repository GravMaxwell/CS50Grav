# write function to grab file extension from string
def getfile (file_name):
    # find postion of the last period in filename
    position = file_name.rfind(".")
     # grab extension from filename
    extension = file_name[position:].lower()

    return extension


# write function to get media type
def getmedia(file_name):
    # match media type with file extensions
    filetype = getfile(file_name)
    match filetype:
        case ".gif":
            return "image/gif"
        case ".jpg" | ".jpeg":
            return "image/jpeg"
        case ".png":
            return "image/png"
        case ".pdf":
            return "application/pdf"
        case ".txt":
            return "text/plain"
        case ".zip":
            return "application/zip"
        case _:
            return "application/octet-stream"

def main():
    # prompt user for file name/type
    file_name = input("File Name: ").strip()

    media = getmedia(file_name)

    print (media)


main ()

