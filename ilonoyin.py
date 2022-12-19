import pygame

# Initialize pygame
pygame.init()

# Set the window size
window_size = (400, 400)

# Create the window
screen = pygame.display.set_mode(window_size)

# Set the title of the window
pygame.display.set_caption("Snake")

# Set the dimensions of the snake
snake_size = 10

# Initialize the snake position
snake_pos = [200, 200]

# Initialize the snake body (a list of squares)
snake_body = [[200, 200], [210, 200], [220, 200]]

# Set the dimensions of the food
food_size = 10

# Initialize the food position
food_pos = [random.randrange(1, (window_size[0]-food_size)//10)*10, random.randrange(1, (window_size[1]-food_size)//10)*10]
food_spawn = True

# Set the initial direction of the snake
direction = "RIGHT"
change_to = direction

# Set the scoring system
score = 0

# Set the speed of the game (in milliseconds)
speed = 200

# Create the game over function
def game_over():
    my_font = pygame.font.SysFont('times new roman', 20)
    game_over_surface = my_font.render('Your score was: ' + str(score), True, (255, 255, 255))
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (window_size[0]/2, window_size[1]/4)
    screen.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    sys.exit()

# Run the game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = "UP"
            if event.key == pygame.K_DOWN:
                change_to = "DOWN"
            if event.key == pygame.K_LEFT:
                change_to = "LEFT"
            if event.key == pygame.K_RIGHT:
                change_to = "RIGHT"

    # Make sure the snake cannot move in the opposite direction instantaneously
    if change_to == "UP" and direction != "DOWN":
        direction = "UP"
    if change_to == "DOWN" and direction != "UP":
        direction = "DOWN"
    if change_to == "LEFT" and direction != "RIGHT":
        direction = "LEFT"
    if change_to == "RIGHT" and direction != "LEFT":
        direction = "RIGHT"

    # Move the snake
    if direction == "UP":
        snake_pos[1] -= 10
    if direction == "DOWN":
        snake_pos[1] += 10
    if direction == "LEFT":
        snake
