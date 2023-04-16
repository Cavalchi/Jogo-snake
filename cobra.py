import pygame
import sys
import random

# Definir cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Tamanho do display
WIDTH = 400
HEIGHT = 400

# Tamanho da cobrinha e da comida
BLOCK_SIZE = 20

# Velocidade da cobrinha
SPEED = 10

class Snake:
    def __init__(self):
        self.body = [(WIDTH//2, HEIGHT//2)]
        self.direction = (0, 0)

    def draw(self, screen):
        for block in self.body:
            pygame.draw.rect(screen, GREEN, pygame.Rect(block[0], block[1], BLOCK_SIZE, BLOCK_SIZE))

    def move(self):
        head = list(self.body[0])
        head[0] += self.direction[0]
        head[1] += self.direction[1]
        self.body.insert(0, tuple(head))
        self.body.pop()

    def grow(self):
        tail = list(self.body[-1])
        tail[0] -= self.direction[0]
        tail[1] -= self.direction[1]
        self.body.append(tuple(tail))

    def check_collision(self):
        if self.body[0][0] < 0 or self.body[0][0] >= WIDTH or self.body[0][1] < 0 or self.body[0][1] >= HEIGHT:
            return True

        for block in self.body[1:]:
            if self.body[0] == block:
                return True

        return False

    def change_direction(self, direction):
        if direction == 'UP':
            self.direction = (0, -BLOCK_SIZE)
        elif direction == 'DOWN':
            self.direction = (0, BLOCK_SIZE)
        elif direction == 'LEFT':
            self.direction = (-BLOCK_SIZE, 0)
        elif direction == 'RIGHT':
            self.direction = (BLOCK_SIZE, 0)

class Food:
    def __init__(self):
        self.position = self.generate_position()

    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, pygame.Rect(self.position[0], self.position[1], BLOCK_SIZE, BLOCK_SIZE))

    def generate_position(self):
        x = random.randint(0, (WIDTH-BLOCK_SIZE)//BLOCK_SIZE) * BLOCK_SIZE
        y = random.randint(0, (HEIGHT-BLOCK_SIZE)//BLOCK_SIZE) * BLOCK_SIZE
        return x, y

# Inicializar Pygame
pygame.init()

# Configurar display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake')

# Inicializar jogo
snake = Snake()
food = Food()
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.change_direction('UP')
            elif event.key == pygame.K_DOWN:
                snake.change_direction('DOWN')
            elif event.key == pygame.K_LEFT:
                snake.change_direction('LEFT')
            elif event.key == pygame.K_RIGHT:
                snake.change_direction('RIGHT')

    snake.move()

    if snake.body[0] == food.position:
        snake.grow()
        food = Food()

    if snake.check_collision():
        pygame.quit()
        sys.exit()

    screen.fill(BLACK)
    snake.draw(screen)
    food.draw(screen)
    pygame
    # Atualizar display
    pygame.display.flip()

    # Controlar a velocidade do jogo
    clock.tick(SPEED)
