hoola =  {
    "Harry":82,
    "John":96,
    "Walid":92,
    "Yousef":62,
    "Lowal": 74
}
def grade_calc(students_score):
    def score_calc(number):
        if number > 91:
            return "Outstanding"
        elif number > 81:
            return "Exceeding Expectation"
        elif number > 71:
            return "Acceptable"
        elif number < 71:
            return "Failed"

    result = {}

    for key in students_score:
        result[key] = score_calc(students_score[key])

    print(result)


grade_calc(hoola)