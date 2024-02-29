import viuw
import model
import text


def find_contacts(message):
    search_word = viuw.input_data(message)
    result = model.find_contact(message)
    viuw.show_contacts(result, text.find_contact_no_result(search_word))
    return True if result else False



def start_app():
    while True:
        user_choice = viuw.show_main_menu()
        match user_choice:
            case 1:
                model.open_phone_book()
                viuw.show_message(text.phone_book_opened_successful)
            case 2:
                model.save_phone_book()
                viuw.show_message(text.phone_book_saved_successful)
            case 3:
                viuw.show_contacts(model.phone_book, text.empty_phone_book_error)
            case 4:
                new_contact = viuw.input_data(text.input_new_contact)
                model.add_new_contact(new_contact)
                viuw.show_message(text.new_contact_added_successful(new_contact[0]))
            case 5:
                find_contacts(text.input_search_word)
            case 6:
                if find_contacts(text.input_search_word_for_edit):
                    u_id = int(viuw.input_data(text.input_id_for_edet))
                    edit_contact  = viuw.input_data(text.edit_contact )
                    name = model.edit_contact(u_id, edit_contact)
                    viuw.show_message(text.edit_contact_successfui(name))
            case 7:
                if find_contacts(text.input_search_word_for_delete):
                     u_id = int(viuw.input_data(text.input_id_for_delete))
                     name = model.edit_contact(u_id)
                     viuw.show_message(text.delete_contact_successfui(name))

            case 8:
                break