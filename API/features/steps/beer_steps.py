from behave import *
from requests import *
import requests
      

@given('we want to get beers using IBU between 9 and 51')
def step_impl(context):
    first_value = 9
    second_value= 51
    context.url = f'https://api.punkapi.com/v2/beers?ibu_gt={first_value}&ibu_lt={second_value}'
    

@when('the request is made using IBU')
def step_impl(context):
    response = requests.get(context.url)
    assert response.status_code == 200
    context.response = response
    
    
@then('we get the expected result')
def step_impl(context):
    results = context.response.json()
    for beer in results:
        #Left this print here if you want to use --no-capture to see those ibu values manually
        print(beer['ibu'])
        #If you want to make it fail change 50 to 40 for example.
        assert(beer['ibu']>=10 and beer['ibu']<=50)
    