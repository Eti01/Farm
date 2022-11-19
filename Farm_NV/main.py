from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

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

grass = Entity(
    model = "plane",
    texture = "grass",
    collider = "mesh",
    scale = (2000,0,2000)
)

random_textures = ["assets/textures/Farmhouse.jpg","assets/textures/Farmhouse1.jpg"]

for i in range(random.randrange(10,20)):
    house = Entity(
        model ="assets/models/Farmhouse.obj",
        texture = random.choice(random_textures),
        position = (random.randrange(-800,800),0,random.randrange(-170,170)),
        scale = 0.4,
        collider = "mesh")

player = FirstPersonController()
player.cursor.texture = 'assets/textures/crosshair.png'
player.cursor.rotation = 0
player.cursor.scale = 0.025

player.z = 0
player.y = 100
player.x = 0


window.fullscreen = True

Sky()
app.run()