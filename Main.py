# ████████████████████████████████████████████████
# ██ Import modules                             ██
# ████████████████████████████████████████████████

import json
import os
import random
import sys
from pathlib import Path
from time import sleep
from winsound import Beep

# ████████████████████████████████████████████████
# ██ Set up system                              ██
# ████████████████████████████████████████████████

#
# Enables console colors
#
os.system('color')

#
# Path to itself
#
CURRENT_DIR = Path(__file__).parent

# ████████████████████████████████████████████████
# ██ Settings                                   ██
# ████████████████████████████████████████████████

#
# Constants
#
ABC = 'abcdefghijklmnopqrstuvwxyz'

#
# ANSI Themes
#
ansi_black = '\033[1;30m'
ansi_white = '\033[0;37m'
ansi_white_l = '\033[0;1;37m'
ansi_red = '\033[0;31m'
ansi_red_l = '\033[1;31m'
ansi_yellow = '\033[0;33m'
ansi_yellow_l = '\033[1;33m'
ansi_green = '\033[0;32m'
ansi_green_l = '\033[1;32m'
ansi_cyan = '\033[0;36m'
ansi_cyan_l = '\033[1;36m'
ansi_blue = '\033[0;34m'
ansi_blue_l = '\033[1;34m'
ansi_purple = '\033[0;35m'
ansi_purple_l = '\033[1;35m'

#
# File settings
#
WORDLIST_FILE = Path.cwd() / CURRENT_DIR / "Wordlist.txt"
GAMEDATA_FILE = Path.cwd() / CURRENT_DIR / "GameData.json"

#
# Game settings
#
START_HP = 10
LETTER_VALUES = {
  'a': 10,
  'b': 30,
  'c': 30,
  'd': 20,
  'e': 10,
  'f': 40,
  'g': 20,
  'h': 40,
  'i': 10,
  'j': 80,
  'k': 50,
  'l': 10,
  'm': 30,
  'n': 10,
  'o': 10,
  'p': 30,
  'q': 10,
  'r': 10,
  's': 10,
  't': 10,
  'u': 10,
  'v': 40,
  'w': 40,
  'x': 80,
  'y': 40,
  'z': 10
}

LEVEL_VALUES = [
  {
    'title': 'Beginner',
    'xp': 0,
    'color': ansi_white
  },
  {
    'title': 'Quartz miner',
    'xp': 1_000,
    'color': ansi_white_l
  },
  {
    'title': 'Pyrite miner',
    'xp': 2_000,
    'color': ansi_green
  },
  {
    'title': 'Amethyst miner',
    'xp': 4_000,
    'color': ansi_green_l
  },
  {
    'title': 'Fluorite miner',
    'xp': 7_000,
    'color': ansi_cyan
  },
  {
    'title': 'Apatite miner',
    'xp': 11_000,
    'color': ansi_cyan_l
  },
  {
    'title': 'Malachite miner',
    'xp': 16_000,
    'color': ansi_blue
  },
  {
    'title': 'Baryte miner',
    'xp': 22_000,
    'color': ansi_blue_l
  },
  {
    'title': 'Emerald miner',
    'xp': 29_000,
    'color': ansi_purple
  },
  {
    'title': 'Ruby miner',
    'xp': 37_000,
    'color': ansi_purple_l
  },
  {
    'title': 'Diamond miner',
    'xp': 45_000,
    'color': ansi_red
  },
  {
    'title': 'Alexandrite miner',
    'xp': 54_000,
    'color': ansi_red_l
  },
  {
    'title': 'Painite miner',
    'xp': 64_000,
    'color': ansi_yellow
  },
  {
    'title': 'Taaffeite miner',
    'xp': 75_000,
    'color': ansi_yellow_l
  },
]

# ████████████████████████████████████████████████
# ██ Functions                                  ██
# ████████████████████████████████████████████████

def clearConsole():
  '''
  Clears the console
  '''
  os.system('cls' if os.name == 'nt' else 'clear')



def printLine():
  '''
  Prints a line to the console
  '''
  print(f'{ansi_white}{48*'-'}{ansi_white}')



def typeWrite(text: str):
  '''
  @param {str} - text
    Text to display.

  Prints a line of text like a typewriter.
  '''
  for char in text:
    if char.lower() in ABC:
      Beep(240, 100)
    sys.stdout.write(char)
    sys.stdout.flush()
  sys.stdout.write('\n')

# ████████████████████████████████████████████████
# ██ Classes                                    ██
# ████████████████████████████████████████████████

class Hangman():
  def openWordList(self):
    """
    @return {list}
      Word list

    Opens the word list file
    """
    wordList = []
    with open(WORDLIST_FILE, 'r') as words:
      for line in words:
        wordList.append(line.strip())
      return wordList
    


  def setUserData(self, userData: dict):
    """
    @param {dict} - userData
      User data dict
    """
    with open(GAMEDATA_FILE, "w") as outfile:
      json.dump(userData, outfile)
    


  def getUserData(self):
    """
    @return {dict}
      User data dict

    Loads the user data
    """
    with open(GAMEDATA_FILE, 'r') as openfile:
      return json.load(openfile)
    


  def createNewUser(self, userName: str):
    """
    @param {str} userName
      The name of the user
      
    Creates a new player data dict
    """
    playerData = {
      'userName': userName,
      'color': ansi_white,
      'xp': 0,
      'level': 0,
      'title': 'Beginner',
      'highscore': 0,
      'hardestWord': '',
      'levelsPlayed': 0,
      'levelsBeaten': 0
    }

    return playerData



  def getRandomWord(self, wordList: list):
    """
    @param {list} wordList
      List of words to get random word from.
    @return {str}
      Random word from word list

    Returns a random word from the word list.
    """
    return random.choice(wordList).lower()
  


  def beep(self, beepType: str = 'error'):
    """
    @param {str} beepType
      Type of beep to produce.
    
    Plays a sequence of beeps
    """
    match beepType:
      case 'intro':
        Beep(320,250)
        Beep(480,250)
        Beep(640,250)
        Beep(480,250)
        Beep(320,250)
        Beep(480,250)
        Beep(640,250)
        Beep(480,250)
        Beep(320,250)
        Beep(480,250)
        Beep(640,500)
      case 'happy':
        Beep(320,250)
        Beep(480,250)
        Beep(640,500)
      case 'sad':
        Beep(320,250)
        Beep(240,250)
        Beep(160,500)
      case 'win':
        Beep(320,250)
        Beep(480,250)
        Beep(640,250)
        Beep(720,250)
      case 'lose':
        Beep(480,250)
        Beep(320,250)
        Beep(240,250)
        Beep(160,250)
      case 'error':
        Beep(320,250)
        Beep(320,250)



  def showIntro(self):
    """
    Plays the game intro.
    """
    clearConsole()
    printLine()
    print(f'{ansi_cyan}Hangman {ansi_green}Geology Edition {ansi_yellow}2024{ansi_white}')
    print('RubenTheCoder')
    printLine()
    self.beep('intro')



  def showTutorial(self):
    """
    Shows the tutorial.
    """
    clearConsole()
    printLine()
    typeWrite(f'In this game, you try to figure out a word by {ansi_yellow}guessing the letters{ansi_white} inside it.')
    sleep(1)
    typeWrite(f'If you guess the {ansi_green}correct letter{ansi_white}, you will be one step {ansi_green}closer to solving the word.{ansi_white}')
    sleep(1)
    typeWrite(f'But if you guess the {ansi_red}wrong letter{ansi_white}, you will {ansi_red}lose a health point.{ansi_white}')
    sleep(1)
    typeWrite(f'{ansi_yellow}Guess all the letters of the word to win{ansi_white} before you are out of health points.')
    sleep(1)
    typeWrite(f'The {ansi_yellow}longer and harder{ansi_white} a word is, the {ansi_blue_l}more points{ansi_white} you get.')
    printLine()
    typeWrite(f'{ansi_cyan}Close tutorial?{ansi_white}')
    input(f"> Press {ansi_blue_l}'Enter'{ansi_white} to close: ")



  def changeName(self):
    """
    Shows a dialog to change the username
    """
    clearConsole()
    printLine()
    typeWrite(f"{ansi_cyan}Enter a new username, or press {ansi_blue_l}'Enter'{ansi_cyan} to keep old one.{ansi_white}")
    typeWrite(f"Current name: '{ansi_yellow_l}{self.userData['userName']}{ansi_white}'")
    newName = input('Enter new name: ')
    if newName == '':
      clearConsole()
      printLine()
      typeWrite('Old username will be kept.')
      sleep(1)
      return
    self.userData['userName'] = newName
    self.setUserData(self.userData)
    clearConsole()
    printLine()
    typeWrite(f"You have set your username to '{ansi_yellow_l}{newName}{ansi_white}'.")
    sleep(1)


  
  def showProfile(self):
    """
    Shows the user profile data
    """
    clearConsole()
    printLine()
    print(f'{self.userData['color']}{self.userData['userName']} - {self.userData['title']}{ansi_white}')
    print(f'------------------------------------------------')
    print(f'Level         | {self.userData['level']}')
    print(f'XP            | {self.userData['xp']}')
    print(f'Levels played | {self.userData['levelsPlayed']}')
    print(f'Levels beaten | {self.userData['levelsBeaten']}')
    print(f'------------------------------------------------')
    typeWrite(f'{ansi_cyan}Close profile view?{ansi_white}')
    input(f"> Press {ansi_blue_l}'Enter'{ansi_white} to close: ")



  def startHangmanRound(self):
    """
    Starts a round of Hangman
    """
    #
    # Set round data
    #
    randomWord = self.getRandomWord(self.wordList)
    lettersGuessed = []
    hasGuessedRight = False
    msg = ''
    xpMsg = ''
    hp = START_HP
    while hp > 0 and not hasGuessedRight:
      #
      # Values for the current turn
      #
      hp_color = ansi_green_l
      if hp <= 6:
        hp_color = ansi_yellow_l
      if hp <= 3:
        hp_color = ansi_red_l

      #
      # Print the current status of the player
      #
      clearConsole()
      print(f'{ansi_yellow}{msg}{ansi_white}')
      print(xpMsg)
      printLine()
      print(f'{ansi_yellow}// HP {hp_color}({hp}/{START_HP}){ansi_white}')
      print(f"{hp_color}{hp * '██ '}{ansi_black}{(START_HP - hp) * '██ '}")
      printLine()
      
      #
      # Display the word in hidden form
      #
      displayWord = ''
      for letter in randomWord:
        if letter in lettersGuessed:
          displayWord += f'{ansi_green_l}{letter}{ansi_white}'
        elif letter == ' ':
          displayWord += f'-'
        else:
          displayWord += f'{ansi_black}□{ansi_white}'
        displayWord += ' '
      print(f'{ansi_yellow}// Word')
      print(displayWord)
      printLine()

      #
      # Ask for a letter
      #
      print(f'{ansi_cyan}Which letter do you guess next?{ansi_white}')
      letterGuess = input('Enter a letter: ')
      if not letterGuess:
        msg = 'Please enter a letter'
        xpMsg = ''
        self.beep('error')
        continue
      letterGuess = letterGuess[0].lower()
      if not letterGuess in ABC:
        msg = 'Please enter a valid letter'
        xpMsg = ''
        self.beep('error')
        continue

      #
      # Get the result of the letter
      #
      if letterGuess in lettersGuessed:
        msg = f"You already tried the letter '{letterGuess}'"
        xpMsg = ''
        self.beep('error')
        continue
      elif letterGuess in randomWord: 
        xpGain = LETTER_VALUES[letterGuess]
        self.userData['xp'] += xpGain
        msg = f"The letter '{letterGuess}' is inside the word"
        xpMsg = f'You have gained {ansi_purple}{xpGain} XP{ansi_white}'
        lettersGuessed += letterGuess
        self.beep('happy')
      else:
        msg = f"The letter '{letterGuess}' is not inside the word"
        xpMsg = ''
        hp -= 1
        lettersGuessed += letterGuess
        self.beep('sad')

      #
      # Check if the word has been guessed
      #
      wordComplete = True
      for letter in randomWord:
        if not letter in lettersGuessed and letter != ' ':
          wordComplete = False
      hasGuessedRight = wordComplete

    #
    # Show game result
    #
    clearConsole()
    printLine()
    if hasGuessedRight:
      self.beep('win')
      self.userData['levelsBeaten'] += 1
      typeWrite(f'You have {ansi_green}won{ansi_white}, {self.userData['color']}{self.userData['userName']}{ansi_white}!')
      xpGain = 0
      for letter in randomWord:
        xpGain += LETTER_VALUES[letter] * 10
    else:
      self.beep('lose')
      typeWrite(f'You have {ansi_red}lost{ansi_white}, {self.userData['color']}{self.userData['userName']}{ansi_white}!')
      xpGain = 0
      for letter in randomWord:
        xpGain += LETTER_VALUES[letter]
    self.userData['xp'] += xpGain
    sleep(1)
    typeWrite(f"The correct word was '{ansi_yellow}{randomWord}{ansi_white}'")
    sleep(1)
    typeWrite(f'You have gained {ansi_purple}{xpGain} XP{ansi_white}')
    sleep(1)

    #
    # Show new highscore
    #
    if xpGain > self.userData['highscore']:
      clearConsole()
      printLine()
      self.userData['highscore'] = xpGain
      self.userData['hardestWord'] = randomWord
      typeWrite(f'You have set a new highscore of {ansi_purple}{xpGain} XP{ansi_white}')
      sleep(1)

    #
    # Level up player if the case
    #
    if self.userData['level'] + 1 < len(LEVEL_VALUES) :
      clearConsole()
      printLine()
      if self.userData['xp'] >= LEVEL_VALUES[self.userData['level'] + 1]['xp']:
        self.userData['level'] += 1
        self.userData['color'] = LEVEL_VALUES[self.userData['level']]['color']
        self.userData['title'] = LEVEL_VALUES[self.userData['level']]['title']
        typeWrite(f'{ansi_yellow}You leveled up{ansi_white}')
        sleep(1)
        typeWrite(f'You are now a {LEVEL_VALUES[self.userData['level']]['color']}{LEVEL_VALUES[self.userData['level']]['title']}{ansi_white}')
      else:
        typeWrite(f'You now have {ansi_purple}{self.userData['xp']} XP{ansi_white}')
        typeWrite(f'{ansi_purple}{LEVEL_VALUES[self.userData['level'] + 1]['xp'] - self.userData['xp']} XP{ansi_white} needed to reach the next level')
      sleep(1)

    #
    # Apply data changes
    #
    self.userData['levelsPlayed'] += 1
    self.setUserData(self.userData)

    #
    # Show gemstone on MinDat.org
    #
    clearConsole()
    printLine()
    typeWrite(f"{ansi_cyan}Show photos of '{randomWord.capitalize()}' on {ansi_blue_l}www.Mindat.org{ansi_cyan}?{ansi_white}")
    if input(f'> Enter ({ansi_green}y{ansi_white}/{ansi_red}n{ansi_white}): ') == 'y':
      os.system(f'start \"\" https://www.mindat.org/photoscroll.php?searchbox={randomWord}')


    
  def startGame(self):
    """
    Starts the game cycle.
    """
    #
    # Show intro
    #
    self.showIntro()
    clearConsole()
    printLine()
    if not self.userData:

      #
      # Register new user
      #
      typeWrite(f'Welcome to {ansi_cyan}Hangman!{ansi_white}')
      sleep(1)
      typeWrite(f'{ansi_cyan}Please enter a username{ansi_white}')
      self.userData = self.createNewUser(input(f'> Enter name: '))
      self.setUserData(self.userData)
      clearConsole()
      printLine()
      typeWrite(f'{ansi_cyan}Show tutorial?{ansi_white}')
      if input(f'> Enter ({ansi_green}y{ansi_white}/{ansi_red}n{ansi_white}): ') == 'y':
        self.showTutorial()
      clearConsole()
      printLine()
      typeWrite(f'Welcome to the game, {self.userData['color']}{self.userData['userName']}{ansi_white}!')
      sleep(1)
    else:

      #
      # Greet existing user
      #
      typeWrite(f'Welcome back, {self.userData['color']}{self.userData['userName']}{ansi_white}!')
      sleep(1)

    #
    # Ask for next action
    #
    userAction = ''
    while userAction != 'exit':
      clearConsole()
      printLine()
      typeWrite(f'{ansi_cyan}What do you want to do next? (Enter one of the following commands){ansi_white}')
      print(f'{ansi_yellow}[play]{ansi_white}         : Play the game') 
      print(f'{ansi_yellow}[change name]{ansi_white}  : Change your username')
      print(f'{ansi_yellow}[show profile]{ansi_white} : Show your stats')
      print(f'{ansi_yellow}[exit]{ansi_white}         : Close the game')
      command = input('Enter command: ')
      match command:
        case 'play':
          userAction = 'play'
          self.startHangmanRound()
        case 'change name':
          userAction = 'change name'
          self.changeName()
        case 'show profile':
          userAction = 'show profile'
          self.showProfile()
        case 'exit':
          userAction = 'exit'
        case _:
          userAction = ''
    
    #
    # Thank player for playing
    #
    clearConsole()
    printLine()
    typeWrite(f"Thanks for playing Hangman {self.userData['color']}{self.userData['userName']}{ansi_white}!")
    sleep(1)
    print('Game has been ended')
    sleep(1)



  def __init__(self):
    """
    Initializes the game.
    """
    self.userData = self.getUserData()
    self.wordList = self.openWordList()
    self.startGame()
  
# ████████████████████████████████████████████████
# ██ Main Program                               ██
# ████████████████████████████████████████████████

Hangman = Hangman()
