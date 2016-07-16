from Basilisk.Taszka.Foreground import Foreground
import sys
class Logger:
  fore = Foreground()
  def info(self, msg):
    print(self.fore.cyan, "[info]", msg, end="")
    self.clear()

  def warn(self, msg):
    print(self.fore.yellow, "[warn]", msg, end="")
    self.clear()

  def err(self, msg):
    print(self.fore.red, "[err]", msg, end="")
    self.clear()

  def fatal(self, msg):
    print(self.fore.red, "[fatal]", msg, end="")
    self.clear()
    sys.exit(1)

  def success(self, msg):
    print(self.fore.green, "[success]", msg, end="")
    self.clear()
    
  def clear(self):
    print(self.fore.reset)

getInstance = Logger()
info = getInstance.info
success = getInstance.success
warn = getInstance.warn
err = getInstance.err
fatal = getInstance.fatal