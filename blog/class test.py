class FourCal:
	def __init__(self,first,second):
		self.first = first
		self.second = second
	def setdata(self, first, second):
		self.first = first
		self.second = second
	def add(self):
		result = self.first + self.second
		return result
	def div(self):
		result = self.first / self.second

a = FourCal(4,2)
#a.setdata(4,2)
print(a.first)
print(a.second)
print(a.add())

b = FourCal(3,7)
#b.setdata(3,7)
print(b.first)
print(b.second)

class MoreFourCal(FourCal): #class 클래스 이름(상속할 클래스 이름)
	def pow(self): # add()만 있는 FourCal을 상속받아 제곱 기능을 추가하는 것.
		result = self.first ** self.second
		return result
	def div(self):
		if self.second == 0:
			return 0
		else:
			return self.first / self.second
		
c = MoreFourCal(4,2) 
print(c.pow())
c = MoreFourCal(4,0)
print(c.div())