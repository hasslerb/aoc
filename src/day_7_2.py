import argparse
import math
from enum import IntEnum

card_values = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
    "J": 1,
}

types = {
    "five_of_a_kind": 10,
    "four_of_a_kind": 8,
    "full_house": 7,
    "three_of_a_kind": 6,
    "two_pair": 5,
    "one_pair": 4,
    "high_card": 2
}


def calculate_value(cards):
    i = len(cards)
    value = 0
    for card in cards:
        value += card_values[card] * ( (card_values["A"]) ** i )
        i -= 1
    return value

def get_type(cards):
    matched_cards = [card for card in cards if cards.count(card)>1 and card != "J"]
    if cards.count("J") == 5:
        return types["five_of_a_kind"]
    elif len(matched_cards) == 0:
        return types["high_card"] + cards.count("J")*2
    elif matched_cards.count(matched_cards[0]) == len(matched_cards):
        if len(matched_cards) == 5:
            return types["five_of_a_kind"]
        elif len(matched_cards) == 4:
            return types["four_of_a_kind"] + cards.count("J")*2
        elif len(matched_cards) == 3:
            return types["three_of_a_kind"] + cards.count("J")*2
        elif len(matched_cards) == 2:
            return types["one_pair"] + cards.count("J")*2
    else:
        if len(matched_cards) == 5:
            return types["full_house"]
        elif len(matched_cards) == 4:
            return types["two_pair"] + cards.count("J")*2

def insert_to_sorted_list(id, element, sorted_list):

    if len(sorted_list) == 0:
        sorted_list = [(id, element)]
    else:
        for index, value in enumerate(sorted_list):
            # Assuming y is in increasing order.
            if value[0] > id:
                sorted_list.insert(index, (id, element))
                break
        else:
            sorted_list.append((id, element))
    return sorted_list

def solve_puzzle(input):
    sum = 0
    with open(input, "r") as f:
        hands_by_type = [[]]*(2*len(types)+1)

        while True:
            line = f.readline().rstrip()
            if not line:
                break

            cards, bet = line.split(" ")
            bet = int(bet)
            value = calculate_value(cards)
            type = get_type(cards)

            print (f"Cards: {cards}, type: {type}, bet: {bet}, value: {value}")

            hands_by_type[type] = insert_to_sorted_list(value, bet, hands_by_type[type])

        rank = 1
        for hands in hands_by_type:
            for hand in hands:
                sum += hand[1] * rank
                rank += 1

    return sum

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='Filename containing puzzle input')
    args = parser.parse_args()

    result = solve_puzzle(args.input)
    print(result)
