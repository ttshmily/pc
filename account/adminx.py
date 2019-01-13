import xadmin
from .models import Users, Tokens


class UsersAdmin(object):
    list_display = ['user_id', 'nickname', 'mobile', 'create_date', 'last_login_date', 'last_login_ip']
    list_filter = ['last_login_date', 'create_date', ]
    search_fields = ['user_id', 'mobile']
    # list_editable = ['nickname', ] # 列表中可编辑
    readonly_fields = ('__all__', )
    list_per_page = 10
    show_detail_fields = ['user_id', 'mobile', ]


class TokensAdmin(object):
    list_display = ['user', 'token', 'expire_to', ]
    search_fields = ['user_id', 'mobile']
    list_editable = ['token', 'expire_to', ]
    list_filter = ['expire_to', 'user__mobile']


xadmin.site.register(Users, UsersAdmin)
# xadmin.site.register(Tokens, TokensAdmin)
