# CircuitPy code to make IBM Model M USB compatible.

The project is similar to those Teensy board Model M driver kits
(e.g. this: https://blog.lmorchard.com/2016/02/21/modelm-controller/),
but with a Raspberry Pi Pico, because it's dirt cheap.

I have a 1391406 version with hungarian layout.
The original board was fully replaced by my solution, I wrote the "firmware" too,
but had to compromise. 

* the first 16 GPIO pins are connected to the 16 pin membrane connector 
of the keyboard (GP0 to pin1, GP1 to pin2, etc.)
* the next 8 GPIO pins are connected to the 8 pin membrane connector of the keyboard
(GP16 to pin1, GP17 to pin2, etc.)
* the GPIO 27 led is num lock led, I put a 330 Ohm resistor before the led
* the GPIO 28 led is caps lock led, with another 330 Ohm resistor 
* I run out of pins so scroll lock led is not used, but I never use that,
so it's ok for me

### Preparations

* connect pins the GPIO pins to the membrane connector of your board,
I used these sockets: 
  * https://www.tme.eu/hu/details/ds1020-16st1d/ffc-fpc-csatlakozok-raszter-2-54mm/connfly/
  * https://www.tme.eu/hu/details/ds1020-08st1d/ffc-fpc-csatlakozok-raszter-2-54mm/connfly/
  * https://www.tme.eu/hu/details/ds1020-04st1d/ffc-fpc-csatlakozok-raszter-2-54mm/connfly/
* the led board can be re-used 
* install Circuit Python to your raspberry pi pico: https://circuitpython.org/board/raspberry_pi_pico/

### Installation

Just copy the contents of the repo to the root folder of your pico.

### Disadvantages

* as I mentioned before, because the GPIO pins are less than the originally
required connections, I had to sacrifice the scroll lock led
(if you are brave/skilled enough, you can use the pico's own led,
given that you can wire it up)
* the Model M is a 2KRO keyboard, see `Secrets of 2KRO Matrices` chapter
of the Les Orchard blog, tl;dr: there is some key combos which you can't press
together at the same time
* you tell me

### Other notes
The usb storage mode is disabled to decrease chance of file system corruption
if the pico is removed unsafely.
If you want to access the pico's usb storage mode, press the D (as debug) key when
connecting the device to the computer.
