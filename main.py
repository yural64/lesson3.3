import pygame # импорт модуля
import random

pygame.init() # инициализация модуля

# создаем константы для игрового окна

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# создаем окно
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Игра Тир") # заголовок экрана
icon = pygame.image.load("img/lesson3_tir.jpg") # иконка окна
pygame.display.set_icon(icon)

# создаем объект - цель для стрельбы

target_img = pygame.image.load("img/target.png")

# ширина и высота изображения

TARGET_WIDTH = 50
TARGET_HEIGHT = 50

target_x = random.randint(0, SCREEN_WIDTH - TARGET_WIDTH)
target_y = random.randint(0, SCREEN_HEIGHT - TARGET_HEIGHT)

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) # рандомный фоновый цвет

# игровой цикл

running = True
while running:
    pass # пустой оператор (заглушка)

pygame.quit() # ф-я выхода из игры как только завершится цикл
