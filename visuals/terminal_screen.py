from enum import Enum

class BorderPresets(Enum):
	BASIC = 0
	DEBUFF = 1
	BUFF = 2

## Adds a border to text and returns it
def add_border(value, top: str = "-", bot: str = "-", corners: str = "+", sides: str = "|", preset: BorderPresets = BorderPresets.BASIC) -> str:
	match preset:
		case BorderPresets.DEBUFF:
			top = "x"
			bot = "x"
			corners = "X"
			sides = "X"
		case BorderPresets.BUFF:
			top = "I"
			bot = "I"
			corners = "0"
		case _:
			pass
	text = ""
	text += corners + "".join([top for i in range(len(value) + 2)]) + corners + "\n"
	text += f"{sides} {value} {sides}\n"
	text += corners + "".join([bot for i in range(len(value) + 2)]) + corners
	return text

## Adds a bit of text then asks for an input.
def add_dialogue(text: str, prompt: str = "Continue by typing and entering 'Y': ", options: list = ["y"], return_idx: bool = False):
	print(add_border(text))
	return add_input(prompt, options, return_idx)

## Checks the input and if it is not in the options, will ask again for a 'correct' input. 
## This check can also be skipped. It then returns either the index or the string of the found option.
def add_input(prompt: str, options: list, return_idx: bool = False) -> str | int:
	prompt_input = input(prompt).lower()
	input_idx = float('inf') # Sets to infinity so it can be compared consistently
	# Does a try except just incase the input isn't able to be indexed
	try:
		input_idx = int(prompt_input)
	except:
		pass
	# If the prompt isn't in options, and options isn't empty, will recursively call add input
	if prompt_input not in options and len(options) != 0:
		# Checks to see if the input was an index
		if input_idx > 0 and input_idx - 1 < len(options):
			return input_idx - 1 if return_idx else options[input_idx - 1]
		print(f'"{prompt_input}" is not a valid input!')
		return add_input(prompt, options, return_idx) # Recursive call
	# Returns the prompt string if it was found
	return options.index(prompt_input) if return_idx else prompt_input

## Adds options for player to pick through and returns the given options list item that was picked
def add_options(text: str, options: list) -> any:
	final_line = ""
	for i in range(len(options)):
		if isinstance(options[i], Enum):
			final_line += f"| {i + 1}: {options[i].value} |"
		else:
			final_line += f"| {i + 1}: {options[i]} |"
	
	print(add_border(final_line, top="=", bot="="))

	result = options[add_input(text, options, True)]
	print(f"You picked {result}!")
	return result