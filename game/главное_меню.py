import pygame
import platform
from scripts import utils as util

pygame.init()

BASE_DIR = '/Users/andrey/python/lessons/game' if platform.system() == 'Darwin' else 'game'

STATE_MAIN_MENU = 'MAIN_MENU'
STATE_LEVEL_SELECT = 'LEVEL_SELECT'
STATE_START_MAP = 'START_MAP'

class Main_menu:
    def __init__(self):
        self.state = STATE_MAIN_MENU
        self.selected_level = None
        self.level_menu = Level_sekect_menu()
        self.start_map = Start_menu_map()
        self.bg_orig = util.load_image(f'{BASE_DIR}/images/icons_menu/background.jpg', 1)
        self.play_button = Button(0.35, 0.5, 0.5, f'{BASE_DIR}/images/icons_menu/play_button-no-bg-preview (carve.photos).png')

    def run(self, screen, fps, next_level, start, run_fn):
        clock = fps
        while True:
            clock.tick(80)
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)
            sw, sh = screen.get_size()
            screen.fill((255, 255, 255))

            if self.state == STATE_MAIN_MENU:
                bg = pygame.transform.scale(self.bg_orig, (sw, sh))
                screen.blit(bg, (0, 0))
                self.play_button.update(screen)
                self.play_button.render(screen)
                if self.play_button.clicked:
                    self.state = STATE_LEVEL_SELECT

            elif self.state == STATE_LEVEL_SELECT:
                clicked = self.level_menu.handle(screen, events)
                if clicked:
                    self.selected_level = clicked
                    self.state = STATE_START_MAP

            elif self.state == STATE_START_MAP:
                result = self.start_map.handle(screen, events, self.selected_level, next_level, start, run_fn)
                if result in (STATE_MAIN_MENU, STATE_LEVEL_SELECT):
                    self.state = result

            pygame.display.flip()

class Button:
    def __init__(self, scale, rel_x, rel_y, image_path):
        self.image_orig = util.load_image(image_path, scale)
        self.rel_x = rel_x
        self.rel_y = rel_y
        self.rect = self.image_orig.get_rect()
        self.clicked = False

    def update(self, screen):
        sw, sh = screen.get_size()
        self.rect = self.image_orig.get_rect(center=(int(self.rel_x * sw), int(self.rel_y * sh)))
        self.clicked = False
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                self.clicked = True

    def render(self, screen):
        screen.blit(self.image_orig, self.rect)

class Level_sekect_menu:
    def __init__(self):
        self.bg_orig = util.load_image(f'{BASE_DIR}/images/icons_menu/background_select_level.jpg', 1)
        self.color = [197, 20, 7]
        self.color_digit = [255, 255, 255]
        self.increment = [0.34375, 0.125, -0.04375]
        self.increment_digit = -1.275
        self.now_counting = True

    def handle(self, screen, events):
        sw, sh = screen.get_size()
        screen.fill((255, 255, 255))
        bg = pygame.transform.scale(self.bg_orig, (sw, sh))
        screen.blit(bg, (0, 0))

        # анимация цветов
        if self.now_counting:
            self.color[0] += self.increment[0]
            self.color[1] += self.increment[1]
            self.color[2] += self.increment[2]
            self.color_digit[0] += self.increment_digit
            if self.color[0] >= 252 or self.color[1] >= 40 or self.color[2] <= 0:
                self.now_counting = False
        else:
            self.color[0] -= self.increment[0]
            self.color[1] -= self.increment[1]
            self.color[2] -= self.increment[2]
            self.color_digit[0] -= self.increment_digit
            if self.color[0] <= 197 or self.color[1] <= 20 or self.color[2] >= 7:
                self.now_counting = True

        cols, rows = 5, 3
        margin_x, margin_y = sw * 0.1, sh * 0.2
        spacing_x = (sw - 2 * margin_x) / (cols - 1)
        spacing_y = (sh - 2 * margin_y) / (rows - 1)

        level = 1
        clicked_level = None
        font_size = int(sh * 0.1)
        font = pygame.font.Font(None, font_size)
        mouse_pos = pygame.mouse.get_pos()

        for row in range(rows):
            for col in range(cols):
                x = margin_x + col * spacing_x
                y = margin_y + row * spacing_y
                rect = pygame.Rect(x - 60, y - 60, 120, 120)

                if rect.collidepoint(mouse_pos):
                    color = (192, 192, 192)
                    for event in events:
                        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                            clicked_level = level
                else:
                    color = tuple(map(int, self.color))

                pygame.draw.circle(screen, color, (int(x), int(y)), 60)
                digit_surf = font.render(str(level), True, tuple(map(int, self.color_digit)))
                ds_rect = digit_surf.get_rect(center=(int(x), int(y)))
                screen.blit(digit_surf, ds_rect)

                level += 1

        return clicked_level

class Start_menu_map:
    def __init__(self):
        self.bg_orig = util.load_image(f'{BASE_DIR}/images/icons_menu/start_LeVel_menu.jpg', 1)
        self.play_button = Button(0.75, 0.75, 0.4, f'{BASE_DIR}/images/icons_menu/play_button_start_menu1.png')
        self.home_button = Button(0.24, 0.75, 0.55, f'{BASE_DIR}/images/icons_menu/home_button_to_play.png')
        self.back_button = Button(0.498, 0.75, 0.25, f'{BASE_DIR}/images/icons_menu/back_button_in_Start_menu_map_menu.png')

    def handle(self, screen, events, level, next_level, start, run_fn):
        sw, sh = screen.get_size()
        screen.fill((255, 255, 255))

        bg_w, bg_h = int(sw * 0.6), int(sh * 0.6)
        bg = pygame.transform.scale(self.bg_orig, (bg_w, bg_h))
        screen.blit(bg, ((sw - bg_w) // 2, (sh - bg_h) // 2))

        self.play_button.update(screen)
        self.play_button.render(screen)
        self.home_button.update(screen)
        self.home_button.render(screen)
        self.back_button.update(screen)
        self.back_button.render(screen)

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.play_button.clicked:
                    next_level(level)
                    start()
                elif self.home_button.clicked:
                    return STATE_MAIN_MENU
                elif self.back_button.clicked:
                    return STATE_LEVEL_SELECT

        return None