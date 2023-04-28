from django.conf import settings
import string, random, uuid, json, requests as req, asyncio, base64 
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from .sec import *


# def Res(res):
#     pass

Key = settings.CKEY
eKey = settings.EKEY
url = URLs["authUrl"]

async def lastLogin(access):
    await req.post(f"{url}auth/v1/lastlogin", headers={"Authorization":  f"Bearer {access}"})


def getUserInfo(token):
    res = req.post(f"{url}auth/v1/getUserInfo", headers={'Authorization': f"Bearer {token}"})
    return res



# def encrypt(raw, t = 'str'):
#     raw = pad(raw.encode(),16)
#     cipher = AES.new(eKey.encode('utf-8'), AES.MODE_ECB)
#     if t == 'str':
#         encrypted = base64.b64encode(cipher.encrypt(raw))
#         return encrypted.decode("utf-8", "ignore")
#     else:
#         encrypted = base64.b64encode(cipher.encrypt(json.loads(raw)))
#         return (encrypted.decode("utf-8", "ignore"))
         

# print(eKey)
# def decrypt(enc, t = 'str'):
#     enc = base64.b64decode(enc)
#     cipher = AES.new(eKey.encode('utf-8'), AES.MODE_ECB)
#     decrypted = unpad(cipher.decrypt(enc),16)
#     if t == 'str':
#         return decrypted.decode("utf-8", "ignore")
#     else:
#         return json.dumps(decrypted.decode("utf-8", "ignore"))
