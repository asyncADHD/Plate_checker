import requests


url = "https://driver-vehicle-licensing.api.gov.uk/vehicle-enquiry/v1/vehicles"

Reg_NUM = input('reg num: ')
Reg_NUM = Reg_NUM.capitalize()
payload_response = '{\n\t\"registrationNumber\": \"'+ Reg_NUM + '\"\n}'


headers = {
  'x-api-key': 'Y8QRgOO9JB7WY7C1r8Q3K5SC8j0ynLV72jc73RxR',
  'Content-Type': 'application/json'
}


response = requests.request("POST", url, headers=headers, data = payload_response)

print(response.text.encode('utf8'))
