import central_system


player_one = central_system.CreateCharacter()
player_two = central_system.CreateCharacter()

central_system.CombatBetween(player_one, player_two)