import subprocess as sp
import requests

while True:
  print("Welcome to IsItDown.py!")
  print("Please write a URL or URLs you want to check. (separated by comma)")
  all_url = input("").replace(" ","").lower().split(",")
  count = 0
  for url in all_url:
    if not(url.startswith("https://")):
      all_url[count] = f"https://{url}"
    count +=1

  for url in all_url:
    try:
      on = requests.get(url)
    except:
      print(f"{url} is not valid URL.")
      continue
    if 200 == on.status_code:
      print(f"{url} is up!")
    else:
      print(f"{url} is down!")
  while True:
    answer = input("do you want to start over? (y,n)")
    if answer == 'n':
      print("k.bye")
      quit()
    elif answer == 'y':
      sp.call('cls', shell=True)
      break
    else:
      print("That's not a vaild answer")
  
  
