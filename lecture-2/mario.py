#print("#")
#print("#")
#print("#")


#for _ in range(3):
  #  print("#")


#def main():
    #print_row(4)


#def print_row(width):
    #print("?" * width)


#main()



#def main():
    #print_square(3)

#def print_square(size):

    # For each row in square
    #for i in range(size):

        # For each brick in row
       #for j in range(size):

            #print brick
           # print("#" , end="")

          #print blank line
       # print()

#main()


def main():
    print_square(3)

def print_square(size):
    for i in range(size):
        print_row(size)

def print_row(width):
    print("#" * width)

main()
