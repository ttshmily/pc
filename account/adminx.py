import xadmin
from .models import Users, Tokens


class UsersAdmin(object):
    list_display = ['user_id', 'nickname', 'mobile', 'create_date', 'last_login_date', 'last_login_ip']
    search_fields = ['user_id', 'mobile']
    list_editable = ['nickname', ]
    # readonly_fields = ['nickname', ]
    list_filter = ['last_login_date', 'create_date', ]


class TokensAdmin(object):
    list_display = ['user', 'token', 'expire_to', ]
    search_fields = ['user_id', 'mobile']
    list_editable = ['token', 'expire_to', ]
    list_filter = ['expire_to', 'user__mobile']


class BaseSetting(object):
    enable_themes = True   # 打开主题功能
    use_bootswatch = True  #


class GlobalSettings(object):
    site_title = "慕学后台管理系统"  # 系统名称
    site_footer = "在线网"      # 底部版权栏


xadmin.site.register(Users, UsersAdmin)
xadmin.site.register(Tokens, TokensAdmin)
xadmin.site.register(xadmin.views.BaseAdminView, BaseSetting)
xadmin.site.register(xadmin.views.CommAdminView, GlobalSettings)
