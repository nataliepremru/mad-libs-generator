

def mad_libs_generator():
    ## Creating the mad lib generator
    print("Welcome to Mad Libs! \n To play enter the required prompts to create a story \n To quit the game at any time enter 'exit'")

    # Asking the user for inputs
    man_name = input("Please enter a mens name (e.g John): ")
    friend_name = input("Please enter another name (e.g Alex): ")
    city_1 = input("Please enter the name of a city (e.g London): ")
    time = input("Please enter a time of day (e.g 2pm): ")
    adjective_1 = input("Please enter an adjective (e.g beautiful): ")
    adjective_2 = input("Please enter another adjective (e.g tall): ")
    length = input("Please enter a adjective for length (e.g long): ")
    colour_1 = input("Please enter a colour (e.g brown): ")
    colour_2 = input("Please enter another colour (e.g green): ")
    place = input("Please enter a name of a place (e.g museum): ")
    adjective_3 = input("Please enter another adjective (e.g old): ")
    noun = input("Please enter a noun (e.g statue): ")
    city_2 = input("Please enter another name of a city (e.g Rome): ")
    adjective_4 = input("Please enter another adjective (e.g nice): ")
    day = input("Please enter a day of the week (e.g Saturday): ")

    # combining all the variables into a story
    story = f'''On a fine day a dashing young man named {man_name} went to {city_1} to meet {friend_name}.\n They met at {time} and he saw that they were {adjective_1} and {adjective_2} with {length} {colour_1} hair and {colour_2} eyes.\n They visited a {place} where they saw a {adjective_3} {noun} from {city_2}.\n They had a {adjective_4} time and promised to meet next {day}.'''
    # display the story the user has created with their inputs
    print(f"Here is the story you have created:\n {story}")

mad_libs_generator()