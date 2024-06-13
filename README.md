API Testing - Project Spotify

The scope of this project is to use all API knowledge gained throught the Software Testing course and apply them in practice, using a live application.

Application under test: The Spotify Web API provides a wide range of functionality for developers, including:

- Retrieve data from your favorite artist, album, or show.
- Search for Spotify content.
- Control and interact with the playback, play and resume, seek to a position, or retrieve your queue.
- Manage your personal library by creating a new playlist and adding your favorite tracks to it.
- Get recommendations based on the music you listen to the most.
- And much more! You can find a complete list of available endpoints in the API Reference. For more details about documentation, visit this website.

Tools used: Postman, Pycharm.

Link to collection: ........

Created token

First steps:
- Go to Spotify and create a new user account.
- Access the dashboard and log in with the user account you created.
- Click on the "Create an app" button.
- Enter a name and description for the new application created.
- Accept the terms and conditions and click on the create button.
- In the opened window, click on "Edit Settings."
- In the Redirect URIs textbox, enter a link. It doesn't have to be specific, but one that can be used later. Example: http://applicationcourse/callback.
- Click on the SAVE button at the bottom.

Second steps:
- Open Postman aplication,you can download this Postman and create a new collection named "Spotify."
- Within the collection, create a new POST request.
- Click on authorization and select from the dropdown type OAuth 2.0.
- In the Callback URL field, enter the Redirect URIs from the first steps. If you are using the Postman web app, you don't need to set it.
- Copy the Client ID and Client Secret from your application and paste them into Postman.
- Treat these links as variables; assign them names and set them as global variables instead of using the actual links.
- In the Access Token URL field, enter the link https://accounts.spotify.com/api/token. After that, put the link https://accounts.spotify.com/authorize in the Auth URL field, and enter the text "playlist-modify-public playlist-read-private playlist-modify-private" in the Scope field.
- Finally, press "Get New Access Token". The token has been created.

Types available for testing

HTTP methods supported by this API are GET, POST, PUT, PATCH, and DELETE. In this section, you can explore and perform tests on various types of operations supported by the Spotify Web API. Some examples include:
- GET Requests: .......... ce testam
- POST Requests: Create new playlists,etc.....
- PUT and PATCH Requests: Update existing data, modify playlists, etc.
- DELETE Requests: Remove playlists, tracks, etc.

Tests used for validation

For this API, an authentication token is needed.

I send responses to some endpoints:

- https://api.spotify.com/v1/users/{user_id}/playlists (Create playlist)
- https://api.spotify.com/v1/playlists/{playlist_id}/tracks (Add Item to playlist)
- https://api.spotify.com/v1/playlists/{playlist_id}/tracks (Update Item to playlist)
- https://api.spotify.com/v1/playlists/{playlist_id} (Get playlist)
- https://api.spotify.com/v1/playlists/{playlist_id}/tracks (Remove playlistItem)
- https://api.spotify.com/v1/playlists/{playlist_id} (Change playlist details)
- https://api.spotify.com/v1/playlists/{playlist_id}/tracks (Add item in playlist)
- https://api.spotify.com/v1/playlists/{playlist_id}/followers (Follow playlist)
- Using all available HTTP methods.
- The expected HTTP responses are received together with the HTTP messages following the requests (200, 201, 204,404 and 401).

