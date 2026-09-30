print("Hello, main AI seekh raha hoon!")


naam = "Ali"
umar = 22
sheher = "Rawalpindi"

print("Mera naam", naam, "hai")
print("Meri umar", umar, "saal hai")
print("Main", sheher, "mein rehta hoon")

user_naam = input("Aap ka naam kya hai? ")
print("Khush amdeed,", user_naam, "!")

umar = int(input("Aap ki umar kya hai? "))

if umar >= 18:
    print("Aap balig hain.")
else:
    print("Aap abhi bacche hain.")


for i in range(5):
    print("Ye baar number:", i)

count = 1
while count <= 3:
    print("Count hai:", count)
    count = count + 1

def welcome_karo(naam):
    print("Assalam-o-Alaikum,", naam, "! AI seekhna shuru karte hain.")

welcome_karo("Raza")
welcome_karo("Ali")
welcome_karo("Sara")


students = ["Ali", "Sara", "Raza", "Hina"]

print("Sab students:", students)
print("Pehla student:", students[0])
print("Doosra student:", students[1])

for student in students:
    print("Student ka naam:", student)