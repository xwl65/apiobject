
from api.get_token import GetToken


class Test_get_token:
    def setup(self):
        self.gettoken = GetToken()
    def test_get_token(self):
        assert self.gettoken.get_token().json()["errcode"] == 0
