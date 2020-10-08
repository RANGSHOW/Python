#input: 54520
#output: 8
#10, 50, 100, 500, 1000, 5000, 10000, 50000
#최소 거스름돈 개수


money = int(input())
charge_unit = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
charge_count = 0
charge_unit_idx = 0
while money != 0:
    
    if money - charge_unit[charge_unit_idx] >= 0:
        charge_count += 1
        money -= charge_unit[charge_unit_idx]
        
    else:
        charge_unit_idx += 1
        
print(charge_count)
        