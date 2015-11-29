from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from tripplanner.forms import NameForm
from tripplanner.apiCall import *


def home(request):
    return render(request, 'story/index_home.html')

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
            #EVENTBRITE
            art = form.cleaned_data['art']
            fashion = form.cleaned_data['fashion']
            film = form.cleaned_data['film']
            holiday = form.cleaned_data['holiday']
            music = form.cleaned_data['music']
            shopping = form.cleaned_data['shopping']
            sports = form.cleaned_data['sports']
            outdoor = form.cleaned_data['outdoor']
            acti = form.cleaned_data['acti']
            #FOURSQUARE


            context_list = []
            #YELP
            if bar == True:
                context_list+=callYelp(city,'bar',2)
            if coffee == True:
                context_list+=callYelp(city,'coffee',2)
            if restaurant == True:
                context_list+=callYelp(city,'restaurant',2)
            if term != "":
                context_list+=callYelp(city,term,2)
            #EVENTBRITE
            if art == True:
                context_list+=callEventbrite(city,'art',2)
            if fashion == True:
                context_list+=callEventbrite(city,'fashion',2)
            if film == True:
                context_list+=callEventbrite(city,'film',2)
            if holiday == True:
                context_list+=callEventbrite(city,'holiday',2)
            if music == True:
                context_list+=callEventbrite(city,'music',2)
            if shopping == True:
                context_list+=callEventbrite(city,'shopping',2)
            if sports == True:
                context_list+=callEventbrite(city,'sports',2)
            if outdoor == True:
                context_list+=callEventbrite(city,'outdoor',2)
            if acti != "":
                context_list+=callEventbrite(city,'concert',2)
            #FOURSQUARE

            #SHOPPING
            #TREND
            # send Post request
            # return HttpResponse(context_list)
            return render(request,'story/response_output.html',{'content_list':context_list})




    # if a GET (or any other method) we'll create a blank form
    # else:
