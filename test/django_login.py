import ast, json, subprocess
try:
    import requests
except ModuleNotFoundError:
    subprocess.run(['python', '-m', 'pipenv', 'install', 'requests'])
finally:
    import requests

payload = {
    'username'              :  '',
    'password'              :  '',
}

with requests.Session() as session:
    res = session.post(
        'https://127.0.0.1:8000/api/login/',
        data = payload,
        verify=False
    )
    print(res.content)
    token = ast.literal_eval(res.content.decode("UTF-8"))['token']
    res = session.get(
        'https://127.0.0.1:8000/api/home/',
        verify=False,
        headers={"Authorization":f"Token {token}"}
    )
    print(res.status_code)
    print(res.content.decode("UTF-8"))
    res = session.post(
        'https://127.0.0.1:8000/api/logoutall/',
        verify=False,
        headers={"Authorization":f"Token {token}"}
    )
    print(res.status_code)
