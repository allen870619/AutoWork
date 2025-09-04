import pyautogui
import time

def check_mouse_position():
    """
    持續顯示滑鼠游標的當前位置
    每秒更新一次，按 Ctrl+C 停止
    """
    print("游標位置檢查工具")
    print("=" * 30)
    print("每秒顯示當前游標位置")
    print("按 Ctrl+C 停止程式")
    print("=" * 30)
    
    try:
        while True:
            # 獲取當前滑鼠位置
            x, y = pyautogui.position()
            
            # 清除上一行並顯示當前位置
            print(f"\r當前游標位置: x={x}, y={y}", end="", flush=True)
            
            # 等待一秒
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\n\n程式已停止")
        print(f"最後記錄的位置: x={x}, y={y}")
        print("你可以將這個位置寫入 config.ini 檔案中")

if __name__ == "__main__":
    check_mouse_position()