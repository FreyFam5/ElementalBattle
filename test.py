import terminal_screen
import races
import skills
import elements


player_one = races.Human(elements.Element.PHYSICAL, "Frey", skills={"punch": skills.Punch(), "moist heal": skills.MoistHeal()})
player_two = races.Elf(elements.Element.WIND, "Elfie", skills={"punch": skills.Punch()})

player_one.skills["punch"].use(player_one, player_two)
player_two.skills["punch"].use(player_two, player_one)
player_one.skills["moist heal"].use(player_one, player_one)
player_one.skills["punch"].use(player_one, player_two)