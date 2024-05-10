from pygame import *

class Actor:
    def __init__(self, idObj, name, x, y, w, h, scale, sprites, surface, actor_manager):
        self.idObj = idObj
        self.name = name
        self.x = x
        self.y = y
        self.prev_x = x
        self.prev_y = y
        self.w = w
        self.h = h
        self.scale = scale
        self.sprites = sprites
        self.surface = surface
        self.actor_manager = actor_manager
        self.ControllableKeyboard = False
        self.taked = False
        self.collision = True
        self.alive = True
    def draw(self):
        #self.showRect()
        pass

        
    def update(self):
        pass

    def check_collision(self, otherObj):
        return (
            (self.x <= otherObj.x + otherObj.w * otherObj.scale) and
            (self.x + self.w * self.scale >= otherObj.x) and
            (self.y <= otherObj.y + otherObj.h * otherObj.scale) and
            (self.y + self.h * self.scale >= otherObj.y)
        )

    def move_AWSD(self):
        keys = key.get_pressed()

        if keys[K_w]:
            self.y -= 5
        if keys[K_s]:
            self.y += 5
        if keys[K_a]:
            self.x -= 5
        if keys[K_d]:
            self.x += 5

    def move_ARROWS(self):
        keys = key.get_pressed()

        if keys[K_UP]:
            self.y -= 5
        if keys[K_DOWN]:
            self.y += 5
        if keys[K_LEFT]:
            self.x -= 5
        if keys[K_RIGHT]:
            self.x += 5

    def showRect(self):
        draw.rect(self.surface, (255,255,255), (self.x, self.y, self.w*self.scale, self.h*self.scale), 1)
