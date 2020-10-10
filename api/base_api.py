import requests
class BaseApi:
    def requests_http(self, req):
        # req = {
        #     "method":"get",
        #     "url":"https://qyapi.weixin.qq.com/cgi-bin/gettoken",
        #     "params" : {
        #         "corpid": self.corpid,
        #         "corpsecret": self.corp_secret
        #
        #      }
        # }

        return  requests.request(**req)
