import arrow
from django.contrib.auth.models import User
from django.conf import settings

def myTime():
    _t = arrow.utcnow()
    _mt = _t.to('Africa/Lagos')
    return _mt

def userInfo(u):
    user = User.objects.get(username=u)
    return user

def BaseUrl(r):
    h = r.scheme
    p = r.get_host()
    return f"{h}://{p}"
# URL = 

Key = settings.CKEY