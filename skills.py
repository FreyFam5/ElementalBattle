import random
from enum import Enum
from races import BaseBeing
from elements import Element, contest_elements


class SkillTypes(Enum):
	ATTACK = "attack"
	SUPPORT = "support"


class BaseSkill():
	def __init__(
			self, 
			name: str, 
			cost: int, 
			value: list[int], 
			element: Element,
			skill_type: SkillTypes
			):
		self.name = name
		self.cost = cost
		self.value = value
		self.element = element
		self.skill_type = skill_type
	
	def use(self, user: BaseBeing, target: BaseBeing):
		match self.skill_type:
			case SkillTypes.ATTACK:
				total_damage = round(random.randrange(self.value[0], self.value[1]))
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
				# Does the damage to the target, also makes sure the damage is always at least 1
				target.stats.defensive.health -= max(total_damage, 1)

				print(f"{user.name} used {self.name} on {target.name}!")
				print(f"It did {total_damage} {self.element.value} damage!")
				target.check_status()
			case SkillTypes.SUPPORT:
				total_healing = round(random.randrange(self.value[0], self.value[1]))
				# Increase healing if skills has same element as user
				if user.element == self.element:
					total_healing *= 2
				else:
					total_healing = round(total_healing * (2 - contest_elements(self.element, user.element)))
				
				# Forces the healing to always equal up to the max health of the being
				total_healing = min(total_healing, target.stats.defensive.max_health - target.stats.defensive.health)
				# Applies healing to target
				target.stats.defensive.health += total_healing

				print(f"{user.name} used {self.name} on {target.name}!")
				print(f"It healed {total_healing} health!")
				target.check_status()

## Attack Skills
class Punch(BaseSkill):
	def __init__(self):
		super().__init__(name="Punch", cost=5, value=[7, 10], element=Element.PHYSICAL, skill_type=SkillTypes.ATTACK)

class DeathRoll(BaseSkill):
	def __init__(self):
		super().__init__(name="Death Roll", cost=20, value=[20, 20], element=Element.PHYSICAL, skill_type=SkillTypes.ATTACK)

## Support Skills
class MoistHeal(BaseSkill):
	def __init__(self):
		super().__init__(name="Moist Heal", cost=20, value=[15, 30], element=Element.WATER, skill_type=SkillTypes.SUPPORT)