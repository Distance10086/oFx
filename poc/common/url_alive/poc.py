# coding:utf-8  
import requests
from lib.common import url_handle,get_random_ua

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

_info = {
    "author" : "jijue",                      # POC作者
    "version" : "1",                    # POC版本，默认是1  
    "CreateDate" : "2021-06-03",        # POC创建时间
    "UpdateDate" : "2021-06-03",        # POC创建时间
    "PocDesc" : """
    略  
    """,                                # POC描述，写更新描述，没有就不写

    "name" : "url存活检测",                        # 漏洞名称
    "AppName" : "各类web应用",                     # 漏洞应用名称
    "AppVersion" : "",                  # 
    "VulnDate" : "2021-06-03",                    # 漏洞公开的时间,不知道就写能查到的最早的文献日期，格式：xxxx-xx-xx
    "VulnDesc" : """
    略
    """,                                # 漏洞简要描述

    "fofa-dork":"略",                     # fofa搜索语句
    "example" : "",                     # 存在漏洞的演示url，写一个就可以了
    "exp_img" : "",                      # 先不管

    "timeout" : 10,
}

def verify(host,proxy):
    vuln = [False,""]
    url = url_handle(host)  # url自己按需调整

    # proxies = None
    

    headers = {"User-Agent":get_random_ua(),}
    try:
        req = requests.get(url,headers = headers,proxies = proxy,verify=False,timeout = 8)  

        if str(req.status_code)[0] !=4 and str(req.status_code)[0] !=5:
            vuln = [True,req.text]
    except Exception as e:
        raise e
    
    return vuln