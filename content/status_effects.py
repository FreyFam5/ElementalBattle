from __future__ import annotations
from visuals.terminal_screen import add_border, BorderPresets
import random
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	import content.races as races

class BaseEffect():
	def __init__(self, name: str, max_counter: int, target: races.BaseBeing, value: int = 0, max_stacks: int = 1):
		self.name = name
		self.max_counter = max_counter
		self.counter = max_counter
		self.target = target
		self.stacks = 0
		self.prev_stacks = self.stacks
		self.value = value
		self.max_stacks = max_stacks
		self.effect_applied = False
	
	def __repr__(self):
		return self.name
	
	def __eq__(self, other):
		if not isinstance(other, BaseEffect):
			return NotImplementedError
		return other.name == self.name

	def effect(self) -> bool: # Returns true if the effect has run out of counters, ie. the effect has "ended" 
		if self.prev_stacks < self.stacks:
			self.added_stack()
		if self.counter > 0:
			self.counter_ticked()
			print(add_border(f"{self} has {self.counter + 1} turns left until expiring!", top="0", bot="0", corners="0"))
			return False
		else:
			print(add_border(f'"{self}" has ended on {self.target.name}!'))
			return True
	
	# Method is called when a stack is added
	def added_stack(self):
		self.counter = self.max_counter
		self.stacks = min(self.stacks, self.max_stacks)
		self.prev_stacks = self.stacks
	
	# Method is called when the counter is incremented
	def counter_ticked(self):
		self.counter -= 1
		

##* Debuffs
##? Does damage to the target every turn
class Burn(BaseEffect):
	def __init__(self, target: races.BaseBeing = None):
		super().__init__("Burn", 3, target, 10)
	
	# When effects counter is incremented, does the value damage to the target
	def counter_ticked(self):
		super().counter_ticked()
		self.target.stats.defensive.health -= self.value
		print(add_border(f"{self.target.name} has been burned for {self.value} damage!", preset=BorderPresets.DEBUFF))

##? Reduces the targets armor based on the amount of stacks
class BrokenBody(BaseEffect):
	def __init__(self, target: races.BaseBeing = None):
		super().__init__("Broken Body", 3, target, 5, 3)
		self.total_armor_reduce = self.value
	
	# When effect ends, gives the armor back to the target
	def effect(self) -> bool:
		if super().effect():
			self.target.stats.defensive.armor += self.total_armor_reduce
			return True

	# When a stack is added, temporarily un-applies the effect
	def added_stack(self):
		super().added_stack()
		self.target.stats.defensive.armor += (self.stacks - 1) * self.value
		self.effect_applied = False

	# When the counter is ticked, if the effect wasn't applied then it will apply it and reduce the armor (value * amount of stacks)
	def counter_ticked(self):
		super().counter_ticked()
		if not self.effect_applied:
			self.effect_applied = True
			self.total_armor_reduce = self.value * self.stacks
			self.target.stats.defensive.armor -= self.total_armor_reduce
			print(add_border(f"{self.target.name} has had {self} applied to them, losing {self.total_armor_reduce} armor", preset=BorderPresets.DEBUFF))

##? Reduces the targets magic resistance base on the amount of stacks
class BrokenMind(BaseEffect):
	def __init__(self, target: races.BaseBeing = None):
		super().__init__("Broken Mind", 3, target, 3, 3)
		self.total_magic_resistance_reduce = self.value
	
	# When effect ends, gives the magic resistance back to the target
	def effect(self):
		if super().effect():
			self.target.stats.defensive.magic_resistance += self.total_magic_resistance_reduce
			return True

	# When a stack is added, temporarily un-applies the effect
	def added_stack(self):
		super().added_stack()
		self.target.stats.defensive.magic_resistance += (self.stacks - 1) * self.value
		self.effect_applied = False

	# When the counter is ticked, if the effect wasn't applied then it will apply it and reduce the magic resistance (value * amount of stacks)
	def counter_ticked(self):
		super().counter_ticked()
		if not self.effect_applied:
			self.effect_applied = True
			self.total_magic_resistance_reduce = self.value * self.stacks
			self.target.stats.defensive.magic_resistance -= self.total_magic_resistance_reduce
			print(add_border(f"{self.target.name} has had {self} applied to them, losing {self.total_magic_resistance_reduce} magic resistance", preset=BorderPresets.DEBUFF))


##* Buffs
##? Slowly heals the target every turn
class SlowHeal(BaseEffect):
	def __init__(self, target: races.BaseBeing = None):
		super().__init__("Slow Heal", 3, target, 5, 3)
	
	# When effects counter is incremented, does the value damage to the target
	def counter_ticked(self):
		super().counter_ticked()
		total_heal = self.value * self.stacks
		total_heal = min(total_heal, self.target.stats.defensive.max_health - self.target.stats.defensive.health)
		self.target.stats.defensive.health += total_heal
		print(add_border(f"{self.target.name} has been healed for {total_heal} hp from {self.name}!", preset=BorderPresets.BUFF))

##? Increases the targets armor based on the amount of stacks
class StrongBody(BaseEffect):
	def __init__(self, target: races.BaseBeing = None):
		super().__init__("Strong Body", 3, target, 5, 3)
		self.total_armor_increase = self.value
	
	# When effect ends, gives the armor back to the target
	def effect(self):
		if super().effect():
			self.target.stats.defensive.armor -= self.total_armor_increase
			return True

	# When a stack is added, temporarily un-applies the effect
	def added_stack(self):
		super().added_stack()
		self.target.stats.defensive.armor -= (self.stacks - 1) * self.value
		self.effect_applied = False

	# When the counter is ticked, if the effect wasn't applied then it will apply it and reduce the armor (value * amount of stacks)
	def counter_ticked(self):
		super().counter_ticked()
		if not self.effect_applied:
			self.effect_applied = True
			self.total_armor_increase = self.value * self.stacks
			self.target.stats.defensive.armor += self.total_armor_increase
			print(add_border(f"{self.target.name} has had {self} applied to them, gaining {self.total_armor_increase} armor", preset=BorderPresets.BUFF))

##? Increase the targets magic resistance based on the amount of stacks
class StrongMind(BaseEffect):
	def __init__(self, target: races.BaseBeing = None):
		super().__init__("Strong Body", 3, target, 5, 3)
		self.total_mag_res_increase = self.value
	
	# When effect ends, gives the magic_resistance back to the target
	def effect(self):
		if super().effect():
			self.target.stats.defensive.magic_resistance -= self.total_mag_res_increase
			return True
	
	# When a stack is added, temporarily un-applies the effect
	def added_stack(self):
		super().added_stack()
		self.target.stats.defensive.magic_resistance -= (self.stacks - 1) * self.value
		self.effect_applied = False

	# When the counter is ticked, if the effect wasn't applied then it will apply it and reduce the magic resistance (value * amount of stacks)
	def counter_ticked(self):
		super().counter_ticked()
		if not self.effect_applied:
			self.effect_applied = True
			self.total_mag_res_increase = self.value * self.stacks
			self.target.stats.defensive.magic_resistance += self.total_mag_res_increase
			print(add_border(f"{self.target.name} has had {self} applied to them, gaining {self.total_mag_res_increase} magic resistance", preset=BorderPresets.BUFF))

class Rest(BaseEffect):
	def __init__(self, target: races.BaseBeing = None):
		super().__init__("Rest", 1, target, 5)
	
	def counter_ticked(self):
		super().counter_ticked()
		picked_stat = ""
		match random.randrange(0, 2):
			case 0:
				self.target.stats.base.stamina += self.value
				picked_stat = "stamina"
			case 1:
				self.target.stats.base.mana += self.value
				picked_stat = "mana"
		print(add_border(f"{self.target.name} has gained {self.value} {picked_stat}!", preset=BorderPresets.BUFF))