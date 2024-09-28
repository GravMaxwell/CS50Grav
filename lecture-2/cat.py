#while True:
#    n = int(input("What's n? "))
 #   if n < 0:
  #      continue
   # else:
    #    break

#while True:
 #   n = int(input("What's n? "))
  #  if n > 0:
   #     break

#for _ in range(n):
 #   print("meow")

# ^^^ previous examples above


def main():
    meow(get_number())


def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n


def meow(n):
    for _ in range(n):
        print("meow")


main()
