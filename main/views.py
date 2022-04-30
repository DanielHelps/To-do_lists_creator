from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoL
from .forms import NewList

def home(respone):
    return render(respone, "main/home.html", {})
    # response.write("<h2>To do item: %s</h2>" %item)
    # return response


def index(response, id):
    ls = ToDoL.objects.get(id=id)
    # print(response.POST)
    if response.method == "POST":
        # print(response.POST.get("new"))
        if response.POST.get("save"):
            for item in ls.items.all():
                if response.POST.get("c"+str(item.id)) == 'clicked':
                    item.complete = True
                else:
                    item.complete = False
                item.save()
        elif response.POST.get("newItem"):
            txt = response.POST.get("new")
            if len(txt) > 2:
                ls.items.create(to_do_text=txt, complete=False)
            else:
                print("invalid input")


    return render(response, "main/check_list.html", {"list": ls})
    # return HttpResponse("<h1>Reddit sentiment analysis tutorial!</h1>")


def create(respone):
    if respone.method == "POST":
        form = NewList(respone.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoL(name=n)
            t.save()

        return HttpResponseRedirect("/%i" %t.id)
    else:
        form = NewList()
    return render(respone, "main/create.html", {"form":form})
    # return HttpResponse("<h1>Reddit sentiment analysis tutorial!</h1>")
