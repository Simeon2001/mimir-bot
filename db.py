import requests
from requests.structures import CaseInsensitiveDict
import json
import os
from dotenv import load_dotenv
import hashlib

load_dotenv()
headers = CaseInsensitiveDict()

headers["Content-Type"] = "application/json"
headers["apikey"] = os.getenv("DB_KEY")
headers["Authorization"] = "Bearer {0}".format(os.getenv("DB_KEY"))


def read_db(msg_id):
    url_selectidd = "https://zmtgekaignlkvgsgetuv.supabase.co/rest/v1/MimirUser?msg_id=eq.{0}".format(
        msg_id
    )
    res = requests.get(url_selectidd, headers=headers)
    v = res.json()
    if v == []:
        return {"code": 0}
    count = v[0]["count"]
    status = v[0]["status"]
    super_user = v[0]["super_user"]
    return {"code": 1, "count": count, "status": status, "su": super_user}


def create_db(msg_id):
    create_url = "https://zmtgekaignlkvgsgetuv.supabase.co/rest/v1/MimirUser"
    info = {"msg_id": msg_id, "status": True}
    data = json.dumps(info, indent=2)
    res = requests.post(create_url, headers=headers, data=data)
    # v = res.json()
    return res.status_code


def update_db(msg_id, count, status=True):
    update_url = "https://zmtgekaignlkvgsgetuv.supabase.co/rest/v1/MimirUser?msg_id=eq.{0}".format(
        msg_id
    )
    info = {"count": count, "status": status}
    data = json.dumps(info, indent=2)
    res = requests.patch(update_url, headers=headers, data=data)

    return res.status_code
