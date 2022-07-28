from rest_framework import serializers
from .models import Profile,Project,Blog,Like,DisLike,Comment

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model= Profile
        fields=('__all__')

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model= Project
        fields=('__all__')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model= Profile
        fields=('__all__')

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model =Like
        fields=('name')


class DisLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model= DisLike
        fields=('name')

        
        

        