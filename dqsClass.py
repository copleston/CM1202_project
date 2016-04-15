import shelve

class UserResult:
	def __init__(self,testID, userID, timeElapsed, questions):
		self.testID = testID
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
	def __init__(self, lessonID):
		self.lessonID = lessonID
		if self.lessonID == "0001":
			self.results = shelve.open("responses1.dat", "n")
		elif self.lessonID == "0002":
			self.results = shelve.open("responses2.dat", "n")

	def getResults():
		return self.results

	def addResult(self, new_result):
		self.results[new_result.userID] = new_result

	def store():
		self.results.close()
