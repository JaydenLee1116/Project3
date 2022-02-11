import requests

LAWD_CD = 11110 # 지역구 코드
DEAL_YMD = 201512 # 연도 4자리, 월 2자리
service_key = 'OaxPEjsnZFUf%2BJIq6Fe2PURnV9nqguIJbABGeI2aSfh6nVOhBkz0pa3L1AeLA%2BC76Q2gWZTRxmndm9uBoQfBPA%3D%3D' # 개인 인증키

API_URL = f'http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptRent?LAWD_CD={LAWD_CD}&DEAL_YMD={DEAL_YMD}&serviceKey={service_key}'

response = requests.get(API_URL)

print(response.text)

