import pyautogui
import configparser
import time
import random
import datetime

class AutoWork:
    def __init__(self, config_file='config.ini'):
        self.config = configparser.ConfigParser()
        self.config.read(config_file)
        self.x = int(self.config['coordinates']['x'])
        self.y = int(self.config['coordinates']['y'])
    
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