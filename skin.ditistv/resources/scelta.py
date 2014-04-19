import xbmc, xbmcaddon, xbmcgui, xbmcplugin, os
from sqlite3 import dbapi2 as sqlite3
import urllib2,urllib
import re
import shutil
import glob
import sys

print '--------------------------------------------'
print sys.argv[1]
print '--------------------------------------------'

localtxt1 = 'Playing Options'
localtxt3 = 'Activate Cinema Experience?'
dialog = xbmcgui.Dialog()

class MyClass(xbmcgui.Window):
  def __init__(self):
    if dialog.yesno(localtxt1, localtxt3):
      xbmc.executebuiltin("XBMC.RunScript(script.cinema.experience,movieid="+sys.argv[1]+")")
    else:
      xbmc.executeJSONRPC('{"jsonrpc": "2.0", "method": "Player.Open", "params": {"item": {"movieid": '+sys.argv[1]+'}, "options": {"resume": true}}, "id": 1}' )

mydisplay = MyClass()
del mydisplay