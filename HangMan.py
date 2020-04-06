import pygame
import time
import random
from pygame.locals import (
    QUIT,
    K_a,
    K_b,
    K_c,
    K_d,
    K_e,
    K_f,
    K_g,
    K_h,
    K_i,
    K_j,
    K_k,
    K_l,
    K_m,
    K_n,
    K_o,
    K_p,
    K_q,
    K_r,
    K_s,
    K_t,
    K_u,
    K_v,
    K_w,
    K_x,
    K_y,
    K_z,
    KEYDOWN
)
pygame.init()
screen = pygame.display.set_mode((700, 500))
run = True
word_to_guess = 'friend'
score = 0
score_to_get = len(word_to_guess)
draw_hang_count = 0
font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('_ _ _ _ _ _', True, (255, 255, 255), (0, 0, 0))
f_text = font.render('F', True, (255, 255, 255), (0, 0, 0))
r_text = font.render('R', True, (255, 255, 255), (0, 0, 0))
i_text = font.render('I', True, (255, 255, 255), (0, 0, 0))
e_text = font.render('E', True, (255, 255, 255), (0, 0, 0))
n_text = font.render('N', True, (255, 255, 255), (0, 0, 0))
d_text = font.render('D', True, (255, 255, 255), (0, 0, 0))
textRect = text.get_rect()
textRect.center = (700 // 2, 500 // 2)
pygame.display.update()
pygame.draw.line(screen, (255, 255, 255), (500, 25), (500, 375), 25)
pygame.draw.line(screen, (255, 255, 255), (400, 375), (600, 375), 25)
pygame.draw.line(screen, (210, 105, 30), (600, 25), (600, 100), 10)
pygame.draw.line(screen, (255, 255, 255), (450, 25), (650, 25), 25)
screen.blit(text, textRect)
pygame.display.update()
draw1 = 0
draw2 = 0
draw3 = 0
draw4 = 0
draw5 = 0
while run:
    pygame.display.update()
    keys = pygame.key.get_pressed()
    for action in pygame.event.get():
        if action.type == KEYDOWN:
            for letter in range(len(word_to_guess)):

                if keys[pygame.K_d] or action.key == K_d:
                    if 'd' == word_to_guess[letter - 1]:
                        score += 1
                        word_to_guess = word_to_guess.replace("d", "")
                        screen.blit(d_text, (407, 225))

                elif keys[pygame.K_e] or action.key == K_e:
                    if 'e' == word_to_guess[letter - 1]:
                        score += 1
                        word_to_guess = word_to_guess.replace("e", "")
                        screen.blit(e_text, (355, 225))

                elif keys[pygame.K_f] or action.key == K_f:
                    if 'f' == word_to_guess[letter - 1]:
                        score += 1
                        word_to_guess = word_to_guess.replace("f", "")
                        screen.blit(f_text, (275, 225))

                elif keys[pygame.K_i] or action.key == K_i:
                    if 'i' == word_to_guess[letter - 1]:
                        score += 1
                        word_to_guess = word_to_guess.replace("i", "")
                        screen.blit(i_text, (332, 225))

                elif keys[pygame.K_n] or action.key == K_n:
                    if 'n' == word_to_guess[letter - 1]:
                        score += 1
                        word_to_guess = word_to_guess.replace("n", "")
                        screen.blit(n_text, (380, 225))

                elif keys[pygame.K_r] or action.key == K_r:
                    if 'r' == word_to_guess[letter - 1]:
                        score += 1
                        word_to_guess = word_to_guess.replace("r", "")
                        screen.blit(r_text, (300, 225))
                else:
                    draw_hang_count += 1
                    break

        elif action.type == QUIT:
            run = False

    if score == score_to_get:
        run = False

    if draw_hang_count == 1:
        if draw1 == 0:
            draw_hang_count = 1
            pygame.draw.circle(screen, (255, 255, 255), (600, 100), 20)
            draw1 += 1

    if draw_hang_count == 2:
        if draw2 == 0:
            draw_hang_count = 2
            pygame.draw.line(screen, (255, 255, 255), (600, 100), (600, 200), 20)
            draw2 += 1

    if draw_hang_count == 3:
        if draw3 == 0:
            draw_hang_count = 3
            pygame.draw.line(screen, (255, 255, 255), (600, 120), (550, 170), 12)
            draw3 += 1

    if draw_hang_count == 4:
        if draw4 == 0:
            draw_hang_count = 4
            pygame.draw.line(screen, (255, 255, 255), (600, 120), (650, 170), 12)
            draw4 += 1
    if draw_hang_count == 5:
        if draw5 == 0:
            draw_hang_count = 5
            pygame.draw.line(screen, (255, 255, 255), (596, 200), (550, 250), 12)
            draw5 += 1

    if draw_hang_count == 6:
        draw_hang_count = 6
        pygame.draw.line(screen, (255, 255, 255), (605, 200), (650, 250), 12)
        pygame.display.update()
        time.sleep(3)
        text = font.render('You Lose', True, (255, 255, 255), (0, 0, 0))
        screen.blit(text, (275, 500 // 2))
        pygame.display.update()
        time.sleep(3)
        run = False
