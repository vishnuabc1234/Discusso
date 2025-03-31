from django.contrib import admin

from .models import TagModel, PostModel, CommentModel, UpvoteModel


admin.site.register(TagModel)
admin.site.register(PostModel)
admin.site.register(CommentModel)
admin.site.register(UpvoteModel)
