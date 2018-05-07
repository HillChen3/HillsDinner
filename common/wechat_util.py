from wechatpy import WeChatClient
APPID = 'wx1010fd146b9b290c'
APPSECRET = '28d394c4e3b83b4145642eec67a5c5d4'
class Menu:
    def creatMenu(self):
        client = WeChatClient(APPID, APPSECRET)
        client.menu.create({
            "button": [
                {
                    "type": "click",
                    "name": "今日歌曲",
                    "key": "V1001_TODAY_MUSIC"
                },
                {
                    "type": "click",
                    "name": "歌手简介",
                    "key": "V1001_TODAY_SINGER"
                },
                {
                    "name": "菜单",
                    "sub_button": [
                        {
                            "type": "view",
                            "name": "搜索",
                            "url": "http://www.soso.com/"
                        },
                        {
                            "type": "view",
                            "name": "视频",
                            "url": "http://v.qq.com/"
                        },
                        {
                            "type": "click",
                            "name": "赞一下我们",
                            "key": "V1001_GOOD"
                        }
                    ]
                }
            ]
        })