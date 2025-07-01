from enum import Enum
from content.elements import Elements
from content.stats import Stats, Defensive, Offensive, Base
from visuals.terminal_screen import add_border

class Races(Enum):
	HUMAN = "human"
	DWARF = "dwarf"
	ELF = "elf"
	LIZARD_MAN = "lizard man"
	DEMON = "demon"


class BaseBeing():
	def __init__(self, element: Elements, stats: Stats, name: str, race: Races, skills = {}, status_effects: dict[str, int] = {}):
		self.stats: Stats = stats
		self.element: Elements = element
		self.skills = skills
		self.name = name
		self.race = race
		self.status_effects = status_effects
	
	## Checks the status of the called being
	def check_status(self):
		# The line that will be printed
		line: str = ""
		if self.stats.defensive.health <= 0:
			line = f"{self.name} has reached 0 hp and died!"
		else:
			line = f"{self.name} has {self.stats.defensive.health} hp!"

		print(add_border(line, top="+", bot="+"))
	# Print the race of the being if it is printed
	def __repr__(self):
		return self.race.value
	# If checked for equal against something
	def __eq__(self, other):
		if not isinstance(other, BaseBeing):
			return other == self.race.value # If the other is a string with the same value as the race string then will return true
		return other.element == self.element and self.race == other.race # If the other is another base being then will check against element and race

class Human(BaseBeing):
	def __init__(self, element: Elements, name: str, race: Races = Races.HUMAN, skills = {}):
		super().__init__(
			element, 
			Stats(
				Base(speed=15, stamina=100, mana=25), 
				Defensive(max_health=100, armor=0, magic_resistance=0), 
				Offensive(physical=25, magic=5)
				), 
			name,
			race,
			skills
			)

class Elf(BaseBeing):
	def __init__(self, element: Elements, name: str, race: Races = Races.ELF, skills = {}):
		super().__init__(
			element, 
			Stats(
				Base(speed=25, stamina=50, mana=100), 
				Defensive(max_health=75, armor=0, magic_resistance=10), 
				Offensive(physical=15, magic=30)
			), 
			name,
			race,
			skills
			)

class Dwarf(BaseBeing):
	def __init__(self, element: Elements, name: str, race: Races = Races.DWARF, skills = {}):
		super().__init__(
			element, 
			Stats(
				Base(speed=10, stamina=200, mana=0), 
				Defensive(max_health=200, armor=25, magic_resistance=20), 
				Offensive(physical=35, magic=0)
			), 
			name,
			race,
			skills
			)

class Demon(BaseBeing):
	def __init__(self, element: Elements, name: str, race: Races = Races.DEMON, skills = {}):
		super().__init__(
			element, 
			Stats(
				Base(speed=15, stamina=125, mana=50), 
				Defensive(max_health=125, armor=10, magic_resistance=-10), 
				Offensive(physical=25, magic=35)
			), 
			name,
			race,
			skills
			)

class LizardMan(BaseBeing):
	def __init__(self, element: Elements, name: str, race: Races = Races.LIZARD_MAN, skills = {}):
		super().__init__(
			element, 
			Stats(
				Base(speed=20, stamina=150, mana=50), 
				Defensive(max_health=125, armor=50, magic_resistance=0), 
				Offensive(physical=30, magic=5)
			), 
			name,
			race,
			skills
			)