import pygame, sys
from button import Button
from main import main

pygame.init()

SCREEN = pygame.display.set_mode((1000, 520))
pygame.display.set_caption("Menu")

BG = pygame.image.load("ui/assets/img/Background.png")


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("ui/assets/font/font.ttf", size)


def play():
    main()



def help():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(12).render("Ayo Game is built with the ability for a Human and Computer Interraction.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(440, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_TEXT2 = get_font(12).render(
              "The Ayo Game follows the standard style of playing.", True, "Black")
        OPTIONS_RECT2 = OPTIONS_TEXT2.get_rect(center=(300, 300))
        SCREEN.blit(OPTIONS_TEXT2, OPTIONS_RECT2)

        OPTIONS_TEXT2 = get_font(12).render(
            "The Ayo Game follows the standard style of playing.", True, "Black")
        OPTIONS_RECT2 = OPTIONS_TEXT2.get_rect(center=(300, 300))
        SCREEN.blit(OPTIONS_TEXT2, OPTIONS_RECT2)

        OPTIONS_TEXT3 = get_font(12).render(
            "The Human starts the Game followed Computer.", True, "Black")
        OPTIONS_RECT3 = OPTIONS_TEXT3.get_rect(center=(270, 350))
        SCREEN.blit(OPTIONS_TEXT3, OPTIONS_RECT3)

        OPTIONS_BACK = Button(image=None, pos=(640, 460),
                              text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(50).render("MAIN MENU ", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(500, 50))

        PLAY_BUTTON = Button(image=pygame.image.load("ui/assets/img/Play Rect.png"), pos=(500, 200),
                             text_input="PLAY", font=get_font(45), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("ui/assets/img/Play Rect.png"), pos=(500, 320),
                                text_input="HELP", font=get_font(55), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("ui/assets/img/Play Rect.png"), pos=(500, 440),
                             text_input="QUIT", font=get_font(55), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    help()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        try:
            pygame.display.update()
        except pygame.error:
            print('')


main_menu()