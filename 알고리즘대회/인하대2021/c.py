input_num = int(input())
if input_num == 0:
  print(0)
  exit()

res = ''
# 암호해독
def base_3(num):
  global res
  if num == 0:
    return
  share, remaider = divmod(num, 3)
  if remaider == 2:
    remaider = -1
    share += 1
  elif remaider == -2:
    remaider = 1
    share -= 1
  res = str(remaider) + res
  return base_3(share)

base_3(input_num)
res = res.replace("-1", "T")

print(res)