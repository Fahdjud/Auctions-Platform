from django.test import TestCase
from django.db.models import Max
from .models import User, Listing, Action, Category, Comment

class Test(TestCase):

    def test(self):
        actions = Action.objects.values('listing').annotate(price=Max('price')).distinct()


        for action in actions:
            print(f"{action['listing']} - {action['price']}")
