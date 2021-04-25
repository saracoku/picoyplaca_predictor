import unittest
import datetime
from picoyplaco import Predictor

class TestMethod(unittest.TestCase):
    #tests for variables initialized and used in Predictor class (not only)
    def test_initval(self):
        time = datetime.datetime.strptime(("18:11"), "%H:%M").time()
        date = datetime.datetime.strptime(("2021-02-1"), "%G-%V-%u")
        obj1 = Predictor("VDA-3809", date, time)
        assert obj1.plates == "VDA-3809"
        assert obj1.date == date
        assert obj1.time == time
        assert obj1.cancirculate() == 1

    def test_initval(self):
        time = datetime.datetime.strptime(("6:53"), "%H:%M").time()
        date = datetime.datetime.strptime(("1978-11-6"), "%G-%V-%u")
        obj1 = Predictor("AUK-8264", date, time)
        assert obj1.plates == "AUK-8264"
        assert obj1.date == date
        assert obj1.time == time
        assert obj1.cancirculate() == 1
    
    def test_initval(self):
        time = datetime.datetime.strptime(("8:24"), "%H:%M").time()
        date = datetime.datetime.strptime(("2001-07-2"), "%G-%V-%u")
        obj1 = Predictor("MKL-1971", date, time)
        assert obj1.plates == "MKL-1971"
        assert obj1.date == date
        assert obj1.time == time
        assert obj1.cancirculate() == 0



