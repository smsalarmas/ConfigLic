from socket import gethostname

import datetime
from Crypto.Cipher import XOR
from base64 import b64encode, b64decode
import uuid
from ConfigParser import ConfigParser


stringbd = 'Driver={SQL Server Native Client 11.0};Server=NOMBREPC;Database=NOMBREBD;Uid=USUARIOBD;Pwd=PASSWORDBD'
stringbd = stringbd.replace('NOMBREPC','SQL5021.Smarterasp.net')
stringbd = stringbd.replace('NOMBREBD','DB_9EED2C_SMSSecurePHP')
stringbd = stringbd.replace('USUARIOBD','DB_9EED2C_SMSSecurePHP_admin')
stringbd = stringbd.replace('PASSWORDBD','11ermsoft.')
    
deco = XOR.new(b64decode('MjAxMDE3MzMtOTYwOTkyNg=='))

StringBD =  b64encode(deco.encrypt(str(stringbd)))
print StringBD

Mac =  b64encode(deco.encrypt('20-10-7A-03-08-50'))
print Mac


PASSWORD = XOR.new(b64decode('MjAxMDE3MzMtOTYwOTkyNg=='))
print 'Lic:'
print PASSWORD.decrypt(b64decode('VAALVFQNVQIXX1MKXVsIDwM='))
print 'Modo:'
print PASSWORD.decrypt(b64decode('Aw=='))
print 'Formato:'
PASSWORD = XOR.new(b64decode('MjAxMDE3MzMtOTYwOTkyNg=='))
print PASSWORD.decrypt(b64decode('AgQABB0HBwEZFQYECA8eBgYCBxwBAwIB'))
print 'Web:'
PASSWORD = XOR.new(b64decode('MjAxMDE3MzMtOTYwOTkyNg=='))
print PASSWORD.decrypt(b64decode('AQYER1RVHVdJV0UeV1xG'))
print 'Web:'
PASSWORD = XOR.new(b64decode('MjAxMDE3MzMtOTYwOTkyNg=='))
print PASSWORD.decrypt(b64decode('dkJYRlRFDkh+aHoQalxAQFdCEX5QQ1pFSBl1XFBcXEISAQAeAUoIYEhLQFVLBHx5f3JjdWF0CHdMTVdSWEpXC19TAwQfWVweREkYXlxNCWNbVAxDUAxjREkEXFVLVA=='))

 


