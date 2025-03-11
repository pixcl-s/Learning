# Write a program that encrypts given words by using the characters: "-|_/\()"
# to structure the word. Use the pyfiglet module.
# Directions
# 1. First you need to install the module that we will be using. To install it go to
# Setting --> Project <your_project_name> --> Project Interpreter --> + --> search for pyfiglet --> install package.
# 2. Import the module
# 3. Implement the logic. We will be using the figlet_format method

from pyfiglet import figlet_format

stuff = input("What to format:")
font = input("Choose font(starwars, poison, ogre, old_banner, etc.):")

print(figlet_format(stuff, font=font))
