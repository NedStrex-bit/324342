from pygame import *
class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(65,65))
        self.speed =player_speed
        self.rect=self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Player(GameSprite):
    def update(self):
        keys= key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width-80:
            self.rect.x += self.speed
window = display.set_mode((700,500))
background = transform.scale(image.load("Fon.jpg"),(700,500))
player=Player("1234.png",5,20,4)
clock = time.Clock()
FPS = 60
FPS=60
game=True
while game: 
    window.blit(background,(0,0))
    for e in event.get():
        if e.type == QUIT:
            game=False
    player.reset()
    clock.tick(FPS)
    display.update()