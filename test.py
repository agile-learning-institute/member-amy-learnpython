import main

answer = main.hello()
if answer == "Hello World":
    print("Hello test success")
else:
    print("fail",answer)


answer = main.goodbye("Amy")
if answer == "goodbye Amy":
    print("goodbye test success")
else:
    print("fail")

answer = main.goodbye("Mi ke")
if answer == "goodbye Mike":
    print("goodbye Mike test succeeded")
else:
    print("fail")

answer = main.panda()
print(answer)
# if answer == "panda":
#     print("success")
# else:
#     print("fail")
    