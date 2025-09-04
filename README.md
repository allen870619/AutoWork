# AutoWork - 自動化點擊程式

這是一個基於 Python 3.13 和 pyautogui 的自動化點擊程式。

# ⚠️ 免責聲明
## 僅供技術交流，被客祥罵我不負責

## 功能特色

- ✅ 自動移動游標到特定位置，點擊框框
- ✅ 自動輸入 `/work`，然後點兩下 enter
- ✅ 隔一小時 + 隨機 1~5 分鐘後再次循環
- ✅ 電腦時間清晨 1~8 點不執行
- ✅ 特定位置設定在 .env 中

## 檔案結構

```
autowork/
├── autowork.py      # 主程式
├── .env            # 環境變數檔案 (點擊座標)
├── .env.example    # 環境變數範例檔案
├── check_position.py # 游標位置檢查工具
├── test_autowork.py # 測試程式
├── requirements.txt # 依賴清單
├── venv/           # Python 虛擬環境
└── README.md       # 說明檔案
```

## 安裝與設定

1. 確保已建立虛擬環境並安裝依賴：
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2. 建立並設定 `.env` 檔案：
```bash
cp .env.example .env
```

修改 `.env` 中的座標設定：
```
x=100    # 修改為實際的 x 座標
y=200    # 修改為實際的 y 座標
```

## 使用方法

### 1. 確定點擊位置座標

使用 check_position.py 來找出正確的點擊位置：

```bash
source venv/bin/activate
python check_position.py
```

將滑鼠移動到你想要點擊的位置，記下顯示的 x, y 座標，然後按 Ctrl+C 停止。

### 2. 設定座標

將取得的座標寫入 `.env`：

```
x=實際的x座標    # 例如: 500
y=實際的y座標    # 例如: 300
```

### 3. 啟動自動化程式

```bash
source venv/bin/activate
python autowork.py
```

程式會自動執行以下流程：
- 移動滑鼠到設定的座標位置
- 點擊該位置
- 輸入 `/work`
- 按兩下 Enter
- 等待 1 小時 + 隨機 1-5 分鐘
- 重複循環

### 4. 停止程式

按 `Ctrl+C` 停止程式

## 注意事項

- 程式在清晨 1-8 點之間不會執行任何動作
- 請確保目標應用程式窗口處於活動狀態
- 建議先測試座標設定是否正確
- 使用前請確保了解自動化操作的風險