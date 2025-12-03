from django import forms
from . import models

class FillInBlanksForm(forms.ModelForm):

   
    emotion_choices = [
            ("Admiration", "Admiration"),
            ("Amusement", "Amusement"),
            ("Anger", "Anger"),
            ("Anxiety", "Anxiety"),
            ("Awe", "Awe"),
            ("Boredom", "Boredom"),
            ("Chaos", "Chaos"),
            ("Compassion", "Compassion"),
            ("Confidence", "Confidence"),
            ("Confusion", "Confusion"),
            ("Contentment", "Contentment"),
            ("Disgust", "Disgust"),
            ("Ecstasy", "Ecstasy"),
            ("Elation", "Elation"),
            ("Embarrassment", "Embarrassment"),
            ("Envy", "Envy"),
            ("Excitement", "Excitement"),
            ("Fear", "Fear"),
            ("Frustration", "Frustration"),
            ("Fury", "Fury"),
            ("Gratitude", "Gratitude"),
            ("Grief", "Grief"),
            ("Guilt", "Guilt"),
            ("Happiness", "Happiness"),
            ("Hope", "Hope"),
            ("Joy", "Joy"),
            ("Loneliness", "Loneliness"),
            ("Love", "Love"),
            ("Pride", "Pride"),
            ("Rage", "Rage"),
            ("Regret", "Regret"),
            ("Sadness", "Sadness"),
            ("Shame", "Shame"),
            ("Surprise", "Surprise"),
            ("Terror", "Terror"),
            ("Trust", "Trust"),
            ("Worry", "Worry"),
            ("Yearning", "Yearning"),
            ("Zeal", "Zeal"),
        ]
    adjective_choices = [
            ("affectionate", "affectionate"),
            ("angry", "angry"),
            ("anxious", "anxious"),
            ("apoplectic", "apoplectic"),
            ("bewildered", "bewildered"),
            ("charismatic", "charismatic"),
            ("cheerful", "cheerful"),
            ("courageous", "courageous"),
            ("curious", "curious"),
            ("dejected", "dejected"),
            ("devastating", "devastating"),
            ("disingenuous", "disingenuous"),
            ("dubious", "dubious"),
            ("ecstatic", "ecstatic"),
            ("epic", "epic"),
            ("fearful", "fearful"),
            ("fraudulent", "fraudulent"),
            ("frivolous", "frivolous"),
            ("grateful", "grateful"),
            ("great", "great"),
            ("honest", "honest"),
            ("hopeful", "hopeful"),
            ("horrible", "horrible"),
            ("intense", "intense"),
            ("jealous", "jealous"),
            ("lonely", "lonely"),
            ("melancholy", "melancholy"),
            ("nervous", "nervous"),
            ("overjoyed", "overjoyed"),
            ("patient", "patient"),
            ("pensive", "pensive"),
            ("poor", "poor"),
            ("positive", "positive"),
            ("resentful", "resentful"),
            ("sweet", "sweet"),
            ("sympathetic", "sympathetic"),
            ("terrified", "terrified"),
            ("tiresome", "tiresome"),
            ("tough", "tough"),
            ("treacherous", "treacherous"),
            ("wistful", "wistful"),
            ("witty", "witty"),
            ("wonderful", "wonderful"),
            ("vengeful", "vengeful"),
            ("yearning", "yearning"),
        ]
    US_state_choice = [
            ('AK','AK'),
            ('AL','AL'),
            ('AR','AR'),
            ('AZ','AZ'),
            ('CA','CA'),
            ('CO','CO'),
            ('CT','CT'),
            ('DE','DE'),
            ('FL','FL'),
            ('GA','GA'),
            ('HI','HI'),
            ('IA','IA'),
            ('ID','ID'),
            ('IL','IL'),
            ('IN','IN'),
            ('KS','KS'),
            ('KY','KY'),
            ('LA','LA'),
            ('MA','MA'),
            ('MD','MD'),
            ('ME','ME'),
            ('MI','MI'),
            ('MN','MN'),
            ('MO','MO'),
            ('MS','MS'),
            ('MT','MT'),
            ('NC','NC'),
            ('ND','ND'),
            ('NE','NE'),
            ('NH','NH'),
            ('NJ','NJ'),
            ('NM','NM'),
            ('NV','NV'),
            ('NY','NY'),
            ('OH','OH'),
            ('OK','OK'),
            ('OR','OR'),
            ('PA','PA'),
            ('RI','RI'),
            ('SC','SC'),
            ('SD','SD'),
            ('TN','TN'),
            ('TX','TX'),
            ('UT','UT'),
            ('VA','VA'),
            ('VT','VT'),
            ('WA','WA'),
            ('WI','WI'),
            ('WV','WV'),
            ('WY','WY')
        ]
    past_tense_verb_choices = [
            ("acted","acted"),
            ("ate","ate"),
            ("danced","danced"),
            ("dumped","dumped"),
            ("engraved","engraved"),
            ("fancied","fancied"),
            ("fought","fought"),
            ("laughed","laughed"),
            ("rioted","rioted"),
            ("sat","sat"),
            ("shook","shook"),
            ("shouted","shouted"),
            ("smoked","smoked"),
            ("swam","swam"),
            ("talked","talked"),
            ("voted","voted"),
            ("vomited","vomited"),
            ("walked","walked"),
            ("wandered","wandered"),
            ("wondered","wondered")
        ]
    social_media_choices = [
            ("Instagram","Instagram"),
            ("Tik Tok","Tik Tok"),
            ("X (formely known as twitter)","X (formely known as twitter)"),
            ("Facebook","Facebook"),
            ("Myspace","Myspace")
        ]
    political_organizations = [
            ("African National Congress","African National Congress"),
            ("aliens","aliens"),
            ("Bolsheviks","Bolsheviks"),
            ("Black Panthers","Black Panthers"),
            ("British Royal Family","British Royal Family"),
            ("conservatives","conservatives"),
            ("Continental Congress","Continental Congress"),
            ("deep state","deep state"),
            ("Democrats","Democrats"),
            ("First Family","First Family"),
            ("Hamas","Hamas"),
            ("independent voters","independent voters"),
            ("Illuminati","Illuminati"),
            ("Irish Mafia","Irish Mafia"),
            ("KGB","KGB"),
            ("Labour Party","Labour Party"),
            ("liberals","liberals"),
            ("lower class","lower class"),
            ("middle class","middle class"),
            ("Mossad","Mossad"),
            ("one-percent","one-percent"),
            ("past presidents","past presidents"),
            ("Republicans","Republicans"),
            ("Sandinistas","Sandinistas"),
            ("suffragettes","suffragettes"),
            ("Tamil Tigers","Tamil Tigers"),
            ("upper class","upper class"),
            ("working class","working class"),
            ("Zapatistas","Zapatistas")
        ]
    group_of_people_choices = [
            ("activists", "activists"),
            ("actors", "actors"),
            ("artists", "artists"),
            ("athletes", "athletes"),
            ("authors", "authors"),
            ("chefs", "chefs"),
            ("clergy", "clergy"),
            ("conclave", "conclave"),
            ("creators", "creators"),
            ("diplomats", "diplomats"),
            ("doctors", "doctors"),
            ("elders", "elders"),
            ("engineers", "engineers"),
            ("explorers", "explorers"),
            ("farmers", "farmers"),
            ("geeks", "geeks"),
            ("generals", "generals"),
            ("gods", "gods"),
            ("governors", "governors"),
            ("hippies", "hippies"),
            ("jocks", "jocks"),
            ("judges", "judges"),
            ("jury", "jury"),
            ("lawyers", "lawyers"),
            ("legislators", "legislators"),
            ("librarians", "librarians"),
            ("mayors", "mayors"),
            ("monarchs", "monarchs"),
            ("musicians", "musicians"),
            ("nerds", "nerds"),
            ("owners", "owners"),
            ("philosophers", "philosophers"),
            ("poor", "poor"),
            ("representatives", "representatives"),
            ("runners", "runners"),
            ("scientists", "scientists"),
            ("senators", "senators"),
            ("soldiers", "soldiers"),
            ("students", "students"),
            ("sweethearts", "sweethearts"),
            ("teachers", "teachers"),
            ("wealthy", "wealthy"),
            ("workers", "workers"),
            ("voters", "voters"),
        ]
    verb_ing_choices = [
            ("running","running"),
            ("dancing","dancing"),
            ("crying","crying"),
            ("laughing","laughing"),
            ("silencing","silencing"),
            ("tickling","tickling"),
            ("slapping","slapping"),
            ("high-fiving","high-fiving"),
            ("eating","eating"),
            ("shaking","shaking"),
            ("hugging","hugging"),
            ("clapping","clapping")
        ]
    past_tense_emotion_choices = [
            ("admired", "admired"),
            ("agitated", "agitated"),
            ("amazed", "amazed"),
            ("amused", "amused"),
            ("angered", "angered"),
            ("annoyed", "annoyed"),
            ("anxious", "anxious"),
            ("awake", "awake"),
            ("bewildered", "bewildered"),
            ("bored", "bored"),
            ("burnt", "burnt"),
            ("confused", "confused"),
            ("dead", "dead"),
            ("delighted", "delighted"),
            ("disappointed", "disappointed"),
            ("disgraced", "disgraced"),
            ("disheveled", "disheveled"),
            ("distressed", "distressed"),
            ("embarrassed", "embarrassed"),
            ("excited", "excited"),
            ("felt", "felt"),
            ("freed", "freed"),
            ("frustrated", "frustrated"),
            ("grateful", "grateful"),
            ("hopeful", "hopeful"),
            ("jealous", "jealous"),
            ("known", "known"),
            ("lonely", "lonely"),
            ("lost", "lost"),
            ("misplaced", "misplaced"),
            ("oppressed", "oppressed"),
            ("overcome", "overcome"),
            ("overwhelmed", "overwhelmed"),
            ("relaxed", "relaxed"),
            ("relieved", "relieved"),
            ("satisfied", "satisfied"),
            ("saved", "saved"),
            ("shaken", "shaken"),
            ("shocked", "shocked"),
            ("silenced", "silenced"),
            ("stained", "stained"),
            ("startled", "startled"),
            ("surprised", "surprised"),
            ("terrified", "terrified"),
            ("tired", "tired"),
            ("violated", "violated"),
            ("worn", "worn"),
        ]
    political_issue_choices = [
            ("abortion rights", "abortion rights"),
            ("access to healthcare", "access to healthcare"),
            ("artificial intelligence", "artificial intelligence"),
            ("banning books", "banning books"),
            ("cancel culture", "cancel culture"),
            ("censorship", "censorship"),
            ("civil rights", "civil rights"),
            ("criminal justice reform", "criminal justice reform"),
            ("cybersecurity", "cybersecurity"),
            ("DEI policies", "DEI policies"),
            ("economic disparity", "economic disparity"),
            ("education policy", "education policy"),
            ("foreign relations", "foreign relations"),
            ("free childcare", "free childcare"),
            ("gender equality", "gender equality"),
            ("gender identity", "gender identity"),
            ("gun control", "gun control"),
            ("gun rights", "gun rights"),
            ("healthcare access", "healthcare access"),
            ("human trafficking", "human trafficking"),
            ("immigration policy", "immigration policy"),
            ("LGBTQIA+ rights", "LGBTQIA+ rights"),
            ("national security", "national security"),
            ("nepotism", "nepotism"),
            ("physician-assisted death", "physician-assisted death"),
            ("race relations", "race relations"),
            ("racial equality", "racial equality"),
            ("tax reform", "tax reform"),
            ("the climate crisis", "the climate crisis"),
            ("transgender rights", "transgender rights"),
            ("voting rights", "voting rights"),
            ("women’s rights", "women’s rights"),
        ]
    name_choices = [
            ("Aisha","Aisha"),
            ("Anya","Anya"),
            ("Chloe","Chloe"),
            ("Diego","Diego"),
            ("Emmanuel","Emmanuel"),
            ("Fatima","Fatima"),
            ("Hiroshi","Hiroshi"),
            ("Isabella","Isabella"),
            ("Javier","Javier"),
            ("Kenji","Kenji"),
            ("Kwame","Kwame"),
            ("Lena","Lena"),
            ("Liam","Liam"),
            ("Mateo","Mateo"),
            ("Mei","Mei"),
            ("Omar","Omar"),
            ("Priya","Priya"),
            ("Samuel","Samuel"),
            ("Sofia","Sofia")
    ]
    age_choices = [
            ("18","18"),
            ("25","25"),
            ("37","37"),
            ("42","42"),
            ("58","58"),
            ("65","65"),
            ("73","73"),
            ("81","81"),
            ("97","97"),
            ("120","120")
    ]
    number_choices=[
        ("5","5"),
        ("10","10"),
        ("100","100"),
        ("100,000","100,000"),
        ("1,000,000","1,000,000")
    ]

    emotion_1 = forms.ChoiceField( choices = emotion_choices, widget = forms.Select(attrs={
                'class': 'form-control'
            }))
    adjective_1 = forms.ChoiceField( choices = adjective_choices, widget = forms.Select(attrs={
                'class': 'form-control'
            }))
    US_state = forms.ChoiceField( choices = US_state_choice, widget = forms.Select(attrs={
                'class': 'form-control'
            }))
    number_1 = forms.ChoiceField( choices = number_choices, widget = forms.Select(attrs={
                'class': 'form-control'
            }))
    past_tense_verb_1 = forms.ChoiceField( choices = past_tense_verb_choices, widget = forms.Select(attrs={
                'class': 'form-control'
            }))
    social_media = forms.ChoiceField( choices = social_media_choices, widget = forms.Select(attrs={
                'class': 'form-control'
            }))
    number_2 = forms.ChoiceField( choices = number_choices, widget = forms.Select(attrs={
                'class': 'form-control'
            }))
    past_tense_verb_2 = forms.ChoiceField( choices = past_tense_verb_choices, widget = forms.Select(attrs={
                'class': 'form-control'
            }))
    political_organization_1 = forms.ChoiceField( choices = political_organizations, widget = forms.Select(attrs={
                'class': 'form-control'
            }))
    adjective_2 = forms.ChoiceField( choices = adjective_choices, widget = forms.Select(attrs={
                'class': 'form-control'
            }))
    group_of_people = forms.ChoiceField( choices = group_of_people_choices, widget = forms.Select(attrs={
                'class': 'form-control'
            }))
    political_organization_2 = forms.ChoiceField( choices = political_organizations, widget = forms.Select(attrs={
                'class': 'form-control'
            }))
    verb_ing = forms.ChoiceField( choices = verb_ing_choices, widget = forms.Select(attrs={
                'class': 'form-control'
            }))
    past_tense_emotion = forms.ChoiceField( choices = past_tense_emotion_choices, widget = forms.Select(attrs={
                'class': 'form-control'
            }))
    name = forms.ChoiceField( choices = name_choices, widget = forms.Select(attrs={
                'class': 'form-control'
            }))
    age = forms.ChoiceField( choices = age_choices, widget = forms.Select(attrs={
                'class': 'form-control'
            }))
    political_issue = forms.ChoiceField( choices = political_issue_choices, widget = forms.Select(attrs={
                'class': 'form-control'
            }))
    Adjective_3 = forms.ChoiceField( choices = adjective_choices, widget = forms.Select(attrs={
                'class': 'form-control'
            }))
    Adjective_4 = forms.ChoiceField( choices = adjective_choices, widget = forms.Select(attrs={
                'class': 'form-control'
            }))
    
    class Meta:
        model = models.fillInBlanks_1
        fields = ['emotion_1', 'adjective_1', 'US_state', 'number_1', 'past_tense_verb_1', 'social_media', 'number_2', 'past_tense_verb_2', 'political_organization_1', 
                  'adjective_2', 'group_of_people', 'political_organization_2', 'verb_ing', 'past_tense_emotion', 'name', 'age', 'political_issue', 'Adjective_3', 'Adjective_4' ]
    
class FillInTheBlanks2(forms.ModelForm):
   
    country_choices = [(c, c) for c in [
    "Afghanistan", "Algeria", "Argentina", "Australia", "Austria", "Bangladesh", "Belarus", "Belgium", "Benin",
    "Bolivia", "Brazil", "Burkina Faso", "Burundi", "Cambodia", "Cameroon", "Canada", "Chad", "Chile", "China",
    "Colombia", "Czech Republic", "DR Congo", "Dominican Republic", "Ecuador", "Egypt", "Ethiopia", "France",
    "Germany", "Ghana", "Greece", "Guatemala", "Guinea", "Haiti", "Honduras", "Hungary", "India", "Indonesia",
    "Iran", "Iraq", "Israel", "Italy", "Ivory Coast", "Japan", "Jordan", "Kazakhstan", "Kenya", "KGB", "Malaysia",
    "Madagascar", "Malawi", "Mali", "Mexico", "Morocco", "Mozambique", "Myanmar", "Nepal", "Netherlands",
    "Niger", "Nigeria", "North Korea", "Pakistan", "Papua New Guinea", "Peru", "Philippines", "Poland", "Portugal",
    "Republicans", "Romania", "Russia", "Rwanda", "Saudi Arabia", "Senegal", "Serbia", "Somalia", "South Africa",
    "South Korea", "South Sudan", "Spain", "Sri Lanka", "Sudan", "Sweden", "Switzerland", "Syria", "Tajikistan",
    "Tanzania", "Thailand", "Tunisia", "Turkey", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom",
    "United States", "Uruguay", "Uzbekistan", "Venezuela", "Vietnam", "Yemen", "Zambia", "Zimbabwe"]
    ]


    # Provided choices
    political_organization_choices = [
        ("African National Congress","African National Congress"),
        ("aliens","aliens"),
        ("Bolsheviks","Bolsheviks"),
        ("Black Panthers","Black Panthers"),
        ("British Royal Family","British Royal Family"),
        ("conservatives","conservatives"),
        ("Continental Congress","Continental Congress"),
        ("deep state","deep state"),
        ("Democrats","Democrats"),
        ("First Family","First Family"),
        ("Hamas","Hamas"),
        ("independent voters","independent voters"),
        ("Illuminati","Illuminati"),
        ("Irish Mafia","Irish Mafia"),
        ("KGB","KGB"),
        ("Labour Party","Labour Party"),
        ("liberals","liberals"),
        ("lower class","lower class"),
        ("middle class","middle class"),
        ("Mossad","Mossad"),
        ("one-percent","one-percent"),
        ("past presidents","past presidents"),
        ("Republicans","Republicans"),
        ("Sandinistas","Sandinistas"),
        ("suffragettes","suffragettes"),
        ("Tamil Tigers","Tamil Tigers"),
        ("upper class","upper class"),
        ("working class","working class"),
        ("Zapatistas","Zapatistas")
    ]

    social_media_choices = [
        ("Instagram","Instagram"),
        ("Tik Tok","Tik Tok"),
        ("X (formely known as twitter)","X (formely known as twitter)"),
        ("Facebook","Facebook"),
        ("Myspace","Myspace")
    ]

    product_choices = [(p, p) for p in [
        "aluminum", "automobiles", "blue jeans", "clothing", "coal", "coffee", "computers", "crude oil", "gold", "iron ore",
        "machinery", "microchips", "medical equipment", "natural gas", "pharmaceuticals", "platinum", "potatoes",
        "soybeans", "wheat", "zinc"
    ]]

    government_role_choices = [(g, g) for g in [
        "ambassador", "chancellor", "count", "countess", "dictator", "duchess", "duke", "emperor", "empress", "governor",
        "king", "mayor", "minister", "monarch", "premier", "president", "prime minister", "queen", "sultan", "viceroy"
    ]]

    endearment_choices = [(e, e) for e in [
        "angel", "baby", "brat", "darling", "dear", "dictator", "dimwit", "doll", "fool", "honey", "idiot", "love",
        "nitwit", "precious", "pumpkin", "scamp", "sweetheart", "treasure", "twit", "wretch"
    ]]

    
    noun_choices = [(n, n) for n in [
        "apple", "bridge", "city", "dream", "engine", "forest", "galaxy", "hero", "island", "jungle", "key", "language",
        "mirror", "night", "ocean", "planet", "quest", "river", "star", "tower", "umbrella", "village", "whale", "xylophone", "youth"
    ]]

    group_of_people_choices = [
        ("actors","actors"),
        ("authors","authors"),
        ("creators","creators"),
        ("gods","gods"),
        ("governors","governors"),
        ("judges","judges"),
        ("jury","jury"),
        ("legislators","legislators"),
        ("librarians","librarians"),
        ("mayors","mayors"),
        ("owners","owners"),
        ("poor","poor"),
        ("representatives","representatives"),
        ("runners","runners"),
        ("senators","senators"),
        ("students","students"),
        ("sweethearts","sweethearts"),
        ("wealthy","wealthy"),
        ("workers","workers"),
        ("voters","voters")
    ]

    plural_noun_choices = [(p, p) for p in [
        "apples", "bread", "carabiners", "diaries", "eggs", "flowers", "goats", "houses", "ideas", "jewels",
        "ketamine injections", "lemons", "monsters", "newspapers", "octopi", "pastries", "quiz shows", "rivalries",
        "vaccines", "water bottles"
    ]]

    weapon_choices = [(w, w) for w in [
        "anthrax attack", "anti-tank guided missiles", "calvary attacks", "cyber weapons", "drones", "electric grid blackout",
        "electromagnetic railgun", "hypersonic missiles", "lasers", "loitering munitions", "militia attacks", "nuclear weapons",
        "parachute bombs", "pressure cooker bombs", "salmonella poisoning", "stealth aircraft", "submarines",
        "suicide bombers", "thermobaric bomb", "zombie disease viral outbreak"
    ]]

    name_choices = [
        ("Aisha","Aisha"), ("Anya","Anya"), ("Chloe","Chloe"), ("Diego","Diego"), ("Emmanuel","Emmanuel"),
        ("Fatima","Fatima"), ("Hiroshi","Hiroshi"), ("Isabella","Isabella"), ("Javier","Javier"), ("Kenji","Kenji"),
        ("Kwame","Kwame"), ("Lena","Lena"), ("Liam","Liam"), ("Mateo","Mateo"), ("Mei","Mei"), ("Omar","Omar"),
        ("Priya","Priya"), ("Samuel","Samuel"), ("Sofia","Sofia")
    ]

    # Define form fields
    country_1 = forms.ChoiceField(choices=country_choices, widget=forms.Select(attrs={'class': 'form-control'}))
    political_organization = forms.ChoiceField(choices=political_organization_choices, widget=forms.Select(attrs={'class': 'form-control'}))
    country_2 = forms.ChoiceField(choices=country_choices, widget=forms.Select(attrs={'class': 'form-control'}))
    social_media = forms.ChoiceField(choices=social_media_choices, widget=forms.Select(attrs={'class': 'form-control'}))
    product = forms.ChoiceField(choices=product_choices, widget=forms.Select(attrs={'class': 'form-control'}))
    government_role = forms.ChoiceField(choices=government_role_choices, widget=forms.Select(attrs={'class': 'form-control'}))
    endearment = forms.ChoiceField(choices=endearment_choices, widget=forms.Select(attrs={'class': 'form-control'}))
    noun = forms.ChoiceField(choices=noun_choices, widget=forms.Select(attrs={'class': 'form-control'}))
    group_of_people = forms.ChoiceField(choices=group_of_people_choices, widget = forms.Select(attrs={'class': 'form-control'}))
    plural_noun = forms.ChoiceField(choices=plural_noun_choices, widget=forms.Select(attrs={'class': 'form-control'}))
    weapon = forms.ChoiceField(choices=weapon_choices, widget=forms.Select(attrs={'class': 'form-control'}))
    name_1 = forms.ChoiceField(choices=name_choices, widget=forms.Select(attrs={'class': 'form-control'}))
    name_2 = forms.ChoiceField(choices=name_choices, widget=forms.Select(attrs={'class': 'form-control'}))

    
    class Meta:
        model = models.fillInBlanks_2
        fields = [
            'country_1','country_2', 'political_organization', 'social_media', 'product',
            'government_role', 'endearment', 'noun', 'group_of_people', 'plural_noun',
            'weapon', 'name_1', 'name_2'
        ]
        

class FillInTheBlanks3(forms.ModelForm):

    NATURAL_DISASTER_CHOICES = [
    ('avalanche', 'Avalanche'), ('blizzard', 'Blizzard'), ('coastal storm surge', 'Coastal Storm Surge'),
    ('cyclone', 'Cyclone'), ('dam failure', 'Dam Failure'), ('dust storm', 'Dust Storm'),
    ('earthquake', 'Earthquake'), ('flash flood', 'Flash Flood'), ('flood', 'Flood'),
    ('hailstorm', 'Hailstorm'), ('hurricane', 'Hurricane'), ('landslide', 'Landslide'),
    ('mudslide', 'Mudslide'), ('plague of locusts', 'Plague Of Locusts'), ('tornado', 'Tornado'),
    ('tropical storm', 'Tropical Storm'), ('tsunami', 'Tsunami'), ('typhoon', 'Typhoon'),
    ('wildfire', 'Wildfire')
    ]

    FEELING_CHOICES = [
        ('annoying', 'annoying'), ('appalling', 'appalling'), ('astonishing', 'astonishing'),
        ('charming', 'charming'), ('confusing', 'confusing'), ('crippling', 'crippling'),
        ('depressing', 'depressing'), ('disturbing', 'disturbing'), ('embarrassing', 'embarrassing'),
        ('exciting', 'exciting'), ('frightening', 'frightening'), ('frustrating', 'frustrating'),
        ('gratifying', 'gratifying'), ('humiliating', 'humiliating'), ('inspiring', 'inspiring'),
        ('overwhelming', 'overwhelming'), ('relaxing', 'relaxing'), ('rewarding', 'rewarding'),
        ('scintillating', 'scintillating'), ('shocking', 'shocking'), ('thrilling', 'thrilling'),
        ('wowing', 'wowing'), ('wondering', 'wondering')
    ]

    MOVEMENT_CHOICES = [
        ('bent', 'bent'), ('barreled', 'barreled'), ('climbed', 'climbed'), ('crawled', 'crawled'),
        ('crept', 'crept'), ('danced', 'danced'), ('dove', 'dove'), ('fell', 'fell'),
        ('galloped', 'galloped'), ('galivanted', 'galivanted'), ('glided', 'glided'),
        ('hopped', 'hopped'), ('jostled', 'jostled'), ('jumped', 'jumped'), ('leapt', 'leapt'),
        ('lollygagged', 'lollygagged'), ('marched', 'marched'), ('pulled', 'pulled'),
        ('pushed', 'pushed'), ('rolled', 'rolled'), ('ran', 'ran'), ('rushed', 'rushed'),
        ('shimmied', 'shimmied'), ('shook', 'shook'), ('shoved', 'shoved'), ('skipped', 'skipped'),
        ('skirted', 'skirted'), ('slid', 'slid'), ('sprinted', 'sprinted'), ('swept', 'swept'),
        ('tumbled', 'tumbled'), ('twisted', 'twisted'), ('walked', 'walked'), ('zig-zagged', 'zig-zagged')
    ]

    NUMBER_CHOICES = [(str(i), str(i)) for i in range(1, 101)]

    FARM_ANIMAL_CHOICES = [
        ('alpaca', 'alpaca'), ('boar', 'boar'), ('bull', 'bull'), ('camel', 'camel'), ('chick', 'chick'),
        ('chicken', 'chicken'), ('donkey', 'donkey'), ('duck', 'duck'), ('emu', 'emu'),
        ('goat', 'goat'), ('hen', 'hen'), ('horse', 'horse'), ('llama', 'llama'), ('mare', 'mare'),
        ('mule', 'mule'), ('ostrich', 'ostrich'), ('pig', 'pig'), ('rabbit', 'rabbit'),
        ('ram', 'ram'), ('rooster', 'rooster'), ('sheep', 'sheep'), ('stallion', 'stallion'),
        ('steer', 'steer'), ('stud colt', 'stud colt'), ('turkey', 'turkey')
    ]

    CHAIN_CHOICES = [
        ('Aldi', 'Aldi'), ('Big Lots', 'Big Lots'), ('Dollar General', 'Dollar General'),
        ('Dollar Tree', 'Dollar Tree'), ('Family Dollar', 'Family Dollar'),
        ('Harbor Freight Tools', 'Harbor Freight Tools'), ('Hobby Lobby', 'Hobby Lobby'),
        ('Home Depot', 'Home Depot'), ('Home Goods', 'Home Goods'), ('Kmart', 'Kmart'),
        ('Kroger', 'Kroger'), ('McDonald’s', 'McDonald’s'), ('Menard’s', 'Menard’s'),
        ('Publix', 'Publix'), ('Radio Shack', 'Radio Shack'), ('ROSS Dress for Less', 'ROSS Dress for Less'),
        ('Save-A-Lot', 'Save-A-Lot'), ('Taco Bell', 'Taco Bell'), ('Target', 'Target'),
        ('Trader Joe’s', 'Trader Joe’s'), ('Waffle House', 'Waffle House'),
        ('Walgreens', 'Walgreens'), ('Walmart', 'Walmart')
    ]

    GOV_AGENCY_CHOICES = [
        ('ATF', 'ATF (Bureau of Alcohol, Tobacco, and Firearms)'), ('CIA', 'CIA (Central Intelligence Agency)'),
        ('DHHS', 'DHHS (Department of Health and Human Services)'), ('DHS', 'DHS (Department of Homeland Security)'),
        ('DOD', 'DOD (Department of Defense)'), ('DOJ', 'DOJ (Department of Justice)'),
        ('DOI', 'DOI (Department of the Interior)'), ('DOT', 'DOT (Department of Transportation)'),
        ('EPA', 'EPA (Environmental Protection Agency)'), ('FBI', 'FBI (Federal Bureau of Investigation)'),
        ('FEMA', 'FEMA (Federal Emergency Management Agency)'), ('NOAA', 'NOAA (National Oceanic and Atmospheric Administration)'),
        ('LIHEAP', 'LIHEAP (Low Income Home Energy Assistance Program)'), ('NORAD', 'NORAD (North American Aerospace Defense Command)'),
        ('USAID', 'USAID (U.S. Agency for International Development)')
    ]

    TECHNOLOGY_CHOICES = [
        ('5G cell towers', '5G cell towers'), ('automated toll booths', 'automated toll booths'),
        ('border surveillance towers', 'border surveillance towers'), ('broadcast antennas', 'broadcast antennas'),
        ('CCTV surveillance cameras', 'CCTV surveillance cameras'), ('emergency siren systems', 'emergency siren systems'),
        ('GPS ground stations', 'GPS ground stations'), ('military communication bunkers', 'military communication bunkers'),
        ('power grid substations', 'power grid substations'), ('radio towers', 'radio towers'),
        ('satellite dishes', 'satellite dishes'), ('solar panels', 'solar panels'),
        ('space lasers', 'space lasers'), ('traffic cameras', 'traffic cameras'),
        ('unmanned drones', 'unmanned drones'), ('weather radar stations', 'weather radar stations'),
        ('wind turbines', 'wind turbines')
    ]

    NON_PROFIT_CHOICES = [
        ('American Cancer Society', 'American Cancer Society'),
        ('American Civil Liberties Union (ACLU)', 'American Civil Liberties Union (ACLU)'),
        ('American Red Cross', 'American Red Cross'),
        ('ASPCA', 'American Society for the Prevention of Cruelty to Animals (ASPCA)'),
        ('Amnesty International USA', 'Amnesty International USA'),
        ('Boys and Girls Clubs of America', 'Boys and Girls Clubs of America'),
        ('Boy Scouts of America', 'Boy Scouts of America'),
        ('Environmental Defense Fund', 'Environmental Defense Fund'),
        ('Everytown for Gun Safety', 'Everytown for Gun Safety'),
        ('Feeding America', 'Feeding America'),
        ('Girl Scouts of the USA', 'Girl Scouts of the USA'),
        ('Habitat for Humanity', 'Habitat for Humanity'),
        ('Heritage Foundation', 'Heritage Foundation'),
        ('Make-A-Wish Foundation', 'Make-A-Wish Foundation'),
        ('Meals on Wheels America', 'Meals on Wheels America'),
        ('NRDC', 'Natural Resources Defense Council (NRDC)'),
        ('PETA', 'People for the Ethical Treatment of Animals (PETA)'),
        ('Planned Parenthood Federation of America', 'Planned Parenthood Federation of America'),
        ('Scouting America', 'Scouting America'),
        ('Sierra Club Foundation', 'Sierra Club Foundation'),
        ('Special Olympics USA', 'Special Olympics USA'),
        ('St. Jude Children’s Research Hospital', 'St. Jude Children’s Research Hospital'),
        ('The Salvation Army USA', 'The Salvation Army USA'),
        ('United Way Worldwide', 'United Way Worldwide'),
        ('WWF', 'World Wildlife Fund (WWF)')
    ]

    ADJECTIVE_CHOICES = [
        ('apoplectic', 'apoplectic'), ('charismatic', 'charismatic'), ('courageous', 'courageous'),
        ('devastating', 'devastating'), ('disingenuous', 'disingenuous'), ('dubious', 'dubious'),
        ('epic', 'epic'), ('fraudulent', 'fraudulent'), ('frivolous', 'frivolous'), ('great', 'great'),
        ('honest', 'honest'), ('hopeful', 'hopeful'), ('horrible', 'horrible'), ('intense', 'intense'),
        ('poor', 'poor'), ('positive', 'positive'), ('sweet', 'sweet'), ('tiresome', 'tiresome'),
        ('treacherous', 'treacherous'), ('witty', 'witty'), ('wonderful', 'wonderful')
    ]

    INDUSTRY_CHOICES = [
        ('ammunition', 'ammunition'), ('appliance manufacturing', 'appliance manufacturing'),
        ('automotive', 'automotive'), ('basket weaving', 'basket weaving'),
        ('board game manufacturing', 'board game manufacturing'), ('book binding', 'book binding'),
        ('clothing', 'clothing'), ('computer microchip', 'computer microchip'),
        ('cosmetic', 'cosmetic'), ('fast fashion', 'fast fashion'), ('food preservative', 'food preservative'),
        ('greeting card', 'greeting card'), ('lithium ion battery', 'lithium ion battery'),
        ('machinery parts', 'machinery parts'), ('medical device', 'medical device'),
        ('metal fabrication', 'metal fabrication'), ('oil refinery', 'oil refinery'),
        ('paper product', 'paper product'), ('pharmaceutical', 'pharmaceutical'),
        ('plastic product', 'plastic product'), ('synthetic chemical', 'synthetic chemical'),
        ('weapons', 'weapons')
    ]

    POLITICAL_ORG_CHOICES = [
        ('African National Congress', 'African National Congress'), ('aliens', 'aliens'),
        ('Bolsheviks', 'Bolsheviks'), ('Black Panthers', 'Black Panthers'),
        ('British Royal Family', 'British Royal Family'), ('conservatives', 'conservatives'),
        ('Continental Congress', 'Continental Congress'), ('deep state', 'deep state'),
        ('Democrats', 'Democrats'), ('First Family', 'First Family'), ('Hamas', 'Hamas'),
        ('independent voters', 'independent voters'), ('Illuminati', 'Illuminati'),
        ('Irish Mafia', 'Irish Mafia'), ('Italian Mafia', 'Italian Mafia'),
        ('KGB', 'KGB'), ('Labour Party', 'Labour Party'), ('liberals', 'liberals'),
        ('lower class', 'lower class'), ('middle class', 'middle class'), ('Mossad', 'Mossad'),
        ('MS-13', 'MS-13'), ('one-percent', 'one-percent'), ('past presidents', 'past presidents'),
        ('Republicans', 'Republicans'), ('Sandinistas', 'Sandinistas'), ('suffragettes', 'suffragettes'),
        ('Tamil Tigers', 'Tamil Tigers'), ('Tren de Aragua', 'Tren de Aragua'),
        ('upper class', 'upper class'), ('working class', 'working class'), ('Zapatistas', 'Zapatistas')
    ]

    natural_disaster = forms.ChoiceField(choices=NATURAL_DISASTER_CHOICES)
    feeling = forms.ChoiceField(choices=FEELING_CHOICES)
    movement_1 = forms.ChoiceField(choices=MOVEMENT_CHOICES)
    movement_2 = forms.ChoiceField(choices=MOVEMENT_CHOICES)
    number = forms.ChoiceField(choices=NUMBER_CHOICES)
    farm_animal = forms.ChoiceField(choices=FARM_ANIMAL_CHOICES)
    chain = forms.ChoiceField(choices=CHAIN_CHOICES)
    government_agency = forms.ChoiceField(choices=GOV_AGENCY_CHOICES)
    technology = forms.ChoiceField(choices=TECHNOLOGY_CHOICES)
    non_profit_agency = forms.ChoiceField(choices=NON_PROFIT_CHOICES)
    adjective = forms.ChoiceField(choices=ADJECTIVE_CHOICES)
    industry = forms.ChoiceField(choices=INDUSTRY_CHOICES)
    political_organization = forms.ChoiceField(choices=POLITICAL_ORG_CHOICES)

    class Meta:
        model = models.fillInBlanks_3
        fields = '__all__'

class FillInTheBlanks4(forms.ModelForm):

    SPORT_CHOICES = [
        ('baseball', 'baseball'), ('basketball', 'basketball'), ('boxing', 'boxing'),
        ('cricket', 'cricket'), ('cycling', 'cycling'), ('darts', 'darts'),
        ('diving', 'diving'), ('esports', 'esports'), ('field hockey', 'field hockey'),
        ('football', 'football'), ('golf', 'golf'), ('gymnastics', 'gymnastics'),
        ('hockey', 'hockey'), ('lacrosse', 'lacrosse'), ('poker', 'poker'),
        ('polo', 'polo'), ('rowing', 'rowing'), ('rugby', 'rugby'),
        ('skateboarding', 'skateboarding'), ('snowboarding', 'snowboarding'),
        ('soccer', 'soccer'), ('swimming', 'swimming'), ('tennis', 'tennis'),
        ('track', 'track'), ('volleyball', 'volleyball'), ('water polo', 'water polo'),
        ('wrestling', 'wrestling')
    ]

    BRAND_CHOICES = [
        ('Cap’n Crunch', 'Cap’n Crunch'), ('Coca-Cola', 'Coca-Cola'), ('Fruity Pebbles', 'Fruity Pebbles'),
        ('Gatorade', 'Gatorade'), ('Hi-C', 'Hi-C'), ('ICEE', 'ICEE'),
        ('Kool-Aid', 'Kool-Aid'), ('Little Debbie’s', 'Little Debbie’s'), ('M&Ms', 'M&Ms'),
        ('Monster Energy', 'Monster Energy'), ('Pop Tarts', 'Pop Tarts'), ('Powerade', 'Powerade'),
        ('Pringles', 'Pringles'), ('Red Bull', 'Red Bull'), ('Skittles', 'Skittles'),
        ('Snapple', 'Snapple'), ('SunnyD', 'SunnyD'), ('Twinkies', 'Twinkies')
    ]

    FEELING_CHOICES = [
        ('annoying', 'annoying'), ('appalling', 'appalling'), ('astonishing', 'astonishing'),
        ('charming', 'charming'), ('confusing', 'confusing'), ('crippling', 'crippling'),
        ('depressing', 'depressing'), ('disturbing', 'disturbing'), ('embarrassing', 'embarrassing'),
        ('exciting', 'exciting'), ('frightening', 'frightening'), ('frustrating', 'frustrating'),
        ('gratifying', 'gratifying'), ('humiliating', 'humiliating'), ('inspiring', 'inspiring'),
        ('overwhelming', 'overwhelming'), ('relaxing', 'relaxing'), ('rewarding', 'rewarding'),
        ('scintillating', 'scintillating'), ('shocking', 'shocking'), ('thrilling', 'thrilling'),
        ('wowing', 'wowing'), ('wondering', 'wondering')
    ]

    YEAR_CHOICES = [(str(year), str(year)) for year in range(1990, 2021)]

    EVENT_CHOICES = [
        ('Academy Awards', 'Academy Awards'), ('Burning Man Festival', 'Burning Man Festival'),
        ('Coachella Valley Festival', 'Coachella Valley Festival'), ('D23 Expo', 'D23 Expo'),
        ('ESPY Awards', 'ESPY Awards'), ('Faster Horses Festival', 'Faster Horses Festival'),
        ('Golden Globe Awards', 'Golden Globe Awards'), ('Grammy Awards', 'Grammy Awards'),
        ('Lollapalooza', 'Lollapalooza'), ('Met Gala', 'Met Gala'), ('MTV Video Music Awards', 'MTV Video Music Awards'),
        ('People’s Choice Awards', 'People’s Choice Awards'), ('San Diego Comic-Con', 'San Diego Comic-Con'),
        ('Sundance Film Festival', 'Sundance Film Festival'), ('Super Bowl', 'Super Bowl')
    ]

    MEDICAL_PROVIDER_CHOICES = [
        ('allergist', 'allergist'), ('athletic trainer', 'athletic trainer'), ('cardiologist', 'cardiologist'),
        ('chiropractor', 'chiropractor'), ('dentist', 'dentist'), ('dermatologist', 'dermatologist'),
        ('dietician', 'dietician'), ('endocrinologist', 'endocrinologist'), ('exercise physiologist', 'exercise physiologist'),
        ('gastroenterologist', 'gastroenterologist'), ('internist', 'internist'), ('massage therapist', 'massage therapist'),
        ('nephrologist', 'nephrologist'), ('neurologist', 'neurologist'), ('orthopedist', 'orthopedist'),
        ('ophthalmologist', 'ophthalmologist'), ('pulmonologist', 'pulmonologist'),
        ('primary care physician', 'primary care physician'), ('physical therapist', 'physical therapist'),
        ('podiatrist', 'podiatrist'), ('psychiatrist', 'psychiatrist'), ('rheumatologist', 'rheumatologist'),
        ('urologist', 'urologist')
    ]

    NUMBER_CHOICES = [(str(i), str(i)) for i in range(1, 11)]

    MEDIA_COMPANY_CHOICES = [
        ('The Athletic', 'The Athletic'), ('The Atlantic', 'The Atlantic'), ('Bleacher Report', 'Bleacher Report'),
        ('The Daily Show', 'The Daily Show'), ('ESPN Magazine', 'ESPN Magazine'), ('Esquire', 'Esquire'),
        ('Forbes', 'Forbes'), ('Good Morning America', 'Good Morning America'), ('GQ', 'GQ'),
        ('The Guardian', 'The Guardian'), ('The Herd with Colin Cowherd', 'The Herd with Colin Cowherd'),
        ('InfoWars', 'InfoWars'), ('The Joe Rogan Experience', 'The Joe Rogan Experience'),
        ('The Late Show with Stephen Colbert', 'The Late Show with Stephen Colbert'),
        ('The New York Times', 'The New York Times'), ('Los Angeles Times', 'Los Angeles Times'),
        ('National Geographic', 'National Geographic'), ('Pardon My Take', 'Pardon My Take'),
        ('The Pat McAfee Show', 'The Pat McAfee Show'), ('People', 'People'),
        ('Rolling Stone', 'Rolling Stone'), ('TIME', 'TIME'), ('Sports Illustrated', 'Sports Illustrated'),
        ('USA Today', 'USA Today'), ('The Washington Post', 'The Washington Post')
    ]

    DISEASE_CHOICES = [
        ('ADHD', 'ADHD'), ('alopecia', 'alopecia'), ('Alzheimer’s disease', 'Alzheimer’s disease'),
        ('anxiety', 'anxiety'), ('arthritis', 'arthritis'), ('autism', 'autism'), ('cancer', 'cancer'),
        ('dementia', 'dementia'), ('dental cavities', 'dental cavities'), ('depression', 'depression'),
        ('diabetes', 'diabetes'), ('dyslexia', 'dyslexia'), ('epilepsy', 'epilepsy'),
        ('erectile dysfunction', 'erectile dysfunction'), ('glaucoma', 'glaucoma'),
        ('high blood pressure', 'high blood pressure'), ('hormone disruption', 'hormone disruption'),
        ('low testosterone', 'low testosterone'), ('male-pattern baldness', 'male-pattern baldness'),
        ('narcolepsy', 'narcolepsy'), ('obesity', 'obesity'), ('scoliosis', 'scoliosis'),
        ('Tourette syndrome', 'Tourette syndrome'), ('vitiligo', 'vitiligo')
    ]

    CITY_CHOICES = [
        ('Athens', 'Athens'), ('Auckland', 'Auckland'), ('Barcelona', 'Barcelona'), ('Berlin', 'Berlin'),
        ('Boston', 'Boston'), ('Brisbane', 'Brisbane'), ('Cairo', 'Cairo'), ('Chicago', 'Chicago'),
        ('Cleveland', 'Cleveland'), ('Dallas', 'Dallas'), ('Detroit', 'Detroit'), ('Helsinki', 'Helsinki'),
        ('Houston', 'Houston'), ('Jakarta', 'Jakarta'), ('London', 'London'), ('Los Angeles', 'Los Angeles'),
        ('Madrid', 'Madrid'), ('Montreal', 'Montreal'), ('Munich', 'Munich'), ('New York City', 'New York City'),
        ('Orlando', 'Orlando'), ('Oslo', 'Oslo'), ('Ottawa', 'Ottawa'), ('Paris', 'Paris'), ('Perth', 'Perth'),
        ('Phoenix', 'Phoenix'), ('Portland', 'Portland'), ('Rome', 'Rome'), ('San Antonio', 'San Antonio'),
        ('São Paolo', 'São Paolo'), ('Seattle', 'Seattle'), ('Seoul', 'Seoul'), ('Shanghai', 'Shanghai'),
        ('Stockholm', 'Stockholm'), ('Sydney', 'Sydney'), ('Tokyo', 'Tokyo'), ('Toronto', 'Toronto'),
        ('Vancouver', 'Vancouver'), ('Venice', 'Venice')
    ]

    # Form definition
    
    sport = forms.ChoiceField(choices=SPORT_CHOICES)
    brand = forms.ChoiceField(choices=BRAND_CHOICES)
    feeling = forms.ChoiceField(choices=FEELING_CHOICES)
    year = forms.ChoiceField(choices=YEAR_CHOICES)
    event = forms.ChoiceField(choices=EVENT_CHOICES)
    medical_provider = forms.ChoiceField(choices=MEDICAL_PROVIDER_CHOICES)
    number = forms.ChoiceField(choices=NUMBER_CHOICES)
    media_company = forms.ChoiceField(choices=MEDIA_COMPANY_CHOICES)
    disease_1 = forms.ChoiceField(choices=DISEASE_CHOICES)
    disease_2 = forms.ChoiceField(choices=DISEASE_CHOICES)
    city = forms.ChoiceField(choices=CITY_CHOICES)

    class Meta:
        model = models.fillInBlanks_4
        fields = '__all__'

class FillInTheBlanks5(forms.ModelForm):

    SPORTING_EVENT_CHOICES = [
        ('American Ninja Warrior', 'American Ninja Warrior'),
        ('Champions League Final', 'Champions League Final'),
        ('Cooper’s Hill Cheese Rolling Race', 'Cooper’s Hill Cheese Rolling Race'),
        ('Daytona 500', 'Daytona 500'), ('Iditarod', 'Iditarod'), ('Indianapolis 500', 'Indianapolis 500'),
        ('Jeopardy! Tournament of Champions', 'Jeopardy! Tournament of Champions'),
        ('Kentucky Derby', 'Kentucky Derby'), ('Masters', 'Masters'),
        ('Miss Universe Pageant', 'Miss Universe Pageant'),
        ('Nathan’s Hot Dog Eating Contest', 'Nathan’s Hot Dog Eating Contest'),
        ('NBA Finals', 'NBA Finals'), ('Preakness Stakes', 'Preakness Stakes'),
        ('Running of the Bulls', 'Running of the Bulls'),
        ('Scripps National Spelling Bee', 'Scripps National Spelling Bee'),
        ('Stanley Cup Playoff', 'Stanley Cup Playoff'), ('Super Bowl', 'Super Bowl'),
        ('Tour de France', 'Tour de France'), ('Wimbledon', 'Wimbledon'),
        ('Westminster Dog Show', 'Westminster Dog Show'), ('World Series', 'World Series')
    ]

    GOVERNMENT_ROLE_CHOICES = [
        ('ambassador', 'ambassador'), ('chancellor', 'chancellor'), ('count', 'count'),
        ('countess', 'countess'), ('crown prince', 'crown prince'), ('crown princess', 'crown princess'),
        ('dictator', 'dictator'), ('duchess', 'duchess'), ('duke', 'duke'), ('emperor', 'emperor'),
        ('empress', 'empress'), ('governor', 'governor'), ('king', 'king'), ('mayor', 'mayor'),
        ('minister', 'minister'), ('monarch', 'monarch'), ('premier', 'premier'), ('president', 'president'),
        ('prime minister', 'prime minister'), ('queen', 'queen'), ('sultan', 'sultan'), ('viceroy', 'viceroy')
    ]

    EX_MONARCHY_CHOICES = [
        ('Afghanistan', 'Afghanistan'), ('Albania', 'Albania'), ('Austria', 'Austria'), ('Bosnia', 'Bosnia'),
        ('Brazil', 'Brazil'), ('Bulgaria', 'Bulgaria'), ('China', 'China'), ('Cyprus', 'Cyprus'),
        ('Egypt', 'Egypt'), ('Ethiopia', 'Ethiopia'), ('Finland', 'Finland'), ('France', 'France'),
        ('Georgia', 'Georgia'), ('Germany', 'Germany'), ('Ghana', 'Ghana'), ('Greece', 'Greece'),
        ('Haiti', 'Haiti'), ('Hungary', 'Hungary'), ('Iceland', 'Iceland'), ('Indonesia', 'Indonesia'),
        ('Iran', 'Iran'), ('Iraq', 'Iraq'), ('Ireland', 'Ireland'), ('Italy', 'Italy'), ('Laos', 'Laos'),
        ('Libya', 'Libya'), ('Madagascar', 'Madagascar'), ('Maldives', 'Maldives'), ('Mali', 'Mali'),
        ('Mongolia', 'Mongolia'), ('Nepal', 'Nepal'), ('Portugal', 'Portugal'), ('Romania', 'Romania'),
        ('Russia', 'Russia'), ('Rwanda', 'Rwanda'), ('Scotland', 'Scotland'), ('Serbia', 'Serbia'),
        ('Sri Lanka', 'Sri Lanka'), ('Suriname', 'Suriname'), ('Taiwan', 'Taiwan'), ('Tibet', 'Tibet'),
        ('Trinidad and Tobago', 'Trinidad and Tobago'), ('Tunisia', 'Tunisia'), ('Vietnam', 'Vietnam'),
        ('Yemen', 'Yemen'), ('Zanzibar', 'Zanzibar'), ('Zimbabwe', 'Zimbabwe')
    ]

    US_STATE_CHOICES = [
        ('AL', 'Alabama'), ('AK', 'Alaska'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA', 'California'),
        ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('FL', 'Florida'), ('GA', 'Georgia'),
        ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'),
        ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'),
        ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'),
        ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'),
        ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'),
        ('ND', 'North Dakota'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'),
        ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'),
        ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VA', 'Virginia'), ('WA', 'Washington'),
        ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming')
    ]

    NAME_CHOICES = [
        ('Aisha', 'Aisha'), ('Anya', 'Anya'), ('Bailey', 'Bailey'), ('Chloe', 'Chloe'), ('Cynthia', 'Cynthia'),
        ('David', 'David'), ('Diego', 'Diego'), ('Emmanuel', 'Emmanuel'), ('Fatima', 'Fatima'),
        ('Gerald', 'Gerald'), ('Harold', 'Harold'), ('Hiroshi', 'Hiroshi'), ('Isabella', 'Isabella'),
        ('Javier', 'Javier'), ('Kenji', 'Kenji'), ('Kwame', 'Kwame'), ('Lena', 'Lena'), ('Liam', 'Liam'),
        ('Marcus', 'Marcus'), ('Mateo', 'Mateo'), ('Mei', 'Mei'), ('Nadia', 'Nadia'), ('Omar', 'Omar'),
        ('Priya', 'Priya'), ('Samuel', 'Samuel'), ('Sofia', 'Sofia'), ('Stacey', 'Stacey'), ('Thomas', 'Thomas')
    ]

    VEGETABLE_CHOICES = [
        ('bell pepper', 'bell pepper'), ('black bean', 'black bean'), ('Carolina Reaper', 'Carolina Reaper'),
        ('carrot', 'carrot'), ('cayenne pepper', 'cayenne pepper'), ('celery', 'celery'),
        ('cherry tomato', 'cherry tomato'), ('chili pepper', 'chili pepper'), ('corn', 'corn'),
        ('edamame', 'edamame'), ('eggplant', 'eggplant'), ('ghost pepper', 'ghost pepper'),
        ('green bean', 'green bean'), ('green onion', 'green onion'), ('habañero pepper', 'habañero pepper'),
        ('Hatch chile', 'Hatch chile'), ('jalapeño', 'jalapeño'), ('kidney bean', 'kidney bean'),
        ('lentil', 'lentil'), ('pinto bean', 'pinto bean'), ('tomatillo', 'tomatillo'),
        ('sweet onion', 'sweet onion'), ('sweet potato', 'sweet potato'), ('tomato', 'tomato'),
        ('zucchini', 'zucchini')
    ]

    SOCIAL_MEDIA_CHOICES = [
        ('AOL Instant Messenger', 'AOL Instant Messenger'), ('BeReal', 'BeReal'), ('Bluesky', 'Bluesky'),
        ('Discord', 'Discord'), ('Facebook', 'Facebook'), ('Gab', 'Gab'), ('Hive Social', 'Hive Social'),
        ('Instagram', 'Instagram'), ('Mastodon', 'Mastodon'), ('MySpace', 'MySpace'), ('Parler', 'Parler'),
        ('Pinterest', 'Pinterest'), ('Quora', 'Quora'), ('Reddit', 'Reddit'), ('Snapchat', 'Snapchat'),
        ('Threads', 'Threads'), ('TikTok', 'TikTok'), ('Truth Social', 'Truth Social'), ('Tumblr', 'Tumblr'),
        ('Vine', 'Vine'), ('X', 'X')
    ]

    sporting_event = forms.ChoiceField(choices=SPORTING_EVENT_CHOICES)
    government_role = forms.ChoiceField(choices=GOVERNMENT_ROLE_CHOICES)
    monarchal_country = forms.ChoiceField(choices=EX_MONARCHY_CHOICES)
    US_state = forms.ChoiceField(choices=US_STATE_CHOICES)
    name_1 = forms.ChoiceField(choices=NAME_CHOICES)
    name_2 = forms.ChoiceField(choices=NAME_CHOICES)
    vegetable = forms.ChoiceField(choices=VEGETABLE_CHOICES)
    social_media_1 = forms.ChoiceField(choices=SOCIAL_MEDIA_CHOICES)
    social_media_2 = forms.ChoiceField(choices=SOCIAL_MEDIA_CHOICES)

    class Meta:
        model = models.fillInBlanks_5
        fields = '__all__'

class FillInTheBlanks6(forms.ModelForm):

    EMOTION_CHOICES = [
        ('amusing', 'amusing'), ('angering', 'angering'), ('astonishing', 'astonishing'),
        ('bewildering', 'bewildering'), ('charming', 'charming'), ('cheering', 'cheering'),
        ('comforting', 'comforting'), ('criticizing', 'criticizing'), ('deflating', 'deflating'),
        ('delighting', 'delighting'), ('depressing', 'depressing'), ('disgusting', 'disgusting'),
        ('disheartening', 'disheartening'), ('disturbing', 'disturbing'), ('embarrassing', 'embarrassing'),
        ('empowering', 'empowering'), ('enraging', 'enraging'), ('exciting', 'exciting'),
        ('frustrating', 'frustrating'), ('gratifying', 'gratifying'), ('humiliating', 'humiliating'),
        ('inspiring', 'inspiring'), ('intimidating', 'intimidating'), ('irritating', 'irritating'),
        ('motivating', 'motivating'), ('offending', 'offending'), ('overwhelming', 'overwhelming'),
        ('provoking', 'provoking'), ('relaxing', 'relaxing'), ('scaring', 'scaring'),
        ('shocking', 'shocking'), ('soothing', 'soothing'), ('uplifting', 'uplifting'),
    ]

    US_STATE_CHOICES = [
        ('AL', 'Alabama'), ('AK', 'Alaska'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA', 'California'),
        ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('FL', 'Florida'), ('GA', 'Georgia'),
        ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'),
        ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'),
        ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'),
        ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'),
        ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'),
        ('ND', 'North Dakota'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'),
        ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'),
        ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VA', 'Virginia'), ('WA', 'Washington'),
        ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming')
    ]

    FRATERNITY_CHOICES = [
        ('Alpha Delta Theta (ΑΔΘ)', 'Alpha Delta Theta (ΑΔΘ)'), ('Alpha Epsilon Pi (ΑΕΠ)', 'Alpha Epsilon Pi (ΑΕΠ)'),
        ('Alpha Gamma Rho (ΑΓΡ)', 'Alpha Gamma Rho (ΑΓΡ)'), ('Alpha Kappa Psi (ΑΚΨ)', 'Alpha Kappa Psi (ΑΚΨ)'),
        ('Alpha Sigma Phi (ΑΣΦ)', 'Alpha Sigma Phi (ΑΣΦ)'), ('Beta Eta Mu (ΒΗΜ)', 'Beta Eta Mu (ΒΗΜ)'),
        ('Beta Theta Pi (ΒΘΠ)', 'Beta Theta Pi (ΒΘΠ)'), ('Gamma Lambda Sigma (ΓΛΣ)', 'Gamma Lambda Sigma (ΓΛΣ)'),
        ('Delta Gamma Rho (ΔΓΡ)', 'Delta Gamma Rho (ΔΓΡ)'), ('Delta Kappa Epsilon (ΔΚΕ)', 'Delta Kappa Epsilon (ΔΚΕ)'),
        ('Delta Sigma Pi (ΔΣΚ)', 'Delta Sigma Pi (ΔΣΚ)'), ('Epsilon Mu Theta (ΕΜΘ)', 'Epsilon Mu Theta (ΕΜΘ)'),
        ('Zeta Beta Tau (ΖΒΤ)', 'Zeta Beta Tau (ΖΒΤ)'), ('Eta Lambda Nu (ΗΛΝ)', 'Eta Lambda Nu (ΗΛΝ)'),
        ('Theta Delta Chi (ΘΔΧ)', 'Theta Delta Chi (ΘΔΧ)'), ('Iota Sigma Tau (ΙΣΤ)', 'Iota Sigma Tau (ΙΣΤ)'),
        ('Kappa Alpha Psi (ΚΑΨ)', 'Kappa Alpha Psi (ΚΑΨ)'), ('Lambda Phi Epsilon (ΛΦΕ)', 'Lambda Phi Epsilon (ΛΦΕ)'),
        ('Lambda Theta Phi (ΤΘΦ)', 'Lambda Theta Phi (ΤΘΦ)'), ('Mu Epsilon Beta (ΜΒΕ)', 'Mu Epsilon Beta (ΜΒΕ)'),
        ('Nu Upsilon Psi (ΝΥΨ)', 'Nu Upsilon Psi (ΝΥΨ)'), ('Xi Omega Chi (ΞΩΧ)', 'Xi Omega Chi (ΞΩΧ)'),
        ('Xi Rho Zeta (ΞΠΖ)', 'Xi Rho Zeta (ΞΠΖ)'), ('Omicron Psi Omega (ΟΨΩ)', 'Omicron Psi Omega (ΟΨΩ)'),
        ('Pi Kappa Sigma (ΠΚΣ)', 'Pi Kappa Sigma (ΠΚΣ)'), ('Pi Kappa Alpha (ΠΚΑ)', 'Pi Kappa Alpha (ΠΚΑ)'),
        ('Pi Kappa Phi (ΠΚΦ)', 'Pi Kappa Phi (ΠΚΦ)'), ('Rho Phi Psi (ΡΦΨ)', 'Rho Phi Psi (ΡΦΨ)'),
        ('Sigma Alpha Epsilon (ΣΑΕ)', 'Sigma Alpha Epsilon (ΣΑΕ)'), ('Sigma Alpha Mu (ΣΑΜ)', 'Sigma Alpha Mu (ΣΑΜ)'),
        ('Sigma Lambda Beta (ΣΛΒ)', 'Sigma Lambda Beta (ΣΛΒ)'), ('Sigma Tau Gamma (ΣΤΓ)', 'Sigma Tau Gamma (ΣΤΓ)'),
        ('Tau Kappa Epsilon (ΤΚΕ)', 'Tau Kappa Epsilon (ΤΚΕ)'), ('Upsilon Delta Eta (ΥΔΗ)', 'Upsilon Delta Eta (ΥΔΗ)'),
        ('Phi Beta Sigma (ΦΒΣ)', 'Phi Beta Sigma (ΦΒΣ)'), ('Phi Delta Theta (ΦΔΘ)', 'Phi Delta Theta (ΦΔΘ)'),
        ('Phi Gamma Delta (ΦΓΔ)', 'Phi Gamma Delta (ΦΓΔ)'), ('Phi Iota Alpha (ΦΙΑ)', 'Phi Iota Alpha (ΦΙΑ)'),
        ('Phi Kappa Sigma (ΦΚΣ)', 'Phi Kappa Sigma (ΦΚΣ)'), ('Chi Delta Pi (ΧΔΠ)', 'Chi Delta Pi (ΧΔΠ)'),
        ('Psi Lambda Rho (ΨΛΡ)', 'Psi Lambda Rho (ΨΛΡ)'), ('Omega Psi Phi (ΩΨΦ)', 'Omega Psi Phi (ΩΨΦ)')
    ]

    NON_PROFIT_CHOICES = [
        ('American Cancer Society', 'American Cancer Society'),
        ('American Civil Liberties Union (ACLU)', 'American Civil Liberties Union (ACLU)'),
        ('American Red Cross', 'American Red Cross'),
        ('American Society for the Prevention of Cruelty to Animals (ASPCA)', 'American Society for the Prevention of Cruelty to Animals (ASPCA)'),
        ('Amnesty International USA', 'Amnesty International USA'),
        ('Boys and Girls Clubs of America', 'Boys and Girls Clubs of America'),
        ('Boy Scouts of America', 'Boy Scouts of America'),
        ('Environmental Defense Fund', 'Environmental Defense Fund'),
        ('Everytown for Gun Safety', 'Everytown for Gun Safety'),
        ('Feeding America', 'Feeding America'),
        ('Girl Scouts of the USA', 'Girl Scouts of the USA'),
        ('Habitat for Humanity', 'Habitat for Humanity'),
        ('Heritage Foundation', 'Heritage Foundation'),
        ('Make-A-Wish Foundation', 'Make-A-Wish Foundation'),
        ('Meals on Wheels America', 'Meals on Wheels America'),
        ('Natural Resources Defense Council (NRDC)', 'Natural Resources Defense Council (NRDC)'),
        ('People for the Ethical Treatment of Animals (PETA)', 'People for the Ethical Treatment of Animals (PETA)'),
        ('Planned Parenthood Federation of America', 'Planned Parenthood Federation of America'),
        ('Scouting America', 'Scouting America'),
        ('Sierra Club Foundation', 'Sierra Club Foundation'),
        ('Special Olympics USA', 'Special Olympics USA'),
        ('St. Jude Children’s Research Hospital', 'St. Jude Children’s Research Hospital'),
        ('The Salvation Army USA', 'The Salvation Army USA'),
        ('United Way Worldwide', 'United Way Worldwide'),
        ('World Wildlife Fund (WWF)', 'World Wildlife Fund (WWF)')
    ]

    NAME_1_CHOICES = [(name, name) for name in [
        'Alan', 'Albert', 'Arthur', 'Billy', 'Bruce', 'Carl', 'Charles', 'Daniel', 'David', 'Donald',
        'Dennis', 'Edward', 'Eldon', 'Eugene', 'Frank', 'Frederick', 'Gary', 'George', 'Gerald', 'Harold',
        'Henry', 'Howard', 'Irving', 'Isaac', 'Jack', 'James', 'John', 'Joseph', 'Kenneth', 'Keith',
        'Larry', 'Leonard', 'Martin', 'Michael', 'Morty', 'Neil', 'Norman', 'Oscar', 'Orville', 'Paul',
        'Peter', 'Phillip', 'Ralph', 'Raymond', 'Richard', 'Robert', 'Roger', 'Ronald', 'Roy', 'Samuel',
        'Stephen', 'Terry', 'Theodore', 'Thomas', 'Walter', 'Wayne', 'William'
    ]]

    NAME_2_CHOICES = [(name, name) for name in [
        'Aaron', 'Aiden', 'Andrew', 'Bradley', 'Brandon', 'Caleb', 'Calvin', 'Cameron', 'Carter', 'Chris',
        'Dominic', 'Dustin', 'Dylan', 'Elliott', 'Elijah', 'Ethan', 'Gabe', 'Gavin', 'Grayson', 'Hunter',
        'Hayden', 'Isaac', 'Ian', 'Jacob', 'Jason', 'Jordan', 'Josh', 'Justin', 'Kevin', 'Kyle',
        'Landon', 'Logan', 'Lucas', 'Luke', 'Marcus', 'Mason', 'Matthew', 'Nate', 'Nick', 'Noah',
        'Oliver', 'Owen', 'Parker', 'Patrick', 'Riley', 'Ryan', 'Sean', 'Skylar', 'Tucker', 'Tyler',
        'Victor', 'Vincent', 'Walker', 'Wyatt', 'Xavier', 'Zack'
    ]]

    COLLEGE_MAJOR_CHOICES = [(major, major) for major in [
        'accounting', 'anthropology', 'architecture', 'biology', 'biomedical engineering', 'business',
        'chemical engineering', 'chemistry', 'civil engineering', 'data science', 'dietetics',
        'communications', 'computer science', 'criminal justice', 'cybersecurity', 'economics',
        'education', 'electrical engineering', 'English literature', 'environmental engineering',
        'environmental studies', 'film studies', 'finance', 'foreign language studies', 'graphic design',
        'healthcare administration', 'history', 'hospitality', 'human resources', 'information technology',
        'international relations', 'journalism', 'kinesiology', 'marketing', 'math', 'mechanical engineering',
        'museum studies', 'music performance', 'neuroscience', 'nursing', 'philosophy', 'physics',
        'political science', 'product design', 'psychology', 'public health', 'social work', 'sociology',
        'theater', 'zoology'
    ]]

    emotion = forms.ChoiceField(choices=EMOTION_CHOICES)
    US_state = forms.ChoiceField(choices=US_STATE_CHOICES)
    Fraternity = forms.ChoiceField(choices=FRATERNITY_CHOICES)
    non_profit_agency = forms.ChoiceField(choices=NON_PROFIT_CHOICES)
    number_1 = forms.CharField(
    label="Number 1",
    widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter a number'
    }),
    error_messages={'invalid': 'Enter numbers only.'}
    )
    number_2 = forms.CharField(
    label="Number 2",
    widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter a number'
    }),
    error_messages={'invalid': 'Enter numbers only.'}
    )
    number_3 =  forms.CharField(
    label="Number 3",
    widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter a number'
    }),
    error_messages={'invalid': 'Enter numbers only.'}
    )
    name_1 = forms.ChoiceField(choices=NAME_1_CHOICES)
    name_2 = forms.ChoiceField(choices=NAME_2_CHOICES)
    college_major = forms.ChoiceField(choices=COLLEGE_MAJOR_CHOICES)

    class Meta:
        model = models.fillInBlanks_6
        fields = '__all__'

class FillInTheBlanks8(forms.ModelForm):

    EMOTION_CHOICES = [(e, e) for e in [
        'admiration', 'amusement', 'anger', 'anxiety', 'awe', 'boredom', 'chaos', 'compassion', 'confidence',
        'confusion', 'contentment', 'disgust', 'ecstasy', 'elation', 'embarrassment', 'envy', 'excitement', 'fear',
        'frustration', 'fury', 'gratitude', 'grief', 'guilt', 'happiness', 'hope', 'joy', 'loneliness', 'love',
        'pride', 'rage', 'regret', 'sadness', 'shame', 'surprise', 'terror', 'trust', 'worry', 'yearning', 'zeal'
    ]]

    LAST_NAME_CHOICES = [(l, l) for l in [
        'Adams', 'Arthur', 'Biden', 'Buchanan', 'Bush', 'Carter', 'Cleveland', 'Clinton', 'Coolidge', 'Eisenhower',
        'Fillmore', 'Ford', 'Garfield', 'Grant', 'Harding', 'Harrison', 'Hayes', 'Hoover', 'Jackson', 'Johnson',
        'Kennedy', 'Lincoln', 'Madison', 'McKinley', 'Monroe', 'Nixon', 'Obama', 'Pierce', 'Polk', 'Reagan',
        'Roosevelt', 'Taft', 'Taylor', 'Truman', 'Trump', 'Tyler', 'Van Buren', 'Washington', 'Wilson'
    ]]

    STATE_CAPITAL_CHOICES = [(c, c) for c in [
        'Albany, NY', 'Annapolis, MD', 'Atlanta, GA', 'Augusta, ME', 'Austin, TX', 'Baton Rouge, LA', 'Bismarck, ND',
        'Boise, ID', 'Boston, MA', 'Carson City, NV', 'Charleston, WV', 'Cheyenne, WY', 'Columbia, SC', 'Columbus, OH',
        'Concord, NH', 'Denver, CO', 'Des Moines, IA', 'Dover, DE', 'Frankfort, KY', 'Harrisburg, PA', 'Hartford, CT',
        'Helena, MY', 'Honolulu, HI', 'Indianapolis, IN', 'Jackson, MS', 'Jefferson City, MO', 'Juneau, AK',
        'Lansing, MI', 'Lincoln, NE', 'Little Rock, AR', 'Madison, WI', 'Montgomery, AL', 'Montpelier, VT',
        'Nashville, TN', 'Oklahoma City, OK', 'Olympia, WA', 'Phoenix, AZ', 'Pierre, SD', 'Providence, RI',
        'Raleigh, NC', 'Richmond, VA', 'Sacramento, VA', 'St. Paul, MN', 'Salem, OR', 'Salt Lake City, UT',
        'Santa Fe, NM', 'Springfield, IL', 'Tallahassee, FL', 'Topeka, KS', 'Trenton, NJ'
    ]]

    PAST_TENSE_EMOTION_CHOICES = [(p, p) for p in [
        'admired', 'agitated', 'amazed', 'amused', 'angered', 'annoyed', 'anxious', 'awake', 'bewildered', 'bored',
        'burnt', 'confused', 'dead', 'delighted', 'disappointed', 'disgraced', 'disheveled', 'distressed',
        'embarrassed', 'excited', 'felt', 'freed', 'frustrated', 'grateful', 'hopeful', 'jealous', 'known', 'lonely',
        'lost', 'misplaced', 'oppressed', 'overcome', 'overwhelmed', 'relaxed', 'relieved', 'satisfied', 'saved',
        'shaken', 'shocked', 'silenced', 'stained', 'startled', 'surprised', 'terrified', 'tired', 'violated', 'worn'
    ]]

    SOCIAL_MEDIA_CHOICES = [(s, s) for s in [
        'AOL Instant Messenger', 'BeReal', 'Bluesky', 'Discord', 'Facebook', 'Gab', 'Hive Social', 'Instagram',
        'Mastodon', 'MySpace', 'Parler', 'Pinterest', 'Quora', 'Reddit', 'Snapchat', 'Threads', 'TikTok',
        'Truth Social', 'Tumblr', 'Vine', 'X'
    ]]

    SCHOOL_CLASS_CHOICES = [(s, s) for s in [
        'accounting', 'algebra', 'band', 'biology', 'business education', 'calculus', 'chemistry', 'choir', 'civics',
        'computer science', 'construction', 'drama', 'economics', 'English literature', 'French', 'geometry',
        'German', 'health', 'home economics', 'journalism', 'physics', 'psychology', 'sociology', 'Spanish',
        'statistics', 'U.S. history', 'world history'
    ]]

    MASCOT_CHOICES = [(m, m) for m in [
        'Bear', 'Bobcat', 'Bronco', 'Bulldog', 'Charger', 'Colt', 'Comet', 'Cougar', 'Coyote', 'Crusader', 'Eagle',
        'Falcon', 'Griffin', 'Grizzlies', 'Hawk', 'Hornet', 'Jaguar', 'Knight', 'Lion', 'Mustang', 'Panther',
        'Pioneer', 'Pirate', 'Ram', 'Raider', 'Shark', 'Spartan', 'Tiger', 'Trojan', 'Wildcat', 'Wolf'
    ]]

    NAME_CHOICES = [(n, n) for n in [
        'Abby', 'Addison', 'Alexis', 'Allison', 'Alyssa', 'Anna', 'Audrey', 'Avaleigh', 'Avery', 'Bailey', 'Becca',
        'Bella', 'Brayleigh', 'Brooklyn', 'Camrynn', 'Catherine', 'Chloe', 'Delynn', 'Elizabeth', 'Ella', 'Emersyn',
        'Emily', 'Emma', 'Evelyn', 'Freyja', 'Gabriella', 'Gracie', 'Gracyn', 'Hailey', 'Harlynn', 'Izabellah',
        'Jazzmyn', 'Jordan', 'Julia', 'Katherine', 'Kaydence', 'Kayla', 'Lauren', 'Lily', 'Londynn', 'Madison', 'Mia',
        'Morgan', 'Mya', 'Mylani', 'Natalie', 'Nevaeh', 'Nylaa', 'Oaklynn', 'Olivia', 'Paislee', 'Quinlyn', 'Rachel',
        'Raelynn', 'Rebecca', 'Samantha', 'Sara', 'Sarah', 'Sierra', 'Sophia', 'Sydnee', 'Taylor', 'Tinsleigh',
        'Vaylee', 'Waverleigh', 'Xavrielle', 'Zaelynn'
    ]]

    LAWN_GAME_CHOICES = [(g, g) for g in [
        'badminton', 'bocce ball', 'cornhole', 'croquet', 'disc golf', 'dodgeball', 'four square', 'giant Connect Four',
        'Giant Jenga', 'hacky sack', 'horseshoes', 'KanJam', 'kickball', 'ladder ball', 'lawn darts', 'limbo',
        'noodle tag', 'spikeball', 'ultimate frisbee'
    ]]

    emotion = forms.ChoiceField(choices=EMOTION_CHOICES)
    last_name = forms.ChoiceField(choices=LAST_NAME_CHOICES)
    US_State_Capital = forms.ChoiceField(choices=STATE_CAPITAL_CHOICES)
    past_tense_emotion = forms.ChoiceField(choices=PAST_TENSE_EMOTION_CHOICES)
    social_media = forms.ChoiceField(choices=SOCIAL_MEDIA_CHOICES)
    school_class = forms.ChoiceField(choices=SCHOOL_CLASS_CHOICES)
    school_mascot = forms.ChoiceField(choices=MASCOT_CHOICES)
    name = forms.ChoiceField(choices=NAME_CHOICES)
    lawn_game = forms.ChoiceField(choices=LAWN_GAME_CHOICES)

    class Meta:
        model = models.fillInBlanks_8
        fields = '__all__'