input.onButtonPressed(Button.A, function () {
    if (is_stopped == false) {
        radio.sendString("" + message1 + " - " + username)
        datalogger.log(datalogger.createCV("", "" + username + " sent " + message1 + " to " + targetuser))
        basic.showLeds(`
            . . . . .
            . . . . #
            . . . # .
            # . # . .
            . # . . .
            `)
        basic.pause(100)
        basic.clearScreen()
    } else {
    	
    }
})
function shutdown () {
    basic.clearScreen()
    basic.showIcon(IconNames.No)
    is_stopped = true
}
input.onButtonPressed(Button.AB, function () {
    if (is_stopped == false) {
        radio.sendString("" + message3 + " - " + username)
        datalogger.log(datalogger.createCV("", "" + username_full + " sent " + message3 + " to " + targetuser_full))
        basic.showLeds(`
            . . . . .
            . . . . #
            . . . # .
            # . # . .
            . # . . .
            `)
        basic.pause(100)
        basic.clearScreen()
    } else {
    	
    }
})
radio.onReceivedString(function (receivedString) {
    basic.showString(receivedString)
})
input.onButtonPressed(Button.B, function () {
    if (is_stopped == false) {
        radio.sendString("" + message2 + " - " + username)
        datalogger.log(datalogger.createCV("", "" + username_full + " sent " + message2 + " to " + targetuser_full))
        basic.showLeds(`
            . . . . .
            . . . . #
            . . . # .
            # . # . .
            . # . . .
            `)
        basic.pause(100)
        basic.clearScreen()
    } else {
    	
    }
})
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    if (is_stopped == true) {
        basic.clearScreen()
        is_stopped = false
    } else {
        shutdown()
    }
})
let is_stopped = false
let message3 = ""
let message2 = ""
let message1 = ""
let targetuser = ""
let username = ""
let targetuser_full = ""
let username_full = ""
let teacher_mode = false
username_full = "Jo Hang Johann LO (3019011)"
targetuser_full = "Josette Yeuk Kuk YAM (3120002)"
username = "imtrollmastr"
targetuser = "J2STARWARSGIRL"
message1 = "Hi!"
message2 = "How are you?"
message3 = "Great!"
let ms_screentime = 900000
let time_used = 0
let strip = neopixel.create(DigitalPin.P0, 24, NeoPixelMode.RGB)
radio.setGroup(66)
loops.everyInterval(60000, function () {
    time_used += 1
    strip.showBarGraph(time_used, 255)
    if (time_used == 15) {
        basic.clearScreen()
        basic.showString("Locked due to screen time.")
    } else {
    	
    }
})
