from bs4 import BeautifulSoup
import sys, subprocess, os
from Basilisk import Logger
import urllib.request
class Downloader:
  def __init__(self, sm):
    self.scope = sm.Scope
  def get(self, data):
    id, dest, type, fname = data
    Logger.info("Downloading informations... ("+str(id)+")")
    useragent = self.scope['UserAgent']
    dest = self.scope['Directories'][dest]
    if os.path.exists(self.scope['Directories']['Cache'] + "/" + fname):
      if not "ignore_cached" in sys.argv:
        Logger.warn("Using from cache: " + fname)
        self.decompress(fname, dest, type)
      return
    url = "http://modthesims.info/download.php?t=" + id + "#actualtab1"
    req = urllib.request.Request(url, data=None, headers={"User-Agent": useragent})
    response = urllib.request.urlopen(req)
    html = b''
    chunk = True
    while chunk:
      chunk = response.read(1024)
      html += chunk
    html = BeautifulSoup(html, "html.parser")
    title = html.body.find('div', attrs={'class': "well profilepic well-small well-inline"}).find("h2").text.strip()
    author = html.body.find('div', attrs={'class': "well profilepic well-small well-inline"}).find("div", attrs={'class': "pull-left"}).text.strip().replace("\n", " ")
    try:
      author = author.split(" ", 2)[1]
    except Exception:
      author = "(unknown)"
    Logger.warn("Downloading: "+"\""+title+"\" ("+fname+") by " + author +" ("+url+")")
    files = html.body.find('div', attrs={'id': 'actualtab1'}).find('tbody').find_all('tr')
    furl = None
    try:
      for file in files:
        a = file.find("a")
        if a.text.strip() == fname:
          furl = a['href']
          break
    except Exception:
      furl = None
    if not furl:
      if not "mts_ignore_errors" in sys.argv:
        Logger.fatal("No such file.")
      else: Logger.err("No such file.")
    Logger.info("Found URL: " + furl)
    req = urllib.request.Request(furl, data=None, headers={"User-Agent": useragent})
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