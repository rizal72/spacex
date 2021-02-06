class ActionKind(Enum):
    Walking = 0
    Idle = 1
    Jumping = 2
@namespace
class SpriteKind:
    counter = SpriteKind.create()
    enemyProjectile = SpriteKind.create()

def on_b_pressed():
    global bombs
    if bombs > 0:
        playerShip.start_effect(effects.halo, 1500)
        for enemyShip in sprites.all_of_kind(SpriteKind.enemy):
            enemyShip.destroy(effects.disintegrate, 200)
            info.change_score_by(1)
        music.pew_pew.play()
        music.power_up.play()
        scene.camera_shake(4, 1000)
        bombs += -1
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_a_pressed():
    global playerShot
    playerShot = sprites.create_projectile_from_sprite(assets.image("""
        shot
    """), playerShip, 200, 0)
    music.pew_pew.play()
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def startGame():
    global playerShip, bombs, bombCount, bombCountN
    scene.set_background_image(img("""
        ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
    """))
    playerShip = sprites.create(assets.image("""
        ship
    """), SpriteKind.player)
    animation.run_image_animation(playerShip,
        assets.animation("""
            ship_anim
        """),
        250,
        True)
    playerShip.set_flag(SpriteFlag.STAY_IN_SCREEN, True)
    controller.move_sprite(playerShip, 100, 100)
    info.set_life(3)
    bombs = 3
    bombCount = sprites.create(assets.image("""
        bcounter
    """), SpriteKind.counter)
    bombCount.set_position(40, 5)
    bombCountN = sprites.create(assets.image("""
        image5
    """), SpriteKind.counter)
    bombCountN.set_position(52, 5)

def on_on_overlap(sprite, otherSprite):
    global bombs
    if bombs < 3:
        otherSprite.destroy(effects.halo, 100)
        music.power_up.play()
        bombs += 1
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_on_overlap)

def on_on_overlap2(sprite, otherSprite):
    otherSprite.destroy(effects.disintegrate, 200)
    sprite.destroy()
    info.change_score_by(1)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap2)

def on_on_overlap3(sprite, otherSprite):
    otherSprite.destroy(effects.fire, 100)
    music.jump_down.play()
    info.change_life_by(-1)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap3)

enemyShot: Sprite = None
enemyShip2: Sprite = None
bomb: Sprite = None
star: Sprite = None
bombCountN: Sprite = None
bombCount: Sprite = None
playerShot: Sprite = None
playerShip: Sprite = None
bombs = 0
scene.set_background_image(assets.image("""
    intro
"""))
music.set_volume(100)
game.splash("Press 'A' to Play - SpaceX: a game by B&A")
startGame()

def on_on_update():
    global star
    if Math.percent_chance(25):
        star = sprites.create_projectile_from_side(assets.image("""
            star
        """), randint(-80, -100), 0)
        star.set_position(scene.screen_width(), randint(0, scene.screen_height()))
        star.set_flag(SpriteFlag.GHOST, True)
        star.set_flag(SpriteFlag.AUTO_DESTROY, True)
    bombCountN.say(bombs)
game.on_update(on_on_update)

def on_update_interval():
    global bomb
    bomb = sprites.create(assets.image("""
        bomb
    """), SpriteKind.food)
    bomb.set_velocity(randint(-50, -80), randint(5, 20))
    bomb.left = scene.screen_width()
    bomb.y = randint(6, scene.screen_height() - 6)
    bomb.set_flag(SpriteFlag.AUTO_DESTROY, True)
game.on_update_interval(randint(30000, 60000), on_update_interval)

def on_forever():
    music.play_melody("E B C5 A B G A F ", 120)
    music.play_melody("E B C5 A B G A F ", 120)
    music.play_melody("E D G F B A C5 B ", 120)
    music.play_melody("E D G F B A C5 B ", 120)
forever(on_forever)

def on_update_interval2():
    global enemyShip2, enemyShot
    enemyShip2 = sprites.create(assets.image("""
        enemy
    """), SpriteKind.enemy)
    animation.run_image_animation(enemyShip2,
        assets.animation("""
            enemy_anim
        """),
        200,
        True)
    enemyShip2.set_velocity(randint(-50, -80), 0)
    enemyShip2.left = scene.screen_width()
    enemyShip2.y = randint(6, scene.screen_height() - 6)
    enemyShip2.set_flag(SpriteFlag.AUTO_DESTROY, True)
    if Math.percent_chance(50):
        enemyShot = sprites.create_projectile_from_sprite(assets.image("""
            enemyshot
        """), enemyShip2, -200, 0)
        enemyShot.set_kind(SpriteKind.enemy)
        enemyShot.set_flag(SpriteFlag.AUTO_DESTROY, True)
game.on_update_interval(500, on_update_interval2)
