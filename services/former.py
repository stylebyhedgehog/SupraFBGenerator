def form_intro(name):
    return "📝"+ name + " прошел 8 занятий в рамках курса , и мы спешим поделиться результатами, которые успели достигнуть за месяц."

def form_attendance(value):
    dr = int(value * 100 / 8)
    result = str(dr) + "% (" + str(value) + "/8)"
    return "📊 Посещаемость - " + result

def form_performance(lessons):
    result = "📖 В рамках блока занятий освоены следующие темы:\n"
    for lesson in lessons:
        if (lesson.getMark() == "-"):
            result += "▪️" + lesson.getTitle() + " - пропуск (запись отправлена)\n" 
        elif (lesson.getMark() != "-"):
            result += "▪️" + lesson.getTitle() + " - " + lesson.getMark() + "% освоения\n"
    return result

def form_comment(comment):
    return "📌 Преподаватель отмечает: " + comment

def form_ending():
    return '''Спасибо Вам за занятия! Мы всегда открыты к вашим вопросам и будем рады ответить на них!

С уважением, команда онлайн-академии Supra'''


def form(students):
  reports = []
  id = 0
  for student in students:
    result = ""
    result += form_intro(student.getName()) + "\n\n"
    result += form_attendance(student.getAttendance()) + "\n\n"
    result += form_performance(student.getLessons()) + "\n\n"
    result += form_comment(student.getComment()) + "\n\n"
    result += form_ending()
    report = {"id": id, "title": student.getSurname()+" "+ student.getName(), "text": result}
    reports.append(report)
    id+=1
  return reports