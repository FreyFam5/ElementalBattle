from elements import Element
from stats import Stats, Defensive, Offensive

class BaseBeing():
	def __init__(self, element: Element, stats: Stats, skills: dict[str, function]):
		self.stats: Stats = stats
		self.element: Element = element
		self.skills: dict[str, function] = skills

class Human(BaseBeing):
	def __init__(self, element: Element):
		super(element, Stats(15.0, Defensive(100.0, 0.0, 0.0), Offensive(25.0, 5.0)))

class Elf(BaseBeing):
	def __init__(self, element: Element):
		super(element, Stats(25.0, Defensive(75.0, 0.0, 10.0), Offensive(15.0, 30.0)))

class Dwarf(BaseBeing):
	def __init__(self, element: Element):
		super(element, Stats(10.0, Defensive(200.0, 25.0, 20.0), Offensive(35.0, 0.0)))

class Demon(BaseBeing):
	def __init__(self, element: Element):
		super(element, Stats(15.0, Defensive(125.0, 10.0, -10.0), Offensive(25.0, 35.0)))