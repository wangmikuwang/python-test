def count_positive_and_negative_numbers():
  positive_count = 0
  negative_count = 0
  while True:
    num = input("请输入一个整数：")
    if num == "0":
      break
    if int(num) > 0:
      positive_count += 1
    elif int(num) < 0:
      negative_count += 1
  return positive_count, negative_count
if __name__ == "__main__":
  positive_count, negative_count = count_positive_and_negative_numbers()
  print("正数的个数：", positive_count)
  print("负数的个数：", negative_count)
