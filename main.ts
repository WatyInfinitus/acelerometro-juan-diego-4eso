let Dado = 0
input.onGesture(Gesture.Shake, function () {
    Dado = randint(4, 9)
    if (Dado == 4) {
        basic.showLeds(`
            . . . . .
            . # . # .
            . . . . .
            . # . # .
            . . . . .
            `)
    }
    if (Dado == 5) {
        basic.showLeds(`
            . . . . .
            . # . # .
            . . # . .
            . # . # .
            . . . . .
            `)
    }
    if (Dado == 6) {
        basic.showLeds(`
            . # . # .
            . . . . .
            . # . # .
            . . . . .
            . # . # .
            `)
    }
    if (Dado == 7) {
        basic.showLeds(`
            # . . . #
            . . . . .
            # . # . #
            . . . . .
            # . . . #
            `)
    }
    if (Dado == 8) {
        basic.showLeds(`
            # . # . #
            . . . . .
            # . . . #
            . . . . .
            # . # . #
            `)
    }
    if (Dado == 9) {
        basic.showLeds(`
            # . # . #
            . . . . .
            # . # . #
            . . . . .
            # . # . #
            `)
    }
})
basic.forever(function () {
	
})
