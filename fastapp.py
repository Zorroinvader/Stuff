import time
import pyautogui
import json
import sqlite3
import os

conn = sqlite3.connect("myDatabase.db")
cursor = conn.cursor()
if os.path.exists("myDatabase.db"):
    print("myDatabase.db exists")

else:
    cursor.execute('''CREATE TABLE  IF NOT EXISTS applist (
        id INTEGER  PRIMARY KEY,
        data TEXT
        )''')
    print("Database created")


def openapp():


    cursor.execute("SELECT data FROM applist")
    rows = cursor.fetchall()
    retrievef_List = json.loads(rows[0][1])
    favapplist = (retrievef_List)


    list_json = json.dumps(favapplist)
    def addlisttodb(list):
        cursor.execute("INSERT INTO applist (id) Values (?)", (0,))
        cursor.execute("INSERT INTO applist (data) VALUES (?)", (list,))
        conn.commit()

    addlisttodb(list_json)
    def presetedit():
        print("not defien yet")
    def changeappindb(appchange):
        cursor.execute("SELECT data FROM applist WHERE id = ?", (1,))
        data = cursor.fetchone()[0]
        my_list = json.loads(data)
        my_list.append(appchange)
        modified_data = json.dumps(my_list)
        cursor.execute("UPDATE applist SET data = ? WHERE id = ?", (modified_data, 1))
        conn.commit()
    def favapplistedit(favapplist):
        answer_app_add = input("Which Apps changed?")

        if answer_app_add == "1":
            appchange = input("Type the name of the app that you want to add hear:")

            favapplist[0] = appchange
            changeappindb(appchange)
            startmenu(favapplist)
        elif answer_app_add == "2":
            appchange = input("Type the name of the app that you want to add hear:")
            favapplist[1] = appchange
            changeappindb(appchange)
            startmenu(favapplist)
        elif answer_app_add == "3":
            appchange = input("Type the name of the app that you want to add hear:")
            favapplist[2] = appchange
            changeappindb(appchange)
            startmenu(favapplist)
        elif answer_app_add == "4":
            appchange = input("Type the name of the app that you want to add hear:")
            favapplist[3] = appchange
            changeappindb(appchange)
            startmenu(favapplist)

    def launchapp(Appname):
        try:
            pyautogui.hotkey("Winleft", "s")
            time.sleep(0.01)
            pyautogui.write(Appname)
            time.sleep(0.01)
            pyautogui.hotkey("enter")
        except Exception as e:
            print("Fehler beim Öffnen der Anwendung:", e)

    def startmenu(favapplist):
        print("[1]" + favapplist[0] + "[2]" + favapplist[1] + "[3]" + favapplist[2] + "[4]" + favapplist[
            3] + "[5]Presets [6] add App to Favorite")
        answer = input("Which Apps should be open?")
        if answer == "1":
            launchapp(favapplist[0])
        elif answer == "2":
            launchapp(favapplist[1])
        elif answer == "3":
            launchapp(favapplist[2])
        elif answer == "4":
            launchapp(favapplist[3])
        elif answer == "5":
            presetedit()
        elif answer == "6":
            favapplistedit(favapplist)

    startmenu(favapplist)


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
                time.sleep(0.001)
                pyautogui.hotkey("alt", "f4")
                time.sleep(0.001)
                pyautogui.hotkey("tab")
                # pyautogui.hotkey("tab")
                time.sleep(0.001)
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
