from ursina import *

app = Ursina()

background = Entity(model='quad', texture='bg', scale=(16, 9), z=1)
perahu = Entity(model='quad', texture='perahu',scale=(10,5), position = (0,-1,0))
awan2 = Entity(model='quad', texture='awan2',scale=(7,7), position = (5,3,0))
awan = Entity(model='quad', texture='awan',scale=(7,7), position = (-5,3,0))
pesawat = Entity(model='quad', texture='pesawat',scale=(1,1), position = (-5,3,0))
burung = Entity(model='quad', texture='burung',scale=(3,3), position = (-7,1,0))

def input(key):
    if key == 'a':
        perahu.scale *= 1.1  
    elif key == 'd':
        perahu.scale /= 1.1  
    if key == 'w':
        background.scale *= 1.1  
    elif key == 's':
        background.scale /= 1.1 

def update():
     perahu.x += 0.3 * time.dt
     if perahu.x > 9:
        perahu.x = -9  # Kembali ke sebelah kiri layar
        
     pesawat.x += 1.0 * time.dt
     if pesawat.x > 9:
        pesawat.x = -9  # Kembali ke sebelah kiri layar
        
     burung.x += 0.5 * time.dt
     burung.y += 0.2 * time.dt


app.run()