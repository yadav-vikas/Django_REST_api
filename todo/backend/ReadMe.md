# Todo App

### This is Todo API using DRF
 
todo

| ├──frontend
      ├──React...

| ├──backend
   ├──Django...


this is AllowAny authentication method which means any requested is accepted in this API.

### Serializers : To convert data into other usable format(like JSON)


Command Line
--------------------------------------------------------------------------------

```
pip install requirements.txt

OR

pipenv lock requirements.txt
```

#### To run this project

```
python manage.py runserver
```

Open this link ( http://127.0.0.1:8000/api/ ) in your browser.

for each Todo endpoint :: e.g. 1st Todo-- http://127.0.0.1:8000/api/1

## Features: CORS 

Whenever a client interacts with an API hosted on a different domain
(mysite.com vs yoursite.com) or port (localhost:3000 vs localhost:8000) there are
potential security issues.
Specifically, CORS requires the server to include specific HTTP headers that allow for
the client to determine if and when cross-domain requests should be allowed.
Our Django API back-end will communicate with a dedicated front-end that is located
on a different port for local development and on a different domain once deployed.


#### read docs : https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS

## React App ::  http://localhost:3000/



