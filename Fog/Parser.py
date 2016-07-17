from Basilisk import Logger
def read(fname):
  f = open(fname, "r")
  super = {}
  data = []
  try:
    for l in f.readlines():
      l = l.strip()
      if l[0] == "#":
        continue
      if l[0] == "@":
        l = l[1:].split(" ", 1)
        super[l[0].strip()] = l[1].strip()
      elif l.startswith("- "): 
        l = l[2:].strip().split(" ", 3)
        data.append(l)
  except Exception as e:
    Logger.err("Parse error.")
    Logger.fatal(e)
  return {"super": super, "data": data}