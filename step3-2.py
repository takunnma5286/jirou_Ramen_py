is_ans_Liaramen = False
is_ans_True = False

while is_ans_True == False:
    print("あなたは嘘つきですか?")
    ans = input("はい or いいえ: ")
    if ans == "はい":
        is_ans_Liaramen = True
        is_ans_True = True
    elif ans == "いいえ":
        is_ans_Liaramen = False
        is_ans_True = False
        print("嘘つきは嘘をつくので、あなたは嘘つきかもしれません！")

if is_ans_Liaramen:
    print("あなたは嘘つきです。")
else:
    print("あなたは嘘つきではありません。")