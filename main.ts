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
        datalogger.log(datalogger.createCV("", "" + username + " sent " + message3 + " to " + targetuser))
        basic.showLeds(`
            . . . . .
            . . . . #
            . . . # .
            # . # . .
            . # . . .
            `)
    } else {
    	
    }
})
radio.onReceivedString(function (receivedString) {
    basic.showString(receivedString)
})
input.onButtonPressed(Button.B, function () {
    if (is_stopped == false) {
        radio.sendString("" + message2 + " - " + username)
        datalogger.log(datalogger.createCV("", "" + username + " sent " + message2 + " to " + targetuser))
        basic.showLeds(`
            . . . . .
            . . . . #
            . . . # .
            # . # . .
            . # . . .
            `)
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
username = "Jo Hang Johann LO (3019011)"
targetuser = "Josette Yeuk Kuk YAM (3120002)"
message1 = "Hi!"
message2 = "How are you?"
message3 = "Great!"
let ms_screentime = 900000
let teacher_mode = false
radio.setGroup(66)
