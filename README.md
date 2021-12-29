
# Pokemon APP

**Pokemon App** is a FastAPI and Reactjs Fullstack Application where people can register and login to there account. And User able to add and remove pokemon in his favourite list.

## Live
Comming

## Tech Stack

**Frontend:** Reactjs,ReactRouter,React-Hook-Form,Bootstrap,ContextAPI,

**Backend:** Python,FastAPI,Sqlalchemy(ORM)






  
## Features

- Register with `username`,`email` and `password`
- Login with `username` and `password`
- All Pokemon in the Home screen
- Add pokemon to user's favourite list
- Remove pokemon from user's favourite list

  
## Run Locally

Clone the project

```bash
  git clone https://github.com/icerahi/pokemon_app
```

Go to the project directory

```bash
  cd pokemon_app
```
### Setup backend 
 Go to project backend directory and write

```bash
  cd backend
  virtualenv -p python3 venv 
  source venv/bin/activate
  pip install -r requirements.txt
  uvicorn main:app --reload
```

### Setup frontend
Go to frontend directory

```bash
  cd frontend
```
And inside the src folder open the .env file and comment down `production domain` and uncomment `localdomain`

```bash
  npm start
```
It will open the Project in your default browser: http://localhost:3000

  
## Authors

- [Imran Hasan Rahi](https://linkedin.com/in/icerahi)

  
