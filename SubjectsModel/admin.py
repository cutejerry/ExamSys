from django.contrib import admin
from SubjectsModel.models import Exam, Subject


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'degree', 'type', 'updated_time', 'created_time')
    search_fields = ('id', 'degree', 'type')
    fieldsets = (
        (None, {
            'fields': ('degree', 'type', 'content_txt', 'answer_idx',
                       'options1', 'options2', 'options3', 'options4',
                       'content_img', 'content_video')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('options5', 'options6', 'options7', 'options8',
                       'attr1', 'attr2', 'attr3'),
        }),
    )
    ordering = ('id',)

# Register your models here.
admin.site.register(Exam)
admin.site.register(Subject, SubjectAdmin)