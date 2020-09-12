print("Welcome to my first game!")
name = input("What is your name? ")
age = int(input("What is your age? "))
health = 10



if age >= 12:
  print("You are old enough to play!")



  wants_to_play = input("Do you want to play? ").lower()
  if wants_to_play == "yes":
    print("You are starting with", health, "health")
    print("Lets's play! ")

    left_or_right = input("First choice.. Left Right (left/right)? ")
    if left_or_right == "left":
      ans = input("Nice, you follow the path and reach a lake... Do you swim across or go around (across/around? ")

      if ans == "around":
        print("You went around and reached the other side of the lake")
        
      elif ans == "across":
        print("You managed to get across and got bit by a fish and lost 5 health")
        health -= 5

      ans = input("You notice a house and a river. Which do you go to? (river/house? ")
      if ans == "house":
        print("You go to the house and you are greeted by the owner... He doesn't like you and you lose 5 health")
        health -= 5
      else:
        print("You fell in the river and lost")

      if health <= 0:
        print("You now have 0 health and you lose the game....")
      else:
        print("You have survived... and won!")
          

    else:
        print("You lost.")


  else:
    print("Goodbye")
  
else:
  print("You are not old enough")
