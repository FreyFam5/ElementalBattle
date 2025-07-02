from copy import deepcopy
import content.presets as presets
from visuals.terminal_screen import add_border, add_dialogue, add_options


races_list: list[presets.races.BaseBeing] = deepcopy(presets.RACE_PRESET_LIST)
element_list: list[presets.elements.Elements] = deepcopy(presets.ELEMENTS_PRESET_LIST)
atk_list: list[presets.skills.BaseSkill] = deepcopy(presets.ATTACK_SKILL_PRESET_LIST)
sup_list: list[presets.skills.BaseSkill] = deepcopy(presets.SUPPORT_SKILL_PRESET_LIST)

## Creates a playable character
def CreateCharacter():
	# Player name input
	player_name = ""
	while True:
		player_name: str = add_dialogue("Welcome new battler! Would you kindly bestow upon me your name?",  "Name here: ", []).capitalize()
		want_to_change = bool(add_dialogue(f'Are you sure you want to use "{player_name}" for your name?', "Y = yes | N = no: ", ["y", "n"], True))

		if not want_to_change:
			break
	
	# Player race input
	player: presets.races.BaseBeing = None
	player = add_options(f"Brilliant {player_name}, well then pick a race!: ", races_list)
	player.name = player_name
	# Players element
	player.element = add_options(f"Alright {player.name}! Pick your favorite element!: ", element_list)
	# Players first attack skill
	player.skills.append(add_options(f"Nice, you are now {player.name} the {player.element.value} {player}! Time to pick some skills! First, pick an attack skill!: ", atk_list))
	# Player second attack skill
	temp_atk_list = deepcopy(atk_list)
	temp_atk_list.remove(player.skills[0])
	player.skills.append(add_options(f"Now pick a second attack skill!: ", temp_atk_list))
	del temp_atk_list
	# Players support skill
	player.skills.append(add_options(f"Now pick a support skill!: ", sup_list))
	# Adds the rest skill to every player
	player.skills.append(deepcopy(presets.skills.Rest()))

	add_dialogue(f"Welcome to the world {player.name}! We hope you enjoy your time!")
	print(player.stats)
	#if len(player.skills) > 4:
	#	player.skills = player.skills[:4]
	return player

## Sets combat between two players
def CombatBetween(fighter_one: presets.races.BaseBeing, fighter_two: presets.races.BaseBeing):
	turn_number: int = 1
	first_fighter: presets.races.BaseBeing = None
	second_fighter: presets.races.BaseBeing = None
	# Decides who goes first based on speed
	if fighter_one.stats.base.speed >= fighter_two.stats.base.speed:
		first_fighter, second_fighter = fighter_one, fighter_two
	elif fighter_one.stats.base.speed < fighter_two.stats.base.speed:
		first_fighter, second_fighter = fighter_two, fighter_one
	print(add_border(f"{first_fighter.name} was faster so they go first!", top=">", bot=">", corners=">", sides=">"))
	CombatRecursive(first_fighter, second_fighter, turn_number)

# Recursively calls combat until one player wins
def CombatRecursive(current_fighter: presets.races.BaseBeing, next_fighter: presets.races.BaseBeing, turn_number: int):
	print("\n")
	winning_fighter: presets.races.BaseBeing = None
	# If either player is dead, calls the other the winner
	if current_fighter.stats.defensive.health <= 0:
		winning_fighter = next_fighter
	if next_fighter.stats.defensive.health <= 0:
		winning_fighter = current_fighter
	if winning_fighter:
		print(add_border(f"{next_fighter.name} has won! Congratulations!", top="&", bot="&", corners="X", sides="%"))
		return
	# Prints the turn number and current fighters name
	print(add_border(f"Turn: {turn_number}"))
	print(add_border(f"{current_fighter.name}'s turn!"))
	turn_number += 1
	# Gives the current fighter a choice of their skills to use, if they can't use that skill it throw them back to choice
	idx = current_fighter.skills.index(add_options(f"{current_fighter.name} choose a skill to use!: ", current_fighter.skills))
	while not current_fighter.skills[idx].use(current_fighter, next_fighter):
		idx = current_fighter.skills.index(add_options(f"{current_fighter.name} choose another skill to use!: ", current_fighter.skills))
	# Recursive call
	CombatRecursive(next_fighter, current_fighter, turn_number)