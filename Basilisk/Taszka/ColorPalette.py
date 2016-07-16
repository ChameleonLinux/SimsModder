class ColorPalette:
  def __init__(self):
    self.registerDict(self.__register__())
  
  def registerDict(self, data):
    for key, value in data.items():
      self.register(key, value)
  
  def register(self, key, value):
    setattr(self, key, value)
    
  def swap(self, key1, key2):
    value1 = getattr(self, key1)
    value2 = getattr(self, key2)
    setattr(self, key1, value2)
    setattr(self, key2, value1)