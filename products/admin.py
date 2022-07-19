from django.contrib import admin
from .models import *


class ReactionAdmin(admin.ModelAdmin):
    list_display = ('reaction_id', 'reaction_desc')
    ordering = ['reaction_id']


admin.site.register(Reactions, ReactionAdmin)
