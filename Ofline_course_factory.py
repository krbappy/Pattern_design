from abc import ABCMeta, abstractmethod
class Iofflinecourse(metaclass=ABCMeta):
    @abstractmethod
    def get_course_details(self):
        pass


class Php(Iofflinecourse):
    def __init__(self):
        self.course_price = 500
        self.course_duration = "20 Hours"
    def get_course_details(self):
        return {"Price": self.course_price, "Course duration": self.course_duration}

class C(Iofflinecourse):
    def __init__(self):
        self.course_price = 600
        self.course_duration = "25 Hours"
    def get_course_details(self):
        return {"Price": self.course_price, "Course Duration": self.course_duration}


class Offline_Course_Factory:
    def get_course_name(name):
        try:
            if name == "Php":
                return Php()

            if name == "C":
                return C()

            raise AssertionError("Course not found")
        except AssertionError as _e:
            print(_e)








