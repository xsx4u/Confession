from django.contrib import admin

# Register your models here.
from confession.models import Confession

class ConfessionAdmin(admin.ModelAdmin):
	fieldsets = [
	(None, {
		'fields': ('status','title','text','pub_date',('likes','dislikes'),'author'),
		})
	]

	list_display=('status','title','pub_date','author','is_popular')
		
admin.site.register(Confession, ConfessionAdmin)