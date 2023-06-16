from django.shortcuts import render
from django.http import HttpResponseRedirect
from webapp.cat_stats_db import CatStatsDb

# Create your views here.


def index(request):
    if request.method == "GET":
        return render(request, "index.html")
    else:
        CatStatsDb.name = request.POST.get("cat_name")
        return HttpResponseRedirect('/cat_stats/')

def cat_stats(request):
    if request.method == "GET":
        context = {
            "name": CatStatsDb.name,
            "age": CatStatsDb.age,
            "satiety": CatStatsDb.satiety,
            "happy": CatStatsDb.happy,
            "avatar": CatStatsDb.avatar
                }
        return render(request, "cat_stats.html", context)
    else:
        action = request.POST.get("action")
        if action == "play":
            CatStatsDb.play()
        elif action == "feed":
            CatStatsDb.satiety()
        elif action == "sleep":
            CatStatsDb.sleep()

        return HttpResponseRedirect('/cat_stats/')
