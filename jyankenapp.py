import random

print("じゃんけんしよう\nじゃーんけーん...\nぐー：１、ちょき：２、ぱー：３")

number = int(input())
hand_pattern = ["ぐー", "ちょき", "ぱー"]

your_select = hand_pattern[number - 1]
print(f"あなた：{your_select}")

index = random.randint(0, 2)
opp_select = hand_pattern[index]
print(f"あいて：{opp_select}")

if your_select == opp_select:
    print("あいこだー")

elif your_select == hand_pattern[0] and opp_select == hand_pattern[1]:
    print("あなたのかち")

elif your_select == hand_pattern[1] and opp_select == hand_pattern[2]:
    print("あなたのかち")

elif your_select == hand_pattern[2] and opp_select == hand_pattern[0]:
    print("あなたのかち")
