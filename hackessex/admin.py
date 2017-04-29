from django.contrib import admin
from .models import Question, Answer

# Register models
class QuestionAdmin(admin.ModelAdmin):
    list_display = ["__str__", "votes"]
    list_filter = ["category"]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
