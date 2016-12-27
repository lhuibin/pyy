class Person(object):
	"""docstring for person"""
	def __init__(self):
		pass

#argsPeter = ['name','age','gender','height','weight','education','property','occupation']
Peter = Person()
Peter.name = 'Peter'
Peter.age = 38

print(Peter.name,':',Peter.age)
print(dir(Person))