### To install requirements :
pip install -r requirements.txt 
### To run app : 
gunicorn -c gunicorn_config.py main:app
### Build Docker image : 
docker build -t email-service .
### Run the Docker container : 
docker run -p 5000:5000 email-service
### Link to test api via Postman :
https://www.postman.com/avionics-meteorologist-32935362/workspace/postman-api-fundamentals-student-expert/collection/29141176-d8a87c81-7d33-47bc-b379-e379f417a314?action=share&creator=29141176
### Documentation of api in postman :
https://documenter.getpostman.com/view/29141176/2s9Ykt3e4o
### Swagger documentation api :
/api/docs
