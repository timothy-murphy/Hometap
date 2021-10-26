# Hometap
I decided to use the FLask Web framework in Python, because it is very lightweight, simple to understand/use, and has built in support for APIS. 
The House Canary documentation was pretty easy to understand so I simply read it through until I found the correct end point to use. The endpoint ended up being the property/details, with the url being https://api.housecanary.com/v2/property/details, and then I added on some test parameters for one to use. 

I then called the API with the get request in order to get data from the API. I then parsed through it, in order to get the data that I really care about, which is the sewer data. 

Once I get the sewer data, I simply passed the returned data to a variable. If the variable is equaled to "Septic", then the Flask app outputs "ask customer for another question". If it does not equal Septic, then it returns "No more information needed". 


The Flask app will run, as right now the data being displayed is from data I copied and pasted in from the docs on the api. 

Since I was unable to call the API due to the restricted access, I decided to test the program with the data I found in the docs. The data is what I used to test the logic of my app.

In order to test it on the api, in line 72 replace "data" with "response" and then run the pro

To run the code, you need to download the file app.py, and then simply run the program. The Flask will open up and display if the customer needs to be asked more questions. 

Next Steps:
  What I would like to do is build out a user interface that could be used to manually input into the API. Since the whole purpose of the exercise is to deterine if the customer should be asked an extra question or not. Also, since Hometap is a Django heavy company, I would like to remake this in Django, in order to get the program integrated with the site. Since knowing what kind of septic tank exists is pretty important, it would be a valuable thing to know. 
