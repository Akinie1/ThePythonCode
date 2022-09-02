
from re import A


class COE2:

  core_courses = []
  core_lectrures = []
  core_classrooms = ['A110','PB012']

  def __init__(self,e_courses,e_lectures,e_classroom):
    self.elective_courses = e_courses
    self.elective_lectures = e_lectures
    self.elective_classroom = e_classroom

  def get_Elective_courses(self):
   AllElectiveCourses = [self.elective_courses,self.elective_lectures,self.elective_classroom]
   return AllElectiveCourses;
  def get_core_courses(cls):
    return cls.core_classrooms

# Make an object or an instance of the class 

instance = COE2("differential Equation","The woman rdyhan","FOSSB4");

# print(f"{instance.elective_lectures} teach us {instance.elective_courses} in the class {instance.elective_classroom}");


# print(f"{instance.get_core_courses()}")

print(f"{instance.get_Elective_courses()}")

# I JUST DID SOME PRACTISE.
