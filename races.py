from elements import Element
from stats import Stats, Defensive, Offensive, Base

class BaseBeing():
	def __init__(self, element: Element, stats: Stats, name: str, skills = {}, status_effects: dict[str, int] = {}):
		self.stats: Stats = stats
		self.element: Element = element
		self.skills = skills
		self.name = name
		self.status_effects = status_effects
	
	## Checks the status of the called being
	def check_status(self):
		# The line that will be printed
		line: str = ""
		if self.stats.defensive.health <= 0:
			line = f"{self.name} has reached 0 hp and died!"
		else:
			line = f"{self.name} has {self.stats.defensive.health} hp!"

		print("".join(["v" for i in range(len(line) + 2)]))
		print("|" + line + "|")
		print("".join(["^" for i in range(len(line) + 2)]))


class Human(BaseBeing):
	def __init__(self, element: Element, name: str, skills = {}):
		super().__init__(
			element, 
			Stats(
				Base(speed=15, stamina=100, mana=25), 
				Defensive(max_health=100, armor=0, magic_resistance=0), 
				Offensive(physical=25, magic=5)
				), 
			name,
			skills
			)

class Elf(BaseBeing):
	def __init__(self, element: Element, name: str, skills = {}):
		super().__init__(
			element, 
			Stats(
				Base(speed=25, stamina=50, mana=100), 
				Defensive(max_health=75, armor=0, magic_resistance=10), 
				Offensive(physical=15, magic=30)
			), 
			name,
			skills
			)

class Dwarf(BaseBeing):
	def __init__(self, element: Element, name: str, skills = {}):
		super().__init__(
			element, 
			Stats(
				Base(speed=10, stamina=200, mana=0), 
				Defensive(max_health=200, armor=25, magic_resistance=20), 
				Offensive(physical=35, magic=0)
			), 
			name,
			skills
			)

class Demon(BaseBeing):
	def __init__(self, element: Element, name: str, skills = {}):
		super().__init__(
			element, 
			Stats(
				Base(speed=15, stamina=125, mana=50), 
				Defensive(max_health=125, armor=10, magic_resistance=-10), 
				Offensive(physical=25, magic=35)
			), 
			name,
			skills
			)

class LizardMan(BaseBeing):
	def __init__(self, element: Element, name: str, skills = {}):
		super().__init__(
			element, 
			Stats(
				Base(speed=20, stamina=150, mana=50), 
				Defensive(max_health=125, armor=50, magic_resistance=0), 
				Offensive(physical=30, magic=5)
			), 
			name,
			skills
			)