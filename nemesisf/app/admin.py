from django.contrib import admin
from .models import Login, Signup
# Register your models here.
@admin.register(Login)
class LoginAdmin(admin.ModelAdmin):
    list_display = ('id','email','password')


@admin.register(Signup)
class SignupAdmin(admin.ModelAdmin):
    list_display = ('id','username','email', 'password', 'confirm_password', 'address')