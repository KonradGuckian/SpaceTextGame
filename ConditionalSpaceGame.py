


planets = {
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
import Konrad_new_solution
comission = 0
def intro():
  global destination_planet, ship_speed, starting_planet, name
  print('Welcome Courier to Ad Astra\nCongratulations on your new career with Planet Express incorporated. Please state your name below to receive your assignment.')
  name = input('Name: \n')
  starting_planet = 'Earth'

  print(f"Welcome back {name}, today your assignment will be to determine the speed necessary to safely exit {starting_planet}'s gravitational field. Start by giving your destination.\n")
  destination_planet = input('Destination Planet: ')
  ship_speed = float(input(f'Please set exit speed in Kilometers per second {name}: '))

def exit_atmosphere():
  global destination_planet, ship_speed, starting_planet, comission, resultant
  if ship_speed < planets[starting_planet] * .9:
    print('Your speed was insufficient, you have plummeted back to the surface')
    comission -= 500
    print(f'Your pay has been docked, balance is now {comission}')
  elif ship_speed >= planets[starting_planet] * 1.1:
    print('You were going to fast, your ship burned up in the atmosphere with you inside')
    comission -= 500
    print(f'Your pay has been docked, balance is now {comission}')
  else:
    print(f"\nCongratulations Courier! You have successfully escaped {starting_planet}'s atmosphere and you are en route to {destination_planet}")
    comission += 500
    print(f'Your comission has been deposited, your balance is now {comission}')
    starting_planet = destination_planet
    destination_planet = input(f'Congratulations on your safe landing {name}, Your ship is being loaded with your next delivery. Please choose your next destination:\n')
    ship_speed = float(input('Now please set your ships speed Courier:\n'))
    exit_atmosphere()


intro()
exit_atmosphere()
