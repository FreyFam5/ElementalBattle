import random
from enum import Enum
from races import BaseBeing
from elements import Element, contest_elements


class SkillTypes(Enum):
	ATTACK = "attack"
	SUPPORT = "support"

class ResistanceTypes(Enum):
	ARMOR = "armor"
	MAG_RES = "magic resistance"

class BaseSkill():
	def __init__(
			self, 
			name: str, 
			cost: int, 
			value: list[int],
			element: Element,
			skill_type: SkillTypes,
			resistance_type: ResistanceTypes = ResistanceTypes.ARMOR
			):
		self.name = name # The name of the skill
		self.cost = cost # The resource cost of the skill
		self.resistance_type = resistance_type # The type of resistance that this speel will be checked against
		self.value = value # The value of the skill, either damage or healing
		self.element = element # The element the skill will use
		self.skill_type = skill_type # Holds wether the skill is an attack/support skill
	
	def use(self, user: BaseBeing, target: BaseBeing):
		match self.skill_type:
			# Skills that are meant to target the users enemy, ie. "attacking" them
			case SkillTypes.ATTACK:
				total_damage = round(random.randrange(self.value[0], self.value[1]))
				# Increase damage of skill if it's element matches its user element
				if user.element == self.element:
					total_damage *= 2
				# Increases/Reduces damage of skill based on the defending element
				total_damage = round(total_damage * contest_elements(self.element, target.element))
				# If the skills restance type is armor, use armor for checking
				if self.resistance_type == ResistanceTypes.ARMOR:
					total_damage -= target.stats.defensive.armor
				# Else use magic resistance
				else: 
					total_damage -= target.stats.defensive.magic_resistance
				# Does the damage to the target, also makes sure the damage is always at least 1
				total_damage = max(total_damage, 1)
				target.stats.defensive.health -= total_damage

				print(f"{user.name} used {self.name} on {target.name}!")
				print(f"It did {total_damage} {self.element.value} damage!")
				target.check_status()

			# Skills that are meant to be used on the user themselves, ie. "supporting" them
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
		super().__init__(name="Punch", cost=5, resistance_type=ResistanceTypes.ARMOR, value=[7, 10], element=Element.PHYSICAL, skill_type=SkillTypes.ATTACK)

class DeathRoll(BaseSkill):
	def __init__(self):
		super().__init__(name="Death Roll", cost=30, resistance_type=ResistanceTypes.ARMOR, value=[25, 40], element=Element.EARTH, skill_type=SkillTypes.ATTACK)

class FIREBALL(BaseSkill):
	def __init__(self):
		super().__init__(name="Fire Ball", cost=10, resistance_type=ResistanceTypes.MAG_RES, value=[10, 15], element=Element.FIRE, skill_type=SkillTypes.ATTACK)

class WINDBLADE(BaseSkill):
	def __init__(self):
		super().__init__(name="Wind Blade", cost=5, resistance_type=ResistanceTypes.MAG_RES, value=[15, 18], element=Element.WIND, skill_type=SkillTypes.ATTACK)

## Support Skills
class MoistHeal(BaseSkill):
	def __init__(self):
		super().__init__(name="Moist Heal", cost=20, value=[15, 30], element=Element.WATER, skill_type=SkillTypes.SUPPORT)