from django.urls import path
from django.urls import include, path
from debug_toolbar.toolbar import debug_toolbar_urls
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("listing/add", views.createListing, name="createListing"),
    path("categories", views.categories, name="categories"),
    path("category", views.category, name="category"),
    path("listingView", views.listingView, name="listingView"),
    path("wishlist", views.wishlist, name="wishlist"),
    path("comment/add", views.addComment, name="addComment"),
    path("action/add", views.addAction, name="addAction"),
    path("listing/remove", views.removeListing, name="removeListing"),

] + debug_toolbar_urls()
