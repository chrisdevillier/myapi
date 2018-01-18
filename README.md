# myapi

REST micro-service

Run Server app and then test with the following commands:

Python:

put('http://127.0.0.1:5000/message', data={'data': 'I have a sore throat and headache'}).json() get('http://localhost:5000/message').json()

On the command Line:

curl http://localhost:5000/todo1 -d "data=I have a sore throat and headache" -X PUT
