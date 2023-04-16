import arrow
from django.contrib.auth.models import User
from django.conf import settings

from .models import (
    UserDetail as UD,
    Stage,
    LastLogin as LL
)

Key = settings.CKEY

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

def getRegStage(u):
    stage = Stage.objects.get(user=userInfo(u))
    s1 = stage.stageOne
    s2 = stage.stageTwo
    s3 = stage.stageThree

    if s1 and s2 and s3:
        res = 'completed'
    if s1 and not s2 and not s3:
        res = 'step two'
    if s1 and s2 and not s3:
        res = 'step three'
    return res
