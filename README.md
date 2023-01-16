# Explanation of how we would install and run your submission

## Run locally
Create and activate a virtual environment with the following commands:
```
python3 -m venv venv 
source venv/bin/activate
```
Install the necessary packages for the project:
```
pip install -r requirements.txt
```
To run the application, use the following command:
```
uvicorn main:app --reload
```
To run unit tests, use the following command:
```
pytest -v
```
## Run in docker
Build image and run container:
```
docker build -t phone-numbers-api .
docker run --name phone_numbers -dp 80:80 phone-numbers-api
```
Docker cleanup 
```
docker rm phone_numbers
docker rmi phone-numbers-api
```

# Explanation of your choice of programming language, framework, library:
I believe that Python, paired with the FastAPI framework, is a logical choice for building APIs. The simplicity and ease of maintenance of Python, in combination with the high-performance and built-in support for testing of FastAPI, results in a robust and efficient solution for creating and maintaining APIs.

# Explanation of how you would deploy to production.
As a demonstration project, I would run it on an EC2 instance for simplicity and ease of setup. However, for a production-level application, it would be more appropriate to deploy it on a container orchestration platform such as Amazon ECS and use AWS Fargate in conjunction with an Elastic Load Balancer for better scalability and management. Ultimately, the choice of deployment method depends on various factors such as the expected load and limitations of the system, and it would be wise to consider these factors before making a final decision.

# Explanation of assumptions you made
- The number of digits in a local phone number can range from 6 to 8
- Area code is always 3 digit
- First suitable country code will be the result
- The endpoint should return information about a phone number in the response, it can be in the form of JSON
- The endpoint should be able to handle a large number of requests per second

# Explanation of improvements you wish to make
In order to further improve the reliability and maintainability of the API, I would definitely invest more time in creating additional utilities for testing and implementing test case factories. Additionally, encapsulating the logic and removing hardcoded cases would make the code more modular and less prone to errors. Another step that would be beneficial would be to utilize pydantic schemas for request and response data. This would not only improve performance but also make the code more organized and readable.
I would definitely consider alternative solutions for handling the mapping of dial codes to country codes, but for the purpose of this demonstration, I chose to simplify it as much as possible to keep the implementation straightforward.