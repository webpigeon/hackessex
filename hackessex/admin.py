from django.contrib import admin
from .models import Room, Question, Answer

# Register models
class QuestionAdmin(admin.ModelAdmin):
    list_display = ["__str__", "room", "votes"]
    list_filter = ["category", "room"]
    search_fields = ["text"]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Room)
admin.site.register(Answer)
