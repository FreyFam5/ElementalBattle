from enum import Enum

class Elements(Enum):
	PHYSICAL: str = "physical"
	FIRE: str = "fire"
	WATER: str = "water"
	EARTH: str = "earth"
	WIND: str = "wind"


def contest_elements(user_element: Elements, target_element: Elements) -> float:
	if user_element == target_element:
		return 1.0

	match user_element:
		case Elements.PHYSICAL:
			match target_element:
				case Elements.FIRE: # Physical X Fire = 50% less damage
					return 0.5 
				case Elements.WATER: # Physical X Water = 10% more damage
					return 1.1
				case Elements.EARTH: # Physical X Earth = 20% more damage
					return 1.2
				case Elements.WIND: # Physical X Wind = 25% less damage
					return 0.75
		case Elements.FIRE:
			match target_element:
				case Elements.PHYSICAL: # Fire X Physical = 50% more damage
					return 1.5
				case Elements.WATER: # Fire X Water = 70% less damage
					return 0.3
				case Elements.EARTH: # Fire X Earth = 25% more damage
					return 1.25
				case Elements.WIND: # Fire X Wind = 25% more damage
					return 1.25
		case Elements.WATER:
			match target_element:
				case Elements.PHYSICAL: # Water X Physical = 10% more damage
					return 1.1
				case Elements.FIRE: # Water X Fire = 75% more damage
					return 1.75
				case Elements.EARTH: # Water X Earth = 10% more damage
					return 1.1
				case Elements.WIND: # Water X Wind = 15% less damage
					return 0.85
		case Elements.EARTH:
			match target_element:
				case Elements.PHYSICAL: # Earth X Physical = 20% more damage
					return 1.2
				case Elements.FIRE: # Earth X Fire = 25% more damage
					return 1.25
				case Elements.WATER: # Earth X Water = 25% less damage
					return 0.75
				case Elements.WIND: # Earth X Wind = 10% more damage
					return 1.1
		case Elements.WIND:
			match target_element:
				case Elements.PHYSICAL: # Wind X Physical = 20% more damage
					return 1.2
				case Elements.FIRE: # Wind X Fire = 20% more damage
					return 1.2
				case Elements.WATER: # Wind X Water = 10% more damage
					return 1.1
				case Elements.EARTH: # Wind X Earth = 10% more damage
					return 1.1