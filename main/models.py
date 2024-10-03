from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import IntegerChoices


class User(AbstractUser):
    phone = models.CharField(max_length=20, blank=True, null=True)
    image = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    job = models.CharField(max_length=128, blank=True, null=True)
    about_me = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=256, null=True, blank=True)
    telegram = models.URLField(max_length=128, null=True, blank=True)
    instagram = models.URLField(max_length=128, null=True, blank=True)
    telegram_id = models.CharField(max_length=25, null=True, blank=True)


class Skill(models.Model):
    user_id = models.ForeignKey('main.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    level = models.PositiveIntegerField()


class Service(models.Model):
    user_id = models.ForeignKey('main.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=400)


class Portfolio(models.Model):
    user_id = models.ForeignKey('main.User', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='portfolio')
    title = models.CharField(max_length=128)

    class RateChoice(IntegerChoices):
        SOFT = 1, 'Software Development'
        CYBER = 2, 'Cybersecurity'
        CLOUD = 3, 'Cloud Computing'
        AI = 4, 'Artificial Intelligence and Machine Learning'
        ECOM = 5, 'E-commerce and Online Retail'
        GRAPH = 6, 'Graphic Design'
    category = models.PositiveIntegerField(
        choices=RateChoice.choices, default=RateChoice.SOFT)
    description = models.TextField()
    create_at = models.DateField(auto_now_add=True)
    company = models.CharField(max_length=128)
    project_url = models.URLField(max_length=128)


class Blog(models.Model):
    user_id = models.ForeignKey('main.User', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog_pics')
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    fullname = models.CharField(max_length=128, blank=True, null=True)
    email = models.EmailField(max_length=128, blank=True, null=True)
    post_id = models.ForeignKey('main.Blog', on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

class Statistic(models.Model):
    user_id = models.ForeignKey('main.User', on_delete=models.CASCADE)
    year = models.PositiveIntegerField(default=0)
    total_client = models.PositiveIntegerField(default=0)
    won = models.PositiveIntegerField(default=0)



class PartnerComment(models.Model):
    user_id = models.ForeignKey('main.User', on_delete=models.CASCADE)
    fullname = models.CharField(max_length=128)
    email = models.EmailField(max_length=128)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
