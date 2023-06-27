from django.contrib import admin
from .models import Ads
# Register your models here.
@admin.register(Ads)
class Adadmin(admin.ModelAdmin):
    list_display = ('title','is_public','publisher')
    