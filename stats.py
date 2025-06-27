class Defensive():
	def __init__(self, health: float, armor: float, magic_resistance: float):
		self.health = health
		self.armor = armor
		self.magic_resistance = magic_resistance


class Offensive():
	def __init__(self, physical: float, magic: float):
		self.physical = physical
		self.magic = magic


class Stats():
	def __init__(self, speed: float, defensive: Defensive, offensive: Offensive):
		self.speed = speed
		self.defensive = defensive
		self.offensive = offensive


