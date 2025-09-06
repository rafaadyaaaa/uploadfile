from pygame import *
width = 700
heigth = 500
window = display.set_mode((width, heigth))
window.fill((255, 255, 0))
display.set_caption('Maze Game')

class GameSprite(sprite.Sprite): # superclass
    def _init_(self,picture,w,h,x,y): 
        super()._init_()
        self.image = transform.scale(image.load(picture), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Hero(GameSprite): # subclass
    def _init_(self, picture, w, h, x, y, x_speed,y_speed): 
        GameSprite._init_(self, picture, w, h, x, y)
        self.x_speed = x_speed
        self.y_speed = y_speed

    def update(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

pacman = Hero('hero.png', 80 ,80, 200, 250, 0, 0)
wall2 = GameSprite('platform2.png', 80 ,180, 300, 250)

run = True 
while run:
    window.fill((255, 255, 0))
    time.delay(50)
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_UP:
                pacman.y_speed = -5
            elif e.key == K_DOWN:
                pacman.y_speed = 5
            elif e.key == K_RIGHT:
                pacman.x_speed = 5
            elif e.key == K_LEFT:
                pacman.x_speed = -5

        elif e.type == KEYUP:
            if e.key == K_UP:
                pacman.y_speed = 0  
            elif e.key == K_DOWN:
                pacman.y_speed = 0
            elif e.key == K_RIGHT:
                pacman.x_speed = 0
            elif e.key == K_LEFT:
                pacman.x_speed = 0
    pacman.reset()
    wall2.reset()
    pacman.update()
    display.update()
display.update()