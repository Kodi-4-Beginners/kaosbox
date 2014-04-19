import os
import sys
import xbmc
import xbmcgui
import xbmcaddon
import datetime
import _strptime
import urllib

if sys.version_info < (2, 7):
    import simplejson
else:
    import json as simplejson

print xbmc.executeJSONRPC('{"jsonrpc": "2.0", "method": "JSONRPC.Introspect", "id": 1}')