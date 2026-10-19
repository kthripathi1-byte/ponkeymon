let mySprite = 0
controller.player2.onButtonEvent(ControllerButton.A, ControllerButtonEvent.Pressed, function () {
    controller.moveSprite(mySprite)
    music.play(music.stringPlayable("- - - - - - - - ", 120), music.PlaybackMode.UntilDone)
    mySprite += 1
})
info.onScore(100, function () {
	
})
game.onUpdateInterval(500, function () {
    game.gameOver(0 == 0 && false)
})
