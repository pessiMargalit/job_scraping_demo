import requests


def get_businesses(api_key, address):
    base_url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"
    params = {
        'input': address,
        'inputtype': 'textquery',
        'fields': 'formatted_address,place_id',
        'key': api_key
    }

    # Make the request to find the place
    response = requests.get(base_url, params=params)
    place_data = response.json()
    print(place_data)
    if response.status_code == 200 and place_data['status'] == 'OK':
        place_id = place_data['candidates'][0]['place_id']

        # Use the obtained place_id to get details about the place, including nearby businesses
        details_url = "https://maps.googleapis.com/maps/api/place/details/json"
        details_params = {
            'place_id': place_id,
            'fields': 'name,formatted_address,place_id,types,opening_hours,website',
            'key': api_key
        }

        details_response = requests.get(details_url, params=details_params)
        details_data = details_response.json()

        if details_response.status_code == 200 and details_data['status'] == 'OK':
            businesses = details_data['result'].get('business_status', '')
            if businesses:
                print("Businesses in the given address:")
                for business in businesses:
                    print("- {}".format(business['name']))
            else:
                print("No businesses found in the given address.")
        else:
            print("Error retrieving place details:", details_data.get('error_message', ''))
    else:
        print("Error finding place:", place_data.get('error_message', ''))


# Replace 'YOUR_API_KEY' with your actual Google Places API key
api_key = 'AIzaSyDmgfGvdp9H0KdKoyK7Vy996g19CukVTlE'
address = "המרפא, 1, ירושלים"
get_businesses(api_key, address)
