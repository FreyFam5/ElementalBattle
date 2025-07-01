import content.races as races
import content.skills as skills

# A list used to make copies for reuse
RACE_PRESET_LIST: list[races.BaseBeing] = [
	races.Human(races.Elements.PHYSICAL, ""),
	races.Elf(races.Elements.PHYSICAL, ""),
	races.Dwarf(races.Elements.PHYSICAL, ""),
	races.Demon(races.Elements.PHYSICAL, ""),
	races.LizardMan(races.Elements.PHYSICAL, "")
]

ATTACK_SKILL_PRESET_LIST: list[skills.BaseSkill] = [
	skills.Punch(),
	skills.DeathRoll(),
	skills.FireBall(),
	skills.WindBlade()
]

SUPPORT_SKILL_PRESET_LIST: list[skills.BaseSkill] = [
	skills.MoistHeal()
]