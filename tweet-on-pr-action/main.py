import tweepy
import os

API_KEY = os.getenv('TWITTER_API_KEY')
API_SECRET_KEY = os.getenv('TWITTER_API_SECRET_KEY')
ACCESS_TOKEN = os.getenv('TWITTER_ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('TWITTER_TOKEN_SECRET')
GITHUB_REPO = 'sleepypioneer/pyladies_IWD'
GITHUB_USER = 'sleepypioneer'

def main():
  auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
  auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

  api = tweepy.API(auth)

  tweet = f'Congratulations {GITHUB_USER} on opening a pull request' + \
    ' on the repository: {GITHUB_REPO}!! Time to celebrate!!'
  status = api.update_status(status=tweet)
  print(status)


if __name__ == "__main__":
  main()