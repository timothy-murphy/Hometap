# Hometap
I decided to use the FLask Web framework in Python, because it is very lightweight, simple to understand/use, and has built in support for APIS. 
The House Canary documentation was pretty easy to understand so I simply read it through until I found the correct end point to use. The endpoint ended up being the property/details, with the url being https://api.housecanary.com/v2/property/details, and then I added on some test parameters for one to use. 

I then called the API with the get request in order to get data from the API. I then parsed through it, in order to get the data that I really care about, which is the sewer data. 

Once I get the sewer data, I simply passed the returned data to a variable. If the variable is equaled to "Septic", then the Flask app outputs "ask user for another question. If it does not equal Septic, then it returns "No more information needed". 


To run the code, you need to download the file app.py, and then simply run the program. The Flask app will run, as right now the data being displayed is from data I copied and pasted in from the docs on the api. 
