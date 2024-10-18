import os
while True:
    first_name = input("Input your first name: ")
    last_name = input("Input your last name: ")
    if first_name.isalpha() and last_name.isalpha:
        break
    print("Error:first name and last name have  to consist in words.")

print("Do you have school education sertificate?(0-no,1-yes): ")
certificate = input("Input 0 or 1: ")
while certificate not in ['0','1']:
    print("Error:Input 0 or 1")
    certificate = input("Input 0 or 1: ")
certificate = bool(int(certificate))
if certificate == 0:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("You cannot be admitted to Ala-Too University without a school education certificate.")
    exit()

while True:
    try:
        ort = int(input("Input your points ORT: "))
        if 0 <= ort <= 240:
            break
        else:
            print("Error:Input correct points(0-240: ")
    except ValueError:
        print("Error:Input a valid numbers")
if ort < 110:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("You cannot be admitted to Ala-Too University without ORT > 110.")
    exit()

print("English language level: ")
level = ["A1",'A2','B1','B2','C1','C2']
for i,j in enumerate(level):
    print(f"{i + 1} - {j}")
eng_level = input("Your answer: ")
while eng_level not in ['1', '2', '3', '4', '5', '6']:
    print('Error:Choose correct level')
    eng_level = input("Your answer: ")
if eng_level in ('1', '2', '3'):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Your level of English is not sufficient for admission.")
    print("We invite you to take the Foundation Course AIU.")
else:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Congratulations! You meet all the requirements for admission to Ala-Too University.")
    print("Please select your specialty:")

specialties = [
     ('Computer Engineering', 2500),
    ('Artificial Intelligence', 2200),
    ('Psychology', 1900),
     ('Journalism', 1700),
     ('International Relations', 2200),
     ('Law', 1800),
     ('Management', 2200),
     ('Medicine', 3300)]
print("Select your specialty:")
for r, v in enumerate(specialties):
    print(f" {v[0]} - {v[1]}$")


specialty_choice = input("Enter the number of your chosen specialty: ")
while specialty_choice not in specialties:
    print("Error: Choose a correct specialty number.")
    specialty_choice = input("Enter the number of your chosen specialty: ")

selected_specialty, base_cost = specialties[specialty_choice]

discount = 0

if 140 <= ort <= 155:
    discount = 5
elif 156 <= ort <= 174:
    discount = 10
elif 175 <= ort <= 199:
    discount = 25
elif 200 <= ort <= 209:
    discount = 50
elif 210 <= ort <= 218:
    discount = 75
elif 219 <= ort <= 240:
    discount = 100
else:
    discount = 0


final_cost = base_cost * (1 - discount / 100)

os.system('cls' if os.name == 'nt' else 'clear')

if discount > 0:
    print(f"Dear {first_name} {last_name}, congratulations!")
    print(f"You have been admitted to the {selected_specialty} program at Ala-Too International University.")
    print(f"The cost of your education with a {discount}% discount will be {final_cost}$ per year.")
else:
    print(f"Dear {first_name} {last_name}, congratulations!")
    print(f"You have been admitted to the {selected_specialty} program at Ala-Too International University.")
    print(f"The cost of your education will be {base_cost}$ per year.")

