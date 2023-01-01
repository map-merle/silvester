def on_button_pressed_a():
    basic.show_string("Frohes")
    basic.show_string("neues")
    basic.show_string("Jahr")
    basic.show_icon(IconNames.HAPPY)
    for index in range(10):
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
                        . . # . .
        """)
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . . . .
                        . # . # .
                        . . # . .
        """)
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . . . .
                        . # . # .
                        . . . . .
        """)
        basic.show_leds("""
            . . . . .
                        . . . . .
                        # . . . #
                        . # . # .
                        . . . . .
        """)
        basic.show_leds("""
            . . . . .
                        . . . . .
                        # . . . #
                        . . . . .
                        . . . . .
        """)
        basic.show_leds("""
            . . . . .
                        . # # # .
                        # . . . #
                        . . . . .
                        . . . . .
        """)
        basic.show_leds("""
            . . # . .
                        . # # # .
                        . . . . .
                        . . . . .
                        . . . . .
        """)
        basic.show_leds("""
            . # . # .
                        . . # . .
                        . . . . .
                        . . . . .
                        . . . . .
        """)
        basic.show_leds("""
            # . . . #
                        . . # . .
                        . . . . .
                        . . . . .
                        . . . . .
        """)
        basic.show_leds("""
            . # . # .
                        . . # . .
                        . . . . .
                        . . . . .
                        . . . . .
        """)
        basic.show_leds("""
            . . # . .
                        . # # # .
                        . . . . .
                        . . . . .
                        . . . . .
        """)
        basic.show_leds("""
            . . . . .
                        . # # # .
                        # . . . #
                        . . . . .
                        . . . . .
        """)
        basic.show_leds("""
            . . . . .
                        . . . . .
                        # . . . #
                        . . . . .
                        . . . . .
        """)
        basic.show_leds("""
            . . . . .
                        . . . . .
                        # . . . #
                        . # . # .
                        . . . . .
        """)
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . . . .
                        . # . # .
                        . . . . .
        """)
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . . . .
                        . # . # .
                        . . # . .
        """)
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
                        . . # . .
        """)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    music.play_melody("C C5 B F A G C E ", 500)
    basic.show_string("Guten Rutsch")
    basic.show_string("ins neue Jahr")
    for index2 in range(10):
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . # . .
                        . . . . .
                        . . . . .
        """)
        basic.show_icon(IconNames.SMALL_DIAMOND)
        basic.show_icon(IconNames.DIAMOND)
        basic.show_leds("""
            . # . # .
                        # . . . #
                        . . . . .
                        # . . . #
                        . # . # .
        """)
        basic.show_leds("""
            # . . . #
                        . . . . .
                        . . . . .
                        . . . . .
                        # . . . #
        """)
        basic.show_leds("""
            . # . # .
                        # . . . #
                        . . . . .
                        # . . . #
                        . # . # .
        """)
        basic.show_icon(IconNames.DIAMOND)
        basic.show_icon(IconNames.SMALL_DIAMOND)
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . # . .
                        . . . . .
                        . . . . .
        """)
input.on_button_pressed(Button.B, on_button_pressed_b)
