
ESCAPE_VELOCITIES = {
  "Earth": 11.186,
  "Mars": 5.03,
  "Venus": 10.36,
  "Mercury": 4.25,
  "Uranus": 21.38,
  "Neptune": 23.56,
  "Jupiter": 60.20,
  "Saturn": 36.09,
  "Pluto": 1.23,
  "The Moon": 2.38
}

DIGITS = '1234567890.'

def main():
  comission = 0
  name = str()
  destination = str()
  location = str()
  speed = float()
  score = int()
  in_game = bool()
  intro_played = bool()
  takeoff_sequence = bool()

  while True:
    if not in_game:
      menu_choice = input('Please choose an option below\n1. Start New Game\n2. Quit\n')
      while True:
        if len(menu_choice) == 1 and menu_choice in "12":
          break
        menu_choice = input('Please choose a valid option\n')
      if menu_choice == '1':
        location = 'Earth'
        in_game = True
      elif menu_choice == '2':
        quit()
    elif in_game:
      if not intro_played:
        print('Welcome Courier to Ad Astra\nCongratulations on your new career with Planet Express incorporated. Please state your name below to receive your assignment.')
        name = input('Name:\n').title()
        while True:
          for letter in name:
            if letter in DIGITS + " " or len(name) == 0:
              name = input('Please input a valid name:\n').title()
              break
          else:
            break
        destination = input(f"Welcome back {name}, today your assignment will be to determine the speed necessary to safely exit {location}'s gravitational field. Start by giving your destination:\n").title()
        intro_played = True
        takeoff_sequence = False
      if not takeoff_sequence:
        while True:
          if destination not in ESCAPE_VELOCITIES or destination == location:
            destination = input('Please give a valid planet.\n').title()
          else:
            break
        speed = input(f'Excellent choice {name}, I hear the weather on {destination} is lovely this time of year. Please state your desired exit velocity in Kilometers per second (km/s):\n')
        while True:
          for digit in speed:
            if digit not in DIGITS or len(speed) == 0:
              speed = input('Please input a valid speed.\n')
              break
          else:
            speed = float(speed)
            break
        takeoff_sequence = True
      if speed >= ESCAPE_VELOCITIES[location] * 1.1:
        score -= 500
        print(f'You were going too fast. Your ship burned up in the atmosphere, and your pay has been docked. Current comission ${score}.')
        end_game = input('Would you like to go again?\n1. Start New Game\n2. Quit to main menu.\n')
        while True:
          if len(end_game) == 1 and end_game in "12":
            break
          end_game = input('Please choose a valid option\n')
        if end_game == '1':
          intro_played = False
        elif end_game == '2':
          in_game = False
      elif speed <= ESCAPE_VELOCITIES[location] * 0.9:
        score -= 500
        print(f'You were going too slow. Your ship plummeted back to the surface, and your pay has been docked. Current comission ${score}.')
        end_game = input('Would you like to go again?\n1. Start New Game\n2. Quit to main menu.\n')
        while True:
          if len(end_game) == 1 and end_game in "12":
            break
          end_game = input('Please choose a valid option\n')
        if end_game == '1':
          score = 0
          intro_played = False
        elif end_game == '2':
          score = 0
          in_game = False
      else:
        score += 500
        print(f'Congratulations {name}, you have successfully Escaped {location} and arrived at {destination}. Current comission ${score}')
        location = destination
        destination = input(f"Please input your next destination:\n").title()
        takeoff_sequence = False

main()
