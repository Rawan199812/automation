import shutil
import re
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
print(potential_contacts)


with open("potential-contacts.txt", "w+") as f:
    f.write(potential_contacts)

shutil.copy('potential-contacts.txt', 'automation/assets/existing-contacts.txt') 

with open('existing-contacts.txt', 'w+') as file:
    file.write(existing_contacts)

shutil.copy('existing-contacts.txt', 'automation/assets/existing-contacts.txt')

with open('potential-contacts.txt', 'r') as file:
    text = file.read().replace('\n', '')

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))? 
    (\s|-|\.)? 
    (\d{3}) 
    (\s|-|\.)
    (\d{4}) 
    (\s*(ext|x|ext.)\s*(\d{2,5}))? 
    )''', re.VERBOSE)

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-] + 
    @                  
    [a-zA-Z0-9.-] +     
    (\.[a-zA-Z]{2,4})   
    )''', re.VERBOSE)


matches_phones = []
matches_emails = []

for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    phoneNum = re.sub(r'[(|)]', '', phoneNum)
    if phoneNum not in matches_phones:
        matches_phones.append(phoneNum)
for groups in emailRegex.findall(text):
    if groups[0] not in matches_emails:
        matches_emails.append(groups[0])

matches_phones.sort()
matches_emails.sort()

with open("phone_numbers.txt", "w+") as f:
    
    for element in matches_phones:
     f.write(element + "\n")

with open("emails.txt", "w+") as f:
    
    for element in matches_emails:
     f.write(element + "\n")


print(len(matches_phones))
print(matches_emails)
