def my_function():
    music.play_sound_effect(music.create_sound_effect(WaveShape.SQUARE,
            5000,
            0,
            255,
            0,
            500,
            SoundExpressionEffect.NONE,
            InterpolationCurve.LINEAR),
        SoundExpressionPlayMode.UNTIL_DONE)
    radio.send_number(3)
    basic.show_number(3)
joystickbit.on_button_event(joystickbit.JoystickBitPin.P14,
    joystickbit.ButtonType.DOWN,
    my_function)

def on_button_pressed_a():
    radio.send_number(5)
    basic.show_number(5)
input.on_button_pressed(Button.A, on_button_pressed_a)

def my_function2():
    music.play_sound_effect(music.create_sound_effect(WaveShape.SQUARE,
            5000,
            0,
            255,
            0,
            500,
            SoundExpressionEffect.NONE,
            InterpolationCurve.LINEAR),
        SoundExpressionPlayMode.UNTIL_DONE)
    radio.send_number(4)
    basic.show_number(4)
joystickbit.on_button_event(joystickbit.JoystickBitPin.P15,
    joystickbit.ButtonType.DOWN,
    my_function2)

def on_button_pressed_ab():
    radio.send_number(11)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    radio.send_number(6)
    basic.show_number(6)
input.on_button_pressed(Button.B, on_button_pressed_b)

def my_function3():
    music.play_sound_effect(music.create_sound_effect(WaveShape.SQUARE,
            5000,
            0,
            255,
            0,
            500,
            SoundExpressionEffect.NONE,
            InterpolationCurve.LINEAR),
        SoundExpressionPlayMode.UNTIL_DONE)
    radio.send_number(2)
    basic.show_number(2)
joystickbit.on_button_event(joystickbit.JoystickBitPin.P13,
    joystickbit.ButtonType.DOWN,
    my_function3)

def my_function4():
    music.play_sound_effect(music.create_sound_effect(WaveShape.SINE,
            5000,
            0,
            255,
            0,
            500,
            SoundExpressionEffect.NONE,
            InterpolationCurve.LINEAR),
        SoundExpressionPlayMode.UNTIL_DONE)
    radio.send_number(1)
    basic.show_number(1)
joystickbit.on_button_event(joystickbit.JoystickBitPin.P12,
    joystickbit.ButtonType.DOWN,
    my_function4)

def on_forever():
    global pX, pY
    if abs(joystickbit.get_rocker_value(joystickbit.rockerType.X) - pX) > 50 and abs(joystickbit.get_rocker_value(joystickbit.rockerType.X) - pX0) > 50:
        if joystickbit.get_rocker_value(joystickbit.rockerType.X) < 500:
            radio.send_number(3)
            basic.show_arrow(ArrowNames.EAST)
        elif joystickbit.get_rocker_value(joystickbit.rockerType.X) >= 500:
            radio.send_number(2)
            basic.show_arrow(ArrowNames.WEST)
        else:
            basic.show_icon(IconNames.NO)
        pX = joystickbit.get_rocker_value(joystickbit.rockerType.X)
    if abs(joystickbit.get_rocker_value(joystickbit.rockerType.Y) - pY) > 50 and abs(joystickbit.get_rocker_value(joystickbit.rockerType.Y) - pY0) > 50:
        if joystickbit.get_rocker_value(joystickbit.rockerType.Y) < 500:
            radio.send_number(4)
            basic.show_arrow(ArrowNames.SOUTH)
        elif joystickbit.get_rocker_value(joystickbit.rockerType.Y) >= 500:
            radio.send_number(1)
            basic.show_arrow(ArrowNames.NORTH)
        else:
            basic.show_icon(IconNames.NO)
        pY = joystickbit.get_rocker_value(joystickbit.rockerType.Y)
basic.forever(on_forever)


pY0 = joystickbit.get_rocker_value(joystickbit.rockerType.Y)
pX0 = joystickbit.get_rocker_value(joystickbit.rockerType.X)
pX = pX0
pY = pY0

joystickbit.init_joystick_bit()
radio.set_group(3)
radio.set_frequency_band(33)
radio.send_number(11)
joystickbit.Vibration_Motor(100)
basic.show_icon(IconNames.CONFUSED)