from django.shortcuts import render
import requests
import datetime
import json
import random
from django.db import connection

# Create your views here.
def get_log(key):
    # 현재 날짜 및 시간
    current_time = datetime.datetime.now()
    # 현재 날짜 및 시간을 long 값으로 변환 (Unix 시간의 밀리초 버전)
    timestamp = int(current_time.timestamp() * 1000)
    # 현재 시간을 원하는 형식으로 출력
    time = current_time.strftime("%Y-%m-%d %H:%M:%S")

    events = {
        1:{'event': 'lgu_app_01', 'timestamp': timestamp, 'local_time': time, 'item_id': '01-001',
         'bt_desc': '식품-과일', 'access_type': 'phone', 'amount': random.randint(1,5)},
        2:{'event': 'lgu_app_01', 'timestamp': timestamp, 'local_time': time, 'item_id': '01-002',
         'bt_desc': '식품-견과/건과', 'access_type': 'web', 'amount': random.randint(1, 5)},
        3:{'event': 'lgu_app_01', 'timestamp': timestamp, 'local_time': time, 'item_id': '01-003',
         'bt_desc': '식품-채소', 'access_type': 'phone', 'amount': random.randint(1, 5)},
        4:{'event': 'lgu_app_01', 'timestamp': timestamp, 'local_time': time, 'item_id': '01-004',
         'bt_desc': '식품-쌀/잡곡', 'access_type': 'web', 'amount': random.randint(1, 5)},
        5:{'event': 'lgu_app_01', 'timestamp': timestamp, 'local_time': time, 'item_id': '01-005',
         'bt_desc': '식품-생수/음료', 'access_type': 'phone', 'amount': random.randint(1, 5)},
        6:{'event': 'lgu_app_01', 'timestamp': timestamp, 'local_time': time, 'item_id': '01-006',
         'bt_desc': '식품-건강식품', 'access_type': 'web', 'amount': random.randint(1, 5)},
        7:{'event': 'lgu_app_01', 'timestamp': timestamp, 'local_time': time, 'item_id': '01-007',
         'bt_desc': '식품-간편요리', 'access_type': 'phone', 'amount': random.randint(1, 5)},
        8:{'event': 'lgu_app_01', 'timestamp': timestamp, 'local_time': time, 'item_id': '01-008',
         'bt_desc': '식품-간편식', 'access_type': 'web', 'amount': random.randint(1, 5)},
        9:{'event': 'lgu_app_01', 'timestamp': timestamp, 'local_time': time, 'item_id': '01-009',
         'bt_desc': '식품-유제품', 'access_type': 'phone', 'amount': random.randint(1, 5)},
        10:{'event': 'lgu_app_02', 'timestamp': timestamp, 'local_time': time, 'item_id': '02-001',
         'bt_desc': '생활용품-헤어', 'access_type': 'web', 'amount': random.randint(1, 5)},
        11:{'event': 'lgu_app_02', 'timestamp': timestamp, 'local_time': time, 'item_id': '02-002',
         'bt_desc': '생활용품-바디/세안', 'access_type': 'phone', 'amount': random.randint(1, 5)},
        12:{'event': 'lgu_app_02', 'timestamp': timestamp, 'local_time': time, 'item_id': '02-003',
         'bt_desc': '생활용품-세탁세제', 'access_type': 'web', 'amount': random.randint(1, 5)},
        13:{'event': 'lgu_app_02', 'timestamp': timestamp, 'local_time': time, 'item_id': '02-004',
         'bt_desc': '생활용품-건강', 'access_type': 'phone', 'amount': random.randint(1, 5)},
        14:{'event': 'lgu_app_02', 'timestamp': timestamp, 'local_time': time, 'item_id': '02-005',
         'bt_desc': '생활용품-수납/정리', 'access_type': 'phone', 'amount': random.randint(1, 5)},
        15:{'event': 'lgu_app_02', 'timestamp': timestamp, 'local_time': time, 'item_id': '02-006',
         'bt_desc': '생활용품-안전', 'access_type': 'web', 'amount': random.randint(1, 5)},
        16:{'event': 'lgu_app_02', 'timestamp': timestamp, 'local_time': time, 'item_id': '02-007',
         'bt_desc': '생활용품-생활잡화', 'access_type': 'web', 'amount': random.randint(1, 5)},
        17:{'event': 'lgu_app_03', 'timestamp': timestamp, 'local_time': time, 'item_id': '03-001',
         'bt_desc': '뷰티-헤어', 'access_type': 'phone', 'amount': random.randint(1, 5)},
        18:{'event': 'lgu_app_03', 'timestamp': timestamp, 'local_time': time, 'item_id': '03-002',
         'bt_desc': '뷰티-향수', 'access_type': 'phone', 'amount': random.randint(1, 5)},
        19:{'event': 'lgu_app_03', 'timestamp': timestamp, 'local_time': time, 'item_id': '03-003',
         'bt_desc': '뷰티-남성화장품', 'access_type': 'phone', 'amount': random.randint(1, 5)},
        20:{'event': 'lgu_app_03', 'timestamp': timestamp, 'local_time': time, 'item_id': '03-004',
         'bt_desc': '뷰티-여성화장품', 'access_type': 'web', 'amount': random.randint(1, 5)},
    }

    return events.get(key, "out of bound")

def index(request):
    return render(request, "index.html")

def gen_i(request):
    return render(request, "geni.html")


def btn_geni_click(request, product_id):

    with open("logi.log", "a+") as fd:
        json_data = json.dumps(get_log(product_id), ensure_ascii=False)
        fd.write(json_data + "\n")  # 한 줄씩 JSON 문자열로 저장 (ensure_ascii=False --> 한글안깨짐)
        print(json_data, type(json_data))

    return render(request, "geni.html")

def gen_ii(request):
    return render(request, "genii.html")

def gen_iii(request):
    return render(request, "geniii.html")