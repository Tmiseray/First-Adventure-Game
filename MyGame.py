from os import system
from random import randint

game_title = 'Deep Dungeons - An Interactive Adventure Game'
system('mode 110,30')
system('Title: '+game_title)

def clear_screen():
	system('cls')

character_name = None
character_race = None
character_class = None
character_strength = None
character_dexterity = None
character_stamina = None
character_intelligence = None
character_intuition = None
character_charisma = None
character_mana = None

clear_screen()


print('Deep Dungeons - An interactive fiction game in python.')	

def Intro():
	print('')
	print('In this adventure, you are the hero!')
	print('Your decisions, skills, and a little bit of luck, will influence the outcome of the game.')
	print('')
	print('The evil sorceress has imprisoned your fellow adventurers!')
	print('Will you succeed in freeing your party from the castle dungeons, or end in perilous failure?!')
	print('')
	input('Press Enter to Continue...')

Intro()

def create_character():
	clear_screen()
	global character_name
	character_name = input('''
						Let's begin by creating your character.
						What is the name of your adventurer?
						
						> ''')
	global character_race
	while character_race is None:
		race_choice = input('''
					  Choose your character's race from the list below by entering the corresponding number:
					  1 - Elf
					  2 - Dwarf
					  3 - Tiefling
					  4 - Human
					  
					  > ''')
		if race_choice == '1':
			character_race = 'Elf'
		elif race_choice == '2':
			character_race = 'Dwarf'
		elif race_choice == '3':
			character_race = 'Tiefling'
		elif race_choice == '4':
			character_race = 'Human'
		else:
			print('Not a valid selection, choose wisely adventurer...')
	clear_screen()

	global character_class
	while character_class is None:
		class_choice = input('''
		Select your character's class from the list below by entering the corresponding number:
		1 - Cleric
		2 - Barbarian
		3 - Druid
		4 - Warlock

		>''')
		if class_choice == '1':
			character_class = 'Cleric'
		elif class_choice == '2':
			character_class = 'Barbarian'
		elif class_choice == '3':
			character_class = 'Druid'
		elif class_choice == '4':
			character_class = 'Warlock'
		else:
			print('Not a valid choice. Pick carefully, your fellow adventurers lives may very well depend on it...')

create_character()

print('Good Morrow '+character_name+'!')
print('How exciting to meet a real life '+character_race+'!')
print('You arrived not a moment too soon!')
print('Your fellow adventurers are in dire need of a crafty '+character_class+' to rescue them from the evil sorceress!')
print('')
input('Press Enter to Continue...')

def create_character_skill_sheet():
	clear_screen()
	global character_name, character_race, character_class, character_strength, character_dexterity, character_stamina, character_intelligence, character_intuition, character_charisma, character_mana
	print('''
	   Now let's determine your character's skills, which you will use throughout the game. In this game, your character has seven skills:
	   - Strength AKA bodily power, which you will use in combat or any strength test
	   - Dexterity AKA physical agility, which you will use in any ability test
	   - Stamina AKA life, which determines your life energy, points will be lost when you are hurt, and whenever Stamina reaches 0, your character dies.
	   - Intelligence AKA analytic skill, which you will use for information recall and general understanding of concepts.
	   - Intuition AKA insight, which you will use for awareness whether it's with other races, classes, animals, items, or places.
	   - Charisma AKA confidence, which you will use for occasional persuasion of leadership or friendship opportunities.
	   - Mana AKA magic, which you will use whenever you need to cast a spell or use/inspect magical items or places.

	   Depending on your race and class, you will have a certain point-base already calculated by the game.
	   You will shortly be able to increase your skills by rolling 3 6-faced dice and totaling the 2 highest dice. Which will then be added to your current ability score.
	   
	   Here is your base Character Skills Sheet:
	   ''')
	
	character_strength = 5
	character_dexterity = 3
	character_stamina = 10
	character_intelligence = 3
	character_intuition = 3
	character_charisma = 3
	character_mana = 0

	if character_race == 'Elf':
		character_strength = character_strength + 2
		character_dexterity = character_dexterity + 3
		character_stamina = character_stamina + 1
		character_intelligence = character_intelligence + 2
		character_intuition = character_intuition + 1
		character_charisma = character_charisma + 2
		character_mana = character_mana + 3

	elif character_race == 'Dwarf':
		character_strength = character_strength + 3
		character_dexterity = character_dexterity + 1
		character_stamina = character_stamina + 2
		character_intelligence = character_intelligence + 1
		character_intuition = character_intuition + 1
		character_charisma = character_charisma + 3
		character_mana = character_mana + 1

	elif character_race == 'Tiefling':
		character_strength = character_strength + 2
		character_dexterity = character_dexterity + 2
		character_stamina = character_stamina + 2
		character_intelligence = character_intelligence + 3
		character_intuition = character_intuition + 2
		character_charisma = character_charisma + 2
		character_mana = character_mana + 3

	elif character_race == 'Human':
		character_strength = character_strength + 1
		character_dexterity = character_dexterity + 1
		character_stamina = character_stamina + 2
		character_intelligence = character_intelligence + 2
		character_intuition = character_intuition + 1
		character_charisma = character_charisma + 2
		character_mana = character_mana + 2

	if character_class == 'Cleric':
		character_strength = character_strength + 2
		character_dexterity = character_dexterity + 1
		character_stamina = character_stamina + 1
		character_intelligence = character_intelligence + 3
		character_intuition = character_intuition + 3
		character_charisma = character_charisma + 1
		character_mana = character_mana + 2

	elif character_class == 'Barbarian':
		character_strength = character_strength + 3
		character_dexterity = character_dexterity + 1
		character_stamina = character_stamina + 3
		character_intelligence = character_intelligence + 1
		character_intuition = character_intuition + 1
		character_charisma = character_charisma + 1
		character_mana = character_mana + 1

	elif character_class == 'Druid':
		character_strength = character_strength + 1
		character_dexterity = character_dexterity + 2
		character_stamina = character_stamina + 2
		character_intelligence = character_intelligence + 2
		character_intuition = character_intuition + 3
		character_charisma = character_charisma + 2
		character_mana = character_mana + 3

	elif character_class == 'Warlock':
		character_strength = character_strength + 1
		character_dexterity = character_dexterity + 2
		character_stamina = character_stamina + 2
		character_intelligence = character_intelligence + 3
		character_intuition = character_intuition + 2
		character_charisma = character_charisma + 3
		character_mana = character_mana + 3

	print('''
	Name: '''+character_name+
	'''
	Race: '''+character_race+
	'''
	Class: '''+character_class+
	'''
	Strength: '''+str(character_strength)+
	'''
	Dexterity: '''+str(character_dexterity)+
	'''
	Stamina: '''+str(character_stamina)+
	'''
	Intelligence: '''+str(character_intelligence)+
	'''
	Intuition: '''+str(character_intuition)+
	'''
	Charisma: '''+str(character_charisma)+
	'''
	Mana: '''+str(character_mana)+
	'''
	''')
	input('Press Enter to apply your skills modifiers.')

create_character_skill_sheet()

def modify_skills():
	clear_screen()
	global character_name, character_race, character_class, character_strength, character_dexterity, character_stamina, character_intelligence, character_intuition, character_charisma, character_mana
	print('To modify your skills, you will roll 3 six face dice for each of your skill.')
	print('Then the game will take the 2 highest values and add your total score to the revelant skill.')
	