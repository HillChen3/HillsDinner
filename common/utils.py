#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import requests

# 请求的头部内容
# 以下的 Id 与 Key 都是无效的仅做示范，在实际试验中请替换成自己的 Id 与 Key
headers = {
    "X-LC-Id": "gVXbnCt49hgnscLzHlKfXBue-gzGzoHsz",
    "X-LC-Key": "d9KhEJyTCDsIpdKNC1HnXNR8",
    "Content-Type": "application/json",
}

# 请求发送验证码 API
REQUEST_SMS_CODE_URL = 'https://api.leancloud.cn/1.1/requestSmsCode'

# 请求校验验证码 API
VERIFY_SMS_CODE_URL = 'https://api.leancloud.cn/1.1/verifySmsCode/'


def send_message(phone):
    """
    通过 POST 请求 requestSmsCode API 发送验证码到指定手机
    :param phone: 通过网页表单获取的电话号
    :return:
    """
    data = {
        "mobilePhoneNumber": phone,
        "ttl": 10,
        "name": "wechat",
    }

    # post 方法参数包含三部分，如我们之前分析 API 所述
    # REQUEST_SMS_CODE_URL: 请求的 URL
    # data: 请求的内容，另外要将内容编码成 JSON 格式
    # headers: 请求的头部，包含 Id 与 Key 等信息
    r = requests.post(REQUEST_SMS_CODE_URL, data=json.dumps(data), headers=headers)

    # 响应 r 的 status_code 值为 200 说明响应成功
    # 否则失败
    if r.status_code == 200:
        return True, "send SMS successfully to " + phone
    return False, "send SMS failed to " + phone


def verify(phone, code):
    """
    发送 POST 请求到 verifySmsCode API 获取校验结果
    :param phone: 通过网页表单获取的电话号
    :param code: 通过网页表单获取的验证码
    :return:
    """
    # 使用传进的参数 code 与 phone 拼接出完整的 URL
    target_url = VERIFY_SMS_CODE_URL + "%s?mobilePhoneNumber=%s" % (code, phone)

    # 这里的 POST 方法只传入了两个参数
    # target_url： 请求的 URL
    # headers: 请求的头部，包含 Id 与 Key 等信息
    r = requests.post(target_url, headers=headers)

    # 响应 r 的 status_code 值为 200 说明验证成功
    # 否则失败
    if r.status_code == 200:
        return True
    else:
        return False


def check_phone_num(phone_num):
    if len(phone_num) == 11:
        return verify_num(phone_num)
    elif len(phone_num) == 14 or len(phone_num) == 13:
        if phone_num[0:3] in ("+86", "086"):
            return verify_num(phone_num[3:])
        if phone_num[0:2] == "86":
            return verify_num(phone_num[2:])
    return False


cn_mobile = [134, 135, 136, 137, 138, 139, 150, 151, 152,
             157, 158, 159, 182, 183, 184, 187, 188, 147, 178, 1705]
cn_union = [130, 131, 132, 155, 156, 185, 186, 145, 176, 1709]
cn_tel = [133, 153, 180, 181, 189, 173, 177, 1700]


def verify_num(phone_num):
    v_number = int(phone_num[:3])

    cnm = v_number in cn_mobile  # 验证为移动
    cnu = v_number in cn_union  # 验证为联通
    cnt = v_number in cn_tel  # 验证为电信

    if cnm or cnu or cnt:
        return True
    else:
        return False
