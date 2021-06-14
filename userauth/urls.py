from django.urls import path, include
from .views import *

urlpatterns = [
    path('login/', login),
    path('signup/', sign_up),
    path('send/email/', send_email),
    path('check/code/', verify_code),
    path('check/username/', check_username),
    path('find/username/',send_username_on_email),
    path('accounts/', include('django.contrib.auth.urls'))
]