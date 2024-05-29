Docker container that serves a machine trained model. To be used with the

## Release in a docker image

1. **Build docker image:**
   ```bash
   sudo docker build -t model-service .
   ```

2. **Run docker conatiner on port 8081:**
   ```bash
   sudo docker run -p8081:8081 model-service
   ```

## Dependencies
Dependencies can be installed with poetry.
   ```bash
   poetry install --no-root
   ```