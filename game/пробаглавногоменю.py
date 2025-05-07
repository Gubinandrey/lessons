import pygame
import util


MAIN_MENU = 'main_menu'
LEVEL_SELECT = 'level_select'
START_MAP = 'start_map'


class Main_Menu:
    def __init__(self):
        self.bg = util.load('images/icons_menu/background.jpg', 0.8)
        self.bg.set_colorkey((255, 255, 255))
        # Кнопка "Play"
        self.play_button = Button(0.35, 750, 425, '/Users/andrey/python/lessons/game/images/icons_menu/play_button-no-bg-preview (carve.photos).png')


    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.play_button.is_hover:
            return LEVEL_SELECT
        return None


    def update(self):
        self.play_button.update()


    def draw(self, screen):
        screen.fill((255, 255, 255))
        screen.blit(self.bg, (0, 0))
        self.play_button.draw(screen)


class LevelSelectMenu:
    def __init__(self):
        self.bg = util.load('images/icons_menu/background_select_level.jpg', 1.1)
        self.bg.set_colorkey((255, 255, 255))
        self.buttons = []
        # создаём кнопки уровней
        x, y = 250, 300
        for level in range(1, 16):  # 3x5
            btn = LevelButton(level, x, y)
            self.buttons.append(btn)
            x += 380
            if level % 5 == 0:
                y += 283
                x = 250


    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for btn in self.buttons:
                if btn.rect.collidepoint(event.pos):
                    btn.on_click()
                    return START_MAP
        return None


    def update(self):
        for btn in self.buttons:
            btn.update()


    def draw(self, screen):
        screen.fill((255, 255, 255))
        screen.blit(self.bg, (0, 0))
        for btn in self.buttons:
            btn.draw(screen)


class StartMapMenu:
    def __init__(self):
        self.bg = util.load('images/icons_menu/start_LeVel_menu.jpg', 1.3)
        self.play_button = Button(0.75, 1350, 425, 'images/icons_menu/play_button_start.png')
        self.home_button = Button(0.24, 1370, 600, 'images/icons_menu/home_button.png')
        self.back_button = Button(0.498, 1360, 280, 'images/icons_menu/back_button.png')


    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.play_button.rect.collidepoint(event.pos):
                # Запуск уровня
                self.start_level()
            elif self.home_button.rect.collidepoint(event.pos):
                return MAIN_MENU
            elif self.back_button.rect.collidepoint(event.pos):
                return LEVEL_SELECT
        return None


    def update(self):
        self.play_button.update()
        self.home_button.update()
        self.back_button.update()


    def draw(self, screen):
        screen.fill((255, 255, 255))
        screen.blit(self.bg, (508, 200))
        self.play_button.draw(screen)
        self.home_button.draw(screen)
        self.back_button.draw(screen)


    def start_level(self):
        # Ваш код запуска уровня
        pass


class Button:
    def __init__(self, scale, x, y, image_path):
        self.rect=pygame.Rect(x, y, 120, 120)
        self.is_hover = False


    def update(self):
        self.is_hover = self.rect.collidepoint(pygame.mouse.get_pos())


    def draw(self, screen):
        pygame.draw.circle(screen, (192, 192, 192, 210), (self.rect.x, self.rect.y), 60)


class LevelButton(Button):
    def __init__(self, level_num, x, y):
        super().__init__(1.0, x-60, y-60, None)
        self.level_num = level_num
        self.radius = 60
        self.rect = pygame.Rect(x-60, y-60, 120, 120)
        self.font = pygame.font.Font(None, 100)
        self.color = (200, 50, 50)


    def update(self):
        super().update()
        # можно добавить анимацию цвета


    def draw(self, screen):
        pos = (self.rect.centerx, self.rect.centery)
        color = (180, 180, 180) if self.is_hover else self.color
        pygame.draw.circle(screen, color, pos, self.radius)
        text = self.font.render(str(self.level_num), True, (255, 255, 255))
        text_rect = text.get_rect(center=pos)
        screen.blit(text, text_rect)


    def on_click(self):
        # Сохранить выбранный уровень где-нибудь
        print(f"Level {self.level_num} selected")


def main():
    pygame.init()
    screen = pygame.display.set_mode((1920, 1080))
    clock = pygame.time.Clock()
    fps = 60


    menus = {
        MAIN_MENU: Main_Menu(),
        LEVEL_SELECT: LevelSelectMenu(),
        START_MAP: StartMapMenu(),
    }
    state = MAIN_MENU
    running = True


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            else:
                next_state = menus[state].handle_event(event)
                if next_state:
                    state = next_state
                    pygame.event.clear()


        menus[state].update()
        menus[state].draw(screen)
        pygame.display.flip()
        clock.tick(fps)


    pygame.quit()


if __name__ == '__main__':
    main()





