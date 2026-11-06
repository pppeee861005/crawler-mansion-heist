# 🏰 現代爬蟲：台彩威力彩「豪宅藏寶圖」奪金工程

> 傳統爬蟲暴力敲磚破牆（HTML 解析），現代工程師直取金庫管線（AJAX/API 逆向分析）。

[![GitHub License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-brightgreen.svg)](https://www.python.org/)
[![Live Demo](https://img.shields.io/badge/Live_Demo-SVG_Animation-gold.svg)](https://pppeee861005.github.io/crawler-mansion-heist/)

---

## 🌟 專案特色

1. **直攻金庫核心 (API 逆向分析)**：
   * 分析台彩新版 AJAX/SPA 架構，繞過繁雜的 DOM 節點與反爬，直接抓取原廠後端 JSON 資料。
2. **生動 SVG 互動故事 (`index.html`)**：
   * 用「豪宅奪金記」的比喻，把 API 請求、JSON 解析、切片取值用沉浸式 SVG 動畫一步步呈現。
3. **規格化標準輸出 (`lottery.py`)**：
   * 自動取得當前最新一期威力彩開獎紀錄，精確解析：
     * **開出順序 (落球)**
     * **大小順序 (排序)**
     * **第二區特別號 (紅球)**

---

## 🗺️ 豪宅藏寶圖理論

```text
1. 大區地址 (API URL)
   👉 https://api.taiwanlottery.com/...
   （導航直達豪宅大門，敲門 GET 直接放行）
           │
           ▼
2. 豪宅平面位置圖 (JSON 物件)
   👉 response.json()
   （整棟豪宅完整格局圖，房間抽屜一目了然）
           │
           ▼
3. 地下金庫大廳 (List 清單)
   👉 house_map["content"]["superLotto638Res"]
   （整齊排列著每一期的保險箱）
           │
           ▼
4. 藏寶抽屜標籤 (Dictionary Key)
   👉 safe["drawNumberSize"]
   （拉開開獎號碼抽屜，裡面放著 7 顆球）
           │
           ▼
5. 取走 6 塊純金 (Slicing 切片)
   👉 [:6]
   （只要前 6 個第一區號碼，精準提領！）
```

---

## 🚀 快速開始

### 1. 執行 Python 爬蟲腳本

```bash
# 安裝依賴
pip install requests

# 提領最新一期開獎金條
python lottery.py
```

**輸出範例：**
```text
第 115000089 期
開出順序 : 33  36  18  37  25  19
大小順序 : 18  19  25  33  36  37
第二區   : 06
```

### 2. 本地預覽 SVG 動畫故事

直接以瀏覽器開啟 `index.html`（或 `mansion_heist_story.html`），即可觀賞四大分鏡互動動畫與代碼對照。

---

## 📁 檔案結構

```text
├── index.html                  # 互動式 SVG 豪宅奪金故事動畫（GitHub Pages / Vercel 首頁）
├── lottery.py                  # 完整封裝的威力彩即時提領腳本
├── 金庫地址偵查5步秘笈.md       # F12 Network 逆向抓 API SOP
├── 現代爬蟲的豪宅藏寶圖理論.md   # 核心隱喻與設計哲學
└── README.md                   # 專案說明文件
```

---

## 📜 開源許可

本專案採 [MIT License](LICENSE) 授權開源。
