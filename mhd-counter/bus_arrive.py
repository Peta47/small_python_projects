import datetime
import time

database = []

now = datetime.datetime.now()
today = now.replace(hour=0, minute=10, second=0)
today1 = now.replace(hour=0, minute=12, second=0)
today2 = now.replace(hour=0, minute=13, second=0)
today3 = now.replace(hour=0, minute=14, second=0)

database.append(today)
database.append(today1)
database.append(today2)
database.append(today3)

def timer(database, i=0):
    while True:
        time.sleep(1)
        now = datetime.datetime.now()
        lengt_db = len(database)

        for i in range(lengt_db):
            if database[i] > now:
                rozdil = database[i] - now
                minutes, second = divmod(rozdil.seconds, 60)
                print("bus jede za {} minut {} sekund".format(minutes, second))
                break
            elif database[i] < now:
                continue
            else:
                print("bus is arriving now")

timer(database)