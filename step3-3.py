questions = [
    "麺の量は？ (普通/大盛り): ",
    "野菜は？ (普通/マシマシ): ",
    "ニンニク入れますか？ (入れる/入れない): "
]

allowed_answers = [
    ["普通", "大盛り"],
    ["普通", "マシマシ"],
    ["入れる", "入れない"]
]

answers = []

for i in range(len(questions)):
    is_answer_valid = False
    while is_answer_valid == False:
        ans = input(questions[i])
        if ans in allowed_answers[i]:
            answers.append(ans)
            break
        else:
            print(f"無効な回答です！これから選んでください！: {allowed_answers[i]}")

print("\nあなたの注文は：")
for i in range(len(questions)):
    print(f"{questions[i]} → {answers[i]}")