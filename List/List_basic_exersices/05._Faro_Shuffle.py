deck_of_cards = input().split()
count = int(input())

for shuffle in range(count):
    middle_od_deck = len(deck_of_cards) // 2
    left_deck = deck_of_cards[0:middle_od_deck]
    right_deck = deck_of_cards[middle_od_deck:]
    deck_after_shuffle = []
    for car_index in range(len(left_deck)):
        deck_after_shuffle.append(left_deck[car_index])
        deck_after_shuffle.append(right_deck[car_index])
    deck_of_cards = deck_after_shuffle
print(deck_of_cards)
