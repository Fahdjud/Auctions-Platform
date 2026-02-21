from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Category(models.Model):
    categoryName = models.CharField(max_length=50)

    def __str__(self):
        return self.categoryName

class Listing(models.Model):
    createTime = models.DateField(auto_now=False, auto_now_add=True)
    lastModefied = models.DateTimeField(auto_now=True, auto_now_add=False)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=250)
    imageUrl = models.CharField(max_length=900)
    price = models.FloatField()
    isActive = models.BooleanField(default=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="user")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, related_name="category")
    watchlist = models.ManyToManyField(User, blank=True, related_name="listingWatchlist")

    def __str__(self):
        return self.title


class Comment(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="comments")
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=100)
    createTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.owner} - {self.listing} - {self.text}"


class Action(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="actionOwner")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="actionListing")
    price = models.FloatField()
    createTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.owner} - {self.listing} - ${self.price}"
