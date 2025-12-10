paraula1 = input("Introdueix la primera paraula: ").lower()
paraula2 = input("Introdueix la segona paraula: ").lower()

ultimes3_1 = paraula1[-3:]
ultimes3_2 = paraula2[-3:]

ultimes2_1 = paraula1[-2:]
ultimes2_2 = paraula2[-2:]

if ultimes3_1 == ultimes3_2:
    print("Les paraules rimen!")
elif ultimes2_1 == ultimes2_2:
    print("Les paraules rimen una mica.")
else:
    print("Les paraules no rimen.")
