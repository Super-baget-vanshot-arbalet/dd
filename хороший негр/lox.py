from pygame import *

window  = display.set_mode((700,500))
display.set_caption("ПОЙМАЙ ХОЛОПА")
background = transform.scale(image.load("galaxy.jpg"),(700 , 500))



class GameSprite(sprite.Sprite):
    def __init__(self, player_image ,player_x ,player_y, player_speed, size_x,size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(size_x,size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.direction = "right"
    def reset(self):
        window.blit(self.image , (self.rect.x , self.rect.y))
    def colliderect(self, rect):
        return self.rect.colliderect(rect)

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
     
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y <  340 - 80:
            self.rect.y += self.speed
        



class Enemy(GameSprite):
    
    def update(self):

        if self.rect.y <= 470:
            self.direction = "right"
        if self.rect.y >= 0:
            self.direction = "left"

        if self.direction == "left":
            self.rect.y += self.speed
        else:
            self.rect.y -= self.speed



speed_x = 3
speed_y = 3
speed_y1 = 3


hero = Player("rocket.png",0,0,5,50,250)
cyborg = Enemy("ufo.png",650,0,5,50,250)
treasure = GameSprite("bullet.png",500,400,5,50,50)
        


clock = time.Clock()
FPS = 60

game = True 
while game :
    
    window.blit(background,(0,0))
    for  e in event.get():
        if e.type == QUIT:
            game = False
    treasure.rect.x += speed_x 
    treasure.rect.y += speed_y 
    cyborg.rect.y += speed_y1

    if treasure.colliderect(hero.rect):
        speed_x *= -1 
    if treasure.colliderect(cyborg.rect):
        speed_x *= -1 
     

    if treasure.rect.y < 650:
        speed_y *= -1
    if cyborg.rect.x > -280:
        speed_y1 *= -1
    
    if treasure.rect.y < 0:
        speed_y *= -1




    
    hero.reset()
    cyborg.reset()
    treasure.reset()

    hero.update()
    cyborg.update()



    clock.tick(FPS)
    display.update()
