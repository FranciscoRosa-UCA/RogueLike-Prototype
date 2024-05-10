class ActorManager:
    def __init__(self, game):
        self.game = game
        self.actors_bg = []
        self.actors_blocks = []
        self.actors_obj = []
        self.actors_entities = []

    def add(self, actor, category):
        if category == 'bg':
            self.actors_bg.append(actor)
        elif category == 'blocks':
            self.actors_blocks.append(actor)
        elif category == 'obj':
            self.actors_obj.append(actor)
        elif category == 'entities':
            self.actors_entities.append(actor)

    def delete(self, actor, category):
        if category == 'bg' and actor in self.actors_bg:
            self.actors_bg.remove(actor)
        elif category == 'blocks' and actor in self.actors_blocks:
            self.actors_blocks.remove(actor)
        elif category == 'obj' and actor in self.actors_obj:
            self.actors_obj.remove(actor)
        elif category == 'entities' and actor in self.actors_entities:
            self.actors_entities.remove(actor)

    def destroy(self, actor, category):
        if category == 'bg' and actor in self.actors_bg:
            self.actors_bg.remove(actor)
            del actor
        elif category == 'blocks' and actor in self.actors_blocks:
            self.actors_blocks.remove(actor)
            del actor
        elif category == 'obj' and actor in self.actors_obj:
            self.actors_obj.remove(actor)
            del actor
        elif category == 'entities' and actor in self.actors_entities:
            self.actors_entities.remove(actor)
            del actor

    def destroyAll(self, category):
        if category == 'bg':
            while self.actors_bg:
                actor = self.actors_bg.pop()
                del actor
        elif category == 'blocks':
            while self.actors_blocks:
                actor = self.actors_blocks.pop()
                del actor
        elif category == 'obj':
            while self.actors_obj:
                actor = self.actors_obj.pop()
                del actor
        elif category == 'entities':
            while self.actors_entities:
                actor = self.actors_entities.pop()
                del actor

    def rewind(self, category):
        if category == 'bg' and self.num_actors('bg') != 0:
            return self.actors_bg[0]
        elif category == 'blocks' and self.num_actors('blocks') != 0:
            return self.actors_blocks[0]
        elif category == 'obj' and self.num_actors('obj') != 0:
            return self.actors_obj[0]
        elif category == 'entities' and self.num_actors('entities') != 0:
            return self.actors_entities[0]
        else:
            return None

    def next(self, category):
        actor = None
        if category == 'bg':
            actor = self.actors_bg[0] if self.num_actors('bg') != 0 else None
        elif category == 'blocks':
            actor = self.actors_blocks[0] if self.num_actors('blocks') != 0 else None
        elif category == 'obj':
            actor = self.actors_obj[0] if self.num_actors('obj') != 0 else None
        elif category == 'entities':
            actor = self.actors_entities[0] if self.num_actors('entities') != 0 else None
        return actor

    def current(self, category):
        actor = None
        if category == 'bg' and self.num_actors('bg') != 0:
            actor = self.actors_bg[0]
        elif category == 'blocks' and self.num_actors('blocks') != 0:
            actor = self.actors_blocks[0]
        elif category == 'obj' and self.num_actors('obj') != 0:
            actor = self.actors_obj[0]
        elif category == 'entities' and self.num_actors('entities') != 0:
            actor = self.actors_entities[0]
        return actor

    def update(self, category=None):
        if category is None:
            for actor in self.actors_bg + self.actors_blocks + self.actors_obj + self.actors_entities:
                actor.update()
        else:
            actors = getattr(self, f"actors_{category}")
            for actor in actors:
                actor.update()

    def draw(self, category=None):
        if category is None:
            for actor in self.actors_bg + self.actors_blocks + self.actors_obj + self.actors_entities:
                actor.draw()
        else:
            actors = getattr(self, f"actors_{category}")
            for actor in actors:
                actor.draw()

    def num_actors(self, category=None):
        if category is None:
            return len(self.actors_bg + self.actors_blocks + self.actors_obj + self.actors_entities)
        else:
            actors = getattr(self, f"actors_{category}")
            return len(actors)
