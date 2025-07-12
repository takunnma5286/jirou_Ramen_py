questions = [
    "麺の量は?: ",
    "野菜は?: ",
    "ニンニク入れますか?: "
]

# 答えを順に格納するリスト
answers = []

for q in questions:
    ans = input(q)
    answers.append(ans)

print("\nあなたの注文は：")
for i in range(len(questions)):
    print(f"{questions[i]} → {answers[i]}")