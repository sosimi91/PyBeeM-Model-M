import board
import digitalio
import time
import usb_hid

from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode


in_pin_numbers = [
    board.GP0, board.GP1, board.GP2, board.GP3,
    board.GP4, board.GP5, board.GP6, board.GP7,
    board.GP8, board.GP9, board.GP10, board.GP11,
    board.GP12, board.GP13, board.GP14, board.GP15,

]


out_pin_numbers = [
    board.GP16, board.GP17, board.GP18, board.GP19,
    board.GP20, board.GP21, board.GP22, board.GP26,
    board.GP27, board.GP28
]

input_pins = []
output_pins = []

num_lock_led = None
caps_lock_led = None

keyboard = Keyboard(usb_hid.devices)


class MyKey:
    def __init__(self, name, code, key_type):
        self.name = name
        self.code = code
        self.type = key_type


keyboard_mapping = [
    # IN0
    [
        None,                                                                   # OUT0
        None,                                                                   # OUT1
        MyKey("LEFT_CONTROL", Keycode.LEFT_CONTROL, "modifier"),                # OUT2
        None,                                                                   # OUT3
        None,                                                                   # OUT4
        None,                                                                   # OUT5
        MyKey("RIGHT_CONTROL", Keycode.RIGHT_CONTROL, "modifier"),              # OUT6
        None                                                                    # OUT7
    ],
    # IN1
    [
        None,                                                                   # OUT0
        MyKey("LEFT_SHIFT", Keycode.LEFT_SHIFT, "modifier"),                    # OUT1
        None,                                                                   # OUT2
        None,                                                                   # OUT3
        None,                                                                   # OUT4
        None,                                                                   # OUT5
        MyKey("RIGHT_SHIFT", Keycode.RIGHT_SHIFT, "modifier"),                  # OUT6
        None                                                                    # OUT7
    ],
    # IN2
    [
        MyKey("ESCAPE", Keycode.ESCAPE, "key"),                                 # OUT0
        MyKey("TAB", Keycode.TAB, "key"),                                       # OUT1
        MyKey("GRAVE_ACCENT", Keycode.GRAVE_ACCENT, "key"),                     # OUT2
        MyKey("ONE", Keycode.ONE, "key"),                                       # OUT3
        MyKey("Q", Keycode.Q, "key"),                                           # OUT4
        MyKey("A", Keycode.A, "key"),                                           # OUT5
        MyKey("Z", Keycode.Z, "key"),                                           # OUT6
        None                                                                    # OUT7
    ],
    # IN3
    [
        MyKey("KEYPAD_BACKSLASH", Keycode.KEYPAD_BACKSLASH, "key"),             # OUT0
        MyKey("CAPS_LOCK", Keycode.CAPS_LOCK, "key"),                           # OUT1
        MyKey("F1", Keycode.F1, "key"),                                         # OUT2
        MyKey("TWO", Keycode.TWO, "key"),                                       # OUT3
        MyKey("W", Keycode.W, "key"),                                           # OUT4
        MyKey("S", Keycode.S, "key"),                                           # OUT5
        MyKey("X", Keycode.X, "key"),                                           # OUT6
        None                                                                    # OUT7
    ],
    # IN4
    [
        MyKey("F4", Keycode.F4, "key"),                                         # OUT0
        MyKey("F3", Keycode.F3, "key"),                                         # OUT1
        MyKey("F2", Keycode.F2, "key"),                                         # OUT2
        MyKey("THREE", Keycode.THREE, "key"),                                   # OUT3
        MyKey("E", Keycode.E, "key"),                                           # OUT4
        MyKey("D", Keycode.D, "key"),                                           # OUT5
        MyKey("C", Keycode.C, "key"),                                           # OUT6
        None                                                                    # OUT7
    ],
    # IN5
    [
        MyKey("G", Keycode.G, "key"),                                           # OUT0
        MyKey("T", Keycode.T, "key"),                                           # OUT1
        MyKey("FIVE", Keycode.FIVE, "key"),                                     # OUT2
        MyKey("FOUR", Keycode.FOUR, "key"),                                     # OUT3
        MyKey("R", Keycode.R, "key"),                                           # OUT4
        MyKey("F", Keycode.F, "key"),                                           # OUT5
        MyKey("V", Keycode.V, "key"),                                           # OUT6
        MyKey("B", Keycode.B, "key")                                            # OUT7
    ],
    # IN6
    [
        MyKey("F5", Keycode.F5, "key"),                                         # OUT0
        MyKey("BACKSPACE", Keycode.BACKSPACE, "key"),                           # OUT1
        MyKey("F9", Keycode.F9, "key"),                                         # OUT2
        MyKey("F10", Keycode.F10, "key"),                                       # OUT3
        None,                                                                   # OUT4
        None,                                                                   # OUT5
        MyKey("ENTER", Keycode.ENTER, "key"),                                   # OUT6
        MyKey("SPACE", Keycode.SPACE, "key")                                    # OUT7
    ],
    # IN7
    [
        MyKey("H", Keycode.H, "key"),                                           # OUT0
        MyKey("Y", Keycode.Y, "key"),                                           # OUT1
        MyKey("SIX", Keycode.SIX, "key"),                                       # OUT2
        MyKey("SEVEN", Keycode.SEVEN, "key"),                                   # OUT3
        MyKey("U", Keycode.U, "key"),                                           # OUT4
        MyKey("J", Keycode.J, "key"),                                           # OUT5
        MyKey("M", Keycode.M, "key"),                                           # OUT6
        MyKey("N", Keycode.N, "key")                                            # OUT7
    ],
    # IN8
    [
        MyKey("F6", Keycode.F6, "key"),                                         # OUT0
        MyKey("RIGHT_BRACKET", Keycode.RIGHT_BRACKET, "key"),                   # OUT1
        MyKey("EQUALS", Keycode.EQUALS, "key"),                                 # OUT2
        MyKey("EIGHT", Keycode.EIGHT, "key"),                                   # OUT3
        MyKey("I", Keycode.I, "key"),                                           # OUT4
        MyKey("K", Keycode.K, "key"),                                           # OUT5
        MyKey("COMMA", Keycode.COMMA, "key"),                                   # OUT6
        None                                                                    # OUT7
    ],
    # IN9
    [
        None,                                                                   # OUT0
        MyKey("F7", Keycode.F7, "key"),                                         # OUT1
        MyKey("F8", Keycode.F8, "key"),                                         # OUT2
        MyKey("NINE", Keycode.NINE, "key"),                                     # OUT3
        MyKey("O", Keycode.O, "key"),                                           # OUT4
        MyKey("L", Keycode.L, "key"),                                           # OUT5
        MyKey("PERIOD", Keycode.PERIOD, "key"),                                 # OUT6
        None                                                                    # OUT7
    ],
    # IN10
    [
        MyKey("QUOTE", Keycode.QUOTE, "key"),                                   # OUT0
        MyKey("LEFT_BRACKET", Keycode.LEFT_BRACKET, "key"),                     # OUT1
        MyKey("MINUS", Keycode.MINUS, "key"),                                   # OUT2
        MyKey("ZERO", Keycode.ZERO, "key"),                                     # OUT3
        MyKey("P", Keycode.P, "key"),                                           # OUT4
        MyKey("SEMICOLON", Keycode.SEMICOLON, "key"),                           # OUT5
        MyKey("BACKSLASH", Keycode.BACKSLASH, "key"),                           # OUT6
        MyKey("FORWARD_SLASH", Keycode.FORWARD_SLASH, "key")                    # OUT7
    ],
    # IN11
    [
        None,                                                                   # OUT0
        MyKey("KEYPAD_FOUR", Keycode.KEYPAD_FOUR, "key"),                       # OUT1
        MyKey("DELETE", Keycode.DELETE, "key"),                                 # OUT2
        MyKey("F11", Keycode.F11, "key"),                                       # OUT3
        MyKey("KEYPAD_SEVEN", Keycode.KEYPAD_SEVEN, "key"),                     # OUT4
        MyKey("KEYPAD_ONE", Keycode.KEYPAD_ONE, "key"),                         # OUT5
        MyKey("KEYPAD_NUMLOCK", Keycode.KEYPAD_NUMLOCK, "modifier"),            # OUT6
        MyKey("DOWN_ARROW", Keycode.DOWN_ARROW, "key")                          # OUT7
    ],
    # IN12
    [
        MyKey("KEYPAD_ZERO", Keycode.KEYPAD_ZERO, "key"),                       # OUT0
        MyKey("KEYPAD_FIVE", Keycode.KEYPAD_FIVE, "key"),                       # OUT1
        MyKey("INSERT", Keycode.INSERT, "key"),                                 # OUT2
        MyKey("F12", Keycode.F12, "key"),                                       # OUT3
        MyKey("KEYPAD_EIGHT", Keycode.KEYPAD_EIGHT, "key"),                     # OUT4
        MyKey("KEYPAD_TWO", Keycode.KEYPAD_TWO, "key"),                         # OUT5
        MyKey("KEYPAD_FORWARD_SLASH", Keycode.KEYPAD_FORWARD_SLASH, "key"),     # OUT6
        MyKey("RIGHT_ARROW", Keycode.RIGHT_ARROW, "key")                        # OUT7
    ],
    # IN13
    [
        MyKey("KEYPAD_PERIOD", Keycode.KEYPAD_PERIOD, "key"),                   # OUT0
        MyKey("KEYPAD_SIX", Keycode.KEYPAD_SIX, "key"),                         # OUT1
        MyKey("PAGE_UP", Keycode.PAGE_UP, "key"),                               # OUT2
        MyKey("PAGE_DOWN", Keycode.PAGE_DOWN, "key"),                           # OUT3
        MyKey("KEYPAD_NINE", Keycode.KEYPAD_NINE, "key"),                       # OUT4
        MyKey("KEYPAD_THREE", Keycode.KEYPAD_THREE, "key"),                     # OUT5
        MyKey("KEYPAD_ASTERISK", Keycode.KEYPAD_ASTERISK, "key"),               # OUT6
        MyKey("KEYPAD_MINUS", Keycode.KEYPAD_MINUS, "key")                      # OUT7
    ],
    # IN14
    [
        MyKey("UP_ARROW", Keycode.UP_ARROW, "key"),                             # OUT0
        None,                                                                   # OUT1
        MyKey("HOME", Keycode.HOME, "key"),                                     # OUT2
        MyKey("END", Keycode.END, "key"),                                       # OUT3
        MyKey("KEYPAD_PLUS", Keycode.KEYPAD_PLUS, "key"),                       # OUT4
        MyKey("KEYPAD_ENTER", Keycode.KEYPAD_ENTER, "key"),                     # OUT5
        MyKey("PAUSE", Keycode.PAUSE, "key"),                                   # OUT6
        MyKey("LEFT_ARROW", Keycode.LEFT_ARROW, "key")                          # OUT7
    ],
    # IN15
    [
        MyKey("LEFT_ALT", Keycode.LEFT_ALT, "modifier"),                        # OUT0
        None,                                                                   # OUT1
        None,                                                                   # OUT2
        MyKey("PRINT_SCREEN", Keycode.PRINT_SCREEN, "key"),                     # OUT3
        MyKey("SCROLL_LOCK", Keycode.SCROLL_LOCK, "key"),                       # OUT4
        None,                                                                   # OUT5
        None,                                                                   # OUT6
        MyKey("RIGHT_ALT", Keycode.RIGHT_ALT, "modifier")                       # OUT7
    ]
]


def initialize():
    global num_lock_led
    global caps_lock_led

    for pin in out_pin_numbers:
        _out = digitalio.DigitalInOut(pin)
        if pin == board.GP27:
            num_lock_led = _out
        elif pin == board.GP28:
            caps_lock_led = _out
        else:
            output_pins.append(_out)
        _out.direction = digitalio.Direction.OUTPUT

    for pin in in_pin_numbers:
        _in_ = digitalio.DigitalInOut(pin)
        _in_.switch_to_input(pull=digitalio.Pull.DOWN)
        input_pins.append(_in_)


def pin_on(pin):
    pin.value = True


def pin_off(pin):
    pin.value = False


def check_leds():
    print("checking leds")
    if keyboard.led_on(Keyboard.LED_NUM_LOCK):
        print("turning on num lock")
        pin_on(num_lock_led)
    else:
        print("turning off num lock")
        pin_off(num_lock_led)
    if keyboard.led_on(Keyboard.LED_CAPS_LOCK):
        print("turning on caps lock")
        pin_on(caps_lock_led)
    else:
        print("turning off caps lock")
        pin_off(caps_lock_led)


initialize()

buffer = []

pin_on(num_lock_led)

while True:
    for o_index, out in enumerate(output_pins):
        pin_on(out)

        for i_index, in_ in enumerate(input_pins):
            key = keyboard_mapping[i_index][o_index]
            if key is None:
                continue

            if key in buffer and not in_.value:
                buffer.remove(key)
                keyboard.release(key.code)
                if key.name == "KEYPAD_NUMLOCK" or key.name == "CAPS_LOCK":
                    check_leds()

            elif key not in buffer and in_.value:
                if len(buffer) < 4:
                    keyboard.press(key.code)
                    buffer.append(key)
                    if key.name == "KEYPAD_NUMLOCK" or key.name == "CAPS_LOCK":
                        check_leds()

        time.sleep(0.0001)
        pin_off(out)
