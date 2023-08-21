from django import forms



mineral_choices = (
    (-1, "Unknown"),
    (6, "Very Dominant"),
    (5, "Major"),
    (4, "Frequent"),
    (3, "Common"),
    (2, "Few"),
    (1, "Minor"),
    (0, "None"),
)

region_choices= (
    ("Australia", "Australia"),
    ("Bismarck", "Bismarck"),
    ("Carolines", "Carolines"),
    ("Maluku", "Maluku"),
    ("Marianas", "Marianas"),
    ("Marquesas", "Marquesas"),
    ("Philippines", "Philippines"),
    ("PNG", "PNG"),
    ("Solomons", "Solomons"),
    ("Taiwan", "Taiwan"),
    ("Tonga", "Tonga"),
    ("Tuvalu", "Tuvalu"),
    ("Vanuatu", "Vanuatu"),
)

lithic_choices = (
    (None, "Unknown"),
    (True, "Present"),
    (False, "Absent"),
)    

class SearchForm(forms.Form):
    calcareous = forms.TypedChoiceField(choices= mineral_choices, coerce = int)
    quartz = forms.TypedChoiceField(choices= mineral_choices, coerce = int)
    feldspars = forms.TypedChoiceField(choices= mineral_choices, coerce = int)
    pyroxene = forms.TypedChoiceField(choices= mineral_choices, coerce = int)
    amphibole = forms.TypedChoiceField(choices= mineral_choices, coerce = int)
    opaque_iron_oxides = forms.TypedChoiceField(choices= mineral_choices, coerce = int)
    biotite = forms.TypedChoiceField(choices= mineral_choices, coerce = int)
    muscovite = forms.TypedChoiceField(choices= mineral_choices, coerce = int)
    olivine = forms.TypedChoiceField(choices= mineral_choices, coerce = int)
    epidote = forms.TypedChoiceField(choices= mineral_choices, coerce = int)
    garnet = forms.TypedChoiceField(choices= mineral_choices, coerce = int)
    igneous_rock_fragments = forms.TypedChoiceField(choices= mineral_choices, coerce = int)
    sedimentary_metasedimentary_rocks = forms.TypedChoiceField(choices= mineral_choices, coerce = int)
    grog = forms.TypedChoiceField(choices= mineral_choices, coerce = int)
    vitric = forms.ChoiceField(choices= lithic_choices, required = False)
    felsitic = forms.ChoiceField(choices= lithic_choices, required = False)
    microlitic = forms.ChoiceField(choices= lithic_choices, required = False)
    microphaneritic = forms.ChoiceField(choices= lithic_choices, required = False)
    lathwork = forms.ChoiceField(choices= lithic_choices, required = False)
    metavolcanic = forms.ChoiceField(choices= lithic_choices, required = False)
    plutonite = forms.ChoiceField(choices= lithic_choices, required = False)
    tectonite = forms.ChoiceField(choices= lithic_choices, required = False)
    argillitic = forms.ChoiceField(choices= lithic_choices, required = False)
    chert = forms.ChoiceField(choices= lithic_choices, required = False)
    quartzite = forms.ChoiceField(choices= lithic_choices, required = False)
    siltstone = forms.ChoiceField(choices= lithic_choices, required = False)
    limeclast = forms.ChoiceField(choices= lithic_choices, required = False)

    regions_to_include = forms.MultipleChoiceField(choices = region_choices, widget= forms.CheckboxSelectMultiple(attrs={"checked":""}), 
        error_messages= {"required": "Please select at least one region."})
