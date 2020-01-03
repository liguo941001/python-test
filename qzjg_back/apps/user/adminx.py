import xadmin
from . import models
from home.models import Song_List,Classify,Music

xadmin.site.register(models.UserInfo)
xadmin.site.register(models.Singer)
xadmin.site.register(models.Author)


