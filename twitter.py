from flask import Flask
import requests, json
import os #create environment variables in server
import tweepy as tw

app= Flask(__name__)
Twitter_API_Key = os.environ.get('Twitter_API_Key')
Twitter_API_Secret= os.environ.get('Twitter_API_Key')



Twitter_Barear_Token= os.environ.get('Twitter_Barear_Token')




auth= tw.OAuthHandler(Twitter_API_Key, Twitter_API_Secret)
api = tw.API(auth, wait_on_rate_limit = True)

print(Twitter_Barear_Token)
def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {Twitter_Barear_Token}"
    r.headers["User-Agent"] = "v2RecentSearchPython"
    return r


def get_params():
    return {"tweet.fields": "created_at"}

def create_url():
    # Replace with user ID below
    user_id = "EmanWamda"

    return "https://api.twitter.com/1.1/users/show.json?screen_name= {}".format(user_id);
#    return "https://api.twitter.com/2/users/{}/tweets".format(user_id)


def connect_to_endpoint(url, params):
    response = requests.request("GET", url, auth=bearer_oauth, params=params) #optionaly put 
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )


    return response.json()


def main():
    url = create_url()
    params = get_params()
    json_response = connect_to_endpoint(url, params)
    print(json.dumps(json_response, indent=4, sort_keys=True))


if __name__ == "__main__":
    main()
