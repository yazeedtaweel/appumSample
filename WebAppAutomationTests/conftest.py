import os


# Remote appium server URL
Appium_URL =  "https://click-ins-public.perfectomobile.com/nexperience/perfectomobile/wd/hub"


# Appium capabilities

desired_cap = {
    "securityToken": "eyJhbGciOiJIUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICI0NjRmODFiOC1hM2M2LTQ1MzUtYmI3Yy05ZTY5NTQ2Y2VjODQifQ."
                     "eyJpYXQiOjE2MTk1MTQ0NjQsImp0aSI6IjFhZDc1MDk1LWRmOTktNDY5MC1iM2RhLTVmMjdjOTkzZTAzZiIsImlzcyI6Imh0dHBzOi8vYX"
                     "V0aDMucGVyZmVjdG9tb2JpbGUuY29tL2F1dGgvcmVhbG1zL2NsaWNrLWlucy1wdWJsaWMtcGVyZmVjdG9tb2JpbGUtY29tIiwiYXVkIjoiaH"
                     "R0cHM6Ly9hdXRoMy5wZXJmZWN0b21vYmlsZS5jb20vYXV0aC9yZWFsbXMvY2xpY2staW5zLXB1YmxpYy1wZXJmZWN0b21vYmlsZS1jb20iLCJ"
                     "zdWIiOiJiNWY2NDk4Ni03ODYzLTQxN2EtYjcwNC03NTBlMjMzMDIxNTkiLCJ0eXAiOiJPZmZsaW5lIiwiYXpwIjoib2ZmbGluZS10b2tlbi1nZ"
                     "W5lcmF0b3IiLCJub25jZSI6IjY4MGRiYTVlLTRlNTktNGQ4ZC04MmNjLTBjMDFkMjAxOWUzOCIsInNlc3Npb25fc3RhdGUiOiIyMzM5OGE0Ni05"
                     "OTJjLTQ1MTktYTVlMC1kYTlmODNhMWQ4N2EiLCJzY29wZSI6Im9wZW5pZCBvZmZsaW5lX2FjY2VzcyBwcm9maWxlIGVtYWlsIn0"
                     ".ycfjb6XIDI1SLHREANbRSx7Ea4fYl-IDCNJsFcYSIAI",

    "environments": [{
        'platformName': 'Android',
        'platformVersion': '9',
        'location': 'NA-US-BOS',
        'resolution': '1080x2280',
        'manufacturer': 'Samsung',
        'model': 'Galaxy Note10'
        },
        {
        'platformName': 'Android',
        'platformVersion': '11',
        'location': 'EU-DE-FRA',
        'resolution': '1440x3200',
        'manufacturer': 'Samsung',
        'model': 'Galaxy S20'
        },
        {
        'platformName': 'Android',
        'platformVersion': '10',
        'location': 'NA-US-BOS',
        'resolution': '1080x2400',
        'manufacturer': 'Samsung',
        'model': 'Galaxy A70'
        }
    ]
}


}


# Page Elements Time Out
pageElementsTimeOut = 300


def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="qa")
    parser.addoption("--remote", action="store", default="perfecto_android")


def pytest_configure(config):
    os.environ['env'] = config.getoption('--env')
    os.environ['remote'] = config.getoption('--remote')
