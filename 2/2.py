


def calculateWin(result):
    hand_two_dict = {
        "X": "rock",
        "Y": "paper",
        "Z": "scissors",
    }
    hand_one_dict = {
        "A": "rock",
        "B": "paper",
        "C": "scissors",
    }
    hand_one = hand_one_dict[result[0]]
    hand_two = hand_two_dict[result[2]]

    answer = calculateWinner(hand_one, hand_two)
    return get_score(answer, hand_two)


def get_score(result, hand_two):
    score_dict = {
        "rock": 1,
        "paper": 2,
        "scissors": 3,

    }
    if result == "draw":
        return score_dict[hand_two] + 3
    if result == "lose":
        return score_dict[hand_two] + 0
    if result == "win":
        return score_dict[hand_two] + 6


def calculateWinner(hand_one, hand_two):
    dict_list = {
        hand_one: "player 1",
        hand_two: "player 2",
    }
    if hand_one == hand_two:
        return "draw"
    if "rock" in [hand_one, hand_two]:
        if "paper" in [hand_one, hand_two]:
            return dict_list["paper"]
        else:
            return dict_list["rock"]
    return dict_list["scissors"]


def calculateHand(line_game):
    hand_two_dict = {
        "X": "lose",
        "Y": "draw",
        "Z": "win",
    }
    hand_one_dict = {
        "A": "rock",
        "B": "paper",
        "C": "scissors",
    }
    hand_one = hand_one_dict[line_game[0]]
    result = hand_two_dict[line_game[2]]
    hand_two = calculateSingleHand(hand_one,result)
    print(hand_two)
    return get_score(result, hand_two)

def calculateSingleHand(hand_one, result):
    cal_win_dict = {
        "rock":"paper",
        "paper":"scissors",
        "scissors": "rock",
    }
    cal_lose_dict = {cal_win_dict[k] : k for k in cal_win_dict}
    if result == "draw":
        return hand_one
    if result == "lose":
        return cal_lose_dict[hand_one]
    if result == "win":
        return cal_win_dict[hand_one]




f = open("2/input.txt", "r")
input_text = f.read()
total_points = 0
for lin in input_text.splitlines():
    print(lin)
    total_points += calculateHand(lin)


print(total_points)