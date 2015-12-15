from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from tripplanner.forms import NameForm
from tripplanner.apiCall import *
from django.contrib.auth.models import User
from tripplanner.models import Registration,Search
from django.contrib.auth import authenticate,login,logout



def home(request):
    return render(request, 'story/index_home.html')


def get_login(request):
    return render(request, 'story/login.html')


def success_login(request):
    username = request.POST['form-username']
    password = request.POST['form-password']
    user = authenticate(username=username, password=password)
    context_dic = {'username': request.user.username}
    if user is not None:
    # the password verified for the user
        if user.is_active:
            login(request, user)
            return render(request,'story/index_userPreference.html', context_dic)
        else:
            return HttpResponse("The password is valid, but the account has been disabled!")
    else:
    # the authentication system was unable to verify the username and password
        return HttpResponse("The username and password were incorrect.", context_dic)


def get_registration(request):
    return render(request, 'story/registration.html')


def success_registration(request):
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    email = request.POST['emailid']
    mobilenumber = request.POST['mobilenumber']
    location = request.POST['location']
    city = request.POST['city']
    country = request.POST['country']
    zipcode = request.POST['zipcode']
    username = request.POST['username']
    password = request.POST['password']
    confirmpassword = request.POST['confirmpassword']
    dateofbirth = request.POST['dateofbirth']
    gender = request.POST['gender']
    user = User.objects.create_user(username=username, password=password, email=email, first_name=firstname, last_name=lastname)
    add = Registration.objects.create_add(user=user, mobilenumber=mobilenumber, location=location, city=city, country=country,\
                                         zipcode=zipcode, confirmpassword=confirmpassword, dateofbirth=dateofbirth,\
                                         gender=gender)

    user = authenticate(username=username, password=password)
    if user.is_active:
        login(request,user)
    user.save()
    add.save()

    return render(request, 'story/index_userPreference.html', {'username': request.user.username})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


def get_userprofile(request):
    if request.user.is_authenticated():
        u=Registration.objects.filter(user=request.user)[0]
        context_dic={'firstname': request.user.first_name, 'lastname': request.user.last_name, 'email': request.user.email,\
                     'mobilenumber': u.mobilenumber, 'location': u.location, 'username': request.user.username,\
                     'city': u.city, 'country': u.country, 'zipcode': u.zipcode,'gender': u.gender, 'dateofbirth': u.dateofbirth}
        content_list=[]
        for s in Search.objects.filter(user=request.user):
            content_list.append({'city': s.city, 'bar': s.bar, 'coffee': s.coffee, 'restaurant': s.restaurant, 'food': s.food,\
                                 'art': s.art, 'fashion':s.fashion, 'film':s.film, 'holiday':s.holiday, 'music': s.music,\
                                 'shopping': s.shopping, 'sports': s.sport, 'outdoor': s.outdoor, 'acti': s.acti, 'trend': s.trend})
        context_dic['content_list'] = content_list
    return render(request, 'story/userprofile.html', context_dic)


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
            num_EventbriteCall = 5
            num_FoursquareCall = 10
            context_list = []
            # YELP
            if bar == True:
                context_list += callYelp(city,'bar', num_YelpCall)
            if coffee == True:
                context_list += callYelp(city, 'coffee', num_YelpCall)
            if restaurant == True:
                context_list += callYelp(city, 'restaurant', num_YelpCall)
            if term != "":
                context_list += callYelp(city, term, num_YelpCall)

            # EVENTBRITE
            if art == True:
                context_list += callEventbrite(city, 'art', num_EventbriteCall)
            if fashion == True:
                context_list += callEventbrite(city, 'fashion', num_EventbriteCall)
            if film == True:
                context_list += callEventbrite(city,'film', num_EventbriteCall)
            if holiday == True:
                context_list += callEventbrite(city, 'holiday', num_EventbriteCall)
            if music == True:
                context_list += callEventbrite(city ,'music', num_EventbriteCall)
            if shopping == True:
                context_list += callEventbrite(city, 'shopping', num_EventbriteCall)
            if sports == True:
                context_list += callEventbrite(city, 'sports', num_EventbriteCall)
            if outdoor == True:
                context_list += callEventbrite(city, 'outdoor', num_EventbriteCall)
            if acti != "":
                context_list += callEventbrite(city, acti, num_EventbriteCall)
            # FOURSQUARE
            # TREND
            if trend == True:
                context_list += callFoursquare(city,num_FoursquareCall)
            # send Post request
            user= request.user

            search=Search.objects.create_search(user=user, city=city, bar=bar, coffee=coffee, restaurant=restaurant, food=term, art=art,\
                        fashion=fashion, film=film, holiday=holiday, music=music, shopping=shopping, sport=sports,\
                        outdoor=outdoor, acti=acti, trend=trend)
            return render(request, 'story/index_userResponse.html', {'content_list': context_list})

    # if a GET (or any other method) we'll create a blank form
    else:
        return render(request, 'story/index_userPreference.html', {'username':request.user.username})