from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from tripplanner.forms import NameForm
from tripplanner.apiCall import *
from django.contrib.auth.models import User
from tripplanner.models import Additional
from django.contrib.auth import authenticate,login

def home(request):
    return render(request, 'story/index_home.html')


def get_login(request):
    return render(request, 'story/login.html')

def success_login(request):
    username = request.POST['form-username']
    password = request.POST['form-password']
    user = authenticate(username=username, password=password)
    context_dic = {'username':username}
    if user is not None:
    # the password verified for the user
        if user.is_active:
            login(request,user)
            return render(request,'story/index_userPreference.html',context_dic)
        else:
            return HttpResponse("The password is valid, but the account has been disabled!")
    else:
    # the authentication system was unable to verify the username and password
        return HttpResponse("The username and password were incorrect.",context_dic)

def get_registration(request):
    return render(request, 'story/registration.html')

def success_registration(request):
    username=request.POST['username']
    password=request.POST['password']
    phone=request.POST['mobilephone']
    user = User.objects.create_user(username=username,password=password)
    add= Additional(user=user,phone=phone)
    user.save()
    add.save()
    return render(request,'story/index_userPreference.html')

def logout(request):
    return HttpResponseRedirect('/')

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
    else:
        return render(request,'story/index_userPreference.html')