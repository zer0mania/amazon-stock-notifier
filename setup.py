from os import system
import platform

os = platform.system()

if os == "Windows":
  system('pip install discord-webhook')
  system('pip install selenium')
  system('pip install requests')
  print('\nFinished Installing dependencies.')
else:
  system('apt update')
  system('apt install chromium-chromedriver -y')
  system('pip install discord-webhook')
  system('pip install selenium')
  system('pip install requests')
  print('\nFinished Installing dependencies.')
