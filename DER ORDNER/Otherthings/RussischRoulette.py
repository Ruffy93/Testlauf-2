import random
import time

Trommel = [False, False, False, False, False, True]
random.shuffle(Trommel)

print("Komm, lass uns Russisch Roulette spielen ;D")
time.sleep(1)
input("Drücke [Enter], um den Abzug zu betätigen, Leben oder Tod?")

Trommel_index = random.randint(0, 5)

if Trommel[Trommel_index]:
    print("Boom! Du bist gestorben.")
else:
    print("Klick... Du hast Schwein gehabt.")
