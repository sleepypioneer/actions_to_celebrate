# 🎬 Action! Celebrate with GitHub Actions workflow and Twitter
Use this action to send a tweet celebrating your and others progress using a GitHub actions workflow.

## Twitter Application Setup 🐦
First, you'll need to create a Twitter application if you haven't already. This will allow you to programmatically authenticate to the Twitter API and send a tweet.

If you haven't already, visit [developer.twitter.com/apps](https://developer.twitter.com/en/portal/projects-and-apps) and create a Twitter application. Then create keys and tokens to use for authentication.

By default, app's access level is read-only. To send out tweets, it requires write permission.
Go to: ´Permissions tab -> What type of access does your application need? -> Choose Read and Write -> Update settings´.

## Secret Configuration 🤫
Configure the authentication keys and tokens for your Twitter app as secrets in your github repository. If you are following this example we use: 
* `TWITTER_CONSUMER_API_KEY`
* `TWITTER_CONSUMER_API_SECRET`
* `TWITTER_ACCESS_TOKEN`
* `TWITTER_ACCESS_TOKEN_SECRET`

## Workflow Usage ⚙️
Configure your workflow to use sleepypioneer/tweet-on-pr-action@master.

Provide the authentication keys and tokens for your Twitter app as the consumer-key, consumer-secret, access-token, and access-token-secret inputs.

Example:

``` yml
name: example
on: [pull_request]
jobs:
  comment:
    name: Add checkout and pull commands
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: sleepypioneer/actions_to_celebrate@main
        with:
          consumer-key: ${{ secrets.TWITTER_CONSUMER_API_KEY }}
          consumer-secret: ${{ secrets.TWITTER_CONSUMER_API_SECRET }}
          access-token: ${{ secrets.TWITTER_ACCESS_TOKEN }}
          access-token-secret: ${{ secrets.TWITTER_ACCESS_TOKEN_SECRET }}
```

Now whenever you or someone else creates a pull request on your repository, GitHub Actions will tweet on your behalf. The format of the Tweet will be:

```text
Congratulations {author} on opening a pull request on the repository: {repo}!! Time to celebrate!!
```