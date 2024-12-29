# image-server
Custom server for handling product images

# Running the server locally
To run the server locally using poetry, you need set up the environment using the following commands:
```
pyenv install 3.12 
pyenv local 3.12 
poetry config virtualenvs.in-project true
poetry env use $(pyenv which python)
source .venv/bin/activate
```

Then you can install the dependencies using the following commands:
```
poetry lock
poetry install
```

Then you can run the server using the following commands:
```
poetry run uvicorn image_server.main:app --host 0.0.0.0 --port 8000
```

# Running the server in a container
To run the server in a container, you need to build the container using the following commands:
```
docker compose build
docker compose up
```