from application.api.v1.handlers import router
from fastapi import FastAPI


def create_app():
    app = FastAPI(
        title = 'microservice',
        docs_url = '/api/docs',
        description = 'api for transactions',
        debug = True,
    )

    app.include_router(router, prefix='/api/v1')

    return app
