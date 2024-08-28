## Frontend file: 
App.py is a flask application that loads the html frontend and receives data from the "/submit" API endpoint. 

Frontend.html uses HTML and Bootstrap to create a UI for the web application and design it. It also uses Javascript to send data to an API endpoint.

## Middleware: 
Chatbot.py uses Langchain and GPT 3.5 turbo engine to create a helpful chatbot that can respond to the users prompts. A persona has been given to the chatbot to appropriately reply to the prompts.

## Backend: 
Azure.py creates a connection to the azure sql database I created. Moreover, its linked to an html template that sends data to the databse when it is submitted and stores it in the form of a table. 
