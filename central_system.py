from copy import deepcopy
import content.presets as presets
from visuals.terminal_screen import add_border, add_dialogue, add_options


races_list: list[presets.races.BaseBeing] = deepcopy(presets.RACE_PRESET_LIST)


def start_game():
	# First message
	add_dialogue("Welcome to elemental battle! Are you ready to join the battle?")

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

	print(add_border(f"You are now {player.name} the {player}!"))