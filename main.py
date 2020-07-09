nb = 0

def on_button_pressed_a():
    global nb
    nb += 1
    basic.show_string("" + str((nb)))
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global nb
    basic.clear_screen()
    nb = 0
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    pass
basic.forever(on_forever)
