# # # # email = input("What's your email? ").strip()

# # # # if "@" in email:
# # # #     print("Valid")
# # # # else:
# # # #     print("Invalid")

# # # email = input("What's your email? ").strip()

# # # if "@" in email and "." in email:
# # #     print("Valid")
# # # else:
# # #     print("Invalid")


# # email = input("What's your email? ").strip()

# # username, domain = email.split("@")

# # if username and domain.endswith(".edu"):
# #     print("Valid")
# # else:
# #     print("Invalid")


# import re

# email = input("What's your email? ").strip()

# if re.search("@", email):
#     print("Valid")
# else:
#     print("Invalid")


import re

email = input("What's your email? ").strip()

if re.search(".+@.+", email):
    print("Valid")
else:
    print("Invalid")
