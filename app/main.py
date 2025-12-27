from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from app.middleware.logging_middleware import LoggingMiddleware
from app.api import routes_auth, routes_predict
from app.core.exceptions import register_exception_handlers

app = FastAPI(title="Fast Christmas", version="1.0.0")

#linking middleware
app.add_middleware(LoggingMiddleware)

#linking endpoints
app.include_router(routes_auth.router, tags=["Authentication"])
app.include_router(routes_predict.router, tags=["Prediction"])

#monitoring
Instrumentator().instrument(app).expose(app)

#exception handling
register_exception_handlers(app)