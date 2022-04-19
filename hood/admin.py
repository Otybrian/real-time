from django.contrib import admin
from .models import Post, Profile,Neighborhood,Location,Category,Business
# Register your models here.

admin.site.register(Location)
admin.site.register(Category)
admin.site.register(Business)
admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(Neighborhood)