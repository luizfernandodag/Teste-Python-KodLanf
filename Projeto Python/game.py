import random

import pgzrun

# Variáveis de estado do jogo
lives = 2
score = 0
game_over = False

# Tamanho da tela
WIDTH = 800
HEIGHT = 600

# Jogador
ship = Actor('playership1_blue')
ship.x = 100
ship.y = 100

# Gema
gem = Actor('gemgreen')
gem.x = random.randint(20, 780)
gem.y = 0

# Velocidade da gema
gem_speed_x = 0
gem_speed_y = 0

def reset_gem_speed():
    global gem_speed_x, gem_speed_y
    gem_speed_x = random.choice([-1, 1]) * random.uniform(2, 3)
    gem_speed_y = random.uniform(2, 3)

reset_gem_speed()

def draw():
    screen.fill((80, 0, 70))

    if game_over:
        screen.draw.text('GAME OVER', center=(WIDTH // 2, HEIGHT // 2 - 30), fontsize=60, color='white')
        screen.draw.text(f'Score: {score}', center=(WIDTH // 2, HEIGHT // 2 + 30), fontsize=50, color='white')
    else:
        ship.draw()
        gem.draw()
        screen.draw.text(f'Lives: {lives}   Score: {score}', (10, 10), fontsize=30, color='white')

def update():
    global gem_speed_x, gem_speed_y, score, game_over, lives

    if game_over:
        return  # Para de atualizar se o jogo acabou

    # Movimento do jogador
    if keyboard.left:
        ship.x -= 5
    if keyboard.right:
        ship.x += 5
    if keyboard.up:
        ship.y -= 5
    if keyboard.down:
        ship.y += 5

    # Movimento da gema
    gem.x += gem_speed_x
    gem.y += gem_speed_y

    # Rebater nas laterais
    if gem.x > WIDTH or gem.x < 0:
        gem_speed_x *= -1

    # Colisão com o jogador
    if gem.colliderect(ship):
        gem.x = random.randint(20, 780)
        gem.y = 0
        score += 1
        reset_gem_speed()

    # Gema caiu no chão
    if gem.y > HEIGHT:
        lives -= 1
        if lives == 0:
            game_over = True
        else:
            gem.x = random.randint(20, 780)
            gem.y = 0
            reset_gem_speed()

pgzrun.go()
