from django.contrib import admin

# Register your models here.
from .models import PrivateChatRoom
from .models import PublicChatRoom
from .models import ChatRoomUser
from .models import ChatAdmin
from .models import ChatBan
from .models import UserBlock
from .models import User

admin.site.register(PrivateChatRoom)
admin.site.register(PublicChatRoom)
admin.site.register(ChatRoomUser)
admin.site.register(ChatAdmin)
admin.site.register(ChatBan)
admin.site.register(UserBlock)
admin.site.register(User)
