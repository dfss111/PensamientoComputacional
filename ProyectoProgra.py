import pygame
import sys
import random


#ventana
from tkinter import *
from tkinter import messagebox as MessageBox

def test():
    MessageBox.showinfo("Juego Ahorcado", "Bienvenido Usuario") # título, mensaje

root = Tk()

Button(root, text = "HAZ CLIC AQUI", command=test).pack()

root.mainloop()

# constantes
WIDTH, HEIGHT = 800, 600
WHITE = (173, 216, 230)
BLACK = (0, 0, 0)
GREEN= (0, 255, 0)
BLUE= (0, 0, 128)
RED= (216, 36, 41)
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'



# pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Aprende colores en inglés")
clock = pygame.time.Clock()


# fonts
font = pygame.font.SysFont("Arial", 48)
small_font = pygame.font.SysFont("Arial", 36)

# palabras 

words = [ "BLUE",
         "GREEN",
         "PINK", 
         "YELLOW"
]

current_word = random.choice(words)
guessed_word = ['_' for _ in current_word]




# variables de juego
attempts = 0
max_attempts = 6  # pasos para terminar de dibujar al mono
game_over = False
won = False

# ciclo de juego
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if not won and attempts < max_attempts:
            if event.type == pygame.KEYDOWN and event.unicode in ALPHABET:
                letter = event.unicode
                if letter in current_word:
                    for i, char in enumerate(current_word):
                        if char == letter:
                            guessed_word[i] = letter
                else:
                    attempts += 1

            # palabra completa 
            if ''.join(guessed_word) == current_word:
                won = True


    screen.fill(WHITE)

    # palabra
    word_text = font.render(' '.join(guessed_word), True, BLACK)
    screen.blit(word_text, (WIDTH // 2 - word_text.get_width() // 2, 400))

    # mono
    if attempts < max_attempts:
        pygame.draw.line(screen, BLACK, (300, 100), (300, 30), 5)  # estructural
        
        pygame.draw.line(screen, BLACK, (300, 30), (500, 30), 5)  #  barra horizontal
        pygame.draw.line(screen, BLACK, (500, 30), (500, 400), 5)  # barra verical
        pygame.draw.circle(screen, BLUE, (300, 130), 30 ,5)  # cabeza

        if attempts > 0:
            pygame.draw.line(screen, BLUE, (300, 180-20), (300, 300-20), 5)  # cuerpo
        if attempts > 1:
            pygame.draw.line(screen, BLUE, (300, 200-20), (330, 240-20), 5)  # brazo izquierdo
        if attempts > 2:
            pygame.draw.line(screen, BLUE, (300, 200-20), (270, 240-20), 5)  # brazo derecho
        if attempts > 3:
            pygame.draw.line(screen, BLUE, (300, 300-20), (270, 340-20), 5)  # pierna izquierda
        if attempts > 4:
            pygame.draw.line(screen, BLUE, (300, 300-20), (330, 340-20), 5)  # pierna derecha
    else:
        game_over = True

    # valida gane o pierde
    if won:
        result_text = font.render("You Win!", True, GREEN)
        screen.blit(result_text, (WIDTH // 2 - result_text.get_width() // 2, 200))
    elif game_over:
        result_text = font.render("Game Over", True, RED)
        screen.blit(result_text, (WIDTH // 2 - result_text.get_width() // 2, 200))
        word_text = font.render(current_word, True, BLACK)
        screen.blit(word_text, (WIDTH // 2 - word_text.get_width() // 2, 300))

    pygame.display.flip()
    # fps
    clock.tick(60)
