from flask import Flask, render_template, request
from sources.ReportSource import ReportSource
from services.former import form
from tests.full import full

app = Flask(  
	__name__,
	template_folder='templates',  
	static_folder='static',
)

source = ReportSource()

@app.route('/', methods=["GET", "POST"])
def index():
  groupNames = source.getGroupsNames()
  reports = []
  if request.method == "POST":
    groupName = request.form["groupName"]
    lessonNumber = int(request.form["lessonNumber"])
    headers = source.getTableHeaders()
    moduleStart, moduleEnd = lessonNumber - 7, lessonNumber
    students = source.getStudentsListByGroup(groupName, moduleStart, moduleEnd, headers)
    reports = form(students)
  return render_template("main.html", groupNames= groupNames, reports = reports)

app.run(host='0.0.0.0', port=81)
