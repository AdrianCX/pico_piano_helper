# Example showing how functions, that accept tuples of rgb values,
# simplify working with gradients

import array, time
from neopixel import Neopixel

colors_rgb=[(255, 0, 0),(255, 50, 0),(255, 100, 0),(255, 150, 0),(255, 200, 0),(255, 255, 0),
             (0, 255, 0), (0, 255, 50), (0, 255, 100),(0, 255, 150), (0, 255, 200), (0, 255, 255),
             (50, 50, 255), (100, 50, 255), (150, 50, 255),(200, 50, 255), (255, 50, 255), (255, 100, 255),
              (255, 150, 255), (255, 200, 255),(255, 250, 255)]

class Gradient:

    def __init__(self):
        numpix = 61
        self.numpix = numpix
        self.strip = Neopixel(numpix, 1, 0, "GRB")
        self.show_gradient()
        self.keys = array.array("I", [0] * numpix)
    
    def clear_key(self, key):
        if key >=0 and key < 61:
            self.strip.set_pixel(key, (0,0,0))
            self.keys[key] = 0
            self.strip.show()
    
    def show_key(self, key):
        if self.display_type != "keys":
            for i in range(0, self.numpix):
                self.keys[i] = 0
                self.strip.set_pixel(i, (0,0,0))
            self.strip.brightness(20)
        
        self.display_type = "keys"
        
        if key >=0 and key < 61:
            self.keys[key] = time.ticks_ms() + 5100
            #green = (0, 255, 0)
            self.strip.set_pixel(key, colors_rgb[(key*time.ticks_ms()*3323)%len(colors_rgb)])

        self.strip.show()
    
    def show_gradient(self):
        self.display_type = "gradient"
        
        numpix = 61
        red = (255, 0, 0)
        orange = (255, 50, 0)
        yellow = (255, 100, 0)
        green = (0, 255, 0)
        blue = (0, 0, 255)
        indigo = (100, 0, 90)
        violet = (200, 0, 100)
        colors_rgb = [red, orange, yellow, green, blue, indigo, violet]

        # same colors as normaln rgb, just 0 added at the end
        colors_rgbw = [color+tuple([0]) for color in colors_rgb]
        colors_rgbw.append((0, 0, 0, 255))

        # uncomment colors_rgbw if you have RGBW strip
        colors = colors_rgb
        # colors = colors_rgbw

        step = round(numpix / len(colors))
        current_pixel = 0
        self.strip.brightness(20)

        for color1, color2 in zip(colors, colors[1:]):
            self.strip.set_pixel_line_gradient(current_pixel, current_pixel + step, color1, color2)
            current_pixel += step

        self.strip.set_pixel_line_gradient(current_pixel, numpix - 1, violet, red)

        self.deadline = time.ticks_add(time.ticks_ms(), 42)


    def update(self):
        if self.display_type == "gradient":
            if time.ticks_diff(self.deadline, time.ticks_ms()) < 0:
                self.strip.rotate_right(1)
                self.strip.show()
                self.deadline = time.ticks_add(time.ticks_ms(), 42)
        elif self.display_type == "keys":
            for i,ts in enumerate(self.keys):
                if ts != 0:
                    diff = time.ticks_diff(ts, time.ticks_ms())
                    if diff > 2550 and diff < 5100:
                        self.strip.set_pixel(i, (255-(diff-2550)/10, (diff-2550)/10, 0))
                    elif diff > 0 and diff < 2550:
                        self.strip.set_pixel(i, (diff/10, 0, 255-diff/10))
                    else:
                        self.strip.set_pixel(i, (0, 0, 0))
                        self.keys[i] = 0
                else:
                    self.strip.set_pixel(i, (0, 0, 0))
                    
            self.strip.show()

    def clear(self):
        self.display_type = ""
        self.strip.brightness(0)
        self.strip.clear()
        self.strip.show()
