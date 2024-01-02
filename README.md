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

## Available Endpoints

### 1. Index

- **Endpoint:** `/`
- **Method:** GET
- **Description:** Check if the email service is operational.

### 2. Send Verification Code Email

- **Endpoint**: `/email/send-verification-code`
- **Method**: POST
- **Description**: Send an email with a verification code.

### 3. Account Created - Pending

- **Endpoint**: `/email/account-pending`
- **Method**: POST
- **Description**: Send an email indicating that the account creation is pending.

### 4. Account Created - Successfully

- **Endpoint**: `/email/account-created`
- **Method**: POST
- **Description**: Send an email confirming the successful creation of the account.

### 5. Account Not Created - Successfully
- **Endpoint**: `/email/account-not-created`
- **Method**: POST
- **Request body**:
  - `message` : Description of the issue encountered during account creation by the administrator.
- **Description**: Send an email indicating a problem in creating the account.

### 6. Vehicle Created - Pending
- **Endpoint**: `/email/vihecule-pending`
- **Method**: POST
- **Description**: Send an email indicating that the vehicle creation is pending.

### 7. Vehicle Created - Successfully
- **Endpoint**: `/email/vihecule-created`
- **Method**: POST
- **Description**: Send an email confirming the successful creation of the vehicle.

### 8. Vehicle Not Created - Successfully
- **Endpoint**: `/email/vihecule-not-created`
- **Method**: POST
- **Request body**:
  - `message` : Description of the issue encountered during vihecule creation by the administrator.
- **Description**: Send an email indicating a problem in creating the vehicle.

### 9. Permit Created - Pending
- **Endpoint**: `/email/licence-driver-pending`
- **Method**: POST
- **Description**: Send an email indicating that the permit creation is pending.

### 10. Permit Created - Successfully
- **Endpoint**: `/email/licence-driver-created`
- **Method**: POST
- **Description**: Send an email confirming the successful creation of the permit.

### 11. Permit Not Created - Successfully
- **Endpoint**: `/email/licence-driver-not-created`
- **Method**: POST
- **Request body**:
  - `message` : Description of the issue encountered during licence driver creation by the administrator.
- **Description**: Send an email indicating a problem in adding the permit.

### 12. Assurance Created - Pending
- **Endpoint**: `/email/assurance-pending`
- **Method**: POST
- **Description**: Send an email indicating that the assurance creation is pending.

### 13. Assurance Created - Successfully
- **Endpoint**: `/email/assurance-created`
- **Method**: POST
- **Description**: Send an email confirming the successful creation of the assurance.

### 14. Assurance Not Created - Successfully
- **Endpoint**: `/email/assurance-not-created`
- **Method**: POST
- **Request body**:
  - `message` : Description of the issue encountered during assurance creation by the administrator.
- **Description**: Send an email indicating a problem in adding the assurance.

### 15. Documentation
- **Endpoint**: `/docs`
- **Method**: GET
- **Description**: Retrieve API documentation using Swagger UI.











## Stay in touch :
- Author - [Ouail Laamiri](https://www.linkedin.com/in/ouaillaamiri/)
- Test - [Postman](https://www.postman.com/avionics-meteorologist-32935362/workspace/postman-api-fundamentals-student-expert/collection/29141176-d8a87c81-7d33-47bc-b379-e379f417a314?action=share&creator=29141176)
- Documentation - [Postman](https://documenter.getpostman.com/view/29141176/2s9Ykt3e4o
)

## License

Email-Service is [MIT licensed](LICENSE).

