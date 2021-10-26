import flask
import requests
import json

f = open('data.json')
data = json.load(f)

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    #endpoint = https://api.housecanary.com/v2/property/details
    
    #This is the custom API endpoint
    url = 'https://api.housecanary.com/v2/property/details'

    #Then we simply add on the specified identifiers to the custom endpoint
    params = {'address': '43 Valmonte Plaza',
          'zipcode': '90274'}
    


    #This is calling the API to get the data. Un-comment lines 26-28 to run the actual api.
    """
    response = requests.get(url, params=params)
    type_of_sewer1 = response.json()
    type_of_sewer = type_of_sewer1['property/details']['result']['property']['sewer']
    """
    #Since the api requires an authentication key, I am using the test data from data.json
    type_of_sewer = data['property/details']['result']['property']['sewer']


    #Since, in this case we only care about the sewer data, we analyze that data
    if type_of_sewer == "Septic" or type_of_sewer == "septic":
        display_content = 'Since the type of Sewer is Septic: Ask user additional question'
    else:
        display_content = 'The owner does not have a septic tank'
    return display_content
app.run()
#In this example, the custom API Endpoint that I used is https://api.housecanary.com/v2/property/details?, with then just plugging in an example address.
#I tested my code with the example response given from the docs