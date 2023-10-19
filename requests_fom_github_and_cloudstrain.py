# on query string limit params:
# https://helpcenter.veeam.com/docs/vac/rest/limit_query_v3.html?ver=70

# requests simple tutorial:
# https://realpython.com/python-requests/

import requests
import pandas as pd
# https://www.youtube.com/watch?v=zmdjNSmRXF4&list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS&index=2&ab_channel=CoreySchafer
# https://ourcodingclub.github.io/tutorials/pandas-python-intro/

def get_status():
    url = 'https://api.github.com/search/repositories?q=language:python&sort=stars&limit=0'
    headers = {'Accept': 'application/vnd.github.v3+json'}
    response = requests.get(url, headers=headers)
    return response.status_code, response.content, response.headers  # the raw bytes of the response payload

def print_requests_repo_from_github():
    response = requests.get(
        'https://api.github.com/search/repositories',
        params={'q': 'requests+language:python'}, # query string 
        headers={'Accept': 'application/vnd.github.v3.text-match+json'},
    )
    
    # # Inspect some attributes of the `requests` repository
    # json_response = response.json()
    # repository = json_response['items'][0]
    # print(f'Repository name: {repository["name"]}')  # Python 3.6+
    # print(f'Repository description: {repository["description"]}')  # Python 3.6+
    
    # View the new `text-matches` array which provides information
    # about your search term within the results
    json_response = response.json()
    repository = json_response['items'][0]
    print(f'Text matches: {repository["text_matches"]}')

def eric_matthens_call():
    # Make an API call and store the response.
    url = 'https://api.github.com/search/repositories?q=language:ruby&sort=stars'
    headers = {'Accept': 'application/vnd.github.v3+json'}
    r = requests.get(url, headers=headers)
    # print(f"Status code: {r.status_code}")

    # Store API response in a variable.
    response_dict = r.json()
    # print(f"Total repositories: {response_dict['total_count']}")
    # print(f'{response_dict.keys()}')

    # Explore information about the repositories.
    repo_dicts = response_dict['items']
    # print(f"Repositories returned: {len(repo_dicts)}")

    # print("\nSelected information about each repository:")
    # for repo_dict in repo_dicts:
    #     print(f"Name: {repo_dict['name']}")
    #     print(f"Owner: {repo_dict['owner']['login']}")
    #     print(f"Stars: {repo_dict['stargazers_count']}")
    #     print(f"Repository: {repo_dict['html_url']}")
    #     print(f"Created: {repo_dict['created_at']}")
    #     print(f"Updated: {repo_dict['updated_at']}")
    #     print(f"Description: {repo_dict['description']}")
    return r.status_code

def eric_matthens_call_():
    # Make an API call and store the response.
    url = 'https://api.github.com/search/repositories?q=language:ruby&sort=stars'
    headers = {'Accept': 'application/vnd.github.v3+json'}
    r = requests.get(url, headers=headers)
    response_dict = r.json()
    repo_dicts = response_dict['items']
    return repo_dicts

def cloud_strain_t_sect_save():
    """
    POST to CloudStrain with save of json
    """
        url = 'https://django-civil-85.herokuapp.com/api/civil_calcs/t_sect_ben_reinf_withsave'
        headers={'Authorization': 'Token 75c716e4fabb1fc1c215a6c22d4fc6757fb7e3ea'}
        json={"title": "t_sect_no_11",
              "the_input_json":{
                  "name": "my first T cross sect.",
                  "b": 0.5,
                  "h": 1.2,
                  "h_sl": 0.2,
                  "b_eff": 1,
                  "cl_conc": "C30_37",
                  "cl_steel": "BSt500S",
                  "c": 30,
                  "fi": 32,
                  "fi_s": 12,
                  "fi_opp": 16,
                  "m_sd": 5000
                  }}
        response = requests.post(url=url, headers=headers, json=json)
        return response.json()

def cloud_strain_t_sect():
    """
    POST to CloudStrain without save of json
    """
        url = 'https://django-civil-85.herokuapp.com/api/civil_calcs/t_sect_ben_reinf'
        json={
                "name": "my first T cross sect.",
                "b": 0.5,
                "h": 1.2,
                "h_sl": 0.2,
                "b_eff": 1,
                "cl_conc": "C30_37",
                "cl_steel": "BSt500S",
                "c": 30,
                "fi": 32,
                "fi_s": 12,
                "fi_opp": 16,
                "m_sd": 1
            }
        response = requests.post(url=url, json=json)
        return response.json()

def to_pandas(_dict):
    ppp = {'a': 2}
    return pd.DataFrame(_dict)

if __name__ == '__main__':
    print(pd.DataFrame(cloud_strain_t_sect(), index=[0]))