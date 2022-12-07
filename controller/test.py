import board
import neopixel
pixels = neopixel.NeoPixel(board.D18, 30, brightness=1)


pixels[0] = (255, 0, 0)
pixels.show()
