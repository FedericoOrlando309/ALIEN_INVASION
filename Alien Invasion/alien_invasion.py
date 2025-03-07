import sys
import pygame

from pygame.sprite import Group

from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from game_stats import GameStats


def run_game():
    # Initialize pygame, settings, and screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    # create an istatnce to store game statistics
    stats = GameStats(ai_settings)

    # set the background colour
    bg_color = (230, 230, 230)

    # Make a ship
    ship = Ship(ai_settings, screen)
    # Make a group to store bullets in 
    bullets = Group()
    aliens = Group()

    #create the fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # make an alien
    alien = Alien(ai_settings, screen)

    # start the main loop for the game
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        
        if stats.game_active:
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
            gf.update_screen(ai_settings, screen, ship, aliens, bullets)

        # Get rid of bullets that have disappeared
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        print(len(bullets))

        # Watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Redraw the screen during each pass through the loop
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        # make the most recently drawn screen visible
        pygame.display.flip()


run_game()

# PAGE 324