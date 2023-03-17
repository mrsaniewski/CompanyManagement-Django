import datetime
from turtle import title

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, request
from django.views.generic import DeleteView
from sqlalchemy import delete

from .models import User, Item, Prize
from .forms import CreateNewList


# Create your views here.

def index(response):
    return render(response, "main/view.html", {})


def home(response):
    return render(response, "main/home.html", {})


def view(response, id):
    ls = User.objects.get(id=id)
    if ls in response.user.todolist.all():
        if response.method == "POST":
            # if response.POST.get("save"):
            #     for item in ls.item_set.all():
            #         if response.POST.get("c" + str(item.id)) == "clicked":
            #             item.complete = True
            #         else:
            #             item.complete = False
            #         item.save()
            if response.POST.get("donn"):
                idxx = int(response.POST.get("donn"))
                item = ls.item_set.get(id=idxx)
                item.complete = True
                item.save()
                ls.points += 20
                ls.save()
            elif response.POST.get("newItem"):
                txt = response.POST.get("new")
                txtt = response.POST.get("newt")
                if len(txt) > 2 and len(txtt) > 2:
                    ls.item_set.create(text=txt, title=txtt, date=datetime.datetime.now(), complete=False)
                else:
                    print("invalid")
            elif response.POST.get("delete"):
                item_id = int(response.POST.get("delete"))
                item = ls.item_set.get(id=item_id)
                item.delete()
        return render(response, "main/list.html", {"ls": ls})
    return render(response, "main/view.html", {})


def loyality(response, id):
    lsp = User.objects.get(id=id)
    if response.POST.get("claim_prize"):
        idx = int(response.POST.get("claim_prize"))
        prize = lsp.prizes.get(id=idx)
        prize.claimed = True
        lsp.points -= prize.value
        lsp.save()
        prize.save()
    return render(response, "main/loyality.html", {"lsp": lsp})


def about(response):
    return render(response, "main/about.html", {})
