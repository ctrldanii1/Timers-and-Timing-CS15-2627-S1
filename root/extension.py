
import random
import time


attempts = []
total_attempts = 5


print("--- REACTION TIME GAME ---")
print("Press ENTER as fast as you can when you see 'GO!'\n")


for attempt in range(1, total_attempts + 1):
   input(f"Attempt {attempt}/{total_attempts}: Press ENTER when you are ready...")


   print("Get ready...")


   delay = random.uniform(2, 5)


   wait_start = time.monotonic()
   while time.monotonic() - wait_start < delay:
       pass


   go_time = time.monotonic()
   input("GO!")


   reaction_time = time.monotonic() - go_time
   attempts.append(reaction_time)


   print(f"Your reaction time: {reaction_time:.3f} seconds\n")


fastest_time = min(attempts)
print("--- GAME OVER ---")
print(f"Your fastest reaction time was: {fastest_time:.3f} seconds!")
