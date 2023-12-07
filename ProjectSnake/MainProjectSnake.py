import time
import pygame
import random

pygame.init()


def main_menu():
    menu = True
    selected = 'start'
    while menu:
        sr.fill((123, 160, 91))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    selected = 'start'
                if event.key == pygame.K_s:
                    selected = 'quit'
                if event.key == pygame.K_RETURN:
                    if selected == 'start':
                        return True
                    else:
                        return False

        a1 = pygame.font.SysFont('DotGothic16 Regular', 100)
        title = a1.render('Snake Game', True, (38, 46, 55))
        a2 = pygame.font.SysFont('DotGothic16 Regular', 70)
        a3 = pygame.font.SysFont('DotGothic16 Regular', 30)
        version = a3.render('GameVersion : 1', True, (38, 46, 55))
        if selected == 'start':
            start = a2.render('Start', True, (0, 0, 0))
        else:
            start = a2.render('Start', True, (25, 51, 53))
        if selected == 'quit':
            quit = a2.render('Quit', True, (0, 0, 0))
        else:
            quit = a2.render('Quit', True, (25, 51, 53))

        sr.blit(title, (WIDTH/2 - 250, 70))
        sr.blit(start, (WIDTH/2 - 80, 200))
        sr.blit(quit, (WIDTH/2 - 80, 300))
        sr.blit(version, (WIDTH/2 - 350, 10))

        pygame.display.update()
        clock.tick(fps)


class Snake:
    def __init__(self, x, y, color, speed, size):
        self.x = x
        self.y = y
        self.color = color
        self.speed = speed
        self.size = size
        self.dir_x = 0
        self.dir_y = 0
        self.count = 1
        self.heads = []
        self.add_head()

    def change_color(self):
        colors = [red, blue, green, purple, pink, yellow, orange]
        self.color = random.choice(colors)

    def add_head(self):
        self.heads.append(SnakeHead(self.x, self.y, self.color, self.speed, self.size))

    def remove_head(self):
        if len(self.heads) > self.count:
            self.heads.pop(0)

    def draw(self, screen):
        for head in self.heads:
            head.draw(screen)

    def move(self):
        if self.dir_x == 1:
            self.x += self.speed
        if self.dir_x == -1:
            self.x -= self.speed
        if self.dir_y == 1:
            self.y += self.speed
        if self.dir_y == -1:
            self.y -= self.speed
        self.add_head()
        self.remove_head()

    def move_right(self):
        if self.count == 1:
            self.dir_x = 1
            self.dir_y = 0
        else:
            if self.dir_y:
                self.dir_x = 1
                self.dir_y = 0

    def move_left(self):
        if self.count == 1:
            self.dir_x = -1
            self.dir_y = 0
        else:
            if self.dir_y:
                self.dir_x = -1
                self.dir_y = 0

    def move_down(self):
        if self.count == 1:
            self.dir_x = 0
            self.dir_y = 1
        else:
            if self.dir_x:
                self.dir_x = 0
                self.dir_y = 1

    def move_up(self):
        if self.count == 1:
            self.dir_x = 0
            self.dir_y = -1
        else:
            if self.dir_x:
                self.dir_x = 0
                self.dir_y = -1

    def draw1(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))

    def check_walls(self):
        if self.x <= 0 or self.y <= 0 or self.y >= HEIGHT - self.size or self.x >= WIDTH - self.size:
            return False
        return True

    def check_snake(self):
        for i in range(len(self.heads)):
            if i != len(self.heads) - 1:
                if self.x == self.heads[i].x and self.y == self.heads[i].y:
                    return False
        return True


    def check_food(self, food_x, food_y):
        if self.x == food_x and self.y == food_y:
            self.count += 1
            return True
        return False

    def welcome(self):
        if self.dir_x == 1 or self.dir_x == -1 or self.dir_y == 1 or self.dir_y == -1:
            return False
        return True

    def welcome_print(self):
        if welcome == True:
            sr.blit(Welcome, (40, 100))


class SnakeHead:
    def __init__(self, x, y, color, speed, size):
        self.x = x
        self.y = y
        self.color = color
        self.speed = speed
        self.size = size
        self.dir_x = 0
        self.dir_y = 0

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))


WIDTH = 720
HEIGHT = 480

sr = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('SnakeGameV1(Release)')
image = pygame.image.load('snake.png')
pygame.display.set_icon(image)

red = 255, 0, 0
blue = 0, 0, 255
green = 0, 255, 0
purple = 204, 0, 204
pink = 255, 51, 153
yellow = 255, 255, 0
orange = 255, 128, 0

fps = 10
clock = pygame.time.Clock()

is_key_right = False
is_key_left = False
is_key_down = False
is_key_top = False

speed = 15
size = 15

width_hero = 15
height_hero = 15

food_x = 150
food_y = 150

is_eat = True

f1 = pygame.font.Font(None, 36)
f3 = pygame.font.Font(None, 60)
Welcome = f1.render('Welcome new player! To start playing press W,A,S,D', True, (162, 180, 137))
Death = f3.render('GAME OVER!', True, (180, 0, 0))

snake = Snake(3 * speed, 3 * speed, (80, 125, 42), speed, size)

is_game_active = True
welcome = True

is_game_active = main_menu()

while is_game_active:
    sr.fill((0, 0, 0))

    f2 = pygame.font.Font(None, 30)
    Score = f2.render('Your Score:' + str(snake.count), True, (162, 180, 137))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                is_key_right = True
            if event.key == pygame.K_a:
                is_key_left = True
            if event.key == pygame.K_w:
                is_key_top = True
            if event.key == pygame.K_s:
                is_key_down = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                is_key_right = False
            if event.key == pygame.K_a:
                is_key_left = False
            if event.key == pygame.K_w:
                is_key_top = False
            if event.key == pygame.K_s:
                is_key_down = False

    if is_key_right:
        snake.move_right()
    if is_key_left:
        snake.move_left()
    if is_key_top:
        snake.move_up()
    if is_key_down:
        snake.move_down()

    snake.move()
    is_game_active2 = snake.check_snake()
    is_game_active1 = snake.check_walls()
    is_game_active = is_game_active1 and is_game_active2
    snake.welcome_print()
    welcome = snake.welcome()
    is_eat = snake.check_food(food_x, food_y)
    snake.draw(sr)
    if is_eat:
        snake.change_color()
        is_repeat = True
        while is_repeat:
            is_repeat = False
        food_x = random.randint(1, WIDTH) * speed % WIDTH
        food_y = random.randint(1, HEIGHT) * speed % HEIGHT
        for snake_head in snake.heads:
            if food_x == snake_head.x and food_y == snake_head.y:
                is_repeat = True

    sr.blit(Score, (0, 460))
    pygame.draw.rect(sr, (237, 72, 48), (food_x, food_y, size, size))
    pygame.display.update()
    clock.tick(fps)

sr.blit(Death, (240, 200))
pygame.display.update()
time.sleep(3)
