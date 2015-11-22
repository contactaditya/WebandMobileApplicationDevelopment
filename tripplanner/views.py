from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from tripplanner.forms import NameForm


from yelpapi import YelpAPI

CONSUMER_KEY = 'wPpxflGeQ2nkq_82_nRlGA'
CONSUMER_SECRET = '4zzfAe7itI9yDZ1nYzlCQq9eXJ8'
TOKEN = '7JHtzAwqKZ66OCFnyaXD5F2lUSUW05Ry'
TOKEN_SECRET = 'xWXX3NnyDrUgsvz0WxhbtvATdVw'


def home(request):
    return render(request, 'story/index.html')
    # POST method
    # return render(request,'story/user_input.html')


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():

            city = form.cleaned_data['city']
            term = form.cleaned_data['term']
            yelp_api = YelpAPI(CONSUMER_KEY, CONSUMER_SECRET, TOKEN, TOKEN_SECRET)
            response = yelp_api.search_query(term=term, location=city, sort=2, limit=5)
            print(response)
            name1 = response['businesses'][0]['name']
            address1 = response['businesses'][0]['location']['display_address']
            link1 = response['businesses'][0]['url']

            name2 = response['businesses'][1]['name']
            address2 = response['businesses'][1]['location']['display_address']
            link2 = response['businesses'][1]['url']
            content_text = {'name1': name1, 'link1': link1, 'address1': address1, 'name2': name2, 'link2': link2,
                            'address2': address2}
            # send Post request
            # return render(request,'story/response_output.html',content_text)
            # return render(request,'story/index.html')

    # if a GET (or any other method) we'll create a blank form

    else:
        city = request.GET.get('city')
        term = request.GET.get('term')
        yelp_api = YelpAPI(CONSUMER_KEY, CONSUMER_SECRET, TOKEN, TOKEN_SECRET)
        response = yelp_api.search_query(term=term, location=city, sort=2, limit=5)
        print(response)
        name1 = response['businesses'][0]['name']
        address1 = response['businesses'][0]['location']['display_address']
        link1 = response['businesses'][0]['url']

        name2 = response['businesses'][1]['name']
        address2 = response['businesses'][1]['location']['display_address']
        link2 = response['businesses'][1]['url']
        content_text = {'name1': name1, 'link1': link1, 'address1': address1, 'name2': name2,'link2': link2,
                        'address2': address2,'city':city}
        return render(request, 'story/response_output.html', content_text)


