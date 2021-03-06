import json
import os
import sys

from github import Github
import tweepy

'''
 GitHub Actions creates an environment variable for the input with the name:
    INPUT_<CAPITALIZED_VARIABLE_NAME> (e.g. "INPUT_FOO" for "foo")
    References
    ----------
    .. [1] https://help.github.com/en/actions/automating-your-workflow-with-github-actions/metadata-syntax-for-github-actions#example  # noqa: E501
'''
API_KEY = os.getenv('INPUT_{}'.format('consumer-key').upper())
API_SECRET_KEY = os.getenv('INPUT_{}'.format('consumer-secret').upper())
ACCESS_TOKEN = os.getenv('INPUT_{}'.format('access-token').upper())
ACCESS_TOKEN_SECRET = os.getenv(
    'INPUT_{}'.format('access-token-secret').upper())


def read_json(filepath):
    """
    Read a json file as a dictionary.
    Parameters
    ----------
    filepath : str
    Returns
    -------
    data : dict
    """
    with open(filepath, 'r') as f:
        return json.load(f)


def main():
    # search a pull request that triggered this action
    gh = Github(os.getenv('GITHUB_TOKEN'))
    event_path = os.getenv('GITHUB_EVENT_PATH')
    if event_path is None:
        print('::set-output name=status::FAIL')
        sys.exit(1)

    event = read_json(event_path)

    if 'pull_request' not in event:
        print('::set-output name=status::FAIL')
        sys.exit(1)

    branch_label = event['pull_request']['head']['label']  # author:branch
    author = branch_label.split(':')[0]

    repo = gh.get_repo(event['repository']['full_name'])

    auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)

    tweet = f'Congratulations @{author} on opening a pull request' + \
        f' on the repository: {repo.full_name} Time to celebrate!!' + \
        ' *This tweet was sent courtesy of actions_to_celebrate ' + \
        'github action 💜'

    status = api.update_status(status=tweet)
    print(f'::set-output name=status::{status}')

    sys.exit(0)


if __name__ == "__main__":
    main()
