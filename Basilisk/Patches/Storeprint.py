class Storeprint:
  print_ = print
  store = ""
  
  def print(self, *args, end="\n", flush=False):
    i=1
    l=len(args)
    for arg in args:
      self.store = self.store + str(arg)
      if l!=i: self.store = self.store + " "
      i = i+1
    self.store = self.store + end
    if flush: self.flush()
  
  def flush(self):
    self.print_(self.store,end="", flush=True)
    self.store = ""
  
  def destroy(self):
    self.store = ""
StoreprintInstance = Storeprint()
print = StoreprintInstance.print
flushstdout = StoreprintInstance.flush
destroystdoutstore = StoreprintInstance.destroy