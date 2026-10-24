nilai = [75, 55, 80, 60, 45, 90]
lulus = []

for x in nilai:
    if x >= 60:
        lulus.append(x)

print(f"nilai lulus = {lulus}")
print(f"jumlah lulus = {len(lulus)}")