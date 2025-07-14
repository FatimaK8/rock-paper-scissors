# Rock Paper Scissors Game
# Copilot Prompt: Create a simple Rock Paper Scissors game using Pygame. Make it interactive with buttons for each choice and display the result of each round. Always import os os.environ["DISPLAY"] = ":1"

import pygame
import random
import sys
import os
os.environ["DISPLAY"] = ":1"
# or run DISPLAY=:1 python main.py 

pygame.init()


WIDTH, HEIGHT = 400, 300
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rock Paper Scissors (Simple)")


pygame.quit()
sys.exit()

# Rock Paper Scissors Game
# Copilot Prompt: Create a simple Rock Paper Scissors game using Pygame. Make it interactive with buttons for each choice and display the result of each round.

import pygame
import random
import sys
import os

os.environ["DISPLAY"] = ":1"
pygame.init()

WIDTH, HEIGHT = 400, 300
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
FONT = pygame.font.SysFont(None, 36)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rock Paper Scissors (Simple)")

choices = ["Rock", "Paper", "Scissors"]

# Button rectangles
button_width = 100
button_height = 50
button_padding = 15
buttons = []
for i, choice in enumerate(choices):
    x = button_padding + i * (button_width + button_padding)
    y = HEIGHT - button_height - 30
    buttons.append(pygame.Rect(x, y, button_width, button_height))

result = ""
player_choice = ""
computer_choice = ""

def get_winner(player, computer):
    if player == computer:
        return "Tie!"
    elif (player == "Rock" and computer == "Scissors") or \
         (player == "Paper" and computer == "Rock") or \
         (player == "Scissors" and computer == "Paper"):
        return "You win!"
    else:
        return "You lose!"

clock = pygame.time.Clock()
running = True
while running:
    screen.fill(WHITE)

    # Draw buttons
    for i, rect in enumerate(buttons):
        pygame.draw.rect(screen, GRAY, rect)
        text = FONT.render(choices[i], True, BLACK)
        text_rect = text.get_rect(center=rect.center)
        screen.blit(text, text_rect)

    # Draw result
    if result:
        result_text = FONT.render(f"You: {player_choice} | Computer: {computer_choice}", True, BLACK)
        result_rect = result_text.get_rect(center=(WIDTH // 2, 60))
        screen.blit(result_text, result_rect)

        winner_text = FONT.render(result, True, BLACK)
        winner_rect = winner_text.get_rect(center=(WIDTH // 2, 100))
        screen.blit(winner_text, winner_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for i, rect in enumerate(buttons):
                if rect.collidepoint(event.pos):
                    player_choice = choices[i]
                    computer_choice = random.choice(choices)
                    result = get_winner(player_choice, computer_choice)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
