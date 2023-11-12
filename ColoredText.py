#Print Colored Text with Python
#black, red, green, yellow, blue, magenta, cyan, and white.
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
           #BLUE
print(Fore.RED+Back.YELLOW+"Hi My name is Sneha Kumbhare "+ Fore.YELLOW+ Back.BLUE+"I am Python Developer")
print(Back.CYAN+"Hi My name is Sneha Kumbhare")
print(Fore.RED + Back.GREEN+ "Hi My name is Sneha Kumbhare")
