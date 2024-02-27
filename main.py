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
                "" + username + " sent " + message3 + " to " + targetuser))
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
                "" + username + " sent " + message2 + " to " + targetuser))
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
        basic.clear_screen()
        is_stopped = False
    else:
        shutdown()
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

is_stopped = False
message3 = ""
message2 = ""
message1 = ""
targetuser = ""
username = ""
username = "Jo Hang Johann LO (3019011)"
targetuser = "Josette Yeuk Kuk YAM (3120002)"
message1 = "Hi!"
message2 = "How are you?"
message3 = "Great!"
ms_screentime = 900000
teacher_mode = False
radio.set_group(66)