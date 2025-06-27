## Defensive stats
class Defensive():
	def __init__(self, health: int, armor: int, magic_resistance: int):
		# If this reaches zero, the being dies
		self.health = health
		# Reduces physical damage by a flat amount
		self.armor = armor
		# Reduces magic damage by a flat amount
		self.magic_resistance = magic_resistance

## Offensive stats
class Offensive():
	def __init__(self, physical: int, magic: int):
		# Increases damage done from attacks that use phyical
		self.physical = physical
		# Increases damage done from attacks that use magic
		self.magic = magic

## Base/Misc stats
class Base():
	def __init__(self, speed: int, stamina: int, mana: int):
		# Determins when this being will have their turn
		self.speed = speed
		# A resource for skills that use physical damage typically
		self.stamina = stamina
		# A resource for skills that use magic damage typically
		self.mana = mana

## The class that will be used for all the other stats
class Stats():
	def __init__(self, base: Base, defensive: Defensive, offensive: Offensive):
		self.base = base
		self.defensive = defensive
		self.offensive = offensive


