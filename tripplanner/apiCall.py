from yelpapi import YelpAPI
import requests

CONSUMER_KEY = 'wPpxflGeQ2nkq_82_nRlGA'
CONSUMER_SECRET = '4zzfAe7itI9yDZ1nYzlCQq9eXJ8'
TOKEN = '7JHtzAwqKZ66OCFnyaXD5F2lUSUW05Ry'
TOKEN_SECRET = 'xWXX3NnyDrUgsvz0WxhbtvATdVw'

def callYelp(location,term,limit):
    yelp_api = YelpAPI(CONSUMER_KEY, CONSUMER_SECRET, TOKEN, TOKEN_SECRET)
    response = yelp_api.search_query(term=term, location=location, sort=0, limit=limit)
    context_list = []

    for r in response['businesses']:
        single = {}
        single['term'] = term
        single['name'] = r['name']
        single['address'] =r['location']['display_address']
        single['link'] = r['url']
        single['lat'] = r['location']['coordinate']['latitude']
        single['lon'] = r['location']['coordinate']['longitude']
        if r['is_closed'] == "False":
            single['close'] = "CLOSE"
        else:
            single['close'] = "OPEN"
        context_list.append(single)
    return context_list


def callEventbrite(city,keyword,limit):
    response = requests.get("https://www.eventbriteapi.com/v3/events/search/?q="+keyword+"&venue.city="+city+"&date_modified.keyword=this_week&sort_by=best&token=5MKESEL3LITBDQVL6J2K")
    events = response.json()['events']
    context_list= []

    for event in events[:limit]:
        single = {}
        #INFO of event&ticket
        single['type'] = keyword
        single['eventName']= event['name']['text']
        single['img'] = event['logo']['url']
        single['ticket']= event['url']
        single['startTime'] = event['start']['local']
        single['endTime'] = event['end']['local']
        single['status'] = event['status']
        #INFO of venue
        r = requests.get("https://www.eventbriteapi.com/v3/venues/"+event['venue_id']+"/?token=5MKESEL3LITBDQVL6J2K").json()
        single['venueName'] = r['name']
        single['lat'] = r['latitude']
        single['lon'] = r['longitude']
        single['address'] = r['address']['address_1']+","+r['address']['city']+","+r['address']['region']+ ","+r['address']['postal_code']
        # #INFO of organizer
        o = requests.get("https://www.eventbriteapi.com/v3/organizers/"+event['organizer_id']+"/?token=5MKESEL3LITBDQVL6J2K").json()
        single['orgName'] = o['name']
        single['orgUrl'] = o['url']
        context_list.append(single)
    return context_list