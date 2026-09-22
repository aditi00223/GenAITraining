import numpy as np

Name = ["Harnoor", "Aditi", "Harsharan", "Ekamoor", "Isha"]

attendance = [95, 84, 86, 80, 91]

fees = [100000, 120000, 90000, 110000, 150000]

n = np.array(Name)
a = np.array(attendance)
f = np.array(fees)

scholarship_percent = []

for attend in a:

    if attend >= 90 and attend <= 100:
        scholarship_percent.append(30)

    elif attend >= 80 and attend <= 89:
        scholarship_percent.append(20)

    elif attend >= 70 and attend <= 79:
        scholarship_percent.append(10)

    else:
        scholarship_percent.append(0)

sp = np.array(scholarship_percent)

scholarship_amount = f * sp / 100

final_fees = f - scholarship_amount

print("\n========== STUDENT SCHOLARSHIP REPORT ==========")

for i in range(len(n)):

    print(
        n[i],
        a[i],
        f[i],
        sp[i],
        scholarship_amount[i],
        final_fees[i]
    )