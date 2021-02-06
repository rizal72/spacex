namespace SpriteKind {
    export const counter = SpriteKind.create()
    export const enemyProjectile = SpriteKind.create()
}

controller.B.onEvent(ControllerButtonEvent.Pressed, function on_b_pressed() {
    
    if (bombs > 0) {
        playerShip.startEffect(effects.halo, 1500)
        for (let enemyShip of sprites.allOfKind(SpriteKind.Enemy)) {
            enemyShip.destroy(effects.disintegrate, 200)
            info.changeScoreBy(1)
        }
        music.pewPew.play()
        music.powerUp.play()
        scene.cameraShake(4, 1000)
        bombs += -1
    }
    
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function on_a_pressed() {
    
    playerShot = sprites.createProjectileFromSprite(assets.image`
        shot
    `, playerShip, 200, 0)
    music.pewPew.play()
})
function startGame() {
    
    scene.setBackgroundImage(img`
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
    `)
    playerShip = sprites.create(assets.image`
        ship
    `, SpriteKind.Player)
    animation.runImageAnimation(playerShip, assets.animation`
            ship_anim
        `, 250, true)
    playerShip.setFlag(SpriteFlag.StayInScreen, true)
    controller.moveSprite(playerShip, 100, 100)
    info.setLife(3)
    bombs = 3
    bombCount = sprites.create(assets.image`
        bcounter
    `, SpriteKind.counter)
    bombCount.setPosition(40, 5)
    bombCountN = sprites.create(assets.image`
        image5
    `, SpriteKind.counter)
    bombCountN.setPosition(52, 5)
}

sprites.onOverlap(SpriteKind.Player, SpriteKind.Food, function on_on_overlap(sprite: Sprite, otherSprite: Sprite) {
    
    if (bombs < 3) {
        otherSprite.destroy(effects.halo, 100)
        music.powerUp.play()
        bombs += 1
    }
    
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy, function on_on_overlap2(sprite: Sprite, otherSprite: Sprite) {
    otherSprite.destroy(effects.disintegrate, 200)
    sprite.destroy()
    info.changeScoreBy(1)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function on_on_overlap3(sprite: Sprite, otherSprite: Sprite) {
    otherSprite.destroy(effects.fire, 100)
    music.jumpDown.play()
    info.changeLifeBy(-1)
})
let enemyShot : Sprite = null
let enemyShip2 : Sprite = null
let bomb : Sprite = null
let star : Sprite = null
let bombCountN : Sprite = null
let bombCount : Sprite = null
let playerShot : Sprite = null
let playerShip : Sprite = null
let bombs = 0
scene.setBackgroundImage(assets.image`
    intro
`)
music.setVolume(100)
game.splash("Press 'A' to shoot laser", "Press 'B' for Nuclear Bomb")
startGame()
game.onUpdate(function on_on_update() {
    
    if (Math.percentChance(25)) {
        star = sprites.createProjectileFromSide(assets.image`
            star
        `, randint(-80, -100), 0)
        star.setPosition(scene.screenWidth(), randint(0, scene.screenHeight()))
        star.setFlag(SpriteFlag.Ghost, true)
        star.setFlag(SpriteFlag.AutoDestroy, true)
    }
    
    bombCountN.say(bombs)
})
game.onUpdateInterval(randint(30000, 60000), function on_update_interval() {
    
    bomb = sprites.create(assets.image`
        bomb
    `, SpriteKind.Food)
    bomb.setVelocity(randint(-50, -80), randint(5, 20))
    bomb.left = scene.screenWidth()
    bomb.y = randint(6, scene.screenHeight() - 6)
    bomb.setFlag(SpriteFlag.AutoDestroy, true)
})
forever(function on_forever() {
    music.playMelody("E B C5 A B G A F ", 120)
    music.playMelody("E B C5 A B G A F ", 120)
    music.playMelody("E D G F B A C5 B ", 120)
    music.playMelody("E D G F B A C5 B ", 120)
})
game.onUpdateInterval(500, function on_update_interval2() {
    
    enemyShip2 = sprites.create(assets.image`
        enemy
    `, SpriteKind.Enemy)
    animation.runImageAnimation(enemyShip2, assets.animation`
            enemy_anim
        `, 200, true)
    enemyShip2.setVelocity(randint(-50, -80), 0)
    enemyShip2.left = scene.screenWidth()
    enemyShip2.y = randint(6, scene.screenHeight() - 6)
    enemyShip2.setFlag(SpriteFlag.AutoDestroy, true)
    if (Math.percentChance(50)) {
        enemyShot = sprites.createProjectileFromSprite(assets.image`
            enemyshot
        `, enemyShip2, -120, 0)
        enemyShot.setKind(SpriteKind.Enemy)
        enemyShot.setFlag(SpriteFlag.AutoDestroy, true)
    }
    
})
