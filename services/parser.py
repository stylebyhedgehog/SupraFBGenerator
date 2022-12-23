from models.Lesson import Lesson
from models.Student import Student

def rawStudentToDTO(array, moduleStart, moduleEnd, headers):
  if int(array[headers["Всего"]]) < 8 or array[headers["Статус"]] == "Отказ":
    return None
  nsl = array[headers["ФИО"]].split(" ")
  name, surname, lastname  = "", "", ""
  if len(nsl) == 3:
    name = nsl[1]
    surname = nsl[0]
    lastname = nsl[2]
  elif len(nsl) == 2:
    name = nsl[1]
    surname = nsl[0]
  elif len(nsl) == 1:
    name = nsl[0]
  group = array[headers["Группа"]]
  commentHeader = "Комментарий" +" "+ str(moduleStart) +"-"+ str(moduleEnd) 
  commentHeader = list(filter(lambda x: commentHeader in x, headers))[0]
  comment = array[headers[commentHeader]]
  attendance = 0
  lessons = []
  for i in range(headers[str(moduleStart)], headers[str(moduleEnd)] +1):
      if len(array[i]) > 0 and len(array[i].split("/")) == 2:
          theme, mark = array[i].split("/")
          lesson = Lesson(theme, mark)
          lessons.append(lesson)
          if mark != "-":
              attendance+=1
  student = Student(name, surname, lastname, group, comment,lessons, attendance)

  return student





