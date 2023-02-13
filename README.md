# Inspiration: A-Microservice

Microservice using a GET request to return inspirational quotes back to user.

## Request Data
The hosting is done locally and is requested through a GET request. To request data, simply type in the base url: ```http://localhost:5000/inspire```.
This will return all quotes of ispiration from the database file inspire.db through a SQL query. 

For a more detailed search for a quote, user can enter the base url in addition to an ID or string. A singular quote will appear if the ID matches the quote's ID or the string text is lies within the quote.

```
    For example: 
   - http://localhost:5000/inspire/1
   - http://localhost:5000/inspire/25
   - http://localhost:5000/inspire/49
   - http://localhost:5000/inspire/Twain
   - http://localhost:5000/inspire/oBaMa
   - http://localhost:5000/inspire/ConfuCIUS
 ```
       
### *DISCLAIMER*
There are only 50 quotes. Any ID higher than 50 will return "null."

## Receive Data
Data will be returned to user as JSON and will appear as the image below if using the web platform Postman. Any other services will slighty change the aesthetics of the quote but will still contain the core content of the quote.

!(https://github.com/nguyev22/Inspiration-A-Microservice-/blob/main/quote_pic.jpg)

## UML Sequence Diagram
!(https://github.com/nguyev22/Inspiration-A-Microservice-/blob/main/UMLsequence.jpg?raw=true)
