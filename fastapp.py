import time
import pyautogui
import sqlite3
import json
import os
# Reminder:
# Create a function wchit Generates a new Preset with the name given by the user 
#The new Preset should be added to the database and can be used in the future as a normal bootup list
# Presets can be replace with new Presets and deleted by the user 
# Ideas:
# 1. Bootup with Windows
# 2. Bootup with a Preset
tablename = 'applist'
db_name = 'your_db_name.db'
default_list = ['app1', 'app2', 'app3', 'app4']  # Replace with your default list
if not os.path.exists(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS applist (
        name TEXT PRIMARY KEY,
        value TEXT NOT NULL
        )   
        """)
    cursor.execute("INSERT INTO applist (name, value) VALUES (?, ?)", ('my_list', json.dumps(default_list)))
    conn.commit()
    conn.close()

class MyList:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        self.my_list = self.get_my_list()

    def get_my_list(self, Preset):
        self.cursor.execute("SELECT value FROM applist WHERE name=?", (Preset,))
        result = self.cursor.fetchone()
        if result:
            return json.loads(result[0])  # Convert JSON string back to Python object
        else:
            return []

    def update_my_list(self, new_list, preset):
        self.my_list = new_list
        self.cursor.execute("UPDATE applist SET value=? WHERE name=?", (json.dumps(new_list), preset))
        self.conn.commit()
    def create_preset(self):
        new_presetname = input("Type the name of the new Preset: ")
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS """ + new_presetname +""" (
        name TEXT PRIMARY KEY,
        value TEXT NOT NULL
        )   
        """)
        my_list_instance = MyList(db_name)
        new_presetname_list = my_list_instance.get_my_list(new_presetname)
        for i in len(new_presetname_list):
             appchange = input("Type the name of the app that you want to add hear:")
             new_presetname[i] = appchange
             my_list_instance.update_my_list(new_presetname, )
             print(new_presetname = new_presetname_list)
             
    def close(self):
        self.conn.close()
        




def openapp():
    my_list_instance = MyList(db_name)  # Replace 'your_db_name.db' with the actual name of your database file
    retrieved_list = default_presetlist1
    templist = retrieved_list
    default_presetlist1 = retrieved_list("my_list")
    try:
        preset1 = my_list_instance.get_my_list(preset1_name)
        preset2 = my_list_instance.get_my_list(preset2_name)
        preset3 = my_list_instance.get_my_list(preset3_name)
    except Exception as e:
        print("Error while retrieving presets:", e)

    print(retrieved_list)

    def exit():
        exit()
    def favapplistedit(favapplist):
        answer_app_add = input("Which Apps changed?")

        if answer_app_add == "1":
            appchange = input("Type the name of the app that you want to add hear:")
            templist[0] = appchange
            my_list_instance.update_my_list(templist, )
            startmenu(retrieved_list)
            
        elif answer_app_add == "2":
            appchange = input("Type the name of the app that you want to add hear:")
            retrieved_list[1] = appchange
            my_list_instance.update_my_list(templist)   
            startmenu(retrieved_list)
        elif answer_app_add == "3":
            appchange = input("Type the name of the app that you want to add hear:")
            retrieved_list[2] = appchange
            my_list_instance.update_my_list(templist)  
            startmenu(retrieved_list)
        elif answer_app_add == "4":
            appchange = input("Type the name of the app that you want to add hear:")
            retrieved_list[3] = appchange
            my_list_instance.update_my_list(templist)
            startmenu(retrieved_list)
        else:
            print("Only Apps can be Edited")
            favapplistedit(retrieved_list)
    def launchapp(Appname):
        try:
            pyautogui.hotkey("Winleft", "s")
            time.sleep(0.01)
            pyautogui.write(Appname)
            time.sleep(0.01)
            pyautogui.hotkey("enter")
            time.sleep(1)
        except Exception as e:
            print("Fehler beim Öffnen der Anwendung:", e)
    def openall():
        for app in retrieved_list:
            launchapp(app)
    def presetedit():
        print("Preset 1: " + str(preset1))
    def startmenu(retrieved_list):
        print("[1]" + retrieved_list[0] + "[2]" + retrieved_list[1] + "[3]" + retrieved_list[2] + "[4]" + retrieved_list[
            3] + "[5]Presets [6] add App to Favorite [7] Open all [8] Exit")
        answer = input("Which Apps should be open?")
        if answer == "1":
            launchapp(retrieved_list[0])
        elif answer == "2":
            launchapp(retrieved_list[1])
        elif answer == "3":
            launchapp(retrieved_list[2])
        elif answer == "4":
            launchapp(retrieved_list[3])
        elif answer == "5":
            presetedit()
        elif answer == "6":
            favapplistedit(retrieved_list)
        elif answer == "7":
            openall()
        elif answer == "8":
            exit()

    startmenu(templist)


def shutdown():
    print("[1] Sekunden")
    print("[2] Minuten")
    print("[3] Stunden")
    questiontime = int(input("Wie lange soll gewartet werden: "))

    def switch_case(questiontime):
        switcher = {
            1: "Sekunden",
            2: "Minuten",
            3: "Stunden"
        }
        return switcher.get(questiontime, "ungültige Eingabe")

    timesettoshutdown = 0

    if questiontime == 1:
        timesettoshutdown = int(input("Wie viele Sekunden? = "))

    elif questiontime == 2:
        timesettoshutdown = int(input("Wie viele Minuten? = ")) * 60

    elif questiontime == 3:
        timesettoshutdown = int(input("Wie viele Stunden? = ")) * 3600

    try:

        i = 0
        start_sequenze = True
        while start_sequenze == True:
            print(timesettoshutdown - i)
            i += 1
            time.sleep(0.5)
            if i == timesettoshutdown - 1:
                pyautogui.hotkey('Winleft', "d")
                time.sleep(0.1)
                pyautogui.hotkey("alt", "f4")
                time.sleep(0.1)
                pyautogui.hotkey("tab")
                # pyautogui.hotkey("tab")
                time.sleep(0.1)
                pyautogui.hotkey("enter")
                for num in range(100):
                    print(num)
                    pyautogui.hotkey("enter")


    except Exception as e:
        print("Ein Fehler ist aufgetreten:", e)


print(
    "[1] Shutdown"
    "[2] Open apps"
)
answer = input("What do you want")
if answer == "1":
    shutdown()
elif answer == "2":
    openapp()
