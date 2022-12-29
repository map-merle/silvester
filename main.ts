input.onButtonPressed(Button.A, function () {
    basic.showString("Frohes")
    basic.showString("neues")
    basic.showString("Jahr")
    basic.showIcon(IconNames.Happy)
    for (let index = 0; index < 10; index++) {
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . # . .
            `)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . # . # .
            . . # . .
            `)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . # . # .
            . . . . .
            `)
        basic.showLeds(`
            . . . . .
            . . . . .
            # . . . #
            . # . # .
            . . . . .
            `)
        basic.showLeds(`
            . . . . .
            . . . . .
            # . . . #
            . . . . .
            . . . . .
            `)
        basic.showLeds(`
            . . . . .
            . # # # .
            # . . . #
            . . . . .
            . . . . .
            `)
        basic.showLeds(`
            . . # . .
            . # # # .
            . . . . .
            . . . . .
            . . . . .
            `)
        basic.showLeds(`
            . # . # .
            . . # . .
            . . . . .
            . . . . .
            . . . . .
            `)
        basic.showLeds(`
            # . . . #
            . . # . .
            . . . . .
            . . . . .
            . . . . .
            `)
        basic.showLeds(`
            . # . # .
            . . # . .
            . . . . .
            . . . . .
            . . . . .
            `)
        basic.showLeds(`
            . . # . .
            . # # # .
            . . . . .
            . . . . .
            . . . . .
            `)
        basic.showLeds(`
            . . . . .
            . # # # .
            # . . . #
            . . . . .
            . . . . .
            `)
        basic.showLeds(`
            . . . . .
            . . . . .
            # . . . #
            . . . . .
            . . . . .
            `)
        basic.showLeds(`
            . . . . .
            . . . . .
            # . . . #
            . # . # .
            . . . . .
            `)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . # . # .
            . . . . .
            `)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . # . # .
            . . # . .
            `)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . # . .
            `)
    }
})
input.onButtonPressed(Button.B, function () {
    music.playMelody("C C5 B F A G C E ", 500)
    basic.showString("Guten Rutsch")
    basic.showString("ins neue Jahr")
    for (let index = 0; index < 10; index++) {
        basic.showLeds(`
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . .
            `)
        basic.showIcon(IconNames.SmallDiamond)
        basic.showIcon(IconNames.Diamond)
        basic.showLeds(`
            . # . # .
            # . . . #
            . . . . .
            # . . . #
            . # . # .
            `)
        basic.showLeds(`
            # . . . #
            . . . . .
            . . . . .
            . . . . .
            # . . . #
            `)
        basic.showLeds(`
            . # . # .
            # . . . #
            . . . . .
            # . . . #
            . # . # .
            `)
        basic.showIcon(IconNames.Diamond)
        basic.showIcon(IconNames.SmallDiamond)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . .
            `)
    }
})
