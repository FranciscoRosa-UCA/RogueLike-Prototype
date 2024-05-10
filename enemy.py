from actor import *
from actorManager import *


class Enemy(Actor):
    def __init__(self, idObj, name, x, y, w, h, scale, sprites, surface, actor_manager, collision):
        super().__init__(idObj, name, x, y, w, h, scale, sprites, surface, actor_manager)
        self.collision = collision
        self.x = x+8
        self.y = y+8
        self.prev_x = x
        self.prev_y = y
        self.w = w-4
        self.h = h-4

    def draw(self):
        self.surface.blit(self.sprites, (self.x-10,self.y-10) )
        return super().draw()

    
    def update(self):
        return super().update()