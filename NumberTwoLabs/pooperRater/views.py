from django.shortcuts import render
from pooperRater.api_calls import yelp_api_call
from pooperRater.api_calls.aggregation import something


def googleplace(request):
    return render(request, 'google_places_snippet.html')

def yelp_api(request):
    yelp_response = yelp_api_call.main()
    x = something(1)
    print x['quality__avg']
    data = {
        "one": "One",
        "two": "Two",
        'yelp_response': yelp_response,
        'businesses' : yelp_response[0]['businesses']
    }
    return render(request, 'yelp_api.html', data)
