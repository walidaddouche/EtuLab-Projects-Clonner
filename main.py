# Press the green button in the gutter to run the script.
import os

if __name__ == '__main__':
    import requests
    import datetime

    # Récupère la liste des projets avec l'API de GitLab
    TOKEN = ""

    date_before = datetime.datetime.now() - datetime.timedelta(days=365 * 5)
    date_before_str = date_before.strftime("%Y-%m-%d")
    import requests

    reqUrl = f"https://etulab.univ-amu.fr/api/v4/projects?&created_after={date_before_str}&per_page=200&membership=true"

    headersList = {
        "Accept": "*/*",
        "User-Agent": "API CLIENT",
        "Private-Token": TOKEN
    }

    payload = ""

    response = requests.request("GET", reqUrl, data=payload, headers=headersList)

    projects = response.json()

    for project in projects:
        url_project = project["http_url_to_repo"]
        os.system(f"git clone {url_project}")
