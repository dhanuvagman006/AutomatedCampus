import requests
from datetime import datetime
from urllib.parse import urlencode

url = "https://cykul.in/app/lifeCykul/webservice/scanning/scanActivities.php"

requests_to_send = [
    {
        "name": "SWB",
        "eventID": "CLCYOE3755260808114215119",
        "address": "Lat: 12.8340593, Lng: 75.1188008",
        "qrCode": "127552",
        "departmentID": "CHEKOUT3755YOE375",
        "latitude": "12.8340593",
        "longitude": "75.1188008",
        "headers": {
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 16; SM-E156B Build/BP4A.251205.006)",
            "Host": "cykul.in",
            "Connection": "keep-alive",
            "Accept-Encoding": "gzip, deflate, br",
        },
        "encode_data": False,
    },
    {
        "name": "Tourism",
        "eventID": "CLCYOE3755260820112924119",
        "address": "Lat: 12.8747, Lng: 74.9397",
        "qrCode": "130915",
        "departmentID": "CHEKOUT3755YOE375",
        "latitude": "12.8747",
        "longitude": "74.9397",
        "headers": {
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 16; SM-E156B Build/BP4A.251205.006)",
            "Host": "cykul.in",
            "Connection": "keep-alive",
        },
        "encode_data": True,
    },
]

for request_details in requests_to_send:
    current_time = datetime.now().strftime("%Y-%b-%d %H:%M")
    data = {
        "whichapp": "campuslife",
        "eventID": request_details["eventID"],
        "riderID": "1558019",
        "address": request_details["address"],
        "qrCode": request_details["qrCode"],
        "departmentID": request_details["departmentID"],
        "latitude": request_details["latitude"],
        "time": current_time,
        "longitude": request_details["longitude"],
    }
    request_data = urlencode(data) if request_details["encode_data"] else data

    response = requests.post(
        url,
        headers=request_details["headers"],
        data=request_data,
        verify=False,
    )

    print(f"{request_details['name']} check-out")
    print("Time sent:", current_time)
    print("Status:", response.status_code)
    print("Response:", response.text)
    print()
