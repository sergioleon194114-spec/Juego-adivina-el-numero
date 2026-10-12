import pyfiglet

name = input("What is your name? ")
name = name.strip()

banner = pyfiglet.figlet_format(name, font="slant")


print(banner)
print(f"Hello, {name.upper()}! Welcome to VS Code.")
