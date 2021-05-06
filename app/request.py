import urllib.request, json


#getting urls
api_key = None

base_url = None

repo_url = None

user_url = None




def configure_request(app):
    global base_url, api_key,repo_url,user_url
    base_url = app.config['BASE_URL']
    api_key = app.config['API_KEY']
    repo_url = app.config['REPO_URL']
    user_url = app.config['USER_URL']


def search_user(username, page):
    userurl = user_url.format(username,page)

    with urllib.request.urlopen(userurl) as url:
        get_user_info = url.read()
        get_user_response = json.loads(get_user_info)

        user_results = {}

        if get_user_response['items']:
            user_results['repos_url'] = get_user_response['repos_url']
            user_results['html_url'] = get_user_response['html_url']

        return user_results


            
            
            

    return user_results 