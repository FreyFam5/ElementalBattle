from enum import Enum

class Element(Enum):
	PHYSICAL: str = "physical"
	FIRE: str = "fire"
	WATER: str = "water"
	EARTH: str = "earth"
	WIND: str = "wind"


def contest_elements(user_element: Element, target_element: Element) -> float:
	if user_element == target_element:
		return 1.0

	match user_element:
		case Element.PHYSICAL:
			match target_element:
				case Element.FIRE: # Physical X Fire = 50% less damage
					return 0.5 
				case Element.WATER: # Physical X Water = 10% more damage
					return 1.1
				case Element.EARTH: # Physical X Earth = 20% more damage
					return 1.2
				case Element.WIND: # Physical X Wind = 25% less damage
					return 0.75
		case Element.FIRE:
			match target_element:
				case Element.PHYSICAL: # Fire X Physical = 50% more damage
					return 1.5
				case Element.WATER: # Fire X Water = 70% less damage
					return 0.3
				case Element.EARTH: # Fire X Earth = 25% more damage
					return 1.25
				case Element.WIND: # Fire X Wind = 25% more damage
					return 1.25
		case Element.WATER:
			match target_element:
				case Element.PHYSICAL: # Water X Physical = 10% more damage
					return 1.1
				case Element.FIRE: # Water X Fire = 75% more damage
					return 1.75
				case Element.EARTH: # Water X Earth = 10% more damage
					return 1.1
				case Element.WIND: # Water X Wind = 15% less damage
					return 0.85
		case Element.EARTH:
			match target_element:
				case Element.PHYSICAL: # Earth X Physical = 20% more damage
					return 1.2
				case Element.FIRE: # Earth X Fire = 25% more damage
					return 1.25
				case Element.WATER: # Earth X Water = 25% less damage
					return 0.75
				case Element.WIND: # Earth X Wind = 10% more damage
					return 1.1
		case Element.WIND:
			match target_element:
				case Element.PHYSICAL: # Wind X Physical = 20% more damage
					return 1.2
				case Element.FIRE: # Wind X Fire = 20% more damage
					return 1.2
				case Element.WATER: # Wind X Water = 10% more damage
					return 1.1
				case Element.EARTH: # Wind X Earth = 10% more damage
					return 1.1