datalogger.onLogFull(function () {
    datalogger.deleteLog(datalogger.DeleteType.Fast)
})
input.onButtonPressed(Button.A, function () {
    if (is_stopped == false) {
        radio.sendString("" + message1 + " - " + username)
        datalogger.log(datalogger.createCV("", "" + username_full + " sent " + message1 + " to " + targetuser_full + " via " + ("" + control.deviceSerialNumber())))
        basic.clearScreen()
        create_faceV2("left")
    } else {
    	
    }
})
function shutdown () {
    basic.clearScreen()
    basic.showIcon(IconNames.No)
    is_stopped = true
}
function create_faceV2 (eye: string) {
    faces.showFace(faces.Eyes.Open, faces.Mouth.Grin)
    if (eye == "left") {
        faces.wink(true, 750, false)
    } else {
        faces.wink(false, 750, false)
    }
}
input.onButtonPressed(Button.AB, function () {
    if (is_stopped == false) {
        radio.sendString("" + message3 + " - " + username)
        datalogger.log(datalogger.createCV("", "" + username_full + " sent " + message3 + " to " + targetuser_full + " via " + ("" + control.deviceSerialNumber())))
        basic.clearScreen()
        create_faceV2("left")
    } else {
    	
    }
})
function setMessageType (authpass: string, messageType: string) {
    if (authpass == "admin") {
        // Events:
        // - Basic messages (How are you?, Good morning!, Good night!)
        // - Morse code (., -, <space>)
        // - Teacher mode messaging (Where are you?, I'm at <room>, My students are all here!)
        // - Disabled messaging
        // - Emergency System (Fire alarm, lockdown activation message, weather report, etc.)
        if (messageType == "basic_messages") {
        	
        } else if (messageType == "morse_code") {
            message1 = "."
            message2 = "-"
            message3 = "<space>"
        } else if (messageType == "teachermode") {
            message1 = "Where are you?"
            message2 = "I'm at Zone 1!"
            message3 = "My students are all here."
        } else if (messageType == "disabled") {
            message1 = ""
            message2 = ""
            message3 = ""
        } else if (messageType == "EmergencyAlert") {
            message1 = "This is a fire alarm. Please return to assembly point."
            message2 = "Lockdown has been activated. Please stay and hide in the room you are in."
            message3 = "This is a weather report alarm. Please stay in a room where it is safe, or follow a teacher to a safe room."
        } else if (messageType == "EasterEgg") {
            randomInt = randint(1, 3)
            if (randomInt == 1) {
                message1 = "You found the Easter Egg!"
            } else if (randomInt == 2) {
                message2 = "You found the Easter Egg!"
            } else if (randomInt == 3) {
                message3 = "You found the Easter Egg!"
            }
        } else {
            basic.showString("Missing 'messageType' parameter.")
        }
    } else {
        basic.showString("Incorrect administrator password, authorization denied")
    }
}
radio.onReceivedString(function (receivedString) {
    basic.showString(receivedString)
})
input.onButtonPressed(Button.B, function () {
    if (is_stopped == false) {
        radio.sendString("" + message2 + " - " + username)
        datalogger.log(datalogger.createCV("", "" + username_full + " sent " + message2 + " to " + targetuser_full + " via " + ("" + control.deviceSerialNumber())))
        basic.clearScreen()
        create_faceV2("right")
    } else {
    	
    }
})
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    if (is_stopped == true) {
        if (shutdown_by_time == true) {
        	
        } else {
            basic.clearScreen()
            is_stopped = false
            create_faceV2("left")
        }
    } else if (shutdown_by_time == true) {
    	
    } else {
        shutdown()
    }
})
let time_used = 0
let randomInt = 0
let is_stopped = false
let shutdown_by_time = false
let message3 = ""
let message2 = ""
let message1 = ""
let username = ""
let targetuser_full = ""
let username_full = ""
username_full = "Jo Hang Johann LO (3019011)"
targetuser_full = "Josette Yeuk Kuk YAM (3120002)"
username = "imtrollmastr"
let targetuser = "J2STARWARSGIRL"
message1 = "Good morning! / Good"
message2 = "Good night! / Bad"
message3 = "How are you?"
let ms_screentime = 150000
shutdown_by_time = false
radio.setGroup(66)
create_faceV2("left")
led.setBrightness(255)
setMessageType("admin", "EasterEgg")
loops.everyInterval(60000, function () {
    time_used += 1
    if (time_used == 15) {
        basic.clearScreen()
        basic.showString("Locked due to screen time.")
        shutdown_by_time = true
        is_stopped = true
    } else {
    	
    }
})
