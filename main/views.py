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
    if ls in response.user.todolist.all():
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
    return render(response, "main/view.html")
 

def create(response):
    if response.method == "POST":
        form = NewList(response.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            # response.user.toDoL_set.create(name=n)
            t = ToDoL(name=n)
            t.save()
            response.user.todolist.add(t)

        return HttpResponseRedirect("/%i" %t.id)
    else:
        form = NewList()
    return render(response, "main/create.html", {"form":form})
    # return HttpResponse("<h1>Reddit sentiment analysis tutorial!</h1>")

def view(response):
    return render(response, "main/view.html", {})