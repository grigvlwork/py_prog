print("Какое сейчас у вас настроение?")
ans = input()
if ans.find("хорош") != -1 or ans.find("прекрасн") != -1:
    print("Отлично, у меня тоже всё хорошо :)")
elif ans.find("плохо") != -1:
    print("Ничего, скоро всё наладится.")
elif ans.find("не") != -1 or ans.find("?") != -1:
    print("Извините, не понимаю ответ.")
else:
    print("Извините, не понимаю ответ.")