from rest_framework import serializers
from .models import Comments, Contributors, Projects, Issues, Users


class CommentsSerializer(serializers.ModelSerializer):
    """"""
    class Meta:
        model = Comments
        fields = "__all__"
