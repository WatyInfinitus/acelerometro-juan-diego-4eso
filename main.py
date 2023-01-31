Dado = 0

def on_gesture_shake():
    global Dado
    Dado = randint(4, 9)
    if Dado == 4:
        basic.show_leds("""
            . . . . .
                        . # . # .
                        . . . . .
                        . # . # .
                        . . . . .
        """)
    if Dado == 5:
        basic.show_leds("""
            . . . . .
                        . # . # .
                        . . # . .
                        . # . # .
                        . . . . .
        """)
    if Dado == 6:
        basic.show_leds("""
            . # . # .
                        . . . . .
                        . # . # .
                        . . . . .
                        . # . # .
        """)
    if Dado == 7:
        basic.show_leds("""
            # . . . #
                        . . . . .
                        # . # . #
                        . . . . .
                        # . . . #
        """)
    if Dado == 8:
        basic.show_leds("""
            # . # . #
                        . . . . .
                        # . . . #
                        . . . . .
                        # . # . #
        """)
    if Dado == 9:
        basic.show_leds("""
            # . # . #
                        . . . . .
                        # . # . #
                        . . . . .
                        # . # . #
        """)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_forever():
    pass
basic.forever(on_forever)
