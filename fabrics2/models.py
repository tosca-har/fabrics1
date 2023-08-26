from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify


class Report(models.Model):
    slug = models.SlugField(default="", blank= True, null = False, db_index=True)
    name = models.CharField(max_length= 20, blank=True)
    fullname = models.CharField(max_length= 100, blank=True)
    author_list = models.CharField(max_length= 500, null=True)
    details = models.TextField(max_length= 1000, null=True, blank=True)
    link = models.CharField(max_length= 100, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.slug} ({self.fullname})" 
    
class Fabric(models.Model):
    slug = models.SlugField(default="", blank=True, null=False, db_index=True)
    name = models.CharField(default="tpr", max_length=20)
    desc = models.CharField(null=True, max_length=100)
    region = models.CharField(null=True, max_length=100)
    calcareous_min = models.IntegerField(default="0", validators=[MinValueValidator(0), MaxValueValidator(6)])
    calcareous_max = models.IntegerField(default="0", validators=[MinValueValidator(0), MaxValueValidator(6)])
    feldspar_min = models.IntegerField(default="0", validators=[MinValueValidator(0), MaxValueValidator(6)])
    feldspar_max = models.IntegerField(default="0", validators=[MinValueValidator(0), MaxValueValidator(6)])
    quartz_min = models.IntegerField(default="0", validators=[MinValueValidator(0), MaxValueValidator(6)])
    quartz_max = models.IntegerField(default="0", validators=[MinValueValidator(0), MaxValueValidator(6)])
    pyroxene_min = models.IntegerField(default="0", validators=[MinValueValidator(0), MaxValueValidator(6)])
    pyroxene_max = models.IntegerField(default="0", validators=[MinValueValidator(0), MaxValueValidator(6)])
    amphibole_min = models.IntegerField(default="0", validators=[MinValueValidator(0), MaxValueValidator(6)])
    amphibole_max = models.IntegerField(default="0", validators=[MinValueValidator(0), MaxValueValidator(6)])
    opaque_min = models.IntegerField(default="0", validators=[MinValueValidator(0), MaxValueValidator(6)])
    opaque_max = models.IntegerField(default="0", validators=[MinValueValidator(0), MaxValueValidator(6)])
    olivine_min = models.IntegerField(default="0", validators=[MinValueValidator(0), MaxValueValidator(6)])
    olivine_max = models.IntegerField(default="0", validators=[MinValueValidator(0), MaxValueValidator(6)])
    biotite_min = models.IntegerField(default="0", validators=[MinValueValidator(0), MaxValueValidator(6)])
    biotite_max = models.IntegerField(default="0", validators=[MinValueValidator(0), MaxValueValidator(6)])
    muscovite_min = models.IntegerField(default="0", validators=[MinValueValidator(0), MaxValueValidator(6)])
    muscovite_max = models.IntegerField(default="0", validators=[MinValueValidator(0), MaxValueValidator(6)])
    epidote_min = models.IntegerField(default="0", validators=[MinValueValidator(0), MaxValueValidator(6)])
    epidote_max = models.IntegerField(default="0", validators=[MinValueValidator(0), MaxValueValidator(6)])
    igneous_rock_fragments_min = models.IntegerField(default="0", validators=[MinValueValidator(0), MaxValueValidator(6)])
    igneous_rock_fragments_max = models.IntegerField(default="0", validators=[MinValueValidator(0), MaxValueValidator(6)])
    sedimentary_metasedimentary_min = models.IntegerField(default="0", validators=[MinValueValidator(0), MaxValueValidator(6)])
    sedimentary_metasedimentary_max = models.IntegerField(default="0", validators=[MinValueValidator(0), MaxValueValidator(6)])
    grog_min = models.IntegerField(default="0", validators=[MinValueValidator(0), MaxValueValidator(6)])
    grog_max = models.IntegerField(default="0", validators=[MinValueValidator(0), MaxValueValidator(6)])
    garnet_min = models.IntegerField(default="0", validators=[MinValueValidator(0), MaxValueValidator(6)])
    garnet_max = models.IntegerField(default="0", validators=[MinValueValidator(0), MaxValueValidator(6)])
    lithics = models.CharField(null=True, max_length=100)
    vitric = models.BooleanField(default=False)
    felsitic = models.BooleanField(default=False)
    microlitic = models.BooleanField(default=False)
    microphaneritic = models.BooleanField(default=False)
    lathwork = models.BooleanField(default=False)
    metavolcanic = models.BooleanField(default=False)
    plutonite = models.BooleanField(default=False)
    tectonite = models.BooleanField(default=False)
    argillitic = models.BooleanField(default=False)
    chert = models.BooleanField(default=False)
    quartzite = models.BooleanField(default=False)
    siltstone = models.BooleanField(default=False)
    limeclast = models.BooleanField(default=False)
    comments = models.CharField(null=True, max_length=500)
    refs = models.ManyToManyField(Report, related_name="fabrics", blank=True)
    has_full = models.BooleanField(default=False) 
    has_image = models.BooleanField(default=False) 

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.slug} ({self.desc})"

class Site(models.Model):
    slug = models.SlugField(default="", blank= True, null = False, db_index=True)
    name = models.CharField(max_length= 20)
    island = models.CharField(max_length= 20, null=True)
    lat = models.DecimalField(null=True, max_digits=9, decimal_places=6) 
    lng = models.DecimalField(null=True, max_digits=9, decimal_places=6)
    fabrics = models.ManyToManyField(Fabric, related_name="sites", blank=True)
    has_full = models.BooleanField(default=False) 
    has_image = models.BooleanField(default=False) 
   
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.slug} ({self.island})" 
    
    @property
    def fabric_string(self):
        fabs = self.fabrics.all()
        fabstring = ''
        for fab in fabs:
            fabstring = fabstring + " (" + fab.name + " " + fab.desc + ")"
        return fabstring
    
class Slide(models.Model):
    name = models.CharField(max_length= 20, db_index=True, unique=True)
    fabric = models.ForeignKey(Fabric, on_delete=models.SET_NULL, null=True, related_name="slides")
    site = models.ForeignKey(Site, on_delete=models.SET_NULL, null=True, blank=True, related_name="slides")
    sherd = models.CharField(null=True, blank=True, max_length=50)
    sherd_origin_site = models.CharField(null=True, max_length=50)
    calcareous = models.IntegerField(default="0", validators=[MinValueValidator(0), MaxValueValidator(6)])
    feldspar = models.IntegerField(default="0", validators=[MinValueValidator(0), MaxValueValidator(6)])
    quartz = models.IntegerField(default="0", validators=[MinValueValidator(0), MaxValueValidator(6)])
    pyroxene = models.IntegerField(default="0", validators=[MinValueValidator(0), MaxValueValidator(6)])
    amphibole = models.IntegerField(default="0", validators=[MinValueValidator(0), MaxValueValidator(6)])
    opaque = models.IntegerField(default="0", validators=[MinValueValidator(0), MaxValueValidator(6)])
    olivine = models.IntegerField(default="0", validators=[MinValueValidator(0), MaxValueValidator(6)])
    biotite = models.IntegerField(default="0", validators=[MinValueValidator(0), MaxValueValidator(6)])
    muscovite = models.IntegerField(default="0", validators=[MinValueValidator(0), MaxValueValidator(6)])
    epidote = models.IntegerField(default="0", validators=[MinValueValidator(0), MaxValueValidator(6)])
    igneous_rock_fragments = models.IntegerField(default="0", validators=[MinValueValidator(0), MaxValueValidator(6)])
    sedimentary_metasedimentary = models.IntegerField(default="0", validators=[MinValueValidator(0), MaxValueValidator(6)])
    grog = models.IntegerField(default="0", validators=[MinValueValidator(0), MaxValueValidator(6)])
    garnet = models.IntegerField(default="0", validators=[MinValueValidator(0), MaxValueValidator(6)]) 
    lithics = models.CharField(null=True, max_length=100, blank=True)
    vitric = models.BooleanField(default=False)
    felsitic = models.BooleanField(default=False)
    microlitic = models.BooleanField(default=False)
    microphaneritic = models.BooleanField(default=False)
    lathwork = models.BooleanField(default=False)
    metavolcanic = models.BooleanField(default=False)
    plutonite = models.BooleanField(default=False)
    tectonite = models.BooleanField(default=False)
    argillitic = models.BooleanField(default=False)
    chert = models.BooleanField(default=False)
    quartzite = models.BooleanField(default=False)
    siltstone = models.BooleanField(default=False)
    limeclast = models.BooleanField(default=False)
    desc = models.CharField(null=True, max_length=500, blank=True)
    image_name = models.CharField(null=True, max_length=100, blank=True)
    image_omero_id = models.IntegerField(null=True, blank=True)
    full_image_name = models.CharField(null=True, max_length=100, blank=True)
    full_image_omero_id = models.IntegerField(null=True, blank=True)
    full_image_oe_omero_id = models.IntegerField(null=True, blank=True)
    source = models.CharField(default="Dickinson Collection, Bishop Museum", null=True, blank=True, max_length=100)
    refs = models.ManyToManyField(Report, related_name="slides", blank=True)

    def __str__(self):
        return f"{self.name} ({self.sherd})" 

