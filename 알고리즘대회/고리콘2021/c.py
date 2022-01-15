import math

strs = input()
number = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]

# 숫자로 대체
strs = strs.replace("ONE", "1")
strs = strs.replace("TWO", "2")
strs = strs.replace("THREE", "3")
strs = strs.replace("FOUR", "4")
strs = strs.replace("FIVE", "5")
strs = strs.replace("SIX", "6")
strs = strs.replace("SEVEN", "7")
strs = strs.replace("EIGHT", "8")
strs = strs.replace("NINE", "9")
strs = strs.replace("ZERO", "0")

temp_str = ""
res = 0
operators = "+, -, x, /, ="
ex_operator = "+"
# 계산
for now in strs:
  if now in operators:
    if ex_operator =="+":
      try:
        res += int(temp_str)
        ex_operator = now
      except:
        print("Madness!")
        exit()
    elif ex_operator =="-":
      try:
        res -= int(temp_str)
        ex_operator = now
      except:
        print("Madness!")
        exit()
    elif ex_operator =="x":
      try:
        res *= int(temp_str)
        ex_operator = now
      except:
        print("Madness!")
        exit()
    elif ex_operator =="/":
      try:
        res /= int(temp_str)
        if res <= 0:
          res = math.ceil(res)
        ex_operator = now
      except:
        print("Madness!")
        exit()
    temp_str = ""  
  else:
    temp_str += now

num_res = ''
res = str(res)
for now in res:
  try:
    if now in operators:
      num_res += now
    else:
      num_res += number[int(now)]
  except:
    print("Madness!")

print(strs)
print(num_res)