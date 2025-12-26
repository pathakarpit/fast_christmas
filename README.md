# fast_christmas
A project built on christmas morning to showcase implementation of FastAPI with AI

Process:
1) setup .env file : simply setup the environment variables (will not be included in git)
2) setuo app/core/config.py : create the app folder and include the __init__.py file to read it as a package. Define the configuration variables.
3) setuo app/core/security.py : define the functions for creating and verifying tokens.
4) setup app/core/dependencies.py : bridge the dependencies for authorisation
5) setup app/core/exceptions.py : handle exceptions (500 types)
6) setup app/api/routes_auth.py : make sure to create __init__.py file in api folder. create function for authorisations.
7) setup notebooks/test.ipynb : perform all the testing that needs to be done with the data and model creation
8) setup a directory `data` for storing the dataset
9) setup training/train_utils.py : create __init__.py file in the training folder. create utility functions and constants
10) setup training/train_model.py : create the file that will perform the decided actions on the test notebook and store the model in a saperate folder
11) setup app/cache/redis_cache.py : setup caching
12) setup app/services/model_service.py : load model, predict output, check cache for existing inputs
13) setup app/api/routes_predict.py : define fastAPI endpoint for the car price prediction by using a router and defining the model of input