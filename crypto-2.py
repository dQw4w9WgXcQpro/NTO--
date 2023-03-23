from requests import get
from Crypto.Util.number import *
from random import randint
import json

n = 93739530455107195424593189081154230539656451322535922885268747712514535610646170318979661937219836222970521137583578047683807409667969561303391553374903083353047337570586799959551978789627083753183331285415763394627518812670919666279048651115236595405568772346776555920536968462105178550559639932239331511203


bits = ''
for i in range(0,135):
    res = []
    for tries in range(50):
        r = get(f"http://10.10.2.10:1177/guess_bit?bit={i}")
        num = json.loads(r.text)["guess"]
        res.append(len(str(num)))
    pass
    if res.count(307) > 0:
        bits += '1'
        print(f"bit {i}: 1")
    else:
        bits += '0'
        print(f"bit {i}: 0")

print(bits)

