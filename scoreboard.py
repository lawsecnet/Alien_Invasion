import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard():
    # class to report scoring information

    def __init__(self, ai_settings, screen, stats):
        # initialize scorekeeping attributes
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # font settings for scoring information
        self.text_color = (0, 255, 0)
        self.font = pygame.font.SysFont(None, 48)

        # prepare the initial score image and high score image
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        # turn the score into a rendered image
        rounded_score = int(round(self.stats.score, -1))
        score_sr = "{:,}".format(rounded_score)
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color,
        self.ai_settings.bg_color)

        # display the score at the top right corner
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 30
        self.score_rect.top = 30

    def show_score(self):
        # draw score and ships to the screen
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)

    def prep_high_score(self):
        # turn the high score into a rendered image
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True,
        self.text_color, self.ai_settings.bg_color)

        #center the high score at the top of teh screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        # render level value
        self.level_image = self.font.render(str(self.stats.level), True,
        self.text_color, self.ai_settings.bg_color)

        # position the level below the score_scale
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        # show remaining ships
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)
