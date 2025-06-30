import races


human = races.Human(races.Element.PHYSICAL, "")
elf = races.Elf(races.Element.PHYSICAL, "")
dwarf = races.Dwarf(races.Element.PHYSICAL, "")
demon = races.Demon(races.Element.PHYSICAL, "")
lizard_man = races.LizardMan(races.Element.PHYSICAL, "")


def start_game():
	add_dialogue("Welcome to elemental battle! Are you ready to join the battle?")
	add_options("Brilliant, well then pick a race!: ", [human, elf, dwarf, demon,	lizard_man])

## Adds a bit of text then asks for an input.
def add_dialogue(text: str, prompt: str = "Continue by typing and entering 'Y': ", options: list = ["y"], skip_checking_input: bool = False):
	print(text)
	add_input(prompt, options, skip_checking_input)

## Checks the input and if it is not in the options, will ask again for a 'correct' input. This check can also be skipped.
def add_input(prompt: str, options: list, skip_checking_input: bool = False) -> str:
	prompt_input = input(prompt).lower()
	input_idx = float('inf')
	# Does a try except just incase the input isn't able to be indexed
	try:
		input_idx = int(prompt_input)
	except:
		pass
	# If the prompt isn't in options, and not skipping check, will recursively call add input
	if prompt_input not in options and not skip_checking_input:
		# Checks to see if the input was an index
		if input_idx > 0 and input_idx - 1 < len(options):
			return options[input_idx - 1]
		add_input(prompt, options)
	else:
		return prompt_input

## Adds options for player to pick through
def add_options(text: str, options: list):
	final_line = ""
	for i in range(len(options)):
		final_line += f"| {i + 1}: {options[i]} |"
	
	print("".join(["\\" for i in range(len(final_line))]))
	print(final_line)
	print("".join(["\\" for i in range(len(final_line))]))

	result = add_input(text, options)
	print(f"You picked {result}!")
	return result