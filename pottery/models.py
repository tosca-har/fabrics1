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
    
class Industry(models.Model):
    TECHNIQUES = [
        ("S", "spiral"),
        ("SB", "spiral-beating"),
        ("SRB", "spiral-ring-beating"),
        ("SR", "spiral-ring"),
        ("PA", "paddle-anvil-added"),
        ("SBU", "spiral-beating-upside-down"),
        ("RG", "ring"),
        ("PR", "pug-ring-beating"),
        ("LBU", "slab-beating-upside-down"),
        ("PO", "paddle-anvil-hand-opened"),
        ("PC", "paddle-anvil-coils-added"),
        ("O", "other"),
        ("U", "unknown"),
    ]

    GENDER = [
        ("W", "women"),
        ("M", "men"),
        ("B", "both"),
        ("U", "unknown")
    ]
    POSITION = [
        ("W", "whole"),
        ("N", "neck"),
        ("R", "rim"),
        ("P", "plain"),
        ("U", "unknown")
    ]

    slug = models.SlugField(default="", blank=True, null=False, db_index=True)
    name = models.CharField(default="", max_length=50)
    time_start = models.IntegerField(null=True, blank =True)
    time_end = models.IntegerField(null=True, blank =True)
    region = models.CharField(null=True, max_length=100)
    language = models.CharField(default="", max_length=50, null=True, blank =True)
    language_code = models.CharField(default="", max_length=5, null=True, blank =True)
    technique = models.CharField(max_length=20, choices=TECHNIQUES, default="U")
    word_cooking = models.CharField(default="", max_length=50, null=True, blank = True)
    words_other = models.CharField(default="", max_length=100, null=True, blank =True)
    use_cooking = models.BooleanField(default=True)
    use_storage = models.BooleanField(default=False)
    use_ceremonial = models.BooleanField(default=False)
    use_serving = models.BooleanField(default=False)
    comments = models.CharField(null=True, max_length=500, blank =True)
    language_family = models.CharField(null=True, max_length=500, blank =True)
    language_superfamily = models.CharField(null=True, max_length=100, blank =True)
    gender = models.CharField(max_length=7, choices=GENDER, default="U")
    temper = models.BooleanField(null = True, blank = True)
    decoration_dentate = models.BooleanField(default=False)
    decoration_incised = models.BooleanField(default=False)
    decoration_comb_incised = models.BooleanField(default=False)
    decoration_applique = models.BooleanField(default=False)
    decoration_exposed_coil = models.BooleanField(default=False)
    decoration_punctate = models.BooleanField(default=False)
    decoration_paint = models.BooleanField(default=False)
    decoration_finger = models.BooleanField(default=False)
    decoration_sculpt = models.BooleanField(default=False)
    decoration_paddle = models.BooleanField(default=False)
    decoration_position = models.CharField(max_length=7, choices=POSITION, default= "U")
    form_w_more = models.BooleanField(default=False)
    form_h_more = models.BooleanField(default=False)
    form_equal = models.BooleanField(default=False)
    refs = models.ManyToManyField(Report, related_name="industries", blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.region})"

class Area(models.Model):
    slug = models.SlugField(default="", blank= True, null = False, db_index=True)
    name = models.CharField(max_length= 100)
    region = models.CharField(max_length= 20, null=True)
    lat = models.DecimalField(null=True, max_digits=9, decimal_places=6) 
    lng = models.DecimalField(null=True, max_digits=9, decimal_places=6)
    industry = models.ManyToManyField(Industry, related_name="area", blank=True)
    geonames_id = models.IntegerField(null=True, blank=True)
    open_location_code = models.CharField(null=True, blank=True, max_length=100)
   
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.region})"

    def thename(self):
        return f"{self.name}" 
    
    @property
    def fabric_string(self):
        fabs = self.industry.all()
        fabstring = ''
        for fab in fabs:
            fabstring = fabstring + " (" + fab.name + " " + str(fab.time_start) + "BP-" + str(fab.time_end) + "BP)"
        return fabstring
    
