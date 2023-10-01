# Alexandria/people/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from people.models import Reader

class ReaderInline(admin.StackedInline):
    model = Reader
    can_delete = False


# Overload User admin model
class UserAdmin(BaseUserAdmin):
    inlines = (ReaderInline, )

    def get_inline_instances(self, request, obj=None):
        return super(UserAdmin, self).get_inline_instances(request, obj) if obj else []

# Register new User admin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
