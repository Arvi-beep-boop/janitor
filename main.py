import options_func

menu = {}
menu['1'] = "Add a new note."
menu['2'] = "Delete a note."
menu['3'] = "View all your notes."
menu['4'] = "Exit."
while True:
    for option in menu:
        print(option, menu[option])
    selection = input("Please select:")
    if selection == '1':
        options_func.add_a_note()
    if selection == '2':
        options_func.delete_a_note()
    if selection == '3':
        options_func.view_notes()
    if selection == '4':
        exit()
    if selection not in menu:
        print('!!No such option!!')