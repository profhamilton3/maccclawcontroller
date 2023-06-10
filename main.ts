joystickbit.onButtonEvent(joystickbit.JoystickBitPin.P14, joystickbit.ButtonType.down, function () {
    music.playSoundEffect(music.createSoundEffect(WaveShape.Square, 5000, 0, 255, 0, 500, SoundExpressionEffect.None, InterpolationCurve.Linear), SoundExpressionPlayMode.UntilDone)
    radio.sendNumber(3)
    basic.showNumber(3)
})
input.onButtonPressed(Button.A, function () {
    radio.sendNumber(5)
    basic.showNumber(5)
})
joystickbit.onButtonEvent(joystickbit.JoystickBitPin.P15, joystickbit.ButtonType.down, function () {
    music.playSoundEffect(music.createSoundEffect(WaveShape.Square, 5000, 0, 255, 0, 500, SoundExpressionEffect.None, InterpolationCurve.Linear), SoundExpressionPlayMode.UntilDone)
    radio.sendNumber(4)
    basic.showNumber(4)
})
input.onButtonPressed(Button.AB, function () {
    radio.sendNumber(11)
})
input.onButtonPressed(Button.B, function () {
    radio.sendNumber(6)
    basic.showNumber(6)
})
joystickbit.onButtonEvent(joystickbit.JoystickBitPin.P13, joystickbit.ButtonType.down, function () {
    music.playSoundEffect(music.createSoundEffect(WaveShape.Square, 5000, 0, 255, 0, 500, SoundExpressionEffect.None, InterpolationCurve.Linear), SoundExpressionPlayMode.UntilDone)
    radio.sendNumber(2)
    basic.showNumber(2)
})
joystickbit.onButtonEvent(joystickbit.JoystickBitPin.P12, joystickbit.ButtonType.down, function () {
    music.playSoundEffect(music.createSoundEffect(WaveShape.Sine, 5000, 0, 255, 0, 500, SoundExpressionEffect.None, InterpolationCurve.Linear), SoundExpressionPlayMode.UntilDone)
    radio.sendNumber(1)
    basic.showNumber(1)
})
let pY0 = joystickbit.getRockerValue(joystickbit.rockerType.Y)
let pX0 = joystickbit.getRockerValue(joystickbit.rockerType.X)
let pX = pX0
let pY = pY0
joystickbit.initJoystickBit()
radio.setGroup(3)
radio.setFrequencyBand(33)
radio.sendNumber(11)
joystickbit.Vibration_Motor(100)
basic.showIcon(IconNames.Surprised)
basic.forever(function () {
    if (Math.abs(joystickbit.getRockerValue(joystickbit.rockerType.X) - pX) > 50 && Math.abs(joystickbit.getRockerValue(joystickbit.rockerType.X) - pX0) > 50) {
        if (joystickbit.getRockerValue(joystickbit.rockerType.X) < 500) {
            radio.sendNumber(10)
            basic.showArrow(ArrowNames.East)
        } else if (joystickbit.getRockerValue(joystickbit.rockerType.X) >= 500) {
            radio.sendNumber(9)
            basic.showArrow(ArrowNames.West)
        } else {
            basic.showIcon(IconNames.No)
        }
        pX = joystickbit.getRockerValue(joystickbit.rockerType.X)
    }
    if (Math.abs(joystickbit.getRockerValue(joystickbit.rockerType.Y) - pY) > 50 && Math.abs(joystickbit.getRockerValue(joystickbit.rockerType.Y) - pY0) > 50) {
        if (joystickbit.getRockerValue(joystickbit.rockerType.Y) < 500) {
            radio.sendNumber(8)
            basic.showArrow(ArrowNames.South)
        } else if (joystickbit.getRockerValue(joystickbit.rockerType.Y) >= 500) {
            radio.sendNumber(7)
            basic.showArrow(ArrowNames.North)
        } else {
            basic.showIcon(IconNames.No)
        }
        pY = joystickbit.getRockerValue(joystickbit.rockerType.Y)
    }
})
