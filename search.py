import os
from Parallel_HC import  PARALLEL_HILL_CLIMBER



phc = PARALLEL_HILL_CLIMBER()

phc.Evolve()
while True:
    input("Press Enter to see")
    phc.Show_Best()
