#########################################################################
# Python x AI Agent
# bs4, requests, json - URL/HTTP 處理程式庫
#
# [專案]
# 威力彩
# 問題：請詳閱附件 ReadMe_lottery.pdf 說明
#       撰寫程式找出台灣彩券公司最新一期「威力彩」開獎結果
#
# 輸入：台灣彩券公司 API 地址 (由 AJAX / Network 分析取得)
#
# 輸出：印出開出順序與大小順序的球碼、以及第二區的紅球，如：
#
#         第 114000030 期
#         開出順序 : 20  29  09  05  01  38
#         大小順序 : 01  05  09  20  29  38
#         第二區   : 02
#
# (提示：新改版網頁採 AJAX (非同步載入) 設計，須分析網頁運作找到最新
#        一期開獎結果記錄的確實所在)
###########################################################################

import requests
from datetime import datetime

def fetch_latest_super_lotto():
    # 1. 取得當前年月，動態產生查詢參數
    now = datetime.now()
    current_month = now.strftime("%Y-%m")
    
    # 2. 金庫大區地址 (API)
    api = "https://api.taiwanlottery.com/TLCAPIWeB/Lottery/SuperLotto638Result"
    url = f"{api}?period&month={current_month}&pageNum=1&pageSize=10"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    try:
        # 3. 發送 GET 請求，取得豪宅位置圖 (JSON)
        res = requests.get(url, headers=headers, timeout=10)
        res.raise_for_status()
        house_map = res.json()

        # 4. 走進地下金庫大廳，鎖定最新一期的保險箱
        records = house_map.get("content", {}).get("superLotto638Res", [])
        if not records:
            print("查無最新開獎紀錄！")
            return

        latest_safe = records[0]

        # 5. 直取純金數據
        period = latest_safe.get("period")
        
        # 開出順序 (落球順序): 前 6 顆為第 1 區，最後 1 顆為第 2 區
        appear_nums = latest_safe.get("drawNumberAppear", [])
        appear_zone1 = "  ".join(f"{num:02d}" for num in appear_nums[:6])
        
        # 大小順序 (大小排序): 前 6 顆為第 1 區，最後 1 顆為第 2 區
        size_nums = latest_safe.get("drawNumberSize", [])
        size_zone1 = "  ".join(f"{num:02d}" for num in size_nums[:6])
        
        # 第二區紅球 (特別號)
        zone2_num = f"{size_nums[6]:02d}" if len(size_nums) > 6 else "N/A"

        # 6. 標準規格輸出
        print(f"第 {period} 期")
        print(f"開出順序 : {appear_zone1}")
        print(f"大小順序 : {size_zone1}")
        print(f"第二區   : {zone2_num}")

    except Exception as e:
        print(f"提領金條失敗: {e}")

if __name__ == "__main__":
    fetch_latest_super_lotto()
