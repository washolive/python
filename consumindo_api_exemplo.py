# Consumindo dados de uma API (exemplo: GitHub)
# Ref: livro "Data Science from Scratch" de Joel Grus

import requests, json
from dateutil.parser import parse

endpoint = "https://api.github.com/users/joelgrus/repos"
repos = json.loads(requests.get(endpoint).text)

ordered_repos = sorted(repos, key=lambda r: r["created_at"], reverse=True)

for repo in ordered_repos: 
    print("{:40} {:20}".format(repo['name'], repo['created_at']))

