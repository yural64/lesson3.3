import pygame # импорт модуля
import random

pygame.init() # инициализация модуля

# создаем константы для игрового окна

SCREEN = "Main screen"
TARGET = "Main target"

SCREEN.WIDTH = 800 # ширина окна 800 пикселей
SCREEN.HEIGHT = 600 # высота окна 600 пикселей
screen = pygame.display.set_mode((SCREEN.WIDTH, SCREEN.HEIGHT)) # отрисовка экрана

pygame.display.set_caption("Игра Тир") # заголовок экрана
icon = pygame.image.load("img/lesson3_tir.jpg") # иконка окна
pygame.display.set_icon(icon)

# создаем объект - цель для стрельбы

target_img = pygame.image.load("img/target.png")

# ширина и высота изображения

TARGET.WIDTH = 50
TARGET.HEIGHT = 50

target_x = random.randint(0, SCREEN.WIDTH - TARGET.WIDTH)
target_y = random.randint(0, SCREEN.HEIGHT - TARGET.HEIGHT)

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) # рандомный фоновый цвет

# игровой цикл

running = True
while running:
    pass # пустой оператор (заглушка)

pygame.quit() # ф-я выхода из игры как только завершится цикл
