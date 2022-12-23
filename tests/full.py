from sources.ReportSource import ReportSource
from services.former import form
import time

def full():
  source = ReportSource()
  
  groupNames = source.getGroupsNames()
  headers = source.getTableHeaders()
  for groupName in groupNames:
    for number in range(8, 81, 8):
      print(groupName, number)
      moduleStart, moduleEnd = number - 7, number
      students = source.getStudentsListByGroup(groupName, moduleStart, moduleEnd, headers)
      reports = form(students)
      time.sleep(1)
