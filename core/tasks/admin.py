from django.contrib import admin
from .models import Priority, Task
# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'priority')
    search_fields = ('id', 'user', 'title', 'priority')
    
class PriorityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    
admin.site.register(Priority, PriorityAdmin)
admin.site.register(Task, TaskAdmin)
