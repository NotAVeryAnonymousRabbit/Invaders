import sys
import pygame

from settings import Settings
from gamestat import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from alien import Alien
import func as gf
#from gamechar import Pika
from pygame.sprite import Group




def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('mygame')
    play_button = Button(ai_settings,screen,"Play")

    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings,screen,stats)

    #ship making
    ship = Ship(ai_settings,screen)

    #bullet make
    bullets = Group()
    aliens = Group()

    # Background color.
    bg_color = (10, 40, 230)

    #make alien
    alien = Alien(ai_settings,screen)

    gf.create_fleet(ai_settings,screen,aliens,ship)

    # Start the main loop for the game.
    while True:
        gf.check_events(ai_settings,screen,sb,bullets,stats,play_button,ship,aliens)

        if stats.game_active:
            ship.update()


            bullets.update(aliens,bullets)
            for bullet in bullets.copy():
                if bullet.rect.bottom <= 0:
                    bullets.remove(bullet)
            gf.update_bullets(ai_settings, screen, aliens,stats,sb,ship, bullets)
            gf.update_aliens(aliens,ship,bullets,stats,sb,screen,ai_settings)
            print(len(bullets))



        #events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        #redraw
        screen.fill(ai_settings.bg_color)
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        alien.bliteme()
        pygame.display.flip()

run_game()