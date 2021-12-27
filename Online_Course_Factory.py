from abc import ABCMeta, abstractmethod
class Ionlinecourse(metaclass=ABCMeta):
    @abstractmethod
    def get_course_details(self):
        pass


class Python(Ionlinecourse):
    def __init__(self):
        self.course_price = 100
        self.course_duration = "10 Hours"
    def get_course_details(self):
        return {"Price": self.course_price, "Course duration": self.course_duration}

class Java(Ionlinecourse):
    def __init__(self):
        self.course_price = 200
        self.course_duration = "15 Hours"
    def get_course_details(self):
        return {"Price": self.course_price, "Course Duration": self.course_duration}


class Online_Course_Factory:
    def get_course_name(name):
        try:
            if name == "Python":
                return Python()
            if name == "Java":
                return Java()

            raise AssertionError("Course not found")
        except AssertionError as _e:
            print(_e)









