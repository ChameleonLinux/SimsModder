import sys, subprocess, os
from Basilisk import Logger
import urllib.request
class Downloader:
  def __init__(self, sm):
    self.scope = sm.Scope
  def get(self, data):
    id, dest, type, url = data
    fname = url.split("/")[-1:][0]
    useragent = self.scope['UserAgent']
    dest = self.scope['Directories'][dest]
    if os.path.exists(self.scope['Directories']['Cache'] + "/" + fname):
      Logger.warn("Using from cache: " + fname)
      self.decompress(fname, dest, type)
      return
    Logger.warn("Downloading: "+url)
    req = urllib.request.Request(url, data=None, headers={"User-Agent": useragent})
    response = urllib.request.urlopen(req)
    o_ = open(self.scope['Directories']['Cache'] + "/" + fname, "wb")
    o_.write(response.read())
    o_.close()
    self.decompress(fname, dest, type)
  def decompress(self, fname, dest, type):
    Logger.info("Decompressing...")
    subprocess.call(["7z", "e", self.scope['Directories']['Cache'] + "/" + fname, "-o"+dest, self.scope['FileTypes'][type], "-r"])
    try:
      self.scope['Hooks'][type]['Extracted'](fname, dest)
    except KeyError: pass