
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
  git clone https://github.com/icerahi/pokemonApp.git
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

## Screenshots
![Login](https://user-images.githubusercontent.com/32910469/147687152-984cd1d5-0c77-407d-9b5a-448e1593e2c2.png)

![Home](https://user-images.githubusercontent.com/32910469/147687157-ce60d878-382a-4e09-bc7a-8ec042269814.png)

 ![Favourite List](https://user-images.githubusercontent.com/32910469/147686907-e9d25e87-1cdd-4742-944e-da0783ab3328.png)

## Authors

- [Imran Hasan Rahi](https://linkedin.com/in/icerahi)

  
