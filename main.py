def on_pin_pressed_p0():
    music.play(music.builtin_playable_sound_effect(soundExpression.giggle),
        music.PlaybackMode.UNTIL_DONE)
input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)
