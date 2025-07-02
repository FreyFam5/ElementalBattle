from __future__ import annotations
from enum import Enum
from content.elements import Elements
from content.stats import Stats, Defensive, Offensive, Base
from visuals.terminal_screen import add_border
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	import content.status_effects as status_effects
	import content.skills as skills

class Races(Enum):
	HUMAN = "human"
	DWARF = "dwarf"
	ELF = "elf"
	LIZARD_MAN = "lizard man"
	DEMON = "demon"


class BaseBeing():
	def __init__(self, element: Elements, stats: Stats, name: str, race: Races, skills: list[skills.BaseSkill], status_effects: dict[str, status_effects.BaseEffect] = {}):
		self.stats: Stats = stats
		self.element: Elements = element
		self.skills = skills
		self.name = name
		self.race = race
		self.status_effects = status_effects
	
	## Checks the status of the called being
	def check_status(self):
		self.increment_effects()
		# The line that will be printed
		line: str = ""
		if self.stats.defensive.health <= 0:
			line = f"{self.name} has reached 0 hp and died!"
		else:
			line = f"{self.name} has {self.stats.defensive.health} / {self.stats.defensive.max_health} hp!"

		print(add_border(line))
	
	# Increments the effects on this being
	def increment_effects(self):
		effects_to_del: status_effects.BaseEffect = []
		for effect in self.status_effects:
			# Will do the effects thing then if it returns True(saying it has ended) it will remove it from the status effects
			if self.status_effects[effect].effect():
				effects_to_del.append(self.status_effects[effect])
		# After using all the effects, checks the effects to delete and gets rid of them
		for effect in effects_to_del:
			del self.status_effects[effect.name]
		effects_to_del.clear() # Deletes 
	
	# Print the race of the being if it is printed
	def __repr__(self):
		return self.race.value.capitalize()

	# If checked for equal against something
	def __eq__(self, other):
		if not isinstance(other, BaseBeing):
			return other == self.race.value # If the other is a string with the same value as the race string then will return true
		return other.element == self.element and self.race == other.race # If the other is another base being then will check against element and race

class Human(BaseBeing):
	def __init__(self, element: Elements, name: str, race: Races = Races.HUMAN, skills: list[skills.BaseSkill] = []):
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
	def __init__(self, element: Elements, name: str, race: Races = Races.ELF, skills: list[skills.BaseSkill] = []):
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
	def __init__(self, element: Elements, name: str, race: Races = Races.DWARF, skills: list[skills.BaseSkill] = []):
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
	def __init__(self, element: Elements, name: str, race: Races = Races.DEMON, skills: list[skills.BaseSkill] = []):
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
	def __init__(self, element: Elements, name: str, race: Races = Races.LIZARD_MAN, skills: list[skills.BaseSkill] = []):
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