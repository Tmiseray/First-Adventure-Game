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

print(game_title)
print('Fictional Game Created in Python.')	

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

		> ''')
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
	   Now let's determine your character's skills, which you will use throughout the game.
	   In this game, your character has seven skills:

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
	print('To modify your skills, you will roll 3 6-faced dice for each of your skills.')
	print('Then the game will take the 2 highest values and add your total score to the revelant skill.')
	
	input('Press Enter to roll for Strength')
	roll1 = randint(1,6)
	roll2 = randint(1,6)
	roll3 = randint(1,6)
	rolls = [roll1, roll2, roll3]
	rolls.sort()
	print('You rolled: '+str(roll1)+', '+str(roll2)+', & '+str(roll3)+'!')
	print('Your highest values are: '+str(rolls[-2:]))
	character_strength = character_strength + rolls[-1] + rolls[-2]

	input('Press Enter to roll for Dexterity')
	roll1 = randint(1,6)
	roll2 = randint(1,6)
	roll3 = randint(1,6)
	rolls = [roll1, roll2, roll3]
	rolls.sort()
	print('You rolled: '+str(roll1)+', '+str(roll2)+', & '+str(roll3)+'!')
	print('Your highest values are: '+str(rolls[-2:]))
	character_dexterity = character_dexterity + rolls[-1] + rolls[-2]

	input('Press Enter to roll for Stamina')
	roll1 = randint(1,6)
	roll2 = randint(1,6)
	roll3 = randint(1,6)
	rolls = [roll1, roll2, roll3]
	rolls.sort()
	print('You rolled: '+str(roll1)+', '+str(roll2)+', & '+str(roll3)+'!')
	print('Your highest values are: '+str(rolls[-2:]))
	character_stamina = character_stamina + rolls[-1] + rolls[-2]

	input('Press Enter to roll for Intelligence')
	roll1 = randint(1,6)
	roll2 = randint(1,6)
	roll3 = randint(1,6)
	rolls = [roll1, roll2, roll3]
	rolls.sort()
	print('You rolled: '+str(roll1)+', '+str(roll2)+', & '+str(roll3)+'!')
	print('Your highest values are: '+str(rolls[-2:]))
	character_intelligence = character_intelligence + rolls[-1] + rolls[-2]

	input('Press Enter to roll for Intuition')
	roll1 = randint(1,6)
	roll2 = randint(1,6)
	roll3 = randint(1,6)
	rolls = [roll1, roll2, roll3]
	rolls.sort()
	print('You rolled: '+str(roll1)+', '+str(roll2)+', & '+str(roll3)+'!')
	print('Your highest values are: '+str(rolls[-2:]))
	character_intuition = character_intuition + rolls[-1] + rolls[-2]

	input('Press Enter to roll for Charisma')
	roll1 = randint(1,6)
	roll2 = randint(1,6)
	roll3 = randint(1,6)
	rolls = [roll1, roll2, roll3]
	rolls.sort()
	print('You rolled: '+str(roll1)+', '+str(roll2)+', & '+str(roll3)+'!')
	print('Your highest values are: '+str(rolls[-2:]))
	character_charisma = character_charisma + rolls[-1] + rolls[-2]

	input('Press Enter to roll for Mana')
	roll1 = randint(1,6)
	roll2 = randint(1,6)
	roll3 = randint(1,6)
	rolls = [roll1, roll2, roll3]
	rolls.sort()
	print('You rolled: '+str(roll1)+', '+str(roll2)+', & '+str(roll3)+'!')
	print('Your highest values are: '+str(rolls[-2:]))
	character_mana = character_mana + rolls[-1] + rolls[-2]

	input('Press Enter to Continue...')
	clear_screen()
	print('''
	   Congratulations! You have completed your character creation!
	   Your final character sheet is:
	   
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
	input('Press Enter to begin your adventure, if you dare...')

modify_skills()

def Scene_1():
	clear_screen()
	choice = None
	while choice is None:
		user_input = input('''
					 You have entered the Castle Dungeon...
					 Tis darker than dusk before the dawn...
					 Luckily your torch is lit and you can see up to 20 paces.
					 The stone walls are damp, the smell of rats and orcs is STRONG...
					 You walk down a narrow corridor, until you reach a thick, stone wall.
					 
					 The corridor continues on the left and to the right...
					 
					 What do you do?
					 
					 1 - Turn Left
					 2 - Turn Right
					 > ''')
		if user_input == '1' or user_input == 'turn left' or user_input == 'Turn Left' or user_input == 'Turn left':
			choice = '1'
			Scene_2()

		elif user_input == '2' or user_input == 'turn right' or user_input == 'Turn Right' or user_input == 'Turn right':
			choice = '2'
			Scene_3()

		else:
			print('''
		 Not a valid selection...
		 Either type a number or "Turn Left" / "Turn Right"
		 ''')
			
def Scene_2():
	clear_screen()
	choice = None
	while choice is None:
		user_input = input('''
					 From the darkness behind you...
					 
					 You hear a strange noise...
					 
					 What do you do?
					 
					 1 - Continue Walking
					 2 - Stop to Listen
					 
					 > ''')
		if user_input == '1' or user_input == 'Continue' or user_input == 'Continue Walking' or user_input == 'continue' or user_input == 'continue walking':
			choice = '1'
			combat()

		elif user_input == '2' or user_input == 'Stop' or user_input == 'Stop to Listen' or user_input == 'stop' or user_input == 'stop to listen' or user_input == 'stop listen' or user_input == 'Stop Listen':
			choice = '2'
			skill_check()

		else:
			print('''
		 Not a valid choice...
		 Either type a number or type "Continue" / "Stop"
		 ''')
			
def Scene_3():
	clear_screen()
	choice = None
	while choice is None:
		user_input = input('''
					 From the darkness ahead of you...
					 
					 You hear a peculiar sound...
					 
					 What do you do?
					 
					 1 - Continue Walking
					 2 - Stop to Listen
					 
					 > ''')
		if user_input == '1' or user_input == 'Continue' or user_input == 'Continue Walking' or user_input == 'continue' or user_input == 'continue walking':
			choice = '1'
			combat()

		elif user_input == '2' or user_input == 'Stop' or user_input == 'Stop to Listen' or user_input == 'stop' or user_input == 'stop to listen' or user_input == 'stop listen' or user_input == 'Stop Listen':
			choice = '2'
			skill_check()

		else:
			print('''
		 Not a valid choice...
		 Either type a number or type "Continue" / "Stop"
		 ''')

def skill_check():
	clear_screen()
	print('''
	   A giant rock falls from the ceiling...
	   Roll a die to see if you can dodge it...
	   Or you will be crushed by it!
	   ''')
	roll = randint(1,6)
	print('You rolled: '+str(roll))
	if roll + character_dexterity > 10:
		print('''
		You dodge the stone and survive!
		Although, you haven't escaped danger yet...
		The bizarre noise in the darkness continues...
		And...
		It feels a lot closer now...
		''')
		input('Press Enter to Continue...')

	else:
		print('''
		You are smashed by the rock...
		You die...
		The game is over...
		''')
		input('Press Enter to Exit the Game.')

def combat():
	clear_screen()
	global character_stamina
	print('A horrific orc attacks you!')
	input('Press Enter to initiate combat...')
# Use a list format for the monster characteristics / skills
# This makes a simple monster character sheet
	orc = [10, 14]
# orc = [Strength, Stamina]
	while orc[1] > 0 and character_stamina > 0:
		char_roll = randint(1,6)
		print('You rolled: '+str(char_roll))
		monst_roll = randint(1,6)
		print('The moster rolled: '+str(monst_roll))
		if char_roll + character_strength >= monst_roll + orc[0]:
			print('You hit the monster!')
			orc[1] = orc[1] - randint(1,6)

		else:
			print('The monster hits you!')
			character_stamina = character_stamina - randint(1,6)

	if character_stamina > 0:
		print('''
		You defeated the orc!
		Congratulations!
		''')

	else:
		print('''
		You lost...
		Your fellow adventurers will never be freed...
		And you're dead...
		''')
		input('Press Enter to Exit the Game.')

Scene_1()
