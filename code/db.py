import requests
import json

url = "https://data.nantesmetropole.fr/api/records/1.0/search/?dataset=244400404_nombre-convives-jour-cantine-nantes-2011&q=&facet=site_type&facet=site_nom_sal"
response = (requests.get(url)
                    .json())

data = [row['fields'] for row in response['records']]