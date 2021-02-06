def on_b_pressed():
    global dart, bombs
    if bombs > 0:
        index = 0
        while index <= scene.screen_height() / 4:
            dart = sprites.create_projectile_from_sprite(img("""
                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . 2 2 2 2 . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . .
                """),
                spacePlane,
                200,
                0)
            dart.y = index * 4
            index += 1
        music.pew_pew.play()
        music.power_up.play()
        scene.camera_shake(4, 1000)
        bombs += -1
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_a_pressed():
    global dart
    dart = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . 2 2 2 2 . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        spacePlane,
        200,
        0)
    music.pew_pew.play()
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap(sprite, otherSprite):
    otherSprite.destroy(effects.disintegrate, 200)
    sprite.destroy()
    info.change_score_by(1)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap)

def on_on_overlap2(sprite, otherSprite):
    otherSprite.destroy(effects.fire, 100)
    music.jump_down.play()
    info.change_life_by(-1)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap2)

bogey: Sprite = None
star: Sprite = None
dart: Sprite = None
spacePlane: Sprite = None
bombs = 0
bombs = 3
spacePlane = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . 2 . . . . . . . . . . . . . 
            . . 2 2 . . . . . . . . . . . . 
            . . 2 2 2 . . . . . . . . . . . 
            . 5 4 8 8 8 8 8 8 8 8 8 9 . . . 
            5 4 2 8 8 8 2 2 2 2 8 8 9 9 8 . 
            . 5 4 8 8 8 8 8 8 8 8 8 8 8 8 8 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.player)
animation.run_image_animation(spacePlane,
    [img("""
            . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . 2 . . . . . . . . . . . . . 
                . . 2 2 . . . . . . . . . . . . 
                . . 2 2 2 . . . . . . . . . . . 
                . 5 4 8 8 8 8 8 8 8 8 8 9 . . . 
                5 4 2 8 8 8 2 2 2 2 8 8 9 9 8 . 
                . 5 4 8 8 8 8 8 8 8 8 8 8 8 8 8 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . .
        """),
        img("""
            . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . 2 . . . . . . . . . . . . . 
                . . 2 2 . . . . . . . . . . . . 
                . . 2 2 2 . . . . . . . . . . . 
                . 2 4 8 8 8 8 8 8 8 8 8 9 . . . 
                2 4 5 8 8 8 2 2 2 2 8 8 9 9 8 . 
                . 2 4 8 8 8 8 8 8 8 8 8 8 8 8 8 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . .
        """)],
    250,
    True)
spacePlane.set_flag(SpriteFlag.STAY_IN_SCREEN, True)
info.set_life(3)
controller.move_sprite(spacePlane, 150, 150)

def on_on_update():
    global star
    if Math.percent_chance(25):
        star = sprites.create_projectile_from_side(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . 1 . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            randint(-80, -100),
            0)
        star.set_position(scene.screen_width(), randint(0, scene.screen_height()))
        star.set_flag(SpriteFlag.GHOST, True)
game.on_update(on_on_update)

def on_update_interval():
    global bogey
    bogey = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . 9 9 9 9 . . . . . . 
                    . . . . . 9 9 9 9 9 9 . . . . . 
                    . . . . 9 9 9 9 9 9 9 9 . . . . 
                    . . 6 6 6 6 6 6 6 6 6 6 6 6 . . 
                    . . 7 6 2 6 7 6 2 6 7 6 2 6 . . 
                    . 6 6 6 6 6 6 6 6 6 6 6 6 6 6 . 
                    6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                    . . 6 5 6 . . . . . . 6 5 6 . . 
                    . . . 2 . . . . . . . . 2 . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.enemy)
    animation.run_image_animation(bogey,
        [img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . 9 9 9 9 . . . . . . 
                        . . . . . 9 9 9 9 9 9 . . . . . 
                        . . . . 9 9 9 9 9 9 9 9 . . . . 
                        . . 6 6 6 6 6 6 6 6 6 6 6 6 . . 
                        . . 7 6 2 6 7 6 2 6 7 6 2 6 . . 
                        . 6 6 6 6 6 6 6 6 6 6 6 6 6 6 . 
                        6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                        . . 6 5 6 . . . . . . 6 5 6 . . 
                        . . . 2 . . . . . . . . 2 . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . 9 9 9 9 . . . . . . 
                        . . . . . 9 9 9 9 9 9 . . . . . 
                        . . . . 9 9 9 9 9 9 9 9 . . . . 
                        . . 6 6 6 6 6 6 6 6 6 6 6 6 . . 
                        . . 2 6 7 6 2 6 7 6 2 6 7 6 . . 
                        . 6 6 6 6 6 6 6 6 6 6 6 6 6 6 . 
                        6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                        . . 6 2 6 . . . . . . 6 2 6 . . 
                        . . . 5 . . . . . . . . 5 . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
            """)],
        500,
        True)
    bogey.set_velocity(randint(-50, -80), 0)
    bogey.left = scene.screen_width()
    bogey.y = randint(6, scene.screen_height())
    bogey.set_flag(SpriteFlag.AUTO_DESTROY, True)
game.on_update_interval(500, on_update_interval)
