from actor import *
from actorManager import *


class Player(Actor):
    def __init__(self, idObj, name, x, y, w, h, scale, sprites, surface, actor_manager, moveType):
        super().__init__(idObj, name, x, y, w, h, scale, sprites, surface, actor_manager)
        self.moveType = moveType
        self.x = x+8
        self.y = y+8
        self.prev_x = x
        self.prev_y = y
        self.w = w-4
        self.h = h-4
        self.keyCounter = 0

    def draw(self):
        self.surface.blit(self.sprites, (self.x-12,self.y-12) )
        return super().draw()

    
    def update(self):
        self.prev_x = self.x
        self.prev_y = self.y

        self.move_AWSD() 

        #if self.moveType == 0 :
            #self.move_AWSD() 
        #elif self.moveType == 1 :
        #    self.move_ARROWS()


        for obj in self.actor_manager.actors_obj:
            if obj.collision == True and obj != self:
                if self.check_collision(obj):
                    if obj.name == "key":
                        self.keyCounter += 1
                        self.actor_manager.destroy(obj, "obj")
                    if obj.name == "chest":
                        obj.alive = False
                    if obj.name == "door" and self.keyCounter > 0:
                        self.keyCounter -= 1
                        self.actor_manager.destroy(obj, "obj")
                    else:
                        self.x = self.prev_x
                        self.y = self.prev_y

        for obj in self.actor_manager.actors_entities:
            if obj.collision == True and obj != self:
                if self.check_collision(obj):
                    if obj.name == "enemy":
                        self.alive = False        
                        
        for obj in self.actor_manager.actors_blocks:
            if obj.collision == True and obj != self:
                if self.check_collision(obj):
                    self.x = self.prev_x
                    self.y = self.prev_y


        return super().update()