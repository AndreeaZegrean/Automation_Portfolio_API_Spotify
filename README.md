API Testing - Project Spotify

The scope of this project is to use all API knowledge gained throught the Software Testing course and apply them in practice, using a live application.

This API provides access to a wide range of functionality and data allowing developers to integrate and extend Spotify's functionality in their applications: 
- getting detailed information about songs, albums, artists and playlists, 
- generating music suggestions based on user preferences or characteristics specific songs or artists, 
- allows users to create, update and delete playlists. They can also add or remove songs from playlists.
- control music playback on different devices connected to the user's Spotify account, including pause, play, skip forward or back.
- allows users to add or remove songs and albums from their personal library.

To run the application, you need:
- You need to have Python installed, at least the version 3.12
- pip is the package manager for Python.
- You need to create a virtual environment (venv) before running the application

Tools used: Postman, Pycharm.

Link to collection: https://github.com/AndreeaZegrean/Automation_Portfolio_API_Spotify

**1. Created token**

- Go to Spotify and create a new user account.
- Access the [dashboard](https://developer.spotify.com/dashboard) and log in with the user account you created.
- Click on the "Create an app" button.
- Enter a name and description for the new application created.
- Accept "Terms and Conditions" and click on the create button.
- In the opened window, click on "Edit Settings."
- In the Redirect URIs textbox, enter a link. It doesn't have to be specific, but one that can be used later. Example: http://applicationcourse/callback.
- Click on the SAVE button at the bottom.

**2. Installation and running**

- Create a folder in your computer where you'd like to store the code to run the app.
- The libraries used are requests (version 2.31), pytest (version 8.2), selenium (version 4.21), seleniumbase (version 4.27.5). To install them, run the Terminal command:
pip install -r requirements.txt

In the generate_token file, enter the data we obtained at point 1 (Created token)

<img src="C:\Users\deea2\PycharmProjects\pythonProject\pythonProject\Examen_Final_Spotify\assets\4.png"/>

**3. Authentication and authorization**

- Click on authorization and select from the dropdown type OAuth 2.0.
- In the Callback URL field, enter the Redirect URIs from the first steps. If you are using the Postman web app, you don't need to set it.
- Copy the Client ID and Client Secret from your application and paste them into Postman.
- Treat these links as variables; assign them names and set them as global variables instead of using the actual links.
- In the Access Token URL field, enter the link https://accounts.spotify.com/api/token. After that, put the link https://accounts.spotify.com/authorize in the Auth URL field, and enter the text "playlist-modify-public playlist-read-private playlist-modify-private" in the Scope field.
- Finally, press "Get New Access Token". The token has been created.

To obtain the access token, you need to run the generate_token.py file and follow the steps described.

For more information you can follow the following URLs:
- Spotify API authorization guide: https://developer.spotify.com/documentation/web-api/concepts/authorization
- Google OAuth2 authorization standard: https://pkg.go.dev/golang.org/x/oauth2/google

**4. Creating requests and running the tests**

The requests can be found in the **requests_folder**. The [documentation](https://developer.spotify.com/documentation/web-api/reference/get-an-album) was used to write the requests

<img src="C:\Users\deea2\PycharmProjects\pythonProject\pythonProject\Examen_Final_Spotify\assets\3.png"/>

The tests can be found in the **tests folder**. To run any test, you can run the corresponding file.
For example, I have attached a screenshot from the test_get_album.py file. To run all the tests in the file, click on the green triangle next to the TestGetAlbum class.
If you want to run a single test, press the green triangle next to the function that describes the desired test, for example the function: def test_get_album_does_not_exist(self):

[](<img src="C:\Users\deea2\PycharmProjects\pythonProject\pythonProject\Examen_Final_Spotify\assets\2.png"/>)

**5. Generating the report**

To generate the report, run the Terminal command: pytest --html=report.html
An HTML file will be created in the project main directory, which can be opened with any browser.