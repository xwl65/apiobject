import requests
import yaml
from string import Template
from api.base_api import BaseApi

class GetToken(BaseApi):
    corpid = "ww5ec2ae9af30fe1f4"
    corp_secret = "S8W26qDor05ykYGwPmB-TNEUOscqtIwMpr1TPqf2QJU"

    #完成模板替换，将yml文件里面的变量进行替换

    #自己定义的template建议放在baseapi里面
    def template(self):
        with open("../api/get_token.yml") as f:
            data = {
                "corpid":self.corpid,
                "corpsecret": self.corp_secret
            }
            #re = Template(f.read()).substitute(corpid = self.corpid,corpsecret=self.corp_secret)
            re = Template(f.read()).substitute(data)
            #re还是string类型，用safe_load之后就可以将其转换为字典
            return yaml.safe_load(re)

    def get_token(self, yml=None):

        # url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        #
        # params = {
        #     "corpid": self.corpid,
        #     "corpsecret": self.corp_secret
        #
        # }
        # req = {
        #     "method":"get",
        #     "url":"https://qyapi.weixin.qq.com/cgi-bin/gettoken",
        #     "params" : {
        #     "corpid": self.corpid,
        #     "corpsecret": self.corp_secret
        #
        #      }
        #
        # }

        # req = yaml.safe_load(open("../api/get_token.yml"))
        #r = requests.get(url=url, params=params)
        req = self.template()
        r= self.requests_http(req)
        return r


