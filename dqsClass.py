class UserResult:
    def __init__(self,testID, studentID, timeElapsed, questions):
        self.testID = testID
        self.studentID = studentID
        self.timeElapsed = timeElapsed
        self.questions = questions

    def getTotalMarks(self):
        total = 0
        for question, answers in questions:
            if answers[0] == answers[1]:
                total = total + 1
        return total

    def getTimeElapsed(self):
        return timeElapsed


def Logic_Average():
    #db = open('LogicData.txt','r')
    #StudentNo = len(db)
    #TotalMarks = sum(db.values())
    #Logic_Percentage = ((5 * StudentNo) * 100) / (TotalMarks)
    return 45


def Sets_Average():
    #db = open('SetData.txt','r')
    #StudentNo = len(db)
    #TotalMarks = sum(db.values())
    #Sets_Percentage((3 * StudentNo) * 100) / (TotalMarks)
    return 78
