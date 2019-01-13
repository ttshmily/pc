import xadmin
from .models import Curricula, Cat1


class CurriculaAdmin(object):
    list_display = ['title', 'category', 'coach', 'start_time', 'location', 'status', ]
    search_fields = ['coach', 'mobile']
    list_filter = ['coach__mobile', 'category__id']
    readonly_fields = ['coach']


class CategoryAdmin(object):
    list_display = ['id', 'category_name', ]


xadmin.site.register(Curricula, CurriculaAdmin)
xadmin.site.register(Cat1, CategoryAdmin)
