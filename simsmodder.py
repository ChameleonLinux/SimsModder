import Fog.Parser, sys, os, time
from Basilisk import Logger

def __insmod__(path, r):
  mod = open(path, "r")
  try:
    exec(mod.read())
    mod.close()
  except Exception as e:
    mod.close()
    Logger.err("Module insertion failed: " + r)
    Logger.fatal(e)
def insmod(fname):
  __insmod__("Modules/"+fname+".py", fname)

class SimsModderConfigScope:
  Handlers = {}
  Fogs = []
  Temp = "out"
  Pause = 1
  Scope = {'Directories':{}}
SM = SimsModderConfigScope()

__insmod__("config.py", "config")
  
Logger.info("Sims Modder\t1.0")
Logger.warn("Compatible with The Sims 2. Some listings may require additional expansion packs.")
Logger.info("Using user-agent: " + SM.Scope['UserAgent'])
time.sleep(1)

Logger.info("Creating directories...")
for k,dir in SM.Scope['Directories'].items():
  if not os.path.exists(dir): os.mkdir(dir)
Logger.success("Done.")

Logger.info("Initializing downloaders...")
for k,v in SM.Handlers.items():
  SM.Handlers[k] = v(SM)
Logger.success("Downloaders initialized.")

Logger.info("Initializing hooks...")
for mk,__unused__ in SM.Scope['Hooks'].items():
  for k,v in SM.Scope['Hooks'][mk].items():
    SM.Scope['Hooks'][mk][k] = v(scope=SM.Scope)
Logger.success("Hooks initialized.")

Logger.info("Processing fog file(s)...")
Fogs = []
for fog in SM.Fogs:
  Fogs.append(Fog.Parser.read(fog))
Logger.success("Processed "+str(len(Fogs))+" fog file(s).")
if "debug" in sys.argv: print(Fogs)

Logger.info("Validation...")
index = 0
for fog in Fogs:
  if not fog["super"]["upstream"] in SM.Handlers:
    Logger.fatal("Unknown downloader: " + fog["super"]["upstream"])
  index = index+1
Logger.success("All fog files use valid downloaders.")

Logger.info("Running downloaders...")
for entry in Fogs:
  handler = SM.Handlers[entry['super']['upstream']]
  for d in entry['data']:
    handler.get(d)
    time.sleep(SM.Pause)