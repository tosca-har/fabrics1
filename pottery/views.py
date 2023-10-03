
from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from .models import Industry, Area
# from .forms import SearchForm, SiteForm
from environs import Env

env = Env()
env.read_env()
mbsu = env.str("MBSU")
thsu = env.str("THSU")

def home(request):
    return render(request, "pottery/home.html")

def index(request, order): 
    if order == 1:
        industries = Industry.objects.all().order_by("time_start")
    elif order == 2:
        industries = Industry.objects.all().order_by("time_end")
    elif order == 3:
        industries = Industry.objects.all().order_by("technique","gender","-temper")
    elif order == 4:
        industries = Industry.objects.all().order_by("word_cooking") 
    elif order == 5:
        industries = Industry.objects.all().order_by("gender","-temper","decoration_position","decoration_exposed_coil","-decoration_comb_incised","-form_h_more" )
    elif order == 6:
        industries = Industry.objects.all().order_by("-temper")
    elif order == 7:
        industries = Industry.objects.all().order_by("decoration_position")
    elif order == 8:
        industries = Industry.objects.all().order_by("-decoration_dentate")
    elif order == 9:
        industries = Industry.objects.all().order_by("-decoration_incised")
    elif order == 10:
        industries = Industry.objects.all().order_by("-decoration_comb_incised") 
    elif order == 11:
        industries = Industry.objects.all().order_by("-decoration_applique")
    elif order == 12:
        industries = Industry.objects.all().order_by("-decoration_exposed_coil")
    elif order == 13:
        industries = Industry.objects.all().order_by("-decoration_punctate")
    elif order == 14:
        industries = Industry.objects.all().order_by("-decoration_paint")
    elif order == 15:
        industries = Industry.objects.all().order_by("-decoration_finger")
    elif order == 16:
        industries = Industry.objects.all().order_by("-decoration_sculpt") 
    elif order == 17:
        industries = Industry.objects.all().order_by("-decoration_paddle")
    elif order == 18:
        industries = Industry.objects.all().order_by("-form_w_more")
    elif order == 19:
        industries = Industry.objects.all().order_by("-form_h_more")
    elif order == 20:
        industries = Industry.objects.all().order_by("-form_equal")
    elif order == 21:
        industries = Industry.objects.all().order_by("-use_cooking")
    elif order == 22:
        industries = Industry.objects.all().order_by("-use_storage")
    elif order == 23:
        industries = Industry.objects.all().order_by("-use_serving")
    elif order == 24:
        industries = Industry.objects.all().order_by("-use_ceremonial")         
    else:
        industries = Industry.objects.all().order_by("name")
    return render(request, "pottery/index.html", {
        "industries": industries
    })

def industry(request, slug):
        # indentified_fabric = next(fabric for fabric in fabricsd if fabric['slug'] == slug)
    identified_industry = get_object_or_404(Industry, slug=slug)
    return render(request, "pottery/industry.html", {
        "industry": identified_industry,
        # "fabric_references": identified_industry.refs.all(),
        "industry_sites": identified_industry.area.all(),
        "mbsu": mbsu,
        "thsu":thsu
    })