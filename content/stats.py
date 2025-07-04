## Defensive stats
class Defensive():
	def __init__(self, max_health: int, armor: int, magic_resistance: int):
		# The max health of this character
		self.max_health = max_health
		# If this reaches zero, the being dies
		self.health = self.max_health
		# Reduces physical damage by a flat amount
		self.armor = armor
		self.max_armor = armor
		# Reduces magic damage by a flat amount
		self.magic_resistance = magic_resistance
		self.max_mag_res = magic_resistance
	
	def __repr__(self):
		return \
			f" Health: {self.health} / {self.max_health}\n" + \
			f" Armor: {self.armor}\n" + \
			f" Magic res: {self.magic_resistance}\n"

## Offensive stats
class Offensive():
	def __init__(self, physical: int, magic: int):
		# Increases damage done from attacks that use physical
		self.physical = physical
		# Increases damage done from attacks that use magic
		self.magic = magic

## Base/Misc stats
class Base():
	def __init__(self, speed: int, stamina: int, mana: int):
		# Determines when this being will have their turn
		self.speed = speed
		# A resource for skills that use physical damage typically
		self.stamina = stamina
		# A resource for skills that use magic damage typically
		self.mana = mana
	
	def __repr__(self):
		return \
			f" Speed: {self.speed} m/s \n" + \
			f" Stamina: {self.stamina}\n" + \
			f" Mana: {self.mana}\n"

## The class that will be used for all the other stats
class Stats():
	def __init__(self, base: Base, defensive: Defensive, offensive: Offensive):
		self.base = base
		self.defensive = defensive
		self.offensive = offensive
	
	def __repr__(self):
		return f"Stats:\n{self.defensive}{self.base}"
			