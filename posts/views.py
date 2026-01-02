from django.shortcuts import render, redirect
from .models import fillInBlanks_1, fillInBlanks_2, fillInBlanks_3, fillInBlanks_4, fillInBlanks_5, fillInBlanks_6, fillInBlanks_7, fillInBlanks_8
from . import forms
from django.http import HttpResponse
from django.db.models import Count
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
import myproject.views as views
# Create your views here.

STORY_MODELS = {
    1: 'fillInBlanks_1',
    2: 'fillInBlanks_2',
    3: 'fillInBlanks_3',
    4: 'fillInBlanks_4',
    5: 'fillInBlanks_5',
    6: 'fillInBlanks_6',
    7: 'fillInBlanks_8'
}

def send_email_url(request):
    if request.method == "POST":
        email = request.POST.get("email")
        story_url = request.build_absolute_uri()  
        send_mail(
            "Your Spin The Story Report",
            f"Here's your generated story: {story_url}",
            "noreply@yourdomain.com",
            [email],
            fail_silently=False,
        )
        return redirect("/")
    
def fill_in_blanks_1(request):
    if request.method == "POST":
        form = forms.FillInBlanksForm(request.POST)
        if form.is_valid():
            form.save()  
            return render(request, 'posts/post_page.html', {'form': form.cleaned_data})
        else:
            return HttpResponse("Form is not valid", status=400)

    else:
        form = forms.FillInBlanksForm()
    return render(request, 'posts/story_1.html', {'form': form })

def most_common(model, field):
    return(
        model.objects
        .values(field)
        .annotate(c=Count(field))
        .order_by('-c')
        .first()
    )

def unique_submission_count(model):
    return int(model.objects.values('idname').distinct().count())

def fill_in_blanks_generated(request):
    stories = []

    story1_fields = [
        'emotion_1', 'adjective_1', 'US_state', 'number_1', 'past_tense_verb_1',
        'social_media', 'number_2', 'past_tense_verb_2', 'political_organization_1',
        'adjective_2', 'group_of_people', 'political_organization_2', 'verb_ing',
        'past_tense_emotion', 'name', 'age', 'political_issue', 'Adjective_3', 'Adjective_4'
    ]

    story1_values = {}
    for field in story1_fields:
        result = most_common(fillInBlanks_1, field)
        story1_values[field] = result[field] if result else "--"
    
    stories.append({
        "id": 1,
        "title": f"{story1_values['emotion_1']} on Election Night!",
        "values": story1_values,
        "submission_count": unique_submission_count(fillInBlanks_1),
        })
    
    story2_fields = [
        'country_1','country_2', 'political_organization', 'social_media', 'product',
        'government_role', 'endearment', 'noun', 'group_of_people', 'plural_noun',
        'weapon', 'name_1', 'name_2'
    ]

    story2_values = {}
    for field in story2_fields:
        result = most_common(fillInBlanks_2, field)
        story2_values[field] = result[field] if result else "--"
    
    stories.append({
        "id": 2,
        "title": f"Invasion in {story2_values['country_1']}!",
        "values": story2_values,
        "submission_count": unique_submission_count(fillInBlanks_2),
        })
    
    story3_fields = [
    'natural_disaster',
    'feeling',
    'movement_1',
    'movement_2',
    'number',
    'farm_animal',
    'chain',
    'government_agency',
    'technology',
    'non_profit_agency',
    'adjective',
    'industry',
    'political_organization'
    ]

    story3_values = {}
    for field in story3_fields:
        result = most_common(fillInBlanks_3, field)
        story3_values[field] = result[field] if result else "--"

    stories.append({
        "id": 3,
        "title": f"{story3_values['natural_disaster'].title()} in South Carolina Leaves Town Reeling, Citizens Asking Questions.",
        "values": story3_values,
        "submission_count": unique_submission_count(fillInBlanks_3),
    })

    story4_fields = [
    'sport',
    'brand',
    'feeling',
    'year',
    'event',
    'medical_provider',
    'number',
    'media_company',
    'disease_1',
    'disease_2',
    'city'
    ]

    story4_values = {}
    for field in story4_fields:
        result = most_common(fillInBlanks_4, field)
        story4_values[field] = result[field] if result else "--"

    stories.append({
        "id": 4,
        "title": f"{story4_values['sport'].title()} Star, Zack “The Snack” Richards Diagnosed With Essential Tremor; Is {story4_values['brand'].title()} To Blame?",
        "values": story4_values,
        "submission_count": unique_submission_count(fillInBlanks_4),
    })
    story5_fields = [
    'sporting_event',
    'government_role',
    'monarchal_country',
    'US_state',
    'name_1',
    'name_2',
    'vegetable',
    'social_media_1',
    'social_media_2'
    ]

    story5_values = {}
    for field in story5_fields:
        result = most_common(fillInBlanks_5, field)
        story5_values[field] = result[field] if result else "--"

    stories.append({
        "id": 5,
        "title": (
            f"Illegal {story5_values['sporting_event'].title()} Gambling Ring Connections Drawn Between "
            f"Local Gardening Store, {story5_values['government_role'].title()} of "
            f"{story5_values['monarchal_country'].title()}."
            
        ),
        "values": story5_values,
        "submission_count": unique_submission_count(fillInBlanks_5),
    })

    story6_fields = [
    'emotion',
    'name_1',
    'number_3',
    'US_state',
    'Fraternity',
    'non_profit_agency',
    'number_1',
    'number_2',
    'name_2',
    'college_major'
    ]

    story6_values = {}
    for field in story6_fields:
        result = most_common(fillInBlanks_6, field)
        story6_values[field] = result[field] if result else "--"

    stories.append({
        "id": 6,
        "title": f"Fraternity members hold a charity run, {story6_values['emotion']} the senior community about the splash of color.",
        "values": story6_values,
        "submission_count": unique_submission_count(fillInBlanks_6),
    })

    story8_fields = [   
    'emotion',
    'US_State_Capital',
    'last_name',
    'past_tense_emotion',
    'social_media',
    'school_class',
    'school_mascot',
    'name',
    'lawn_game'
    ]

    story8_values = {}
    for field in story8_fields:
        result = most_common(fillInBlanks_8, field)
        story8_values[field] = result[field] if result else "--"

    stories.append({
        "id": 7,
        "title": f"New technology rules at local high school causes {story8_values['emotion']} in students, leads to walkout.",
        "values": story8_values,
        "submission_count": unique_submission_count(fillInBlanks_8),
    })

    stories.sort(
        key=lambda story: story["submission_count"],
        reverse=True
    )

    return render(request, 'posts/generated_stories.html', {'stories': stories})

def fillin_detail_view(request, idname):
    entry = get_object_or_404(fillInBlanks_1, idname=idname)
    return render(request, 'fillin_detail.html', {'entry': entry})

def fill_in_blanks_2(request):
    if request.method == "POST":
        form = forms.FillInTheBlanks2(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'posts/post_page_2.html', {'form': form.cleaned_data})
        else:
            return HttpResponse("Form is not valid", status=400)


    else:
        form = forms.FillInTheBlanks2()
    return render(request, 'posts/story_2.html', {'form': form })

def fill_in_blanks_3(request):
    if request.method == "POST":
        form = forms.FillInTheBlanks3(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'posts/post_page_3.html', {'form': form.cleaned_data})
        else:
            return HttpResponse("Form is not valid", status=400)
    
    else:
        form = forms.FillInTheBlanks3()
    return render(request, 'posts/story_3.html', {'form': form })

def fill_in_blanks_4(request):
    if request.method == "POST":
        form = forms.FillInTheBlanks4(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'posts/post_page_4.html', {'form': form.cleaned_data})
        else:
            return HttpResponse("Form is not valid", status=400)
    
    else:
        form = forms.FillInTheBlanks4()
    return render(request, 'posts/story_4.html', {'form': form })

def fill_in_blanks_5(request):
    if request.method == "POST":
        form = forms.FillInTheBlanks5(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'posts/post_page_5.html', {'form': form.cleaned_data})
        else:
            return HttpResponse("Form is not valid", status=400)
    
    else:
        form = forms.FillInTheBlanks5()
    return render(request, 'posts/story_5.html', {'form': form })

def fill_in_blanks_6(request):
    if request.method == "POST":
        form = forms.FillInTheBlanks6(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'posts/post_page_6.html', {'form': form.cleaned_data})
        else:
            return HttpResponse("Form is not valid", status=400)
    
    else:
        form = forms.FillInTheBlanks6()
    return render(request, 'posts/story_6.html', {'form': form })

def fill_in_blanks_8(request):
    if request.method == "POST":
        form = forms.FillInTheBlanks8(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'posts/post_page_8.html', {'form': form.cleaned_data})
        else:
            return HttpResponse("Form is not valid", status=400)
    
    else:
        form = forms.FillInTheBlanks8()
    return render(request, 'posts/story_8.html', {'form': form })

def post_page(request):
    return render(request, 'posts/post_page.html')

def story_selection(request):
    return render(request, 'posts/post_selection.html')
