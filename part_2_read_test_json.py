import test_data
import json

#Creates and returns a GameLibrary object(defined in test_data) from loaded json_data
def make_game_library_from_json( json_data ):
    #Initialize a new GameLibrary
    game_library = test_data.GameLibrary()

    ### Begin Add Code Here ###
    #Loop through the json_data
    for game in json_data:
        #Create a new Game object from the json_data by reading
        #  title
        title = game["title"]
        #  year
        year = game["Year"]
        #  platform (which requires reading name and launch_year)
        name = game["platform"]["name"]
        launch_year = game["platform"]["launch year"]
        platform = test_data.Platform(name, launch_year)
        #Add that Game object to the game_library
        G = test_data.Game(title, platform, year)
        game_library.add_game(G)
    ### End Add Code Here ###

    return game_library


#Part 2
input_json_file = "data/test_data.json"

### Begin Add Code Here ###
#Open the file specified by input_json_file
#Use the json module to load the data from the file
with open(input_json_file, "r") as reader:
    json_data = json.load(reader)
#Use make_game_library_from_json(json_data) to convert the data to GameLibrary data
make_game_library_from_json(json_data)
#Print out the resulting GameLibrary data using print()
print(make_game_library_from_json(json_data))
### End Add Code Here ###
