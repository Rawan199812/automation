import shutil

from faker import Faker

fake = Faker('en_US')

potential_contacts = ""

existing_contacts = ""


for i in range(100):

    email = fake.email()
    phone_number = fake.phone_number()

    potential_contacts += fake.paragraph()
    potential_contacts += " " + email + " "
    potential_contacts += fake.paragraph()
    potential_contacts += fake.ssn()
    potential_contacts += fake.sentence()
    potential_contacts += phone_number
    potential_contacts += fake.paragraph()

    if i % 7 == 0: 
        potential_contacts += " " + email + " "
        potential_contacts + fake.sentence()

    if i % 9 == 0: 
        potential_contacts += phone_number
        potential_contacts += fake.paragraph()


    if i % 5 == 0:
        existing_contacts += email + "\n"
        existing_contacts += phone_number + "\n"


    potential_contacts += "\n"


# with open("potential-contacts.txt", "w+") as f:
#     f.write(potential_contacts)

# shutil.copy('potential-contacts.txt', '../../lab/assets/potential-contacts.txt')

# # for stretch goal
# with open("existing-contacts.txt", "w+") as f:
#     f.write(existing_contacts)

# shutil.copy('existing-contacts.txt', '../../lab/assets/existing-contacts.txt')
