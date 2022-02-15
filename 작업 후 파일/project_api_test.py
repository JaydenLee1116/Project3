# 스케쥴러 시도

import pandas as pd
import urllib.request
from bs4 import BeautifulSoup
import time
from apscheduler.schedulers.blocking import BlockingScheduler


# UTC+0 기반으로 실행하려면 Timezone 에 매개변수를 선언 후 사용
scheduler = BlockingScheduler({'apscheduler.timezone':'UTC'})


req = urllib.request

serviceKey = 'OaxPEjsnZFUf%2BJIq6Fe2PURnV9nqguIJbABGeI2aSfh6nVOhBkz0pa3L1AeLA%2BC76Q2gWZTRxmndm9uBoQfBPA%3D%3D' # 개인 인증키
LAWD_CD_list = [11680, 11740, 11305, 11500, 11620, 11215, 11530, 11545, 11350, 11320, 11230, 11590, 11440, 11410, 11650, 11200, 11290, 11710, 11470, 11560, 11170, 11380, 11110, 11140, 11260]   # 지역구 코드
# '01', '02', '03', '04', '05', '06',  에러 : '08'
aptTradeTotal = pd.DataFrame()
def collect():
    for LAWD_CD in LAWD_CD_list:
        for YEAR in range(2020, 2021):
            for MONTH in list(range(1, 13)):
                if MONTH <= 9:
                    DEAL_YMD = str(YEAR)+str(0)+str(MONTH)
                else:
                    DEAL_YMD = str(YEAR)+str(MONTH)
                
                API_URL = f'http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptRent?LAWD_CD={LAWD_CD}&DEAL_YMD={DEAL_YMD}&serviceKey={serviceKey}'
                
                xml = req.urlopen(API_URL)
                resp = xml.read()
                soup = BeautifulSoup(resp, 'lxml-xml')
    
                items = soup.find_all('item')
                aptTrade = pd.DataFrame()
    
                for item in items:
                    dealAmountYear      = item.find("보증금액").text.strip()
                    dealAmountMonth     = item.find("월세금액").text.strip()
                    buildYear           = item.find("건축년도").text.strip()
                    dealYear            = item.find("년").text.strip()
                    dealMonth           = item.find("월").text.strip()
                    dealDay             = item.find("일").text.strip()
                    dong                = item.find("법정동").text.strip()
                    apartmentName       = item.find("아파트").text.strip()
                    regionalCode        = item.find("지역코드").text.strip()
                    # jibun               = item.find("지번").text.strip()
                    areaForExclusiveUse = item.find("전용면적").text.strip()
                    floor               = item.find("층").text.strip()
    
    
                    temp = pd.DataFrame(([[dealAmountYear,dealAmountMonth,buildYear,dealYear,dealMonth,dealDay,dong,apartmentName,regionalCode,areaForExclusiveUse,floor]]), columns=["dealAmountYear","dealAmountMonth","buildYear","dealYear","dealMonth","dealDay","dong","apartmentName","regionalCode","areaForExclusiveUse","floor"]) 
                    aptTrade=pd.concat([aptTrade,temp])
    
                aptTrade = aptTrade.reset_index(drop=True)
                aptTradeTotal=pd.concat([aptTradeTotal,aptTrade])
    
    df_apt = aptTradeTotal.reset_index(drop=True)

scheduler.add_job(func=collect, trigger='interval', seconds=1)

scheduler.start()