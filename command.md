### To run app : 
gunicorn -c gunicorn_config.py main:app
### Build Docker image : 
docker build -t email-service .
### Run the Docker container : 
docker run -p 5000:5000 email-service