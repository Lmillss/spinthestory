from django.shortcuts import render, redirect
from .models import fillInBlanks_1
from . import forms
from django.http import HttpResponse
from django.db.models import Count
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
import myproject.views as views
# Create your views here.

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

def fill_in_blanks_1_generated(request):
    fields = [
        'emotion_1', 'adjective_1', 'US_state', 'number_1', 'past_tense_verb_1',
        'social_media', 'number_2', 'past_tense_verb_2', 'political_organization_1',
        'adjective_2', 'group_of_people', 'political_organization_2', 'verb_ing',
        'past_tense_emotion', 'name', 'age', 'political_issue', 'Adjective_3', 'Adjective_4'
    ]

    common_answers = {}

    for field in fields:
        qs = fillInBlanks_1.objects.values(field).annotate(count=Count(field)).order_by('-count')
        for item in qs:
            val = item[field]
            if val:
                common_answers[field] = val
                break
        else:
            common_answers[field] = None

    return render(request, 'posts/generated_stories.html', {'form': common_answers})

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
