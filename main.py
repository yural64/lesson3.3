import pygame # импорт модуля

pygame.init() # инициализация модуля

# создаем константы для игрового окна

SCREEN.WIDTH = 800 # ширина окна 800 пикселей
SCREEN.HEIGHT = 600 # высота окна 600 пикселей
screen = pygame.display.set_mode((SCREEN.WIDTH, SCREEN.HEIGHT)) # отрисовка экрана

pygame.display.set_caption("Игра Тир") # заголовок экрана
icon = pygame.image.load("") # иконка окна

# игровой цикл

running = True
while running:
    pass # пустой оператор (заглушка)

pygame.quit() # ф-я выхода из игры как только завершится цикл
