import pygame # импорт модуля
import random

pygame.init() # инициализация модуля pygame
pygame.mixer.init() # инициализация модуля звука

# загрузка звука
shot_sound = pygame.mixer.Sound('img/Winchester12-RA_The_Sun_God-1722751268.wav')
# создаем константы для игрового окна

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# создаем окно
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
font = pygame.font.Font(None, 36)

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

# инициализация счетчика попаданий
hits = 0

# игровой цикл

running = True
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # Воспроизведение звука
            shot_sound.play()

            if target_x < mouse_x < target_x + TARGET_WIDTH and target_y < mouse_y < target_y + TARGET_HEIGHT:

                # увеличиваем счетчик попаданий
                hits += 1
                print(f'Попаданий: {hits}')

                # перемещаем цель на новое случайное место
                target_x = random.randint(0, SCREEN_WIDTH - TARGET_WIDTH)
                target_y = random.randint(0, SCREEN_HEIGHT - TARGET_HEIGHT)

    # Отображение количества попаданий на экране
    text=font.render(f'Попаданий: {hits}', True, (255, 255, 255))
    screen.blit(text, (10, 10))

    # Отображение цели
    screen.blit(target_img, (target_x, target_y))
    pygame.display.update()
    
pygame.quit() # ф-я выхода из игры как только завершится цикл
