import cc_dat_utils
import cc_classes
import json

#Part 3
#Load your custom JSON file
#Convert JSON data to CCLevelPack


def make_level_pack_from_json(json_data):
    new_level_pack = cc_classes.CCLevelPack()    

    #Loop through the json_data
    for level in json_data:
        #  Create a new Level object from the json_data by reading
        new_level = cc_classes.CCLevel()
        #  level_number
        new_level.level_number = level["level_number"]
        #  time
        new_level.time = level["time"]
        #  num_chips
        new_level.num_chips = level["num_chips"]
        #  upper_layer
        new_level.upper_layer = level["upper_layer"]
        #  Loop through the optional_fields
        for field in level["optional_fields"]:
            #  Create a new Field object from the json_data by reading
            #  field_int
            if field["field_int"] == 3:
                #  title
                title = field["title"]
                #  create a new TitleField object
                F3 = cc_classes.CCMapTitleField(title)
                new_level.add_field(F3)

            elif field["field_int"] == 6:
                #  password
                password = field["password"]
                #  create a new PasswordField object
                F6 = cc_classes.CCEncodedPasswordField(password)
                new_level.add_field(F6)

            elif field["field_int"] == 7:
                #  hint
                hint = field["hint"]
                #  create a new HintField object
                F7 = cc_classes.CCMapHintField(hint)
                new_level.add_field(F7)

            elif field["field_int"] == 10:
                #  Loop through the monster_move
                coordinate = []
                for coor in field["monster_move"]:
                    x, y = coor[0], coor[1]
                    # create a new Coordinate object
                    C = cc_classes.CCCoordinate(x, y)
                    coordinate.append(C)
                # create a new MonsterMovementField object
                F10 = cc_classes.CCMonsterMovementField(coordinate)
                new_level.add_field(F10)

            elif field["field_int"] == 4:
                trap_controls = []
                tx, ty = field["trap"][0], field["trap"][1]
                # Loop through the brown_buttons
                for button in field["brown_buttons"]:
                    bx, by = button[0], button[1]
                    # create a new TrapControl object
                    T = cc_classes.CCTrapControl(bx, by, tx, ty)
                    trap_controls.append(T)
                # create a new TrapControlsField object
                F4 = cc_classes.CCTrapControlsField(trap_controls)
                new_level.add_field(F4)

            elif field["field_int"] == 5:
                cloning_controls = []
                tx, ty = field["cloning_machine"][0], field["cloning_machine"][1]
                # Loop through the red_buttons
                for button in field["red_buttons"]:
                    bx, by = button[0], button[1]
                    # create a new CloningMachineControl object
                    CM = cc_classes.CCTrapControl(bx, by, tx, ty)
                    cloning_controls.append(CM)
                # create a new CloningMachineControlsField object
                F5 = cc_classes.CCCloningMachineControlsField(cloning_controls)
                new_level.add_field(F5)
        # add level to level pack
        new_level_pack.add_level(new_level)
    return new_level_pack

input_json_file = "data/kexinl_cc1.json"

#Open the file specified by input_json_file
#Use the json module to load the data from the file
with open(input_json_file, "r") as reader:
    json_data = json.load(reader)
#Use make_game_library_from_json(json_data) to convert the data to GameLibrary data
make_level_pack_from_json(json_data)
#Print out the resulting GameLibrary data using print()
new_level_pack = make_level_pack_from_json(json_data)
print(new_level_pack)
#Save converted data to DAT file
cc_dat_utils.write_cc_level_pack_to_dat(new_level_pack, "data/kexinl_cc1.dat")
