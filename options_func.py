notes = []
one_one_option = {}
one_one_option['1.'] = 'Yes'
one_one_option['any_key: '] = "No, go back to main menu"
def add_a_note():
    note = input("Type your note here:")
    notes.append(note)
    print('Do you want to add another note:')
    for option in one_one_option:
        print(option, one_one_option[option])
    selection = input("Please select:")
    if selection == '1':
        add_a_note()


def view_notes():
    if notes == []:
        print("You don't have any notes")
    i = 1
    for note in notes:
        print(i, note)
        i += 1
    ans = input("Press enter to go back to main menu")

def delete_a_note():
    if notes == []:
        print("You have nothing to remove")
    else:
        del_num = input("Select a number of a note You'd like to remove:")
        if 1 <= int(del_num) <= len(notes):
            del notes[int(del_num)-1]
