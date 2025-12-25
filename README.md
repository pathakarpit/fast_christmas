# fast_christmas
A project built on christmas morning to showcase implementation of FastAPI with AI

Process:
1) setup .env file : simply setup the environment variables (will not be included in git)
2) setuo app/core/config.py : create the app folder and include the __init__.py file to read it as a package. Define the configuration variables.
3) setuo app/core/security.py : define the functions for creating and verifying tokens.
4) setup app/core/dependencies.py : bridge the dependencies for authorisation
5) setup app/core/exceptions.py : handle exceptions (500 types)
6) setup app/api/routes_auth.py : make sure to create __init__.py file in api folder. create function for authorisations.
