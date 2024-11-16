from src.infrastructure.application import create_app
from src.api import UserRouter, AuthRouter, ProjectRouter, AttachmentsRouter
from src.config import ROOT_PATH

app = create_app(
    routers=[
        UserRouter,
        AuthRouter,
        ProjectRouter,
        AttachmentsRouter
    ],
    root_path=ROOT_PATH,
    # ignoring_log_endpoints=[("/system/ping", "GET")]
)