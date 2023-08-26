from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from .models import Fabric, Site, Slide, Report
from .forms import SearchForm


abundances = ["None", "Minor","Few", "Common", "Frequent", "Major", "Very Dominant"]
ab = ["n", "m", "f", "C", "F", "M", "V"]

def home(request):
    return render(request, "fabrics2/home.html")

def index(request, order, limited = 0):
    if order == 1:
        fabricsd = Fabric.objects.all().order_by("-calcareous_max", "-calcareous_min")
    elif order == 2:
        fabricsd = Fabric.objects.all().order_by("-quartz_max", "-quartz_min")
    elif order == 3:
        fabricsd = Fabric.objects.all().order_by("-feldspar_max", "-feldspar_min")
    elif order == 4:
        fabricsd = Fabric.objects.all().order_by("-pyroxene_max", "-pyroxene_min")
    elif order == 5:
        fabricsd = Fabric.objects.all().order_by("-amphibole_max", "-amphibole_min")
    elif order == 6:
        fabricsd = Fabric.objects.all().order_by("-opaque_max", "-opaque_min")
    elif order == 7:
        fabricsd = Fabric.objects.all().order_by("-olivine_max", "-olivine_min")
    elif order == 8:
        fabricsd = Fabric.objects.all().order_by("-biotite_max", "-biotite_min")
    elif order == 9:
        fabricsd = Fabric.objects.all().order_by("-muscovite_max", "-muscovite_min")
    elif order == 10:
        fabricsd = Fabric.objects.all().order_by("-epidote_max", "-epidote_min")
    elif order == 11:
        fabricsd = Fabric.objects.all().order_by("-garnet_max", "-garnet_min")
    elif order == 12:
        fabricsd = Fabric.objects.all().order_by("-igneous_rock_fragments_max", "-igneous_rock_fragments_min")
    elif order == 13:
        fabricsd = Fabric.objects.all().order_by("-sedimentary_metasedimentary_max", "-sedimentary_metasedimentary_min")
    elif order == 14:
        fabricsd = Fabric.objects.all().order_by("-grog_max", "-grog_min")
    elif order == 15:
        fabricsd = Fabric.objects.all().order_by("lithics")
    elif order == 16:
        fabricsd = Fabric.objects.all().order_by("region", "desc")              
    else:
        fabricsd = Fabric.objects.all().order_by("desc")
    return render(request, "fabrics2/index.html", {
        "fabrics": fabricsd
    })


def site_index(request):
    sites = Site.objects.all().order_by("name")
    return render(request, "fabrics2/site-index.html", {
        "sites": sites
    })

def fabric_by_number(request, atpr):
    fabricsd = Fabric.objects.all()
    if atpr > len(fabricsd):
        return HttpResponseNotFound("<h1>Invalid index</h1>")
    redirect_fabric = fabricsd[atpr - 1]['slug']
    redirect_path = reverse("fabric-type", args=[redirect_fabric])
    return HttpResponseRedirect(redirect_path)


def fabric(request, slug):
        # indentified_fabric = next(fabric for fabric in fabricsd if fabric['slug'] == slug)
    identified_fabric = get_object_or_404(Fabric, slug=slug)
        # identified_fabric = Fabric.objects.get(slug=slug)
    id_fabrics = identified_fabric.slides.all()
    return render(request, "fabrics2/fabric.html", {
        "fabric": identified_fabric,
        "fabric_slides": id_fabrics,
        "fabric_references": identified_fabric.refs.all(),
        "fabric_sites": identified_fabric.sites.all(),
        "ab": ab

    })

def report(request, slug):
    identified_report = get_object_or_404(Report, slug=slug)
    return render(request, "fabrics2/report.html", {
        "report": identified_report,
        "report_slides": identified_report.slides.all(),
        "report_fabrics": identified_report.fabrics.all()
    })

def site(request, slug):
    identified_site = get_object_or_404(Site, slug=slug)
    site_slides = identified_site.slides.all()
    return render(request, "fabrics2/site.html", {
        "site": identified_site,
        "site_slides": site_slides,
        "site_fabrics": identified_site.fabrics.all()
    })

def glossary(request):
    return render(request, "fabrics2/glossary.html")

def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST) 
        fabrics = Fabric.objects.all() 
        query = "Matching fabrics for"    
        if form.is_valid():
            val = form.cleaned_data.get("calcareous")
            if val > -1:
                fabrics = fabrics.filter(calcareous_min__lte=val, calcareous_max__gte=val)
                query = query + ";  Calcareous-" + abundances[val]
            val = form.cleaned_data.get("quartz")
            if val > -1:
                fabrics = fabrics.filter(quartz_min__lte=val, quartz_max__gte=val)
                query = query + ";  Quartz-" + abundances[val]
            val = form.cleaned_data.get("feldspars")
            if val > -1:
                fabrics = fabrics.filter(feldspar_min__lte=val, feldspar_max__gte=val)
                query = query + ";  Feldspar-" + abundances[val]
            val = form.cleaned_data.get("pyroxene")
            if val > -1:
                fabrics = fabrics.filter(pyroxene_min__lte=val, pyroxene_max__gte=val)
                query = query + ";  Pyroxene-" + abundances[val]
            val = form.cleaned_data.get("amphibole")
            if val > -1:
                fabrics = fabrics.filter(amphibole_min__lte=val, amphibole_max__gte=val)
                query = query + ";  Amphibole-" + abundances[val]
            val = form.cleaned_data.get("opaque_iron_oxides")
            if val > -1:
                fabrics = fabrics.filter(opaque_min__lte=val, opaque_max__gte=val)
                query = query + ";  Opaques-" + abundances[val]
            val = form.cleaned_data.get("biotite")
            if val > -1:
                fabrics = fabrics.filter(biotite_min__lte=val, biotite_max__gte=val)
                query = query + ";  Biotite-" + abundances[val]                              
            val = form.cleaned_data.get("muscovite")
            if val > -1:
                fabrics = fabrics.filter(muscovite_min__lte=val, muscovite_max__gte=val)
                query = query + ";  Muscovite-" + abundances[val]
            val = form.cleaned_data.get("olivine")
            if val > -1:
                fabrics = fabrics.filter(olivine_min__lte=val, olivine_max__gte=val)
                query = query + ";  Olivine-" + abundances[val]                              
            val = form.cleaned_data.get("epidote")
            if val > -1:
                fabrics = fabrics.filter(epidote_min__lte=val, epidote_max__gte=val)
                query = query + ";  Epidote-" + abundances[val]  
            val = form.cleaned_data.get("garnet")
            if val > -1:
                fabrics = fabrics.filter(garnet_min__lte=val, garnet_max__gte=val)
                query = query + ";  Garnet-" + abundances[val]
            val = form.cleaned_data.get("igneous_rock_fragments")
            if val > -1:
                fabrics = fabrics.filter(igneous_rock_fragments_min__lte=val, igneous_rock_fragments_max__gte=val)
                query = query + ";  Igneous Rocks-" + abundances[val]                              
            val = form.cleaned_data.get("sedimentary_metasedimentary_rocks")
            if val > -1:
                fabrics = fabrics.filter(sedimentary_metasedimentary_min__lte=val, sedimentary_metasedimentary_max__gte=val)
                query = query + ";  Meta/Sedimentary Rocks-" + abundances[val] 
            val = form.cleaned_data.get("grog")
            if val > -1:
                fabrics = fabrics.filter(grog_min__lte=val, grog_max__gte=val)
                query = query + ";  Grog-" + abundances[val] 
            val = form.cleaned_data.get("vitric")
            if val != '':
                fabrics = fabrics.filter(vitric=val)
                query = query + ";  Vitric-" + val 
            val = form.cleaned_data.get("felsitic")
            if val != '':
                fabrics = fabrics.filter(felsitic=val)
                query = query + ";  Felsitic-" + val
            val = form.cleaned_data.get("microlitic")
            if val != '':
                fabrics = fabrics.filter(microlitic=val)
                query = query + ";  Microlitic-" + val 
            val = form.cleaned_data.get("microphaneritic")
            if val != '':
                fabrics = fabrics.filter(microphaneritic=val)
                query = query + ";  Microphaneritic-" + val 
            val = form.cleaned_data.get("lathwork")
            if val != '':
                fabrics = fabrics.filter(lathwork=val)
                query = query + ";  Lathwork-" + val
            val = form.cleaned_data.get("metavolcanic")
            if val != '':
                fabrics = fabrics.filter(metavolcanic=val)
                query = query + ";  Metavolcanic-" + val 
            val = form.cleaned_data.get("plutonite")
            if val != '':
                fabrics = fabrics.filter(plutonite=val)
                query = query + ";  Plutonite-" + val 
            val = form.cleaned_data.get("tectonite")
            if val != '':
                fabrics = fabrics.filter(tectonite=val)
                query = query + ";  Tectonite-" + val
            val = form.cleaned_data.get("argillitic")
            if val != '':
                fabrics = fabrics.filter(argillitic=val)
                query = query + ";  Argillitic-" + val     
            val = form.cleaned_data.get("chert")
            if val != '':
                fabrics = fabrics.filter(chert=val)
                query = query + ";  Chert-" + val 
            val = form.cleaned_data.get("quartzite")
            if val != '':
                fabrics = fabrics.filter(quartzite=val)
                query = query + ";  Quartzite-" + val
            val = form.cleaned_data.get("siltstone")
            if val != '':
                fabrics = fabrics.filter(siltstone=val)
                query = query + ";  Siltstone-" + val 
            val = form.cleaned_data.get("limeclast")
            if val != '':
                fabrics = fabrics.filter(limeclast=val)
                query = query + ";  Limeclast-" + val 

            val = form.cleaned_data.get("regions_to_include") 
            fabrics = fabrics.filter(region__in=val)
            query = query + "." 
            query2 = "Regions searched: " + ', '.join(val) + '.'

            sites = Site.objects.all().filter(fabrics__in = fabrics).distinct()

            if len(fabrics) > 0:
                return render(request, "fabrics2/results.html", {
                    "fabrics": fabrics,
                    "query": query,
                    "query2": query2,
                    "sites": sites,
                })
            else: return HttpResponseRedirect("no-match")
                
    else:   
        form = SearchForm()
    return render(request, "fabrics2/search.html", {
        "form": form
    })


def no_match(request):
    return render(request, "fabrics2/no-match.html")
