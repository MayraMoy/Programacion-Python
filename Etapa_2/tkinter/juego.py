import tkinter as tk
import random

# Configuración de la ventana principal
root = tk.Tk()
root.title("Juego de Aviones y Disparos")
root.resizable(False, False)

# Configuración del canvas
width = 500
height = 600
canvas = tk.Canvas(root, width=width, height=height, bg="skyblue")
canvas.pack()

# Variables del juego
player_size = 50
enemy_size = 50
bullet_size = 5
player_speed = 20
bullet_speed = 10
enemy_speed = 5

# Inicialización del jugador
player = canvas.create_rectangle(width//2 - player_size//2, height - player_size - 10, 
                                width//2 + player_size//2, height - 10, fill="blue")

# Lista para las balas y los enemigos
bullets = []
enemies = []

def move_player(event):
    x1, y1, x2, y2 = canvas.coords(player)
    if event.keysym == "Left" and x1 > 0:
        canvas.move(player, -player_speed, 0)
    elif event.keysym == "Right" and x2 < width:
        canvas.move(player, player_speed, 0)

def shoot_bullet():
    x1, y1, x2, y2 = canvas.coords(player)
    bullet = canvas.create_rectangle((x1+x2)//2 - bullet_size//2, y1 - bullet_size, 
                                    (x1+x2)//2 + bullet_size//2, y1, fill="red")
    bullets.append(bullet)
    root.after(100, shoot_bullet)

def create_enemy():
    enemy_x = random.randint(0, width - enemy_size)
    enemy = canvas.create_rectangle(enemy_x, 0, enemy_x + enemy_size, enemy_size, fill="green")
    enemies.append(enemy)
    root.after(2000, create_enemy)

def move_bullets():
    for bullet in bullets:
        canvas.move(bullet, 0, -bullet_speed)
        x1, y1, x2, y2 = canvas.coords(bullet)
        if y2 < 0:
            canvas.delete(bullet)
            bullets.remove(bullet)
    root.after(50, move_bullets)

def move_enemies():
    for enemy in enemies:
        canvas.move(enemy, 0, enemy_speed)
        x1, y1, x2, y2 = canvas.coords(enemy)
        if y2 > height:
            canvas.delete(enemy)
            enemies.remove(enemy)
    root.after(100, move_enemies)

def check_collisions():
    for bullet in bullets:
        x1_b, y1_b, x2_b, y2_b = canvas.coords(bullet)
        for enemy in enemies:
            x1_e, y1_e, x2_e, y2_e = canvas.coords(enemy)
            if x1_b < x2_e and x2_b > x1_e and y1_b < y2_e and y2_b > y1_e:
                canvas.delete(bullet)
                canvas.delete(enemy)
                bullets.remove(bullet)
                enemies.remove(enemy)
                break
    root.after(50, check_collisions)

# Controles del jugador
root.bind("<Left>", move_player)
root.bind("<Right>", move_player)
root.bind("<space>", lambda event: shoot_bullet())

# Iniciar el juego
create_enemy()
move_bullets()
move_enemies()
check_collisions()
root.mainloop()