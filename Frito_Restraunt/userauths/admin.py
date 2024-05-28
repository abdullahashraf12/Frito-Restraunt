from django.contrib import admin
from userauths.models import User,UserToken
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ["username","email","bio"]
admin.site.register(User,UserAdmin)
class UserAdminToken(admin.ModelAdmin):
    list_display = ["user","token"]
admin.site.register(UserToken,UserAdminToken)