123457890121314252627181920
mySprite = 0

def on_player2_button_a_pressed():
    global mySprite
    controller.move_sprite(mySprite)
    music.play(music.string_playable("- - - - - - - - ", 120),
        music.PlaybackMode.UNTIL_DONE)
    mySprite += 1
controller.player2.on_button_event(ControllerButton.A,
    ControllerButtonEvent.PRESSED,
    on_player2_button_a_pressed)

def on_on_score():
    pass
info.on_score(100, on_on_score)

def on_update_interval():
    game.game_over(0 == 0 and False)
game.on_update_interval(500, on_update_interval)
