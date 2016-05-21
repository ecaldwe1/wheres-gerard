from django.contrib import admin
from game.models import Puzzle, Answer


class PuzzleAdmin(admin.ModelAdmin):
    list_display = ('creator', 'submission_time', 'latitude', 'longitude')
    list_filter = ('creator', 'submission_time')


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('puzzle', 'is_correct', 'creator', 'submission_time', 'latitude', 'longitude')
    list_filter = ('puzzle', 'is_correct', 'creator', 'submission_time')

admin.site.register(Puzzle, PuzzleAdmin)
admin.site.register(Answer, AnswerAdmin)
