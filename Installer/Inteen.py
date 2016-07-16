from Basilisk import Logger
import os
class _:
  def __init__(self, scope={}): self.scope = scope
  def __call__(self, fname, dest):
    Logger.info("Moving zzzInTeenimater_G.package to AL overrides")
    if os.path.exists(self.scope['Directories']['ALOverrides']+"/zzzInTeenimater_G.package"): os.remove(self.scope['Directories']['ALOverrides']+"/zzzInTeenimater_G.package")
    os.rename(dest+"/zzzInTeenimater_G.package", self.scope['Directories']['ALOverrides']+"/zzzInTeenimater_G.package")