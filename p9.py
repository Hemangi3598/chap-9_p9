class employee:
	def __init__ (self, ename, eid, epds):
		self.ename = ename
		self.eid = eid
		self.epds = epds
	def __mul__ (self, other):
		res = self.epds * other.nodp
		return res
class attendance:
	def __init__ (self, nodp):
		self.nodp = nodp
e = employee(10, "amit", 500)
a = attendance(25)
sal = e * a; print("sal = ", sal)