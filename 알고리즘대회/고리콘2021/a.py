str = list(input())
check_str = list("driip")

# 뒤에 5글자 확인
for no in range(5):
  if str.pop() != check_str.pop():
    print("not cute")
    exit()

print("cute")