from pprint import pprint
import re
# читаем адресную книгу в формате CSV в список contacts_list
import csv
with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

def change_phonebook():
    for i in contacts_list:
        str_i = [str(j) for j in i]
        all_names_str = ' '.join(str_i[:3])
        all_names_list = all_names_str.split()
        i[0], i[1] = all_names_list[0], all_names_list[1]
        if len(all_names_list) > 2:
            i[2] = all_names_list[2]
        else:
            i[2] = ''
        pattern = re.compile(r'(\+7|8)?\s*\(?(\d{3})\)?\s*\D?(\d{3})[-\s+]?(\d{2})-?(\d{2})((\s)?\(?(доб.)?\s?(\d+)\)?)?')
        i[5] = pattern.sub(r'+7(\2)\3-\4-\5\7\8\9', str_i[5])
    return contacts_list

def delete_dubble(new_contacts):
    dictionary = {}
    for contacts in new_contacts:
        last_name = contacts[0]
        if last_name not in dictionary:
            dictionary[last_name] = contacts
        else:
            existing_contact = dictionary[last_name]
            for i in range(2, 7): 
                if existing_contact[i] == "" and contacts[i] != "":
                    existing_contact[i] = contacts[i]
    contacts_list = list(dictionary.values())
    pprint(contacts_list)
    return contacts_list
        

       

change_phonebook()
contacts_list = delete_dubble(new_contacts= contacts_list)
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding="utf-8") as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(contacts_list)
