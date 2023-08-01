from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


fabrics = {
    'tpr250': "Pyribole-Poor",
    "tpr272": "metavolcanic",
    "tpr211": "lithic volcanic sand tempers",
    "tpr179": "Feldspathic",
    "tpr86": "B",
    "tpr276": "Quartzo-feldspathic temper",
    "tprx": None
}


def index(request):

    fabs = list(fabrics.keys())

    return render(request, "fabrics2/index.html", {
        "fabrics": fabs
    })


def fabric_by_number(request, tpr):
    fabric = list(fabrics.keys())
    if tpr > len(fabric):
        return HttpResponseNotFound("<h1>Invalid index</h1>")
    redirect_fabric = fabric[tpr - 1]
    redirect_path = reverse("fabric-type", args=[redirect_fabric])
    return HttpResponseRedirect(redirect_path)


def fabric(request, tpr):
    try:
        desc_text = fabrics[tpr]
        return render(request, "fabrics2/fabric.html", {
            "desc": desc_text,
            "fabric": tpr
        })

    except:
        return HttpResponseNotFound("<h1>Fabric Not Found</h1>")
