from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

admin.site.register(User, UserAdmin)    # user만드는 과정에만 UserAdmin이 필요 다른 admin 파일엔 import할 class 이름만 넣으면 됨