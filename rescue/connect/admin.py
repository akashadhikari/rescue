from django.contrib import admin
from .models import Need, HelpCenter, Help, SomeoneNeedsHelp


admin.site.register(Need)
admin.site.register(HelpCenter)
admin.site.register(Help)
admin.site.register(SomeoneNeedsHelp)
