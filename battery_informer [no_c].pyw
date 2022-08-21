import pyautogui as pg
import psutil
import time

exit = False
pg.alert(text = "Started!!", title = "Batter Alert", button = "Ok")
while not exit:
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = int(str(battery.percent))
    plugged = "Plugged In" if plugged else "Not Plugged In"
    if percent >= 92 and plugged == "Plugged In":
        if pg.confirm(text = 'Battery Full, UNPLUG NOW.', title = 'Battery Alert'\
            , buttons = ["Ok", "End Yourself"]) == "End Yourself":
            exit = True
    time.sleep(60)

