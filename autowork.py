import pyautogui
import os
import time
import random
import datetime

class AutoWork:
    def __init__(self, env_file='.env'):
        self.load_env(env_file)
        try:
            self.x = int(os.getenv('x', '0'))
            self.y = int(os.getenv('y', '0'))
            print(f"Loaded coordinates: x={self.x}, y={self.y}")
        except ValueError as e:
            print(f"Config error: Invalid coordinate values - {e}")
            exit(1)
    
    def load_env(self, env_file):
        if os.path.exists(env_file):
            with open(env_file, 'r') as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith('#') and '=' in line:
                        key, value = line.split('=', 1)
                        os.environ[key.strip()] = value.strip()
        else:
            print(f"Warning: {env_file} not found, using default coordinates (0, 0)")
            print("Create a .env file with:")
            print("x=100")
            print("y=200")
    
    def click_position(self):
        pyautogui.moveTo(self.x, self.y)
        pyautogui.click()
    
    def type_work_command(self):
        pyautogui.typewrite('/work')
        pyautogui.press('enter')
        pyautogui.press('enter')
    
    def is_sleep_time(self):
        current_hour = datetime.datetime.now().hour
        return 1 <= current_hour <= 8
    
    def work_cycle(self):
        if self.is_sleep_time():
            print(f"Sleep time (1-8 AM), skipping work cycle at {datetime.datetime.now()}")
            return
        
        print(f"Executing work cycle at {datetime.datetime.now()}")
        self.click_position()
        time.sleep(1)
        self.type_work_command()
        print("Work cycle completed")
    
    def run(self):
        print("AutoWork started...")
        while True:
            try:
                self.work_cycle()
                
                wait_time = 3600 + random.randint(60, 300)
                next_run = datetime.datetime.now() + datetime.timedelta(seconds=wait_time)
                print(f"Next run scheduled at: {next_run}")
                time.sleep(wait_time)
                
            except KeyboardInterrupt:
                print("AutoWork stopped by user")
                break
            except Exception as e:
                print(f"Error occurred: {e}")
                time.sleep(60)

if __name__ == "__main__":
    auto_work = AutoWork()
    auto_work.run()