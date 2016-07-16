from Basilisk.Taszka.ColorPalette import ColorPalette
import colorama
colorama.init()
class Foreground(ColorPalette):
  def __init__(self):
    ColorPalette.__init__(self)
  
  def __register__(self):
    return {
      "black": '\033[30m',
      "red": '\033[31m',
      "green": '\033[32m',
      "yellow": '\033[33m',
      "blue": '\033[34m',
      "magenta": '\033[35m',
      "cyan": '\033[36m',
      "white": '\033[37m',
      "reset": '\033[39m'
    }