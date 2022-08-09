from django.contrib import admin
from social import models
# Register your models here.

admin.site.register([
    models.Friends,
    models.Post,
    models.Likes,
    models.Comment
]   
)