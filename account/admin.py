from django.contrib import admin
from account.models import UserProfile


# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'birth', 'phone')
    search_fields = ('user__username', 'phone')


admin.site.register(UserProfile, UserProfileAdmin)
