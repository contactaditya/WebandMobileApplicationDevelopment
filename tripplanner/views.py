from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from tripplanner.forms import NameForm
from tripplanner.apiCall import *


def home(request):
    return render(request, 'story/index_home.html')


def get_login(request):
    return render(request, 'story/login.html')


def get_registration(request):
    return render(request, 'story/registration.html')


def get_userprofile(request):
    return render(request, 'story/userprofile.html')


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            # YELP
            bar = form.cleaned_data['bar']
            coffee = form.cleaned_data['coffee']
            restaurant = form.cleaned_data['restaurant']
            term = form.cleaned_data['term']
            # EVENTBRITE
            art = form.cleaned_data['art']
            fashion = form.cleaned_data['fashion']
            film = form.cleaned_data['film']
            holiday = form.cleaned_data['holiday']
            music = form.cleaned_data['music']
            shopping = form.cleaned_data['shopping']
            sports = form.cleaned_data['sports']
            outdoor = form.cleaned_data['outdoor']
            acti = form.cleaned_data['acti']
            # FOURSQUARE
            trend = form.cleaned_data['trend']
            num_YelpCall = 5
            num_EventbriteCall = 3
            num_FoursquareCall=10
            context_list = []
            # YELP
            if bar == True:
                context_list+=callYelp(city,'bar',num_YelpCall)
            if coffee == True:
                context_list+=callYelp(city,'coffee',num_YelpCall)
            if restaurant == True:
                context_list+=callYelp(city,'restaurant',num_YelpCall)
            if term != "":
                context_list+=callYelp(city,term,2)
            # EVENTBRITE
                context_list+=callYelp(city,term,num_YelpCall)
            #EVENTBRITE
            if art == True:
                context_list+=callEventbrite(city,'art',num_EventbriteCall)
            if fashion == True:
                context_list+=callEventbrite(city,'fashion',num_EventbriteCall)
            if film == True:
                context_list+=callEventbrite(city,'film',num_EventbriteCall)
            if holiday == True:
                context_list+=callEventbrite(city,'holiday',num_EventbriteCall)
            if music == True:
                context_list+=callEventbrite(city,'music',num_EventbriteCall)
            if shopping == True:
                context_list+=callEventbrite(city,'shopping',num_EventbriteCall)
            if sports == True:
                context_list+=callEventbrite(city,'sports',num_EventbriteCall)
            if outdoor == True:
                context_list+=callEventbrite(city,'outdoor',num_EventbriteCall)
            if acti != "":
                context_list+=callEventbrite(city,'concert',num_EventbriteCall)
            #FOURSQUARE
            #TREND
            if trend == True:
                context_list+=callFoursquare(city,num_FoursquareCall)
            # send Post request
            return render(request,'story/index_userResponse.html',{'content_list':context_list})

    # if a GET (or any other method) we'll create a blank form
    # else:
