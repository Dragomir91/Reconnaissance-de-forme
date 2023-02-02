from django.contrib import admin
from .models import Question, Choice, Persone, Login

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']


    
class PersoneAdmin(admin.ModelAdmin):
    fields =    ['first_name','last_name','age_name']    
    list_display = ('first_name', 'last_name', 'age_name')



admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Login)
admin.site.register(Persone,PersoneAdmin)
# Register your models here.
