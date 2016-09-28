import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # initialize game and create screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set.mode((ai_settings.screen_width,
    ai_settings.screen_height))
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")

    # make a ship
    ship = Ship(screen)

    bg_color = (230, 230, 230)

    # the main loop for the game
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)


run_game()
