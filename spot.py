import requests
import time

from pprint import pprint


SPOTIFY_GET_CURRENT_TRACK_URL = 'https://api.spotify.com/v1/me/player/currently-playing'
ACCESS_TOKEN = 'BQBz9YDvlo5Ohhw-yfQFfV-In5eyZwM-Pg2autIRzYdmmmOqdJrscxHzg-vKWlPwcmXqSUr6sbWKInyQHQCkQQMi8LS2tifwQUC68C9gxg8at4P_ezCsI_64Yczmrah74GLKojpep-9j7zMBGi6DshNTulNDy5yj4PF0U9YL8vVAABoMGA'


def get_current_track(access_token):
    response = requests.get(
        SPOTIFY_GET_CURRENT_TRACK_URL,
        headers={
            "Authorization": f"Bearer {access_token}"
        }
    )
    json_resp = response.json()

    track_id = json_resp['item']['id']
    track_name = json_resp['item']['name']
    artists = [artist for artist in json_resp['item']['artists']]

   
    artist_names = ', '.join([artist['name'] for artist in artists])

    current_track_info = {
    	"id": track_id,
    	"track_name": track_name,
    	"artists": artist_names,
    	
    }

    return current_track_info


def main():
	current_track_id = None
	while True:
	    current_track_info = get_current_track(ACCESS_TOKEN)

	    if current_track_info['id'] != current_track_id:
		    pprint(
		    	current_track_info,
		    	indent=4,
		    )
		    current_track_id = current_track_info['id']

	    time.sleep(1)


if __name__ == '__main__':
    main()
