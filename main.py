import requests
import pandas as pd


results = []

for bl in ["Research and development on medical sciences",
           "Research and experimental development on biotechnology",
           "Laboratory examinations"]:

    response = requests.get(
        url="http://avoindata.prh.fi/bis/v1",
        params={
            "maxResults": 999,
            "companyRegistrationFrom": "2015-01-01",
            "businessLine": bl,
        }
    )

    results += response.json()["results"]

df = pd.DataFrame(results)
df.to_excel("companies.xlsx")
