from abc import ABCMeta, abstractmethod
from Online_Course_Factory import Online_Course_Factory
from Ofline_course_factory import Offline_Course_Factory
class Icoursefactory(metaclass=ABCMeta):
    @abstractmethod
    def get_course(course_name):
        pass
class CourseFactory(Icoursefactory):
    def get_course(course_name):
        if course_name in ["Java", "Python"]:
            return Online_Course_Factory.get_course_name(course_name)
        if course_name in ["C","Php"]:
            return Offline_Course_Factory.get_course_name(course_name)
if __name__ == "__main__":
    c = input("Enter your Course name:")
    a = CourseFactory.get_course(c)
    print(a.get_course_details())

