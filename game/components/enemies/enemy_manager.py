import random
from game.components.enemies.enemy import Enemy

class EnemyManager:
    def __init__(self):
        self.enemies = []
    def update(self, game):
        self.add_enemy(game)
        for enemy in self.enemies:
            enemy.update(self.enemies, game)
    
    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)
    
    def add_enemy(self,game):
        enemy_type = random.randint(1,4)
        if enemy_type == 1:
            enemy = Enemy()
        else:
            x_speed = 5
            y_speed = 2
            move_x_for = [50,120]
            enemy = Enemy(enemy_type,x_speed,y_speed,move_x_for)
        if game.score <= 10:
            if len(self.enemies)<3:
                enemy = Enemy()
                self.enemies.append(enemy)
        elif game.score <=20:
            if len(self.enemies)<3:
                enemy = Enemy()
                self.enemies.append(enemy)
        elif game.score <=32:
            if len(self.enemies)<4:
                enemy = Enemy()
                self.enemies.append(enemy)
        else:
            if len(self.enemies)< random.randint(3,7):
                enemy = Enemy()
                self.enemies.append(enemy)