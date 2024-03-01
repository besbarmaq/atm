import pygame
import sys
import random
from Button import ImageButton

pygame.init()

Width, Height = 960, 600
max_fps = 60

balance = 0
accumulate_amount = 0

transaction_history = []


screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Menu")
main_background = pygame.image.load("images/background.jpg")
atm_background = pygame.image.load("images/bankomat1.1.png")
atm_background = pygame.transform.scale(atm_background, (Width, Height))
mine_background = pygame.image.load("images/mine_background.png")
mine_background = pygame.transform.scale(mine_background, (Width, Height))
transaction_background = pygame.image.load("images/transaction_background.jpg")
transaction_background = pygame.transform.scale(transaction_background, (Width, Height))

clock = pygame.time.Clock()

cursor = pygame.image.load("images/cursor.png")
pygame.mouse.set_visible(False)

def main_menu():
    start_button = ImageButton(Width / 2 - (252 / 2), 150, 252, 74, "WORK", "images/do.png", "images/posle.png","sound/click.wav")
    settings_button = ImageButton(Width / 2 - (252 / 2), 250, 252, 74, "SETTINGS", "images/do.png", "images/posle.png","sound/click.wav")
    exit_button = ImageButton(Width / 2 - (252 / 2), 350, 252, 74, "EXIT", "images/do.png", "images/posle.png","sound/click.wav")

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(main_background, (0, -300))

        font = pygame.font.Font(None, 72)
        text_surface = font.render("MENU", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(Width/2, 100))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.USEREVENT and event.button == start_button:
                fade()
                working()

            if event.type == pygame.USEREVENT and event.button == settings_button:
                fade()
                settings_menu()


            if event.type == pygame.USEREVENT and event.button == exit_button:
                running = False
                pygame.quit()
                sys.exit()

            for btn in [start_button, settings_button, exit_button]:
                btn.handle_event(event)

        for btn in [start_button, settings_button, exit_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

            x, y = pygame.mouse.get_pos()
            screen.blit(cursor, (x-1,y-1))

        pygame.display.flip()

def working():

    global balance

    back_button = ImageButton(10, 10, 50, 50, "", "images/back.png", "images/back.png","sound/click.wav")
    work_button = ImageButton( Width - 252 - 10, Height - 74 - 10, 252, 74, "WORK", "images/do.png", "images/posle.png","sound/click.wav")
    bank_button = ImageButton(10,Height - 74 - 10 , 252, 74, "GO TO BANK", "images/do.png", "images/posle.png","sound/click.wav")
    history_button = ImageButton(Width - 180, 10, 170, 50, "HISTORY", "images/do.png", "images/posle.png","sound/click.wav")
    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(mine_background, (0, 0))

        font = pygame.font.Font(None, 36)
        text_surface = font.render("BALANCE: $" + str(balance), True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(Width / 2, 30))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                fade()
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    fade()

            if event.type == pygame.USEREVENT and event.button == work_button:
                amount = random.randint(1, 100)
                balance += amount
                transaction_history.append(f"Worked and earned ${amount}")

            if event.type == pygame.USEREVENT and event.button == bank_button:
                fade()
                new_game()

            if event.type == pygame.USEREVENT and event.button == history_button:
                fade()
                show_history()

            if event.type == pygame.USEREVENT and event.button == back_button:
                running = False
                fade()

            for btn in [back_button, bank_button, work_button , history_button]:
                btn.handle_event(event)

        for btn in [back_button, bank_button, work_button , history_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

            x, y = pygame.mouse.get_pos()
            screen.blit(cursor, (x - 2, y - 2))

        pygame.display.flip()

def settings_menu():
    audio_button = ImageButton(Width / 2 - (252 / 2), 150, 252, 74, "BUTTON", "images/do.png", "images/posle.png","sound/click.wav")
    video_button = ImageButton(Width / 2 - (252 / 2), 250, 252, 74, "BUTTON", "images/do.png", "images/posle.png","sound/click.wav")
    back_button = ImageButton(Width / 2 - (252 / 2), 350, 252, 74, "BACK", "images/do.png", "images/posle.png","sound/click.wav")

    running = True
    while running:
        screen.fill((0,0,0))
        screen.blit(main_background, (0,0))

        font = pygame.font.Font(None, 72)
        text_surface = font.render("SETTINGS", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(Width / 2, 100))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                fade()
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    fade()

            if event.type == pygame.USEREVENT and event.button == back_button:
                running = False
                fade()

            for btn in [audio_button, video_button, back_button]:
                btn.handle_event(event)

        for btn in [audio_button, video_button, back_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

            x, y = pygame.mouse.get_pos()
            screen.blit(cursor, (x - 2, y - 2))

        pygame.display.flip()

def new_game():
    global balance, transaction_history, accumulate_amount

    input_button = ImageButton(678, 275, 40, 40, "", "images/icon.png", "images/icon.png", "sound/click.wav")
    back_button = ImageButton(10, 10, 50, 50, "", "images/back1.png", "images/back1.png", "sound/click.wav")
    output_button = ImageButton(300, 380, 50, 50, "", "images/icon1.webp", "images/icon1.webp", "sound/click.wav")

    running = True
    while running:
        screen.fill((0,0,0))
        screen.blit(atm_background, (0,0))

        font = pygame.font.Font(None, 36)
        text_surface = font.render("BALANCE: $" + str(balance), True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(Width / 2, 30))
        screen.blit(text_surface, text_rect)

        text_surface = font.render("ACCUMULATED: $" + str(accumulate_amount), True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(Width / 2, 90))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                fade()
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    fade()

            if event.type == pygame.USEREVENT and event.button == back_button:
                running = False
                fade()

            if event.type == pygame.USEREVENT and event.button == input_button:
                accumulate_amount += balance
                transaction_history.append(f"Deposited ${balance}")
                balance = 0

            if event.type == pygame.USEREVENT and event.button == input_button:
                accumulate_amount += balance
                transaction_history.append(f"Deposited ${balance}")

            if event.type == pygame.USEREVENT and event.button == output_button:
                balance += accumulate_amount
                transaction_history.append(f"Withdrew ${accumulate_amount} to balance")
                accumulate_amount = 0

            for btn in [back_button, input_button , output_button]:
                btn.handle_event(event)

        for btn in [back_button, input_button, output_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

            x, y = pygame.mouse.get_pos()
            screen.blit(cursor, (x - 2, y - 2))

        pygame.display.flip()

def show_history():
    back_button = ImageButton(10, 10, 50, 50, "", "images/back1.png", "images/back1.png", "sound/click.wav")
    running = True
    while running:
        screen.fill((0,0,0))
        screen.blit(transaction_background, (0, 0))

        font = pygame.font.Font(None, 36)
        text_surface = font.render("TRANSACTION HISTORY", True, (0,0,0))
        text_rect = text_surface.get_rect(center=(Width / 2, 50))
        screen.blit(text_surface, text_rect)

        y_offset = 100
        for transaction in transaction_history:
            text_surface = font.render(transaction, True, (0,0,0))
            text_rect = text_surface.get_rect(center=(Width / 2, y_offset))
            screen.blit(text_surface, text_rect)
            y_offset += 30

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                fade()
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    fade()

            if event.type == pygame.USEREVENT and event.button == back_button:
                running = False
                fade()

            for btn in [back_button]:
                btn.handle_event(event)

        for btn in [back_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

            x, y = pygame.mouse.get_pos()
            screen.blit(cursor, (x - 2, y - 2))

        pygame.display.flip()

def fade():
    running = True
    fade_alpha = 0            #Уровень прозрачности для анимации
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        fade_surface = pygame.Surface((Width, Height))
        fade_surface.fill((0,0,0))
        fade_surface.set_alpha(fade_alpha)
        screen.blit(fade_surface, (0,0))

        fade_alpha += 5
        if fade_alpha >= 105:
            fade_alpha = 255
            running = False

        pygame.display.flip()
        clock.tick(max_fps)


if __name__ == "__main__":
    main_menu()
