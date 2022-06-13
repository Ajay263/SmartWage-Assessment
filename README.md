This repository is a Django Assessment project for SmartWage, which contains a  Whatsapp Chatbot.

What is this repository for?
Assessment for a technical Interview.

How do I get set up?
Run the following step to get up and running with the project:

Dependency
Make sure the following dependencies are install
Django and twilio(pip install django twilio pyngrok)

Step 1: Download source code on Github (an alternative is to clone the repository on Github) 

Step 2: Extract file


Database
Run following code in commandline at the root of folder:

python manage.py migrate

Run application
python manage.py runserver

Nb=> The Django web server is only available locally inside your computer, which means that it cannot be accessed over the Internet. To be able to connect with WhatsApp, Twilio needs to be able to send web requests to this server

ngrok http 8000





