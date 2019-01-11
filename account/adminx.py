import xadmin
from .models import Users, Tokens


class UsersAdmin(object):
    list_display = ['user_id', 'nickname', 'mobile', 'create_date', 'last_login_date', 'last_login_ip']
    search_fields = ['user_id', 'mobile']
    list_editable = ['nickname', ]
    list_filter = ['last_login_date', 'create_date', ]


class TokensAdmin(object):
    list_display = ['user', 'token', 'expire_to', ]
    search_fields = ['user_id', 'mobile']
    list_editable = ['token', 'expire_to', ]
    list_filter = ['expire_to']


xadmin.site.register(Users, UsersAdmin)
xadmin.site.register(Tokens, TokensAdmin)
