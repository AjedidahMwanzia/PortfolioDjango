
from django.db import models
import datetime as dt
from django.dispatch import receiver
from django.db.models.signals import post_save
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.forms import ModelForm, widgets
from django import forms
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_photo = CloudinaryField("image")
    bio = models.TextField(max_length=250, blank=True, null=True)
    contact = models.CharField(max_length=250, blank=True, null=True)

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def filter_by_id(cls, id):
        profile = Profile.objects.filter(user=id).first()
        return profile

    def __str__(self):
        return self.user.username

    
class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    description = models.TextField()
    image = CloudinaryField("image")
    url = models.URLField(blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True)

    @classmethod
    def search_by_title(cls, search_term):
        projects = cls.objects.filter(title__icontains=search_term)
        return projects

    @classmethod
    def get_project_by_id(cls, id):
        project = cls.objects.get(id=id)
        return project

    @classmethod
    def get_all_projects(cls):
        projects = cls.objects.all()
        return projects

    @classmethod
    def get_all_projects_by_user(cls, user):
        projects = cls.objects.filter(user=user)
        return projects

    
    def update_project(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.save()

    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment=models.TextField()
    posted_on = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return str(self.comment)


class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    image = CloudinaryField("image")
    content = models.TextField()
    comment=models.ForeignKey(Comment, on_delete=models.CASCADE)
    url = models.URLField(blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True)

    def save_blog(self):
        self.save()

    def delete_blog(self):
        self.delete()

    @classmethod
    def filter_by_id(cls, id):
        blog= Blog.objects.filter(id=id).title()
        return blog

    def __str__(self):
        return self.title


class Like(models.Model):
    comment=models.OneToOneField(Comment,related_name ='likes' ,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.comment.comment)

class DisLike(models.Model):
    comment = models.OneToOneField(Comment, related_name="dis_likes", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.comment.comment)

class UpdateProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ("user", "profile_photo", "bio", "contact")

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ("user", "title", "description", "image", "url")


class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ("user", "title", "content", "image", "url")


