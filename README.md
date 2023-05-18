Raspberry pi pico piano lights

![Alt text](/pictures/piano.jpg "")

Pull requests welcome.

# 1. Introduction

Can display a static gradient effect.

Can also display keys in sequence based on a converted midi file. (with variable delays and minimum key lengths)
This is pretty fun for learning.

It's controlled via HTTP:

![Alt text](/pictures/webui.jpg "")


# 2. How to use

a. Set up micropython on pico (use the firmware for 'Raspberry Pi Pico W (with urequests and upip preinstalled)') URL https://www.raspberrypi.com/documentation/microcontrollers/micropython.html

b. Update 'src/config.py' with your SSID and password. Copy all files from pico folder to the microcontroller. (you can use thonny for this)

c. Run main.py via thonny and grab the ip address from the output. (you can set it up as static IP on the router so it doesn't change and you know what to connect to later)

d. Log into web ui and issue commands.

# 3. How to convert other songs

a. Download midi you want.

b. Go to 'converter/' subfolder and check out readme there.


# 4. How to make this


4.1. Parts used:

![Alt text](/pictures/parts.jpg "")

a. Raspberry pi pico

https://www.kiwi-electronics.com/nl/raspberry-pi-pico-w-10938?search=raspberry%20pi%20pico

b. Leds

You usually need ~61 leds. Using 30 per meter so we can arrange as needed without cutting and soldering: https://www.tinytronics.nl/shop/en/lighting/led-strips/led-strips/worldsemi-ws2813-digital-5050-rgbw-led-strip-30-leds-5m
   
Or multiple smaller bundles: https://www.tinytronics.nl/shop/en/lighting/led-strips/led-strips/ws2812b-digital-5050-rgb-led-strip-30-leds-1m

c. White and black insulation tapes

leds can light up through white insulation tape, black for accents.

d. A wooden stick or some sort of support.

Since we're covering with white tape, it doesn't matter how pretty it is.

e. JST 3 pin/4pin cable

Useful if you want to connect/disconnect leds, otherwise can solder directly onto pico and skip

https://www.kiwi-electronics.com/nl/2-5mm-pitch-3-pin-kabelset-jst-xh-compatibel-10998?search=jst%203

f. Some M2 nuts to fix pico to a box

https://www.kiwi-electronics.com/nl/messing-male-female-spacer-set-m2-5-120-stuks-9965?search=m2

g. Some random plastic box that you can use a cutter on to open up usb/jst ports.


4.2. How to build:

a. Solder everything to the led strip so we can test that leds are working properly.

b. Align leds onto wooden stick with the keys on piano.

It helps that there's a lot of space between leds, we can bend as needed to align them.

![Alt text](/pictures/before_tape.jpg "")

c. Apply white tape over each tape / covering the whole stick.

d. Apply black tape where black keys are (don't cover leds)

