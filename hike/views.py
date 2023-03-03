from django.http import HttpResponse
from django.template import loader
from .models import Challenge, Range, Hike, Mountain
from django.core.paginator import Paginator
import glob
import cv2 

# from pathlib import Path
from nyhiker.settings import BASE_DIR

def getContext():
    challenges = Challenge.objects.order_by("name")
    ranges = Range.objects.order_by("name")
    context = {"challenges": challenges
            , "ranges": ranges}
    return context

def index(request):
    context = getContext()

    template = loader.get_template('hike/index.html')
    return HttpResponse(template.render(context, request))

def hike_details(request, hike_id):
    context = getContext()
    hike = Hike.objects.get(id=hike_id)

    context['hike'] = hike

    # Find all images for this hike
    img_files = f"{BASE_DIR}/hike/static/hike/img/{hike.name_small}/*.jpg"
    img_list = glob.glob(img_files)
    hike_images = []
    for img in img_list:
        hike_images.append(img[img.rfind('/', 0, img.rfind('/')) + 1:])
    print(hike_images)
    context['hike_images'] = hike_images

    # Hike duration progress bar information
    hike_duration_max_value = 18
    hike_duration_decimal = hike.duration / hike_duration_max_value
    context["hike_duration_max_value"] = hike_duration_max_value
    context["hike_duration_decimal"] = hike_duration_decimal
    context["hike_duration_pct"] = f"{ hike_duration_decimal * 100 }%"

    # Hike mileage progress bar information
    hike_mileage_max_value = 32
    hike_mileage_decimal = hike.mileage / hike_mileage_max_value
    context["hike_mileage_max_value"] = hike_mileage_max_value
    context["hike_mileage_decimal"] = hike_mileage_decimal
    context["hike_mileage_pct"] = f"{ hike_mileage_decimal * 100 }%"

    # Hike gain progress bar information
    hike_gain_max_value = 10000
    hike_gain_decimal = hike.gain / hike_gain_max_value
    context["hike_gain_max_value"] = hike_gain_max_value
    context["hike_gain_decimal"] = hike_gain_decimal
    context["hike_gain_pct"] = f"{ hike_gain_decimal * 100 }%"

    # Weather conditions
    weather = [condition.name for condition in hike.conditions.all()]
    context["weather"] = weather
    
    template = loader.get_template('hike/hike_details.html')
    return HttpResponse(template.render(context, request))

def search(request, type):
    context = getContext()
    context["type"] = type 
    mountains = Mountain.objects.order_by("name")
    hikes = Hike.objects.order_by("range", "name")
    print(len(mountains))
    context["mountains"] = mountains 
    context["hikes"] = hikes 
    template = loader.get_template('hike/search.html')
    return HttpResponse(template.render(context, request))    

def challenge(request, challenge_id):
    context = getContext()
    challenge = Challenge.objects.get(id=challenge_id)
    context["challenge"] = challenge

    # Hike Data 
    hikes = challenge.hikes.all().order_by("-completed_on")
    # context["hikes"] = hikes
    hikes_completed = hikes_completed_mileage = hikes_planned = hikes_planned_mileage = 0
    hikes_completed_duration = hikes_planned_duration = 0
    for hike in hikes:
        if hike.completed_on:
            hikes_completed += 1
            hikes_completed_mileage += hike.mileage
            hikes_completed_duration += hike.duration
        else:
            hikes_planned += 1
            hikes_planned_mileage += hike.mileage 
            hikes_planned_duration += hike.duration 
    context["hikes_completed"] = hikes_completed
    context["hikes_completed_mileage"] = hikes_completed_mileage
    context["hikes_completed_duration"] = hikes_completed_duration
    context["hikes_planned"] = hikes_planned 
    context["hikes_planned_mileage"] = hikes_planned_mileage 
    context["hikes_planned_duration"] = hikes_planned_duration 
    
    mountains = challenge.mountains.all().order_by("name")
    context["mountains_completed"] = len([1 for mountain in mountains if mountain.rating])

    hikes_paginator = Paginator(hikes, 3)
    hikes_page_number = request.GET.get('hikes_page')
    hikes_page_obj = hikes_paginator.get_page(hikes_page_number)
    context["hikes_page_obj"] = hikes_page_obj
    context["hikes_paginator"] = hikes_paginator

    # A list of mountains that have been both planned and completed
    hikes_mountains = set()
    for hike in hikes:
        for mountain in hike.mountains.all():
            hikes_mountains.add(mountain)
    context['hikes_mountains'] = list(hikes_mountains)

    mountains_paginator = Paginator(mountains, 12)
    mountains_page_number = request.GET.get('mountains_page')
    mountains_page_obj = mountains_paginator.get_page(mountains_page_number)
    context["mountains_page_obj"] = mountains_page_obj
    context["mountains_paginator"] = mountains_paginator

    template = loader.get_template('hike/challenge.html')
    return HttpResponse(template.render(context, request))

