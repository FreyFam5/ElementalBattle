from __future__ import annotations
import random
from copy import deepcopy
from enum import Enum
import content.status_effects as status_effects
from content.elements import Elements, contest_elements
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from content.races import BaseBeing


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
			cost: tuple[str, int], 
			value: list[int],
			element: Elements,
			skill_type: SkillTypes,
			resistance_type: ResistanceTypes = ResistanceTypes.ARMOR,
			effect: status_effects.BaseEffect = None
			):
		self.name = name # The name of the skill
		self.cost = cost # The resource cost of the skill
		self.resistance_type = resistance_type # The type of resistance that this skill will be checked against
		self.value = value # The value of the skill, either damage or healing
		self.element = element # The element the skill will use
		self.skill_type = skill_type # Holds wether the skill is an attack/support skill
		self.effect = effect # The optional effect that is applied by this skill
	
	def __eq__(self, other):
		if not isinstance(other, BaseSkill):
			return other == self.name
		return other.name == self.name

	def __repr__(self):
		return self.name

	## Uses the skill and returns if it was used or not
	def use(self, user: BaseBeing, target: BaseBeing) -> bool:
		# Takes the correct resource if possible
		match self.cost[0]:
			case "s":
				if user.stats.base.stamina < self.cost[1]:
					return False
				user.stats.base.stamina -= self.cost[1]
			case "m":
				if user.stats.base.mana < self.cost[1]:
					return False
				user.stats.base.mana -= self.cost[1]

		match self.skill_type:
			# Skills that are meant to target the users enemy, ie. "attacking" them
			case SkillTypes.ATTACK:
				
				total_damage = 0
				# Checks to see if it is a random amount of damage or not
				if len(self.value) > 1:
					total_damage = round(random.randrange(self.value[0], self.value[1]))
				else:
					total_damage = self.value[0]
					if total_damage == 0:
						print(f"{user.name} used {self.name} on {target.name}!")
						return
				# Increase damage of skill if it's element matches its user element
				if user.element == self.element:
					total_damage *= 2
				# Increases/Reduces damage of skill based on the defending element
				total_damage = round(total_damage * contest_elements(self.element, target.element))
				# If the skills resistance type is armor, use armor for checking
				if self.resistance_type == ResistanceTypes.ARMOR:
					total_damage -= target.stats.defensive.armor
				# Else use magic resistance
				else: 
					total_damage -= target.stats.defensive.magic_resistance
				# Does the damage to the target, also makes sure the damage is always at least 1
				total_damage = max(total_damage, 1)
				target.stats.defensive.health -= total_damage
				
				print(f"{user.name} used {self.name} on {target.name}!")
				if total_damage > 0:
					print(f"It did {total_damage} {self.element.value} damage!")

			# Skills that are meant to be used on the user themselves, ie. "supporting" them
			case SkillTypes.SUPPORT:
				total_healing: int = 0
				# Checks to see if it is a random amount of healing or not
				if len(self.value) > 1:
					total_healing = round(random.randrange(self.value[0], self.value[1]))
				else:
					total_healing = self.value[0]
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
				if total_healing > 0:
					print(f"It healed {total_healing} health!")

		self.apply_effect(target)
		target.check_status()

	def apply_effect(self, target: BaseBeing):
		if not self.effect:
			return
		if self.effect.name not in target.status_effects:
			effect = deepcopy(self.effect)
			effect.target = target
			target.status_effects[effect.name] = effect
		target.status_effects[self.effect.name].stacks += 1


##* Attack Skills
class Punch(BaseSkill):
	def __init__(self):
		super().__init__(
			name="punch", 
			cost=("s", 5), 
			resistance_type=ResistanceTypes.ARMOR, 
			value=[7, 10], 
			element=Elements.PHYSICAL, 
			skill_type=SkillTypes.ATTACK
			)

class DeathRoll(BaseSkill):
	def __init__(self):
		super().__init__(
			name="death roll", 
			cost=("s", 30), 
			resistance_type=ResistanceTypes.ARMOR, 
			value=[25, 40], 
			element=Elements.EARTH, 
			skill_type=SkillTypes.ATTACK, 
			effect=status_effects.BrokenBody()
			)

class FireBall(BaseSkill):
	def __init__(self):
		super().__init__(
			name="fire ball", 
			cost=("m", 10), 
			resistance_type=ResistanceTypes.MAG_RES, 
			value=[10, 15], 
			element=Elements.FIRE, 
			skill_type=SkillTypes.ATTACK,
			effect=status_effects.Burn()
			)

class WindBlade(BaseSkill):
	def __init__(self):
		super().__init__(
			name="wind blade", 
			cost=("m", 5), 
			resistance_type=ResistanceTypes.MAG_RES, 
			value=[30, 40], 
			element=Elements.WIND, 
			skill_type=SkillTypes.ATTACK
			)

class WaterBolt(BaseSkill):
	def __init__(self):
		super().__init__(
			name="water bolt", 
			cost=("m", 25), 
			resistance_type=ResistanceTypes.MAG_RES, 
			value=[15, 22], 
			element=Elements.WATER, 
			skill_type=SkillTypes.ATTACK,
			effect=status_effects.BrokenMind()
			)

##* Support Skills
class MoistHeal(BaseSkill):
	def __init__(self):
		super().__init__(
			name="moist heal", 
			cost=("m", 20), 
			resistance_type=ResistanceTypes.MAG_RES,
			value=[15, 30], 
			element=Elements.WATER, 
			skill_type=SkillTypes.SUPPORT
			)

class WarmHeal(BaseSkill):
	def __init__(self):
		super().__init__(
			name="warm heal", 
			cost=("m", 20), 
			resistance_type=ResistanceTypes.MAG_RES,
			value=[5, 7], 
			element=Elements.FIRE, 
			skill_type=SkillTypes.SUPPORT, 
			effect=status_effects.SlowHeal()
			)

class ArmorUp(BaseSkill):
	def __init__(self):
		super().__init__(
			name="armor up", 
			cost=("s", 25), 
			resistance_type=ResistanceTypes.ARMOR,
			value=[0], 
			element=Elements.EARTH, 
			skill_type=SkillTypes.SUPPORT, 
			effect=status_effects.StrongBody()
			)

class MindUp(BaseSkill):
	def __init__(self):
		super().__init__(
			name="mind up", 
			cost=("m", 30), 
			resistance_type=ResistanceTypes.MAG_RES,
			value=[0], 
			element=Elements.WIND, 
			skill_type=SkillTypes.SUPPORT, 
			effect=status_effects.StrongMind()
			)