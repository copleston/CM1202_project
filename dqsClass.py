class UserResult:
    def __init__(self,testID, studentID, timeElapsed, questions):
        self.testID = testID
        self.studentID = studentID
        self.timeElapsed = timeElapsed
        self.questions = questions

    def getTotalMarks():
        total = 0
        for question, answers in questions:
            total += answers[1]
        return total

    def getTimeElapsed():
        return timeElapsed

"""
class ClassResult:
    def __init__(self, userResultIn):
        self.userResult = userResultIn

        self.lessonID = lessonID
        if self.lessonID == "Logic":
            self.results = shelve.open("responses1.dat", "n")
        elif self.lessonID == "Sets":
            self.results = shelve.open("responses2.dat", "n")

    def getResults():
        return self.results

    def addResult(self, userID, timeElapsed, questions):
        self.results[userID] = new_result

    def store():
        self.results.close()
"""