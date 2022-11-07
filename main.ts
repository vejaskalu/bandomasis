input.onButtonPressed(Button.A, function () {
    basic.showLeds(`
        . . . . .
        . # # # .
        # # # # #
        . # # # .
        . . # . .
        `)
})
basic.showLeds(`
    . . # . .
    . . # . .
    # # # # #
    . . # . .
    . . # . .
    `)
basic.forever(function () {
    basic.showLeds(`
        . . . . .
        # . # . #
        . # # # .
        . # # # .
        # . # . #
        `)
    basic.pause(1000)
    basic.showIcon(IconNames.TShirt)
    basic.showIcon(1)
basic.pause(1000)
})
