import pygame
import random

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
GRID_SIZE = 20
GRID_WIDTH, GRID_HEIGHT = SCREEN_WIDTH // GRID_SIZE, SCREEN_HEIGHT // GRID_SIZE
UP, DOWN, LEFT, RIGHT = 0, 1, 2, 3
WHITE, BLACK, RED = (255, 255, 255), (0, 0, 0), (255, 0, 0)

# Display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

# Snake class
class Snake:
    def __init__(self):
        self.body = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = RIGHT

    def move(self, apple):
        head_x, head_y = self.body[0]
        if self.direction == UP:
            new_head = (head_x, head_y - 1)
        elif self.direction == DOWN:
            new_head = (head_x, head_y + 1)
        elif self.direction == LEFT:
            new_head = (head_x - 1, head_y)
        elif self.direction == RIGHT:
            new_head = (head_x + 1, head_y)

        self.body.insert(0, new_head)

        if new_head == apple.position:
            apple.randomize()
        else:
            self.body.pop()

    def change_direction(self, new_direction):
        if new_direction == UP and self.direction != DOWN:
            self.direction = UP
        elif new_direction == DOWN and self.direction != UP:
            self.direction = DOWN
        elif new_direction == LEFT and self.direction != RIGHT:
            self.direction = LEFT
        elif new_direction == RIGHT and self.direction != LEFT:
            self.direction = RIGHT

    def check_collision(self):
        head = self.body[0]
        return head in self.body[1:]

    def draw(self):
        for segment in self.body:
            pygame.draw.rect(screen, WHITE, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

# Apple class
class Apple:
    def __init__(self):
        self.randomize()

    def randomize(self):
        self.position = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

    def draw(self):
        pygame.draw.rect(screen, RED, (self.position[0] * GRID_SIZE, self.position[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

def main():
    snake = Snake()
    apple = Apple()

    clock = pygame.time.Clock()
    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.change_direction(UP)
                elif event.key == pygame.K_DOWN:
                    snake.change_direction(DOWN)
                elif event.key == pygame.K_LEFT:
                    snake.change_direction(LEFT)
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction(RIGHT)

        snake.move(apple)

        if snake.check_collision() or snake.body[0][0] < 0 or snake.body[0][0] >= GRID_WIDTH or snake.body[0][1] < 0 or snake.body[0][1] >= GRID_HEIGHT:
            game_over = True

        screen.fill(BLACK)
        snake.draw()
        apple.draw()

        pygame.display.update()
        clock.tick(10)  # Adjust the value to control the snake's speed

    pygame.quit()

if __name__ == "__main__":
    main()


