def on_log_full():
    datalogger.delete_log(datalogger.DeleteType.FAST)
datalogger.on_log_full(on_log_full)

def on_button_pressed_a():
    if is_stopped == False:
        radio.send_string("" + message1 + " - " + username)
        datalogger.log(datalogger.create_cv("",
                "" + username_full + " sent " + message1 + " to " + targetuser_full + " via " + ("" + str(control.device_serial_number()))))
        basic.clear_screen()
        create_faceV2("left")
    else:
        pass
input.on_button_pressed(Button.A, on_button_pressed_a)

def shutdown():
    global is_stopped
    basic.clear_screen()
    basic.show_icon(IconNames.NO)
    is_stopped = True
def create_faceV2(eye: str):
    faces.show_face(faces.Eyes.OPEN, faces.Mouth.GRIN)
    if eye == "left":
        faces.wink(True, 750, False)
    else:
        faces.wink(False, 750, False)

def on_button_pressed_ab():
    if is_stopped == False:
        radio.send_string("" + message3 + " - " + username)
        datalogger.log(datalogger.create_cv("",
                "" + username_full + " sent " + message3 + " to " + targetuser_full + " via " + ("" + str(control.device_serial_number()))))
        basic.clear_screen()
        create_faceV2("left")
    else:
        pass
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def setMessageType(authpass: str, messageType: str):
    global message1, message2, message3
    if authpass == "admin":
        if messageType == "basic_messages":
            pass
        elif messageType == "morse_code":
            message1 = "."
            message2 = "-"
            message3 = "<space>"
        elif messageType == "teachermode":
            message1 = "Where are you?"
            message2 = "I'm at Zone 1!"
            message3 = "My students are all here."
        elif messageType == "disabled":
            message1 = ""
            message2 = ""
            message3 = ""
        else:
            basic.show_string("Missing 'messageType' parameter.")
    else:
        basic.show_string("Incorrect administrator password, authorization denied")

def on_received_string(receivedString):
    basic.show_string(receivedString)
radio.on_received_string(on_received_string)

def on_button_pressed_b():
    if is_stopped == False:
        radio.send_string("" + message2 + " - " + username)
        datalogger.log(datalogger.create_cv("",
                "" + username_full + " sent " + message2 + " to " + targetuser_full + " via " + ("" + str(control.device_serial_number()))))
        basic.clear_screen()
        create_faceV2("right")
    else:
        pass
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_logo_pressed():
    global is_stopped
    if is_stopped == True:
        if shutdown_by_time == True:
            pass
        else:
            basic.clear_screen()
            is_stopped = False
            create_faceV2("left")
    elif shutdown_by_time == True:
        pass
    else:
        shutdown()
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

time_used = 0
is_stopped = False
shutdown_by_time = False
message3 = ""
message2 = ""
message1 = ""
username = ""
targetuser_full = ""
username_full = ""
username_full = "Jo Hang Johann LO (3019011)"
targetuser_full = "Josette Yeuk Kuk YAM (3120002)"
username = "imtrollmastr"
targetuser = "J2STARWARSGIRL"
message1 = "Good morning! / Good"
message2 = "Good night! / Bad"
message3 = "How are you?"
ms_screentime = 150000
shutdown_by_time = False
radio.set_group(66)
create_faceV2("left")
led.set_brightness(255)
setMessageType("admin", "basic_messages")

def on_every_interval():
    global time_used, shutdown_by_time, is_stopped
    time_used += 1
    if time_used == 15:
        basic.clear_screen()
        basic.show_string("Locked due to screen time.")
        shutdown_by_time = True
        is_stopped = True
    else:
        pass
loops.every_interval(60000, on_every_interval)
