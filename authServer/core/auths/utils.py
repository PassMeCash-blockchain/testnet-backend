import arrow
from django.contrib.auth.models import User

def myTime():
    _t = arrow.utcnow()
    _mt = _t.to('Africa/Lagos')
    return _mt