## Process:
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
14) setup app/middleware/logging_middleware.py : capture the rsponse of the middleware
15) setup app/main.py : put everything together
16) setup Dockerfile : 
17) setup prometheus.yml :
18) setup docker-compose.yml :
19) setup requirements.txt : 

## Testing locally:
1) run docker-compose up --build : will just install the necessary libraries and run all the services in containers
2) debug all the issues one by one


# Code wise operation explainations:
1. Core Configuration & Security

```app/core/config.py```
Purpose: Centralizes application settings and environment variables.

Line-by-Line:

load_dotenv(): Loads variables from a .env file into the environment.

class Settings: Defines the schema for configuration.

API_KEY, JWT_SECRET_KEY, REDIS_URL: Uses os.getenv to fetch values, providing defaults if not found.

MODEL_PATH: Hardcoded path to the serialized model file.

settings = Settings(): Instantiates the class for global use.

Referenced By: app/core/security.py, app/core/dependencies.py, app/cache/redis_cache.py, and app/services/model_service.py.

app/core/security.py
Purpose: Manages JWT (JSON Web Token) creation and validation.

Line-by-Line:

create_token(...): Takes a data dictionary and expiration time.

datetime.now(timezone.utc): Ensures timestamps are in UTC.

jwt.encode(...): Signs the payload using the JWT_SECRET_KEY.

verify_token(...): Decodes a token; returns None if JWTError occurs (invalid/expired).

Referenced By: app/api/routes_auth.py (token generation) and app/core/dependencies.py (token validation).

app/core/dependencies.py
Purpose: Provides reusable security checks (Dependencies) for FastAPI routes.

Line-by-Line:

get_api_key(...): Extracts api_key from request headers. Throws 403 if it doesn't match settings.API_KEY.

get_current_user(...): Extracts token from headers. Calls verify_token and throws 401 if invalid.

Referenced By: app/api/routes_predict.py to secure the prediction endpoint.

2. Data Processing & Caching
app/cache/redis_cache.py
Purpose: Interfaces with Redis to store/retrieve prediction results.

Line-by-Line:

redis.Redis.from_url(...): Connects to the Redis instance.

get_cache_prediction(key): Fetches a value and parses it from JSON.

set_cache_prediction(...): Uses setex to store a value with a 1-hour (3600s) Time-To-Live.

Referenced By: app/services/model_service.py.

app/services/model_service.py
Purpose: The bridge between the API and the Machine Learning model.

Line-by-Line:

model = joblib.load(...): Loads the pre-trained model into memory at startup.

cache_key = ' '.join(...): Creates a unique string from input features to use as a Redis key.

if cached: return cached: Returns the result immediately if found in Redis.

pd.DataFrame([data]): Formats dictionary input into a DataFrame for the model.

Referenced By: app/api/routes_predict.py.

3. API Endpoints & Middleware
app/api/routes_auth.py
Purpose: Handles user login and token issuance.

Line-by-Line:

AuthInput: Pydantic model for validating login request bodies.

if auth_input.username == "admin"...: Checks hardcoded dummy credentials.

create_token(...): Generates the JWT upon successful login.

Referenced By: app/main.py.

app/api/routes_predict.py
Purpose: Main endpoint for car price predictions.

Line-by-Line:

CarFeatures: Pydantic model defining the 11 required car attributes (year, engine_cc, etc.).

user=Depends(get_current_user): Ensures requester has a valid JWT.

_=Depends(get_api_key): Ensures requester has the correct API Key header.

Referenced By: app/main.py.

app/middleware/logging_middleware.py
Purpose: Logs every request and response status code.

Line-by-Line:

dispatch(...): Intercepts the request.

await call_next(request): Passes the request to the next handler and waits for the response.

Referenced By: app/main.py.

app/main.py
Purpose: Entry point of the FastAPI application.

Line-by-Line:

app = FastAPI(...): Initializes the app instance.

app.add_middleware(LoggingMiddleware): Enforces logging for all routes.

app.include_router(...): Registers authentication and prediction routes.

Instrumentator().instrument(app).expose(app): Sets up the /metrics endpoint for Prometheus.

register_exception_handlers(app): Attaches global error handling.

Referenced By: Dockerfile (via Uvicorn).

4. Training Pipeline
app/training/train_utils.py
Purpose: Standardizes file paths for data and models.

Line-by-Line:

APP_DIR: Calculates the base directory of the project.

DATA_FILE_PATH, MODEL_PATH: Joins directories and filenames into absolute paths.

Referenced By: app/training/train_model.py.

app/training/train_model.py
Purpose: Preprocesses data and trains the Random Forest model.

Line-by-Line:

.drop(columns=...): Removes non-predictive columns (name, owner, etc.).

num_pipe / cat_pipe: Pipelines for handling missing values and scaling/encoding.

ColumnTransformer: Applies numerical logic to numbers and categorical logic to strings.

rf_model.fit(...): Trains the model on the preprocessed training set.

joblib.dump(...): Saves the model to the path specified in train_utils.

5. Infrastructure & DevOps
Dockerfile: Builds a Python 3.12 image, installs dependencies from requirements.txt, and starts the Uvicorn server.

docker-compose.yml: Orchestrates four services (api, redis, prometheus, grafana) on a shared backend network.

prometheus.yml: Configures Prometheus to scrape metrics from the API every 10 seconds.