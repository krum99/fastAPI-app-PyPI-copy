from starlette.requests import Request
from viewmodels.shared.viewmodel import ViewModelBase


class RegisterViewModel(ViewModelBase):

    def __init__(self, request: Request):
        super().__init__(request)

        self.name = None
        self.password = None
        self.email = None

    async def load(self):
        form = await self.request.form()

        self.name = form.get('name')
        self.password = form.get('password')
        self.email = form.get('email')

        if not self.name or not self.name.strip():
            self.error = "Name is required."
        elif not self.email or not self.name.strip():
            self.error = "Email is required."
        elif not self.password or len(self.password) < 5:
            self.error = "Password is required and must be at least five characters."
