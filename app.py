import flask
import requests

data = {
    "property/details": {
        "api_code_description": "ok",
        "api_code": 0,
        "result": {
            "property": {
                "air_conditioning": "yes",
                "attic": False,
                "basement": "full_basement",
                "building_area_sq_ft": 1824,
                "building_condition_score": 5,
                "building_quality_score": 3,
                "construction_type": "Wood",
                "exterior_walls": "wood_siding",
                "fireplace": False,
                "full_bath_count": 2,
                "garage_parking_of_cars": 1,
                "garage_type_parking": "underground_basement",
                "heating": "forced_air_unit",
                "heating_fuel_type": "gas",
                "no_of_buildings": 1,
                "no_of_stories": 2,
                "number_of_bedrooms": 4,
                "number_of_units": 1,
                "partial_bath_count": 1,
                "pool": True,
                "property_type": "Single Family Residential",
                "roof_cover": "Asphalt",
                "roof_type": "Wood truss",
                "site_area_acres": 0.119,
                "style": "colonial",
                "total_bath_count": 2.5,
                "total_number_of_rooms": 7,
                "sewer": "Septic",
                "subdivision" : "CITY LAND ASSOCIATION",
                "water": "municipal",
                "year_built": 1957,
                "zoning": "RH1"
            },

            "assessment":{
                "apn": "0000 -1111",
                "assessment_year": 2015,
                "tax_year": 2015,
                "total_assessed_value": 1300000.0,
                "tax_amount": 15199.86
            }
        }
    }
}
app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    response = requests.get('https://api.housecanary.com/v2/property/details?address=123+Main+St&zipcode=94132')
    type_of_sewer = data["property/details"]["result"]["property"]["sewer"]
    if type_of_sewer == "Septic":
        display_content = 'Since the type of Sewer is Septic: Ask user additional question'
    else:
        display_content = 'They are all set'
    return display_content

app.run()
#In this example, the custom API Endpoint that I used is https://api.housecanary.com/v2/property/details?, with then just plugging in an example address.
#I tested my code with the example response given from 