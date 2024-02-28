def on_button_pressed_a():
    if is_stopped == False:
        radio.send_string("" + message1 + " - " + username)
        datalogger.log(datalogger.create_cv("",
                "" + username + " sent " + message1 + " to " + targetuser))
        basic.show_leds("""
            . . . . .
            . . . . #
            . . . # .
            # . # . .
            . # . . .
            """)
        basic.pause(100)
        basic.clear_screen()
    else:
        pass
input.on_button_pressed(Button.A, on_button_pressed_a)

def shutdown():
    global is_stopped
    basic.clear_screen()
    basic.show_icon(IconNames.NO)
    is_stopped = True

def on_button_pressed_ab():
    if is_stopped == False:
        radio.send_string("" + message3 + " - " + username)
        datalogger.log(datalogger.create_cv("",
                "" + username_full + " sent " + message3 + " to " + targetuser_full))
        basic.show_leds("""
            . . . . .
            . . . . #
            . . . # .
            # . # . .
            . # . . .
            """)
        basic.pause(100)
        basic.clear_screen()
    else:
        pass
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_received_string(receivedString):
    basic.show_string(receivedString)
radio.on_received_string(on_received_string)

def on_button_pressed_b():
    if is_stopped == False:
        radio.send_string("" + message2 + " - " + username)
        datalogger.log(datalogger.create_cv("",
                "" + username_full + " sent " + message2 + " to " + targetuser_full))
        basic.show_leds("""
            . . . . .
            . . . . #
            . . . # .
            # . # . .
            . # . . .
            """)
        basic.pause(100)
        basic.clear_screen()
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
    else:
        if shutdown_by_time == True:
            pass
        else:
            shutdown()
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

is_stopped = False
shutdown_by_time = False
message3 = ""
message2 = ""
message1 = ""
targetuser = ""
username = ""
targetuser_full = ""
username_full = ""
faces.show_face(faces.Eyes.OPEN, faces.Mouth.FLAT)
teacher_mode = False
username_full = "Jo Hang Johann LO (3019011)"
targetuser_full = "Josette Yeuk Kuk YAM (3120002)"
username = "imtrollmastr"
targetuser = "J2STARWARSGIRL"
message1 = "Hi!"
message2 = "How are you?"
message3 = "Great!"
ms_screentime = 900000
time_used = 0
shutdown_by_time = False
troll_mode = False
radio.set_group(66)
if troll_mode == True:
    pass
else:
    pass

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
