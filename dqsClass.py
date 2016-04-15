class UserResult:
	def __init__(self,lessonID, userID, timeElapsed, questions):
		self.lessonID = lessonID
		self.userID = userID
		self.timeElapsed = timeElapsed
		self.questions = questions

	def getTotalMarks():
		total = 0
		for question, answers in questions:
			total += answers[1]
		return total

	def getTimeElapsed():
		return timeElapsed


class ClassResult:
	def __init__(self, testID, results):
		testID = 0
		results = []

	def getResults():
		return results

	def addResult(userID, timeElapsed, questions):
		new_result = UserResult(self.testID, userID, timeElapsed, questions)
		results.append(new_result)
