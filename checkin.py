import requests
from datetime import datetime

url = "https://cykul.in/app/lifeCykul/webservice/scanning/scanActivities.php"

headers = {
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 16; SM-E156B Build/BP4A.251205.006)",
    "Host": "cykul.in",
    "Connection": "keep-alive",
    "Accept-Encoding": "gzip, deflate, br",
}

requests_to_send = [
    {
        "name": "SWB",
        "eventID": "CLCYOE3755260808114215119",
        "address": "Lat: 12.8340593, Lng: 75.1188008",
        "qrCode": "127552",
        "latitude": "12.8340593",
        "longitude": "75.1188008",
    },
    {
        "name": "Tourism",
        "eventID": "CLCYOE3755260820112924119",
        "address": "Lat: 12.8747, Lng: 74.9397",
        "qrCode": "130915",
        "latitude": "12.8747",
        "longitude": "74.9397",
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
        "departmentID": "CHEKIN3755YOE375",
        "latitude": request_details["latitude"],
        "time": current_time,
        "longitude": request_details["longitude"],
    }

    response = requests.post(
        url,
        headers=headers,
        data=data,
        verify=False,
    )

    print(f"{request_details['name']} check-in")
    print("Time sent:", current_time)
    print("Status:", response.status_code)
    print("Response:", response.text)
    print()
