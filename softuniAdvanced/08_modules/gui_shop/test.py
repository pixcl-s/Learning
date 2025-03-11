# import json
#
# with open("db/products.txt") as file:
#     products = [json.loads(x) for x in file]
#
#     print(products)
# import os
#
# file_path = os.path.dirname(__name__)
# image_path = os.path.join(file_path, "db/pngs")
#
# print(image_path)

lul = {"a": 1, "b": 2, "c": 3, "d": 4}

print([[x, y] for x, y in enumerate(lul)])

with open("db/current_user.txt") as file:
    logged_in_user = file.read()

print(logged_in_user)