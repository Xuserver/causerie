import requests

def get_popular_projects(language=None, count=10):
    if language:
        url = f"https://api.github.com/search/repositories?q=language:{language}&sort=stars&order=desc"
    else:
        url = "https://api.github.com/search/repositories?q=stars:>1&sort=stars&order=desc"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        projects = data['items'][:count]
        return projects
    else:
        print("Error fetching data:", response.status_code)
        return None

def listpopular(language=None):
    popular_projects = get_popular_projects(language=language)
    if popular_projects:
        print(f"Les projets les plus populaires sur GitHub ({language}) :")
        for index, project in enumerate(popular_projects, start=1):
            print(f"{index}. {project['name']} - {project['html_url']} (Étoiles : {project['stargazers_count']})")
    else:
        print("Aucun projet n'a été trouvé.")


# listpopular()

listpopular("sql")

listpopular("javascript")
