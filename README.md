## Description

Email-Service is an Application Programming Interface (API) to send emails to the customer of ZOHS assurance company.
## Installation :
```bash
# install requirements
$ pip install -r requirements.txt 
```
## Running the app : 
```bash
# Run application
$ gunicorn -c gunicorn_config.py main:app
```
## Build Docker image : 
```bash
# build a docker image
$ docker build -t email-service .
```
## Running the app in the Docker : 
```bash
# Run docker image
$ docker run -p 5000:5000 email-service
```
## Stay in touch :
- Author - [Ouail Laamiri](https://www.linkedin.com/in/ouaillaamiri/)
- Test - [Postman](https://www.postman.com/avionics-meteorologist-32935362/workspace/postman-api-fundamentals-student-expert/collection/29141176-d8a87c81-7d33-47bc-b379-e379f417a314?action=share&creator=29141176)
- Documentation - [Postman](https://documenter.getpostman.com/view/29141176/2s9Ykt3e4o
)

## License

Email-Service is [MIT licensed](LICENSE).

