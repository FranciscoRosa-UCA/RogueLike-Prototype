from actor import *
from actorManager import *


class Key(Actor):
    def __init__(self, idObj, name, x, y, w, h, scale, sprites, surface, actor_manager, collision):
        super().__init__(idObj, name, x, y, w, h, scale, sprites, surface, actor_manager)
        self.collision = collision

    def draw(self):
        self.surface.blit(self.sprites, (self.x,self.y) )
        return super().draw()

    
    def update(self):
        return super().update()