from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models


class Dog(models.Model):
    """
    Dog Model
    """
    DOG_GENDERS = (
        ('m', 'male'),
        ('f', 'female'),
        ('u', 'unknown'),
    )
    DOG_SIZES = (
        ('s', 'small'),
        ('m', 'medium'),
        ('l', 'large'),
        ('xl', 'extra large'),
        ('u', 'Unknown'),
    )
    name = models.CharField(max_length=255)
    image_filename = models.FilePathField()
    breed = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    gender = models.CharField(choices=DOG_GENDERS, max_length=1)
    size = models.CharField(choices=DOG_SIZES, max_length=2)


class UserDog(models.Model):
    STATUS = (
        ('l', 'liked'),
        ('d', 'disliked'),
    )

    user = models.ForeignKey(User)
    dog = models.ForeignKey(Dog)
    status = models.CharField(choices=STATUS, max_length=1)


class UserPref(models.Model):
    """
    User dog preferences
    """
    AGES = (
        ('b', 'baby'),
        ('y', 'young'),
        ('a', 'adult'),
        ('s', 'senior'),
    )
    DOG_GENDERS = (
        ('m', 'male'),
        ('f', 'female'),
    )
    DOG_SIZES = (
        ('s', 'small'),
        ('m', 'medium'),
        ('l', 'large'),
        ('xl', 'extra large'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.CharField(choices=AGES, max_length=1)
    gender = models.CharField(choices=DOG_GENDERS, max_length=1)
    size = models.CharField(choices=DOG_SIZES, max_length=2)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserPref.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()









