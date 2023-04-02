from django.shortcuts import render
from .models import Ad
from .owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView


class AdsListView(OwnerListView):
    model = Ad
    # By convention:
    # template_name = "myarts/Ads_list.html"


class AdsDetailView(OwnerDetailView):
    model = Ad

class AdsCreateView(OwnerCreateView):
    model = Ad
    # List the fields to copy from the Ads model to the Ads form
    fields = ['title', 'text']

class AdsUpdateView(OwnerUpdateView):
    model = Ad
    fields = ['title', 'text']
    # This would make more sense
    # fields_exclude = ['owner', 'created_at', 'updated_at']


class AdsDeleteView(OwnerDeleteView):
    model = Ad
