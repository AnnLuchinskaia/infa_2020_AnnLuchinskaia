# Ввод имени игрока
name = input('Your name: ')
import pygame
from pygame.draw import *
from random import randint
pygame.init()
# Переменные для изображения счета
font = pygame.font.Font(None, 60)
FPS = 50
width = 800
length = 800
# Создание экрана
pygame.display.set_caption('Pac-Man')
screen = pygame.display.set_mode((width, length))
# Кортежb цветjd, который будет использован в игре
YELLOW = (230, 230, 0)
BLUE = (0, 0, 204)
# Загрузка и расположение фоновой картинки
back_position = [0, 0]
back_image = pygame.image.load('Фон.jpg').convert()
# Загрузка фоновой музыки
pygame.mixer.music.load('Музыка.mp3')
pygame.mixer.music.play(loops=-1)
x = 100
y = 100
global x, y 

#Функция, рисующая стены лабиринта по клеткам
def rec(a, b, c, d):
    pygame.draw.rect(screen, BLUE, (a*40+x,b*40+100, 40*c, 40*d))
    

#Функция, рисующая лабиринт
def lab():
    rec(0, 0, 1, 15)
    rec(0, 0, 15, 1)
    rec(14, 0, 1, 15)
    rec(0, 14, 15, 1)
    rec(2, 2, 1, 4)
    rec(3, 5, 1, 1)
    rec(4, 2, 1, 2)
    rec(5, 3, 1, 2)
    rec(6, 1, 3, 1)
    rec(7, 2, 1, 3)
    rec(9, 3, 1, 2)
    rec(10, 2, 1, 2)
    rec(11, 5, 1, 1)
    rec(12, 2, 1, 4)
    rec(2, 7, 1, 2)
    rec(3, 7, 1, 1)
    rec(5, 6, 2, 1)
    rec(5, 7, 1, 3)
    rec(4, 9, 1, 2)
    rec(5, 9, 2, 1)
    rec(6, 8, 3, 1)
    rec(8, 9, 3, 1)
    rec(10, 10, 1, 1)
    rec(9, 6, 1, 3)
    rec(8, 6, 1, 1)
    rec(11, 7, 2, 1)
    rec(12, 8, 1, 1)
    rec(2, 10, 1, 3)
    rec(3, 12, 1, 1)
    rec(5, 12, 2, 1)
    rec(6, 11, 1, 1)
    rec(8, 11, 1, 2)
    rec(9, 12, 1, 1)
    rec(11, 12, 1, 1)
    rec(12, 10, 1, 3)

      
#Функция, рисующая мишени        
def circ():
    for i in range(15):
        for j in range(15):
            pygame.draw.circle(screen, YELLOW, 
                   (40*i+120, 40*j+120), 5)
    

# Класс, в котором находятся фукции, необходимые для движения объектов
class Target:
    def __init__(self, screen, width, length):
        '''
        Функция задает начальные координаты объектов и их скорость 
        self - ссылка на объект 
        screen - объект pygame.display
        width - ширина окна игры
        length - длина окна игры 
        '''
        self.x = 0
        self.y = 0
        self.screen = screen
        self.v_x = 0
        self.v_y = 0
        self.rect = (self.x, self.y)
        
    
    def move(self):
        '''
        Функция задает равномерное движение объектов
        self - ссылка на объект 
        '''
        self.x += self.v_x
        self.y += self.v_y
        self.rect = (self.x, self.y)

    
# Класс объектов             
class Pictures(Target):
    def __init__(self, screen, width, length, a):
        '''
        Функция загружает изображения, 
        задает их размеры, начальные координаты и скорость
        self - ссылка на объект 
        screen - объект pygame.display
        width - ширина окна игры
        length - длина окна игры 
        '''
        super().__init__(screen, width, length)
        if a == 1:
            self.image = pygame.image.load('Призрак1.png')
        elif a == 2:
            self.image = pygame.image.load('Призрак2.png')
        elif a == 3:
            self.image = pygame.image.load('Призрак3.png')
        else:
            self.image = pygame.image.load('Пакман.png')
        self.scal = 30
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (self.scal, self.scal))
        
        
    def draw(self):
        ''''
        Функция рисует объекты
        self - ссылка на объект
        '''
        screen.blit(self.image, self.rect)
        
# Функция, рисующая счет        
def score(Score):
    '''
    Функция пишет в углу счет игрока
    Score - количество набранных игроком очков 
    '''
    text = font.render("Score: " + str(Score), True, YELLOW)
    screen.blit(text, (10, 10))


clock = pygame.time.Clock()
finished = False
Score =  0 
screen.blit(back_image, back_position)


# Создание изображений 
while not finished:
    clock.tick(FPS) 
    screen.blit(back_image, back_position)
    circ()
    for i in range(4):
        pictures = Pictures(screen, width, length, i)
        if i == 1:
            pictures.x = 385
            pictures.y = 385
        elif i == 2:
            pictures.x = 345
            pictures.y = 385
        elif i == 3:
            pictures.x = 425
            pictures.y = 385
        else:
            pictures.x = 385
            pictures.y = 465
        pictures.move()
        pictures.draw()        
    score(Score) 
    lab()
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True  
                    
                
# Занесение результатов игры в файл                   
file = open('results.txt', 'a')
file.write(name +': ' + str(Score) + '\n')
file.close()
    
pygame.quit()
