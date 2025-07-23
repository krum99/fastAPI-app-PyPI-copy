import datetime
from typing import List

from starlette.requests import Request

from data.release import Release
from services import package_service, user_service
from viewmodels.shared.viewmodel import ViewModelBase


class DetailsViewModel(ViewModelBase):
    def __init__(self, package_name: str, request: Request):
        super().__init__(request)

        self.x = 9
        self.package_name = package_name
        self.package = package_service.get_package_by_id(package_name)
        self.latest_release = package_service.get_latest_release_for_package(package_name)
        self.latest_version = "0.0.0"
        self.is_latest = True
        self.maintainers = []

        if not self.package or not self.latest_release:
            return
        # self.latest_version = self.latest_version.version
        # self.maintainers = self.package.maintainers



    # return {
    #     'package_count': 274_000,
    #     'release_count': 2_234_847,
    #     'user_count': 73_874,
    #     'packages': [
    #         {'id': 'fastapi', 'summary': 'A great web framework'},
    #         {'id': 'uvicorn', 'summary': 'Your favorite ASGI server'},
    #         {'id': 'httpx', 'summary': 'Requests for an async world'},
    #     ],
    # }