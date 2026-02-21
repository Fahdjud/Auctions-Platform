from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Max
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import User, Category, Listing, Comment, Action


def index(request):
    if request.method == "POST":

        return HttpResponseRedirect(reverse("index"))
    else:

        listings = Listing.objects.all()

        for listing in listings:
            action = Action.objects.filter(listing=listing).order_by('-price').first()
            if action:
                listing.price = action.price

        return render(request, "auctions/index.html", {
            'listing': listings
        })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


def createListing(request):
    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]
        imageUrl = request.POST["imageUrl"]
        owner = request.user
        category = request.POST["category"]
        price = request.POST["price"]

        categoryInfo = Category.objects.get(categoryName=category)

        createList = Listing(title=title, description=description,
                             imageUrl=imageUrl, owner=owner, price=price,
                             category=categoryInfo)

        createList.save()

        return HttpResponseRedirect(reverse("index"))
    else:
        CategoryList = Category.objects.all()
        return render(request, "auctions/createListing.html", {
            "categories": CategoryList
        })


def categories(request):
    categories = Category.objects.all()

    return render(request, "auctions/categories.html", {
        "categories": categories
    })


def category(request):
    category = request.GET["category"]

    categoryId = Category.objects.get(categoryName=category)

    listings = Listing.objects.filter(category=categoryId)

    return render(request, "auctions/category.html", {
        "listing": listings,
        "category": category
    })


def listingView(request):
    if request.method == "POST":

        listingId = request.POST['listingId']
        owner = request.user

        listing = Listing.objects.get(id=listingId)

        if owner in listing.watchlist.all():
            listing.watchlist.remove(owner)

        else:

            listing.watchlist.add(owner)

        return HttpResponseRedirect(reverse("listingView") + "?listing=" + str(listingId))
    else:
        listingId = request.GET["listing"]
        owner = request.user

        listing = Listing.objects.get(id=listingId)

        currentAction = Action.objects.filter(listing=listingId).order_by('-price').first()

        actions = Action.objects.filter(listing=listingId).order_by('-price')

        comments = Comment.objects.filter(listing=listingId)

        if owner in listing.watchlist.all():
            wishlisted = True
        else:
            wishlisted = False

        if listing.owner == owner:
            isOwner = True
        else:
            isOwner = False

        return render(request, "auctions/listingView.html", {
            "listing": listing,
            "wishlisted": wishlisted,
            "comments": comments,
            "currentAction": currentAction,
            "actions": actions,
            "isOwner": isOwner
        })


def wishlist(request):
    owner = request.user

    wishlists = Listing.objects.filter(watchlist=owner)

    return render(request, "auctions/wishlists.html", {
        "wishlists": wishlists
    })


@login_required
def addComment(request):

    if request.method == "POST":

        listingId = request.POST['listing']
        commentText = request.POST['comment']
        owner = request.user

        listing = Listing.objects.get(id=listingId)

        comment = Comment.objects.create(listing=listing, owner=owner, text=commentText)
        comment.save()

        return HttpResponseRedirect(reverse("listingView") + "?listing=" + str(listingId))
    else:
        return HttpResponseRedirect(reverse("index"))


@login_required
def addAction(request):

    if request.method == "POST":
        from django.contrib import messages

        owner = request.user
        listingId = request.POST['listingId']
        addAction = request.POST['addAction']

        currentAction = Action.objects.filter(listing=listingId).order_by('-price').first()

        if currentAction:
            price = currentAction.price
        else:
            price = Listing.objects.filter(id=listingId).values_list('price', flat=True).first()

        if int(addAction) <= int(price):
            messages.error(request, f"Bid must be greater than the current price of ${price}")
            return HttpResponseRedirect(reverse("listingView") + "?listing=" + str(listingId))

        else:

            listing = Listing.objects.get(id=listingId)

            action = Action.objects.create(owner=owner, listing=listing, price=addAction)

            action.save()

            messages.success(request, f"Your bid of ${addAction} was placed successfully!")
            return HttpResponseRedirect(reverse("listingView") + "?listing=" + str(listingId))


def removeListing(request):
    if request.method == "POST":
        listingId = request.POST['listingId']
        owner = request.user

        listing = Listing.objects.get(id=listingId)

        if owner == listing.owner:
            listing.isActive = False
            listing.save()

    return HttpResponseRedirect(reverse("listingView") + "?listing=" + str(listingId))
