import datetime

#dictionary which stores the plates constricted for circulation on specific days
myDict = {
    "Monday": [5, 6, 7, 8],
    "Tuesday": [9, 0, 1, 2],
    "Wednesday": [3, 4, 5, 6],
    "Thursday": [7, 8, 9, 0],
    "Friday": [1, 2, 3, 4]
}


class Predictor():
    #constructor for plates, date and time and initializes weekday and lastdigit
    def __init__(self, plates, date, time):
        self.plates = plates 
        self.date = date
        self.weekday = datetime.datetime.weekday(self.date)
        self.time = time
        self.lastdigit = int(self.plates[-1])
    
    #checks whether a car can pass of not in specific time and date and with specific plates
    def cancirculate(self):
        
        if (self.time >= datetime.time(6, 0)) and (self.time <= datetime.time(9, 0)) or (self.time >= datetime.time(17, 0)) and (self.time <= datetime.time(20, 0)):
            result = 1
            if (self.lastdigit in myDict['Monday']) and (self.weekday==0):
                result = 0
            elif (self.lastdigit in myDict['Tuesday']) and (self.weekday==1):
                result = 0
            elif (self.lastdigit in myDict['Wednesday']) and (self.weekday==2):
                result = 0
            elif (self.lastdigit in myDict['Thursday']) and (self.weekday==3):
                result = 0
            elif (self.lastdigit in myDict['Friday']) and (self.weekday==4):
                result = 0
        else:
            result = 1
        return result

                 
