from django.contrib import admin

from ads.models import Ads, Location, Categories, User

admin.site.register(Ads)
admin.site.register(User)
admin.site.register(Location)
admin.site.register(Categories)
