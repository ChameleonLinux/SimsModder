from Basilisk.Taszka.ColorPalette import ColorPalette
import colorama
colorama.init()
class Background(ColorPalette):
  def __init__(self):
    ColorPalette.__init__(self)
  
  def __register__(self):
    return {
      "black": '\033[40m',
      "red": '\033[41m',
      "green": '\033[42m',
      "yellow": '\033[43m',
      "blue": '\033[44m',
      "magenta": '\033[45m',
      "cyan": '\033[46m',
      "white": '\033[47m',
      "reset": '\033[49m'
    }