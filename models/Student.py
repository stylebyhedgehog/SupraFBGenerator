class Student:
  def __init__(self, name, surname, lastName, group, comment, lessons, attendance):
    self.name = name
    self.surname = surname
    self.lastName = lastName
    self.group = group
    self.comment = comment
    self.lessons = lessons
    self.attendance = attendance

  
  def getName(self):
    return self.name
    
  def getSurname(self):
    return self.surname
    
  def getLastName(self):
    return self.lastName

  def getFIO(self):
    return self.surname + " " + self.name + " " + self.lastName

  def getGroup(self):
    return self.group

  def getComment(self):
    return self.comment

  def getLessons(self):
    return self.lessons

  def getAttendance(self):
    return self.attendance