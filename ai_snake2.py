import pygame
import random

pygame.init()

CELL = 20
COLS = 30
ROWS = 20

WIDTH = COLS * CELL
HEIGHT = ROWS * CELL

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("AI Snake 🐍")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)

snake = [(5, 5)]
food = (15, 10)
score = 0
running = True
game_over = False

def new_food():
    while True:
        pos = (
            random.randrange(COLS),
            random.randrange(ROWS)
        )
        if pos not in snake:
            return pos

def ai_move():
    head_x, head_y = snake[0]
    food_x, food_y = food

    moves = [
        (head_x + 1, head_y),
        (head_x - 1, head_y),
        (head_x, head_y + 1),
        (head_x, head_y - 1)
    ]

    # Алмаға жақындататын қозғалыстарды таңдау
    moves.sort(
        key=lambda p: abs(p[0] - food_x) + abs(p[1] - food_y)
    )

    for x, y in moves:
        if (
            0 <= x < COLS
            and 0 <= y < ROWS
            and (x, y) not in snake[:-1]
        ):
            return (x, y)

    return None

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        next_head = ai_move()

        if next_head is None:
            game_over = True
        else:
            snake.insert(0, next_head)

            if next_head == food:
                score += 1
                food = new_food()
            else:
                snake.pop()

    screen.fill((20, 20, 30))

    # Алма
    pygame.draw.rect(
        screen, (255, 60, 60),
        (food[0] * CELL, food[1] * CELL, CELL, CELL)
    )

    # AI жылан
    for x, y in snake:
        pygame.draw.rect(
            screen, (50, 220, 100),
            (x * CELL, y * CELL, CELL - 2, CELL - 2)
        )

    text = font.render(f"AI Score: {score}", True, (255, 255, 255))
    screen.blit(text, (10, 10))

    if game_over:
        message = font.render("AI Game Over!", True, (255, 200, 50))
        screen.blit(message, (WIDTH // 2 - 75, HEIGHT // 2))

    pygame.display.flip()
    clock.tick(8)

pygame.quit()