for i in range(10):
  num = eval (input ('Enter a Value Range (60-100):'))
  if 60 <= num <= 74:
    print("Derp!")
  elif 75 <= num <= 84:
    print("Good!")
  elif 85 <= num <= 94:
    print("Very Good!")
  elif 95 <= num <= 100:
    print("Level Asian!")
  else:
    print("Invalid Value")