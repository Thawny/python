class Contact:
    def __init__(self, lastname, firstname):
        self.lastname = lastname
        self.firstname = firstname


class ContactList:
    def __init__(self, contacts = []):
        self.contacts = contacts

    def addContact(self, contact):
        self.contacts.append(contact)

    def enumerateContacts(self):
        if len(self.contacts) == 0:
            print("Vous n'avez aucun contact et personne ne vous aime.")
        else:
            for c in self.contacts:
                print(c.lastname, c.firstname, " ")


def main():
    contactList, opt = ContactList(), " "
    while opt != "0":
        choice = input('Choisissez un option :\n 0: quitter\n 1: lister les contacts\n 2: ajouter un contact\n')
        if choice == "1":
            print('Voici vos contacts :')
            contactList.enumerateContacts()
        elif choice == "2":
            lastname = input("Entrez le nom de votre nouveau contact\n")
            firstname = input("Entrez le prénom de votre nouveau contact\n")
            contactList.addContact(Contact(lastname, firstname))
            print(lastname, firstname, "a bien été ajouté", end=" ")
        else:
            opt = "0"

if __name__ == "__main__":
    main()
    print("Au revoir !")
