# Model-Service
The model-service represents a wrapper service for the released ML model. It offers a REST API
to exposes the model to other components and make it scalable. \
[GitHub Pages](https://remla24-team-15.github.io/model-service/)

## Setup Instructions 
If you want to run it locally, cd to the  `model-service` repository and execute the `run.sh` file. 

### To Run with Docker
Make sure you have docker running locally 

1. Clone the repository:
```bash 
$ git clone https://github.com/REMLA24-TEAM-15/model-service
$ cd model-service
```
2. Load the Github package registry:
```bash
$ docker pull ghcr.io/remla24-team-15/model-service:2.6.latest
$ docker run -p 8081:8081 --name model-service -it ghcr.io/remla24-team-15/model-service:2.6.latest
```

3. To build and run docker container Locally:
```bash
$ docker-compose build --no-cache
$ docker compose up 
```

## API USAGE 
You can test this service using the [app-front-end](https://github.com/REMLA24-TEAM-15/app) or follow instructions below: 
1. Use Postman to make a ```POST Predict``` for example : "http://127.0.0.1:8081/predict" with body :
```bash
{"link": "spam or ham"}
 ```
sample response :
```bash 
{
    "Link": " spam or ham",
    "Prediction": [
        0
    ]
}
```


## Tokens Required:
For this repository you require a GitHub token (e.g GH_Token) with package and repo read/write permissions. 
