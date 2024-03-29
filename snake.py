import pygame
import random
pygame.init()

# Game window dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake")

# Colors
black = (0,0,0)
blue = (0,0,255)
red = (255,0,0)

snake_pos = [[50,50], [55,55], [60,60]]
snake_size = 20
food_pos = [random.randrange(1, (width // 10)) * 10, random.randrange(1, (height // 10)) * 10]
food_spawn = True

clock = pygame.time.Clock()

direction = 'right'
changeTo = direction

game_over = False

# Game functions
def draw_snake(snake_size, snake_pos):
    for pos in snake_pos:
        pygame.draw.rect(screen, blue, pygame.Rect(pos[0], pos[1], snake_size, snake_size))

def draw_food(food_pos, food_spawn):
    if food_spawn:
        pygame.draw.rect(screen, red, pygame.Rect(food_pos[0], food_pos[1], snake_size, snake_size))


# Game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                changeTo = 'up'
            if event.key == pygame.K_DOWN:
                changeTo = 'down'
            if event.key == pygame.K_RIGHT:
                changeTo = 'right'
            if event.key == pygame.K_LEFT:
                changeTo = 'left'
    
    if changeTo == 'up' and direction != 'down':
        direction = 'up'
    if changeTo == 'down' and direction != 'up':
        direction = 'down'
    if changeTo == 'right' and direction != 'left':
        direction = 'right'
    if changeTo == 'left' and direction != 'right':
        direction = 'left'

    if direction == "up":
        snake_pos.insert(0, [snake_pos[0][0], snake_pos[0][1] - 5])
    if direction == "down":
        snake_pos.insert(0, [snake_pos[0][0], snake_pos[0][1] + 5])
    if direction == "left":
        snake_pos.insert(0, [snake_pos[0][0] - 5, snake_pos[0][1]])
    if direction == "right":
        snake_pos.insert(0, [snake_pos[0][0] + 5, snake_pos[0][1]])
    
    if snake_pos[0][0] > width:
        snake_pos[0][0] = 0
    if snake_pos[0][0] < 0:
        snake_pos[0][0] = width
    if snake_pos[0][1] > height:
        snake_pos[0][1] = 0
    if snake_pos[0][1] < 0:
        snake_pos[0][1] = height

    for self in snake_pos[1:]:
        if self[0] == snake_pos[0][0] and self[1] == snake_pos[0][1]:
            game_over = True
    
    if snake_pos[0][0] == food_pos[0] and snake_pos[0][1] == food_pos[1]:
        food_spawn = False
    else:
        snake_pos.pop()

    if not food_spawn:
        food_pos = [random.randrange(1, (width // 10)) * 10, random.randrange(1, (height // 10)) * 10]

        food_spawn = True

    screen.fill(black)

    draw_snake(snake_size, snake_pos)
    draw_food(food_pos, food_spawn)

    pygame.display.update()

    clock.tick(45)

pygame.quit()