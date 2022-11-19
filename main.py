
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import random

class Voxel(Button):
    def __init__(self, position = (0,0,0)):
        super().__init__(
            parent = scene,
            position = position,
            model = 'cube',
            origin_y = 0.5,
            texture = 'grass.png',
            color = color.color(0,0, random.uniform(0.9,1)),
            highlight_color = color.red
        )

def spawn():
    player.x = 34
    player.y = 0
    player.z = 12

def update():
    if player.speed >= 6:
        print_on_screen("Sprinting...",position = (-0.79,0.49))

    if player.Y <= -20:
        print_on_screen("You died!",position = (-0.27,0.3), scale = 5, duration = 5)
        spawn()

sprint = False

def input(key):
    global sprint
    if key == 'escape':
        quit()

    if held_keys['control'] and held_keys['w']:
        sprint = True
        player.speed = 7

    if sprint and not held_keys['w']:
        sprint = False
        player.speed = 4

    if key == 'escape':
        quit()
        
sizerandom = [0.1, 0.15, 0.2, 0.25, 0.3, 0.35]
print(random.choice(sizerandom))

app = Ursina()
player = FirstPersonController()

for z in range(46):
    for x in range(46):
        voxel = Voxel(position = (x,0,z))

house = Entity(model ="assets/models/Farmhouse.obj", texture = "assets/textures/Farmhouse.jpg", position = (34,0,30), scale = 0.4, collider = "mesh")

player.cursor.scale = 0.1/5
player.cursor.texture = 'assets/textures/crosshair.png'
player.cursor.rotation = 0
player.speed = 4
player.jump_height = 1
window.name = 'Models test'
window.fullscreen = True

spawn()
Sky()
app.run()