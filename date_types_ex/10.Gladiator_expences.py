lost_fight_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
total_helmet_broken = lost_fight_count // 2
total_sword_broken = lost_fight_count // 3
total_shield_broken = lost_fight_count // (2 * 3)
total_armor_broken = total_shield_broken // 2
expenses = (total_helmet_broken * helmet_price
            + total_sword_broken * sword_price + total_shield_broken * shield_price
            + total_armor_broken * armor_price)
print(f"Gladiator expenses: {expenses:.2f} aureus")
# You will receive Peter's lost fights count.
# Every second lost game, his helmet is broken.
# Every third lost game, his sword is broken.
# When both his sword and helmet are broken in the same lost fight, his shield also breaks.
# Every second time his shield brakes, his armor also needs to be repaired.
# You will receive the price of each item in his equipment. Calculate his expenses for the year for renewing his
