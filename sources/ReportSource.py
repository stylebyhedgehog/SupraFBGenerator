import gspread
from services.parser import rawStudentToDTO

class ReportSource:
  def __init__(self):
    self.gspread_client = gspread.service_account(filename="sources/credentials.json")
    self.spreadsheet = self.gspread_client.open_by_key("17fX-bB8tvSsO7-v7zgilcIhLjCaAxEYsKtQ79m8ZIuM").sheet1
  
  def getTableHeaders(self):
    headers = {}
    row = self.spreadsheet.row_values(1)
    for i in range(len(row)):
        if len(row[i]) > 0:
            name = row[i].replace('\n', ' ')
            headers.update({name: i})
    return headers
  
  def getStudentsListByGroup(self, groupName, moduleStart, moduleEnd, headers):
      all = self.spreadsheet.get_all_values()[1::]
      studentsInGroup = []
      for row in all:
          if row[headers["Группа"]] == groupName and row[headers["Статус"]] != "Отказ":
              student = rawStudentToDTO(row, moduleStart, moduleEnd, headers)
              if student:
                studentsInGroup.append(student)
      return studentsInGroup
  
  def getGroupsNames(self):
    allNames = self.spreadsheet.col_values(4)[1::]
    uniqueNames = list(set(allNames))
    uniqueNames.sort()
    uniqueNames.remove("-")
    return uniqueNames

