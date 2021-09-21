from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed

from django.contrib.auth.models import User
from django.db import connection
from django.dispatch import receiver
@receiver(user_logged_in,sender=User) 
#(connection using decorators or receiver Function, This will be set above defined function.)
def login_success(sender,request,user,**kwargs):
    print('________')
    print('This is login Success Signal')
    print('sender',sender)
    print('Request',request)
    print('User',user)
    print('User',user.password)
    print(f'Kwargs:{kwargs}')
    #user_logged_in.connect(login_success,sender=User)  # Mannual Connection
    