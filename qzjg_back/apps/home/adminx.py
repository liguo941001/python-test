import xadmin

from xadmin import views


class GlobalSettings(object):
    '''xadmin的全局配置'''
    site_title = '拆东墙音乐'  # 设置站点标题
    site_footer = '拆东墙音乐集团'  # 设置站点的页脚
    menu_style = 'accordion'  # 设置菜单折叠


xadmin.site.register(views.CommAdminView, GlobalSettings)

from . import models
xadmin.site.register(models.Banner)
xadmin.site.register(models.Nav)
xadmin.site.register(models.Music)
xadmin.site.register(models.Classify)
xadmin.site.register(models.Song_List)
