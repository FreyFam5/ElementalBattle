from copy import deepcopy
import content.presets as presets
from visuals.terminal_screen import add_border, add_dialogue, add_options


races_list: list[presets.races.BaseBeing] = deepcopy(presets.RACE_PRESET_LIST)
element_list: list[presets.elements.Elements] = deepcopy(presets.ELEMENTS_PRESET_LIST)
atk_list: list[presets.skills.BaseSkill] = deepcopy(presets.ATTACK_SKILL_PRESET_LIST)
sup_list: list[presets.skills.BaseSkill] = deepcopy(presets.SUPPORT_SKILL_PRESET_LIST)


def CreateCharacter():
	# Player name input
	player_name = ""
	while True:
		player_name: str = add_dialogue("Well, write your great name below adventurer!",  "Name here: ", []).capitalize()
		want_to_change = bool(add_dialogue(f'Are you sure you want to use "{player_name}" for your name?', "Y = yes | N = no: ", ["y", "n"], True))

		if not want_to_change:
			break
	
	# Player race input
	player: presets.races.BaseBeing = add_options(f"Brilliant {player_name}, well then pick a race!: ", races_list)
	player.name = player_name

	player.element = add_options(f"Alright {player.name}! Pick your favorite element!: ", element_list)

	player.skills.append(add_options(f"Nice, you are now {player.name} the {player.element.value} {player}! Time to pick some skills! First, pick an attack skill!: ", atk_list))

	temp_atk_list = deepcopy(atk_list)
	temp_atk_list.remove(player.skills[0])
	player.skills.append(add_options(f"Now pick a second attack skill!: ", temp_atk_list))
	del temp_atk_list

	player.skills.append(add_options(f"Now pick a support skill!: ", sup_list))

	add_dialogue(f"Welcome to the world {player.name}! We hope you enjoy your time!")
	print(player.stats)
	return player


