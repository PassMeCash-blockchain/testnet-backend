from django.conf import settings
import string, random, uuid, json, requests as req, asyncio

URLs = {
    "authUrl": "http://localhost:7781/"
}

# def Res(res):
#     pass

Key = settings.CKEY
url = URLs["authUrl"]

async def lastLogin(access):
    await req.post(f"{url}auth/v1/lastlogin", headers={"Authorization": access})