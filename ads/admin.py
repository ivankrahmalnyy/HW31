from django.contrib import admin
from django.contrib.auth.models import User

from ads.models import Ad, Category
from users.models import Location

admin.site.register(Ad)
admin.site.register(Category)


