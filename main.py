from picoyplaco import Predictor
import datetime
import re

def main():
    #validates plate number inputted and if wrong format asks again for input
    plateform = r'^[A-Z]{3}[-]{1}[0-9]{4}$'
    plates=input("Enter license plate in the format 'ABC-1234': ")
    while (not(re.search(plateform, plates))):
        print("Invalid Plate Number")
        plates=input("Enter license plate in the format 'ABC-1234': ")
    
    #validates date inputted and if wrong format asks again for input
    flag=1
    date=input("Enter date in the ISO8601 format 'YYYY-MM-WeekDay': ")
    while flag:
        try:
            date = datetime.datetime.strptime((date), "%G-%V-%u")
            flag = 0
        except:
            print("Invalid Date")
            date=input("Enter date in the ISO8601 format 'YYYY-MM-WeekDay': ")
            flag = 1

    #validates time inputted and if wrong format asks again for input
    flag = 1
    time=input("Enter time in the format 'HH-MM': ")
    while flag:
        try:
            time = datetime.datetime.strptime((time), "%H:%M").time()
            flag = 0
        except:
            print("Invalid Time")
            time=input("Enter time in the format 'HH-MM': ")
            flag = 1
    #object vehicle creaated by calling Predictor class
    vehicle=Predictor(plates, date, time)
    result=vehicle.cancirculate()

    if result == 1:
        print("Car can circulate!")
    else:
        print("Car cannot circulate!")    

if __name__ == '__main__':
    main()
