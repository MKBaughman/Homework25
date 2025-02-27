imp# Initialize Pygame
pygame.init()

# Set window dimensions
width = 600
height = 400
screen = pygame.display.set_mode((width, height))

# Set window title
pygame.display.set_caption("Snake")

# To Do List

todo_list = ["call mom", "walk the dog", "go to store"]
todo_list.append("read a book")
todo_list.remove("call mom")
print(len(todo_list))

print(todo_list)

coordinates = [
  (100,200),
  (200,300)
]