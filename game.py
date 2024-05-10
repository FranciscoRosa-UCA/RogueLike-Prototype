from pygame import *
from actorManager import *
from spriteManager import *

from player import *
from block import *
from door import *
from key import *
from enemy import *
from chest import *

from math import *
from random import *

pygame.init()
screen =  pygame.display.set_mode((640, 640))
actor_manager = ActorManager(game=None)

ruta_imagen = "./assets/jerom.png"
sprite_sheet_image = pygame.image.load(ruta_imagen).convert_alpha()
sprite_sheet = SpriteSheet(sprite_sheet_image)





running = True
clock = pygame.time.Clock()
dt = 0

count = 3


spawn = [0,0]

def load_map(blocks, objects):
    global spawn

    for y in range(len(blocks)):
        for x in range(len(blocks[0])):
            var = blocks[y][x]
            idObj = 1
            name="block"
            name="wall"
            actor_type = "blocks"
            collision = True

            if var == 0:
                idObj =  26
                name="floor"
                collision = False
                actor_type = "bg"

            elif var == 1:
                idObj =  21
                
            elif var == 2:
                idObj =  22
                
            elif var == 3:
                idObj =  23
                
            elif var == 4:
                idObj =  31
                
            elif var == 5:
                idObj =  32
                
            elif var == 6:
                idObj =  33
                
            elif var == 7:
                idObj =  41
                
            elif var == 8:
                idObj =  42
                
            elif var == 9:
                idObj =  43
                
            elif var == 10:
                idObj =  24
            elif var == 11:
                idObj =  25
            elif var == 12:
                idObj =  34
            elif var == 13:
                idObj =  35

            elif var == 14:
                idObj =  45

            column = (idObj % 10)-1
            row = idObj // 10
            scale = 4

            actor_manager.add( Block(idObj=count, name=name, x=x*16*scale, y=y*16*scale, w=16, h=16, scale=scale, sprites=sprite_sheet.get_image(row, column, 16,16, scale, (0,0,0)), surface=screen, actor_manager=actor_manager,  collision=collision), actor_type)


    for y in range(len(objects)):
        for x in range(len(objects[0])):
            var = objects[y][x]
            if var != 0:
                idObj = 1
                name="block"
                if var == 1:
                    idObj =  5
                    name="door"
                    collision = True          
                    column = (idObj % 10)-1
                    row = idObj // 10
                    scale = 4
                    actor_manager.add( Door(idObj=count, name=name, x=x*16*scale, y=y*16*scale, w=16, h=16, scale=scale, sprites=sprite_sheet.get_image(row, column, 16,16, scale, (0,0,0)), surface=screen, actor_manager=actor_manager,  collision=collision), "obj")
                elif var == 2:
                    idObj =  83
                    name="key"
                    collision = True
                    column = (idObj % 10)-1
                    row = idObj // 10
                    scale = 4
                    actor_manager.add( Key(idObj=count, name=name, x=x*16*scale, y=y*16*scale, w=16, h=16, scale=scale, sprites=sprite_sheet.get_image(row, column, 16,16, scale, (0,0,0)), surface=screen, actor_manager=actor_manager,  collision=collision), "obj")
                elif var == 3:
                    idObj =  214
                    name="enemy"
                    collision = True
                    column = (idObj % 10)-1
                    row = idObj // 10
                    scale = 4
                    actor_manager.add( Enemy(idObj=count, name=name, x=x*16*scale, y=y*16*scale, w=16, h=16, scale=scale, sprites=sprite_sheet.get_image(row, column, 16,16, scale, (0,0,0)), surface=screen, actor_manager=actor_manager,  collision=collision), "entities")
                elif var == 4:
                    idObj =  85
                    name="chest"
                    collision = True
                    column = (idObj % 10)-1
                    row = idObj // 10
                    scale = 4
                    actor_manager.add( Chest(idObj=count, name=name, x=x*16*scale, y=y*16*scale, w=16, h=16, scale=scale, sprites=sprite_sheet.get_image(row, column, 16,16, scale, (0,0,0)), surface=screen, actor_manager=actor_manager,  collision=collision), "obj")
                
                elif var == -1:
                    idObj = 196
                    column = (idObj % 10)-1
                    row = idObj // 10
                    actor_manager.add( Player(idObj=1, name="player", x=x*16*scale, y=y*16*scale, w=16, h=16, scale=4, sprites=sprite_sheet.get_image(row, column, 16,16,4,(0,0,0)), surface=screen, actor_manager=actor_manager, moveType=0), "entities")
                    spawn = [x*16*scale, y*16*scale]



map=[
    [1 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,3 ],
    [4 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,6 ],
    [4 ,0 ,0 ,1 ,2 ,2 ,2 ,2 ,3 ,0 ,0 ,0 ,0 ,14,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,6 ],
    [4 ,0 ,0 ,4 ,0 ,0 ,0 ,0 ,6 ,0 ,0 ,0 ,0 ,0 ,1 ,2 ,2 ,2 ,2 ,2 ,2 ,3 ,0 ,0 ,0 ,0 ,6 ],
    [4 ,0 ,0 ,4 ,0 ,0 ,0 ,0 ,6 ,0 ,0 ,14,0 ,0 ,4 ,0 ,0 ,0 ,0 ,0 ,0 ,6 ,0 ,0 ,0 ,0 ,6 ],
    [4 ,0 ,0 ,7 ,2 ,0 ,2 ,2 ,9 ,0 ,0 ,0 ,0 ,0 ,4 ,0 ,0 ,0 ,0 ,1 ,2 ,3 ,0 ,0 ,0 ,0 ,6 ],
    [4 ,0 ,1 ,9 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,4 ,0 ,14,0 ,0 ,4 ,0 ,6 ,0 ,0 ,0 ,0 ,6 ],
    [4 ,1 ,13,0 ,0 ,0 ,7 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,13,0 ,0 ,0 ,0 ,7 ,2 ,9 ,0 ,0 ,0 ,0 ,6 ],
    [4 ,4 ,0 ,0 ,0 ,0 ,0 ,0 ,14,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,6 ],
    [4 ,7 ,2 ,2 ,11,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,2 ,2 ,2 ,9 ,0 ,0 ,0 ,6 ],
    [4 ,0 ,0 ,0 ,1 ,2 ,3 ,0 ,0 ,0 ,0 ,14,0 ,0 ,0 ,0 ,0 ,1 ,3 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,6 ],
    [4 ,0 ,0 ,0 ,4 ,0 ,6 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,4 ,6 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,6 ],
    [4 ,0 ,0 ,0 ,7 ,2 ,9 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,7 ,9 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,6 ],
    [7 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2, 9 ]
] 


map1=[
    [1,2,2,2,2,2,2,2,2,3],
    [4,0,0,0,0,6,0,0,0,6],
    [4,0,0,0,0,6,0,0,0,6],
    [4,0,0,0,0,6,0,0,0,6],
    [4,2,2,0,2,9,0,0,0,6],
    [4,0,0,0,0,0,0,0,0,6],
    [4,0,0,0,0,0,0,0,0,6],
    [4,0,0,0,0,0,0,0,0,6],
    [4,0,0,0,0,0,0,0,0,6],
    [7,2,2,2,2,2,2,2,2,9]
]


map2=[
    [1,2,2,2,2,2,2,2,2,3],
    [4,0,0,0,14,0,0,0,0,6],
    [4,0,0,0,0,14,0,0,0,6],
    [4,0,0,0,0,0,14,0,0,6],
    [4,2,2,2,2,0,2,2,0,6],
    [4,0,0,0,0,0,14,0,0,6],
    [4,0,0,0,0,14,0,0,0,6],
    [4,0,0,0,14,0,0,0,0,6],
    [4,0,0,0,0,0,0,0,0,6],
    [7,2,2,2,2,2,2,2,2,9]
]


map3=[
    [1,2,2,2,2,2,2,2,2,3],
    [4,0,0,0,0,0,0,0,0,6],
    [4,0,0,14,0,0,0,14,0,6],
    [4,0,0,0,14,0,0,0,0,6],
    [4,0,14,0,14,0,14,0,0,6],
    [4,0,0,0,0,0,0,0,0,6],
    [4,0,0,0,0,14,0,0,0,6],
    [4,0,14,0,0,0,14,0,0,6],
    [4,0,0,0,0,0,0,0,0,6],
    [7,2,2,2,2,2,2,2,2,9]
]

objectsMap=[
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,3,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
] 

objectsMap1=[
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,4,3,0,0,0,0,0,0],
    [0,3,0,3,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,3,0],
    [0,0,0,1,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,2,0,0],
    [0,0,0,-1,0,3,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,3,0,0,0,0,3,0,0],
    [0,0,0,0,0,0,0,0,0,0]
]

objectsMap2=[
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,-1,0,0,0,0,0,4,0],
    [0,3,0,0,3,0,0,0,3,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,1,0],
    [0,0,0,3,0,0,0,0,0,0],
    [0,2,3,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,3,0,0,0,0,3,0,0],
    [0,0,0,0,0,0,0,0,0,0]
]

objectsMap3=[
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,1,0,3,0,3,0,0],
    [0,0,4,0,0,0,3,0,3,0],
    [0,0,3,0,0,0,0,0,0,0],
    [0,0,0,3,0,3,0,3,0,0],
    [0,3,0,0,0,0,0,0,0,0],
    [0,0,3,0,3,0,0,0,0,0],
    [0,0,0,0,2,3,0,3,0,0],
    [0,0,0,3,3,3,0,0,-1,0],
    [0,0,0,0,0,0,0,0,0,0]
]

load_map(map1, objectsMap1)


#actor2 = Player(idObj=2, name="player", x=400, y=200, w=16, h=16, scale=4, sprites=sprite_sheet.get_image(row, column, 16,16,4,(0,0,0)), surface=screen, actor_manager=actor_manager, moveType=1)

#actor_manager.add(actor2, "entities")

level = 0

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False


    actor_manager.update()
    
    keys = key.get_pressed()
    if keys[K_ESCAPE]:
        running = False
    if keys[K_1]:
        idObj = randint(0, 279)
        column = (idObj % 10)
        row = idObj // 10
        scale = randint(1,6)
        ##actor_manager.add( Block(idObj=count, name="actor", x=randint(0, 1920), y=randint(0, 1080), w=16, h=16, scale=scale, sprites=sprite_sheet.get_image(row, column, 16,16, scale, (0,0,0)), surface=screen, actor_manager=actor_manager, collision=False))
        count += 1

    #if actor1.alive == False:
    #    running = False
    for entitie in actor_manager.actors_entities:
        if entitie.name == "player" and entitie.alive == False:
            actor_manager.destroyAll("bg")
            actor_manager.destroyAll("obj")
            actor_manager.destroyAll("entities")
            actor_manager.destroyAll("blocks")
            if level == 0:
                load_map(map1, objectsMap1)
            if level == 1:
                load_map(map2, objectsMap2)
            if level == 2:
                load_map(map3, objectsMap3)
            entitie.x, entitie.y = spawn[0], spawn[1]
            entitie.alive = True

    for entitie in actor_manager.actors_obj:
        if entitie.name == "chest" and entitie.alive == False:
            actor_manager.destroyAll("bg")
            actor_manager.destroyAll("obj")
            actor_manager.destroyAll("entities")
            actor_manager.destroyAll("blocks")
            level += 1
            level %= 3
            if level == 0:
                load_map(map1, objectsMap1)
            if level == 1:
                load_map(map2, objectsMap2)
            if level == 2:
                load_map(map3, objectsMap3)

    screen.fill((30,30,30))

    actor_manager.draw()

    pygame.display.flip()
    #pygame.event.pump()
    dt = clock.tick(60)

quit()