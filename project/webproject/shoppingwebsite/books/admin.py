from django.contrib import admin
from books.models import Bookinfo,Person,UserRecommend,PuplationRecommend

class PersonAdmin(admin.ModelAdmin):
	llist_display = ('userid','location','age')
	search_fields = ['userid']

admin.site.register(Person,PersonAdmin)
admin.site.register(Bookinfo)
admin.site.register(UserRecommend)
admin.site.register(PuplationRecommend)
