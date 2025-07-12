import csv


def write_contacts_to_file(filename, contacts):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        columns = contacts[0].keys()
        writer = csv.DictWriter(f, delimiter=",", fieldnames=columns)
        writer.writeheader()
        for row in contacts:
            writer.writerow(row)

             
def read_contacts_from_file(filename):
    contacts = []
    with open(filename, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for contact in reader:
            contacts.append(contact)
    return contacts
    
    #    contacts = []  # створюємо список у функції
    #     for contact in reader:
    #         contacts.append(contact)
    # return contacts 



filename = "contact.csv"
contacts = contacts = [
    {
        "name": "Allen Raymond",
        "email": "nulla.ante@vestibul.co.uk",
        "phone": "(992) 914-3792",
        "favorite": False
    },
    {
        "name": "Jane Doe",
        "email": "jane@example.com",
        "phone": "123-456-7890",
        "favorite": True
    }
]
write_contacts_to_file(filename, contacts)
print(read_contacts_from_file(filename))