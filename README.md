petstore api tests
https://petstore.swagger.io/

Python 3.10
Pytest 7.1.2
Allure 2.9.45

- Create venv

`python -m venv venv`

- Activate venv

`venv/Sripts/activate`

- Install requirements

`pip install -r requirements.txt`

- Run tests

`pytest -n=<thread>`

- Open allure report

`allure serve -h localhost`
