# Initialize Pygame
pygame.init()

# Set window dimensions
width = 600
height = 400
screen = pygame.display.set_mode((width, height))

# Set window title
pygame.display.set_caption("HW6")

# Melissa_Kempton_Buaghman
# 02-25-2025
# Homework 6
# Create a basic Python program that will ask for 2 numbers from the user and perform at least 4 arithmetic operations. Print each operation and its answer to the terminal. Each output should be formatted and readable, as shown in class.

# Make sure to push the final code back to the remote repository.
# Submit the url of the repository on GitHub. Commits on the repository after the deadline of the assignment will not be graded.

import pygame
import random

# define variables
num1 = (float)("enter the first number:"))
num2 = (float)("enter the second number:"))

# perform 4 arithmetic operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2

print("addition:" num1 + num2)
print("subtraction:" num1 - num2)
print("multiplication:" num1 * num2)
print("division:" num1 / num2)

