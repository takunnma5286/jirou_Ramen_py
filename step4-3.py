q_and_a = {
    "麺の量は?: ": ["普通", "大盛り"],
    "野菜は?: ": ["普通", "マシマシ"],
    "ニンニク入れますか?: ": ["入れる", "入れない"]
}

answers = []

questions = list(q_and_a.keys())
for i in range(len(questions)):
    is_answer_valid = False
    while is_answer_valid == False:
        now_q = questions[i]
        allowed_ans = q_and_a[now_q]
        ans = input(questions[i])
        if ans in allowed_ans:
            answers.append(ans)
            break
        else:
            print(f"無効な回答です！これから選んでください！: {allowed_ans}")

print("\nあなたの注文は：")
for i in range(len(questions)):
    print(f"{questions[i]} → {answers[i]}")