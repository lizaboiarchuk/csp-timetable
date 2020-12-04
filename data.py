
import random as rnd
from info import *
from model import *

class Data:
    def __init__(self):
        self._days = DAYS
        self._meetingTimes = MEETING_TIMES
        self._subjects = self.init_subjects(SUBJECTS)
        self._specs = self.init_specs(SPECIALITIES)
        self._rooms = ROOMS
        self._classes = self.init_classes()
      
    
        

    def init_subjects(self, subjects):
        subj = []
        for s in subjects:
            name = s["name"]
            num = s["number_of_students"]
            gr = s["groups"]
            tea = s["teacher"]
            subj.append(Subject(name, num,gr, tea))
        return subj

    def get_domains(self):
        domains = []
        for i in range(30):
            domains.append(i)
        return domains


    def init_specs(self, specialities):
        spec = []
        for s in specialities:
            name = s["name"]
            sub = []
            for i in s["subjects"]:
                for j in self._subjects:
                    if i == j._name:
                        sub.append(j)
            spec.append(Speciality(name, sub))
        return spec


    def init_classes(self):
        classes = []
        for sp in self._specs:
            for sub in sp._subjects:
                lect = Class(sp, sub, None, None, None, "lecture")
                classes.append(lect)
                i = 1
                for g in range(sub._groups):
                    st = "Practice " + str(i)
                    cl = Class(sp, sub, None, None, None, st)
                    classes.append(cl)
                    i+=1
        return classes


