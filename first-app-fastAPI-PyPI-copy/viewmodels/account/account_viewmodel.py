from starlette.requests import Request
from viewmodels.shared.viewmodel import ViewModelBase
from data.user import User


class AccountViewModel(ViewModelBase):
    def __init__(self, request: Request):
        super().__init__(request)
        self.user = User('Krum', 'krum@myemail.com', 's65dvsdbds91v')