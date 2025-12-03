import uuid
from django.db import models
from django.core.exceptions import ValidationError

def generate_short_id():
    return uuid.uuid4().hex[:8]  # e.g. 'a1b2c3d4'


   


# Create your models here.

class fillInBlanks_1(models.Model):

    idname = models.CharField(default=generate_short_id, max_length=8, unique=True, editable=False)

    emotion_1 = models.CharField(null=True, blank = True, max_length=60)
    adjective_1 = models.CharField(max_length=60)
    US_state = models.CharField(max_length=60)
    number_1 = models.CharField(max_length=60)
    past_tense_verb_1 = models.CharField(max_length=60)
    social_media = models.CharField(max_length=60)
    number_2 = models.CharField(max_length=60)
    past_tense_verb_2 = models.CharField(max_length=60)
    political_organization_1 = models.CharField(max_length=60)
    adjective_2 = models.CharField(max_length=60)
    group_of_people = models.CharField(max_length=60)
    political_organization_2 = models.CharField(max_length=60)
    verb_ing = models.CharField(max_length=60)
    past_tense_emotion = models.CharField(max_length=60)
    name = models.CharField(max_length=60)
    age = models.CharField(max_length=60)
    political_issue = models.CharField(max_length=60)
    Adjective_3 = models.CharField(max_length=60)
    Adjective_4 = models.CharField(max_length=60)
    
    def __str__(self):
        return f"{self.idname}"
    class Meta:
        db_table = 'fillInBlanks_1'

class fillInBlanks_2(models.Model):

    idname = models.CharField(default=generate_short_id, max_length=8, unique=True, editable=False)

    country_1 = models.CharField(max_length=60)
    country_2 = models.CharField(max_length=60)
    political_organization = models.CharField(max_length=60)
    social_media = models.CharField(max_length=60)
    product = models.CharField(max_length=60)
    government_role = models.CharField(max_length=60)
    endearment = models.CharField(max_length=60)
    noun = models.CharField(max_length=60)
    group_of_people = models.CharField(max_length=60, null=True, blank=True)
    plural_noun = models.CharField(max_length=60)
    weapon = models.CharField(max_length=60)
    name_1 = models.CharField(max_length=60)
    name_2 = models.CharField(max_length=60)

    def __str__(self):
        return f"{self.idname}"

    class Meta:
        db_table = 'fillInBlanks_2'

class fillInBlanks_3(models.Model):

    idname = models.CharField(default=generate_short_id, max_length=8, unique=True, editable=False)

    natural_disaster = models.CharField(max_length=60)
    feeling = models.CharField(max_length=60)
    movement_1 = models.CharField(max_length=60)
    movement_2 = models.CharField(max_length=60)
    number = models.CharField(max_length=60)
    farm_animal = models.CharField(max_length=60)
    chain = models.CharField(max_length=60)
    government_agency = models.CharField(max_length=60)
    technology = models.CharField(max_length=60)
    non_profit_agency = models.CharField(max_length=60)
    adjective = models.CharField(max_length=60)
    industry = models.CharField(max_length=60)
    political_organization = models.CharField(max_length=60)
    
    def __str__(self):
        return f"{self.idname}"
    
    class meta:
        db_table = 'fillInBlanks_3'

class fillInBlanks_4(models.Model):

    idname = models.CharField(default=generate_short_id, max_length=8, unique=True, editable=False)

    sport = models.CharField(max_length=60)
    brand = models.CharField(max_length=60)
    feeling = models.CharField(max_length=60)
    year = models.CharField(max_length=60)
    event = models.CharField(max_length=60)
    medical_provider = models.CharField(max_length=60)
    number = models.CharField(max_length=60)
    media_company = models.CharField(max_length=60)
    disease_1 = models.CharField(max_length=60)
    disease_2 = models.CharField(max_length=60)
    city = models.CharField(max_length=60)

    def __str__(self):
        return f"{self.idname}"
    
    class meta:
        db_table = 'fillInBlanks_4'

class fillInBlanks_5(models.Model):

    idname = models.CharField(default=generate_short_id, max_length=8, unique=True, editable=False)

    sporting_event = models.CharField(max_length=60)
    government_role = models.CharField(max_length=60)
    monarchal_country = models.CharField(max_length=60)
    US_state = models.CharField(max_length=60)
    name_1 = models.CharField(max_length=60)
    name_2 = models.CharField(max_length=60)
    vegetable = models.CharField(max_length=60)
    social_media_1 = models.CharField(max_length=60)
    social_media_2 = models.CharField(max_length=60)

    def __str__(self):
        return f"{self.idname}"
    
    class meta:
        db_table = 'fillInBlanks_5'

class fillInBlanks_6(models.Model):

    idname = models.CharField(default=generate_short_id, max_length=8, unique=True, editable=False)

    emotion = models.CharField(max_length=60)
    US_state = models.CharField(max_length=60)
    Fraternity = models.CharField(max_length=60)
    non_profit_agency = models.CharField(max_length=60)
    number_1 = models.CharField(max_length=60)
    number_2 = models.CharField(max_length=60)
    name_1 = models.CharField(max_length=60)
    number_3 = models.CharField(max_length=60)
    name_2 = models.CharField(max_length=60)
    college_major = models.CharField(max_length=60)

    def clean(self):
        for field in ['number_1', 'number_2', 'number_3']:
            value = getattr(self, field)
            if not value.isdigit():
                raise ValidationError({field: 'Only numbers are allowed.'})


    def __str__(self):
        return f"{self.idname}"
    
    class meta:
        db_table = 'fillInBlanks_6'

class fillInBlanks_7(models.Model):

    idname = models.CharField(default=generate_short_id, max_length=8, unique=True, editable=False)

    emotion = models.CharField(max_length=60)
    soccer_league = models.CharField(max_length=60)
    stadium = models.CharField(max_length=60)
    team_1 = models.CharField(max_length=60)
    team_2 = models.CharField(max_length=60)


    def __str__(self):
        return f"{self.idname}"
    
    class meta:
        db_table = 'fillInBlanks_7'

class fillInBlanks_8(models.Model):

    idname = models.CharField(default=generate_short_id, max_length=8, unique=True, editable=False)

    emotion = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    US_State_Capital = models.CharField(max_length=60)
    past_tense_emotion = models.CharField(max_length=60)
    social_media = models.CharField(max_length=60)
    school_class = models.CharField(max_length=60)
    school_mascot = models.CharField(max_length=60)
    name = models.CharField(max_length=60)
    lawn_game = models.CharField(max_length=60)
    

    def __str__(self):
        return f"{self.idname}"
    
    class meta:
        db_table = 'fillInBlanks_8'

