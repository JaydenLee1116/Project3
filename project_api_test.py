import requests

LAWD_CD = 11110 # 지역구 코드
DEAL_YMD = 201512 # 연도 4자리, 월 2자리
service_key =  # 개인 인증키

API_URL = f'http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptRent?LAWD_CD={LAWD_CD}&DEAL_YMD={DEAL_YMD}&serviceKey={service_key}'

response = requests.get(API_URL)

print(response.text)

