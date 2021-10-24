from random import randint
import urllib
import os
import requests

def clipboard(url):
    command = 'echo ' + url.strip() + '| clip'
    os.system(command)

def find_game():
    random_code = randint(10**(10-1), (10**10)-1)
    url = ("https://www.roblox.com/games/" + str(random_code))

    try:
        return urllib.request.urlopen(url).geturl()
    except:
        return True

def main():
    while True:
        game = find_game()
        if game != True and 'Place' not in game:
            os.system('cls')
            print('[Found Valid URL] -- Added To Your Clipboard\n\n' + game + '\n')
            clipboard(game)
            
            restart = input("Roll Again? Y/N: ")
            if restart.lower() in ["n", "no"]:
                break

if __name__ == "__main__":
    main()
