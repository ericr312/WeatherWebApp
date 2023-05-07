# WeatherWebApp - Weather app for desktop browser

### Recommended steps prior to using the app ###

-- Obtain a personal API key from Open Weather -- 
1. Go to https://openweathermap.org/guide and create a free account.
2. Ensure you have selected the "free account" option from the "API" tab.
3. Go to <your account> (located in the top right hand corner of the screen).
4. Select "My API Keys".
5. If you do not already have a default API key, create a new one.
6. Copy this API key and save it in a .txt file (e.g. "APIkey.txt").
7. Ensure APIkey.txt is located inside of your app directory (i.e., WeatherWebApp/app/APIkey.txt)


-- Setting up the WeatherApp --
1. Ensure your interpreter has Django installed.
2. Recommended to store your Django secret in a seperate .txt file (e.g. "DjangoSecret") prior to publishing code.
  Note: this will be used in settings.py
3. Ensure that your directories and files are stored correctly inside the project.
    i.e., WeatherWebApp (Project directory) --> app (app directory), manage.py, urls.py, wsgi.py, asgi.py, __init__.py, DjangoSecret.py


-- Start WeatherApp --
1. Open terminal inside your IDE, and run the following command:
    >> python /Users/<your_username_on_localpc>/WeatherWebApp/manage.py runserver
