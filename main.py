import central_system
def main():
	print("Player One: ")
	player_one = central_system.CreateCharacter()
	print("Player Two: ")
	player_two = central_system.CreateCharacter()

	central_system.CombatBetween(player_one, player_two)


if __name__ == "__main__":
	main()