import board
import digitalio
import storage


output_pin = digitalio.DigitalInOut(board.GP21)
output_pin.direction = digitalio.Direction.OUTPUT

input_pin = digitalio.DigitalInOut(board.GP4)
input_pin.switch_to_input(pull=digitalio.Pull.DOWN)

disable_usb_drive = True

output_pin.value = True
if input_pin.value:
    disable_usb_drive = False
    print("----------DEBUG MODE WITH STORAGE ENABLED----------")
output_pin.value = False

if disable_usb_drive:
    storage.disable_usb_drive()
    print("USB DRIVE DISABLED")
