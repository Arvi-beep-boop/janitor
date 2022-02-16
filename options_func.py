rooms = {
    'Lobby': [],
    'Office_1': [],
    'Office_2': [],
    'Server_room_1': [],
    'Server_room_2': [],
    'Kitchen': [],
    'Bathroom':  [],
    'Conference_room': [],
    'Warehouse': [],
    'Shittyroom':  []
}


one_one_option = {}
one_one_option['1.'] = 'Yes'
one_one_option['any_key: '] = "No, go back to main menu"


def add_a_note():
    room_names = list(rooms.keys())
    for index, room in enumerate(room_names, 1):
        print(index, room)
    selection = input("Please select:")
    selected_room = rooms[room_names[int(selection) - 1]]
    selected_room.append(input('Type your note here:'))
    print('Do you want to add another note:')
    for option in one_one_option:
        print(option, str(one_one_option[option]))
    selection = input("Please select:")
    if selection == '1':
        add_a_note()


def view_notes():
    room_names = list(rooms.keys())
    for index, room in enumerate(room_names, 1):
        print(index, room)
    selection = input("Please select:")
    selected_room = rooms[room_names[int(selection)-1]]
    if selected_room == []:
        print("You don't have any notes")
    for i, note in enumerate(selected_room, 1):
        print(i, note)
    ans = input("Press enter to go back to main menu")


def delete_a_note():
    room_names = list(rooms.keys())
    for index, room in enumerate(room_names, 1):
        print(index, room)
    selection = input("Please select:")
    selected_room = rooms[room_names[int(selection) - 1]]
    if selected_room == []:
        print("You have nothing to remove")
    else:
        del_num = input("Select a number of a note You'd like to remove:")
        if 1 <= int(del_num) <= len(selected_room):
            del selected_room[int(del_num)-1]
