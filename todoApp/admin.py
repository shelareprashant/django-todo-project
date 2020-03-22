from django.contrib import admin
from .models import Todo

# We won't see the 'created' field becoz it is auto complete date. So see that customize the Admin

class TodoAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

admin.site.register(Todo, TodoAdmin)

