import requests      #imports the requests libaries for pytest
BASE_URL = "https://randomuser.me/api"
API = BASE_URL + "?q={city_name}&appid={api_key}&units=metric"

# checks the HTTP status code to equal 200
def test_get_locations_for_api_88715_check_status_code_equals_200():
     response = requests.get("https://randomuser.me/api")
     assert response.status_code == 200

# This checks the response content type header is correctly with the response of the JSON body
def test_get_locations_for_api_88715_check_content_type_equals_json():
     response = requests.get("https://randomuser.me/api")
     assert response.headers["Content-Type"] == "application/json; charset=utf-8"

# Check to see how many entries the api has, it has 2 entries
def test_get_locations_for_api_check_one_place_is_returned():
     response = requests.get("https://randomuser.me/api")
     response_body = response.json()
     assert len(response_body) == 2











