from races import BaseBeing
from elements import Element, contest_elements

class BaseSkill():
	def __init__(
			self, 
			name: str, 
			cost: int, 
			damage: int, 
			element: Element
			):
		self.cost = cost
		self.damage = damage
		self.element = element
		self.name = name
	
	def use(self, user: BaseBeing, target: BaseBeing):
		total_damage = self.damage
		# Increase damage of skill if it's element matches its user element
		if user.element == self.element:
			total_damage *= 2
		# Increases/Reduces damage of skill based on the defending element
		total_damage = round(total_damage * contest_elements(self.element, target.element))
		# If the skill is using physical element, use armor for checking
		if self.element == Element.PHYSICAL:
			total_damage -= target.stats.defensive.armor
		# Else use the magic resistance
		else: 
			total_damage -= target.stats.defensive.magic_resistance

		print(f"{user.name} used {self.name} on {target.name}!")
		print(f"It did {total_damage} {self.element.value} damage!")
		target.check_status()

class Punch(BaseSkill):
	def __init__(self,):
		super().__init__(name="Punch", cost=5, damage=10, element=Element.PHYSICAL)
	
	def use(self, user: BaseBeing, target: BaseBeing):
		super().use(user, target)
