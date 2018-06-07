# save all constant

# constant of wechat
class wechatConstants:
    URL = 'http://www.aceyouth.org'
    TOKEN = '123456'
    APPID = 'wx1010fd146b9b290c'
    APPSECRET = '28d394c4e3b83b4145642eec67a5c5d4'
    MENU_DATA = {
        "button": [
            {
                "name": "社群",
                "sub_button": [
                    {
                        "type": "view",
                        "name": "我的社群",
                        "url": "http://www.aceyouth.org"
                    },
                    {
                        "type": "view",
                        "name": "发起社群",
                        "url": "http://www.aceyouth.org"
                    },
                    {
                        "type": "view",
                        "name": "发现社群",
                        "url": "http://www.aceyouth.org"
                    },
                ]

            },
            {
                "name": "活动",
                "sub_button": [
                    {
                        "type": "view",
                        "name": "发现活动",
                        "url": "http://www.aceyouth.org"
                    },
                    {
                        "type": "view",
                        "name": "发起活动",
                        "url": "http://www.aceyouth.org"
                    },
                ]

            },
            {
                "name": "空间",
                "sub_button": [
                    {
                        "type": "view",
                        "name": "发现空间",
                        "url": "http://www.aceyouth.org"
                    },
                    {
                        "type": "view",
                        "name": "发起空间",
                        "url": "http://www.aceyouth.org"
                    },
                ]
            }
        ]
    }


def get_token():
    return wechatConstants.TOKEN


def get_appid():
    return wechatConstants.APPID


def get_appsecret():
    return wechatConstants.APPSECRET


def get_menudata():
    return wechatConstants.MENU_DATA


def get_URL():
    return wechatConstants.URL
