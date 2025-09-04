import pyautogui
import configparser
import datetime

def test_config_loading():
    try:
        config = configparser.ConfigParser()
        config.read('config.ini')
        x = int(config['coordinates']['x'])
        y = int(config['coordinates']['y'])
        print(f"✓ Config loaded successfully: x={x}, y={y}")
        return True
    except Exception as e:
        print(f"✗ Config loading failed: {e}")
        return False

def test_time_checking():
    try:
        current_hour = datetime.datetime.now().hour
        is_sleep_time = 1 <= current_hour <= 8
        print(f"✓ Time checking works. Current hour: {current_hour}, Sleep time: {is_sleep_time}")
        return True
    except Exception as e:
        print(f"✗ Time checking failed: {e}")
        return False

def test_imports():
    try:
        import pyautogui
        import configparser
        import time
        import random
        import datetime
        print("✓ All imports successful")
        return True
    except Exception as e:
        print(f"✗ Import failed: {e}")
        return False

if __name__ == "__main__":
    print("Testing AutoWork components...")
    print("="*40)
    
    all_tests_passed = True
    
    all_tests_passed &= test_imports()
    all_tests_passed &= test_config_loading()
    all_tests_passed &= test_time_checking()
    
    print("="*40)
    if all_tests_passed:
        print("✓ All tests passed! AutoWork is ready to use.")
    else:
        print("✗ Some tests failed. Please fix the issues above.")