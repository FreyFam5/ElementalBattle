def start_game():
	add_dialogue("Welcome to elemental battle! Are you ready to join the battle?")
	add_dialogue("Brilliant! Well pick a race!")


def add_dialogue(text: str, prompt: str = "Continue by typing and entering 'Y': ", options: list = ["Y"]):
	print(text)
	add_input(prompt, options)


def add_input(prompt: str, options: list) -> str:
	prompt_input = input(prompt)
	if prompt_input not in options:
		add_input(prompt, options)
	else:
		return prompt_input