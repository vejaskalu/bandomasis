def on_button_pressed_a():
    basic.show_leds("""
        . . . . .
                . # # # .
                # # # # #
                . # # # .
                . . # . .
    """)
input.on_button_pressed(Button.A, on_button_pressed_a)

basic.show_leds("""
    . . # . .
        . . # . .
        # # # # #
        . . # . .
        . . # . .
""")

def on_forever():
    basic.show_leds("""
        . . . . .
                # . # . #
                . # # # .
                . # # # .
                # . # . #
    """)
    basic.pause(1000)
    basic.show_icon(IconNames.TSHIRT)
    basic.show_icon(1)
    basic.pause(1000)
basic.forever(on_forever)
