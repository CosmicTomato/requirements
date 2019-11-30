def main():
process_array = []
extinct_runs = 0
For i in range (0,100): #100 runs
  new_process = birth_death_process()
  process_array.append( new_process  )
  if new_process[1][-1] == 0:
    extinct_runs += 1
print( extinct_runs, "out of 100 runs went extinct" )

#TO ADD:
#PLOT FIRST FIVE RUNS IN ARRAY

def birth_death_process():
  birth_rate = 1
  death_rate = 0.5
  start_pop = 1
  end_time = 14
  process = [ [0], [start_pop] ] #stores times and populations
  while ( process[0][-1] < end_time ):
    next_birth = -math.log( 1.0 - random.random() ) / birth_rate
    next_death = -math.log( 1.0 - random.random() ) / death_rate
    #note: random.random() returns a random number in range [0,1)
    time_add = min( next_birth, next_death )
    if ( process[0][-1] + time_add ) > end_time:
      process[0].append( end_time )
      process[1].append( process[1][-1] )
    elif next_birth < next_death:
      process[0].append( process[0][-1] + time_add )
      process[1].append( process[1][-1] +1 )
    else:
      process[0].append( process[0][-1] + time_add )
      process[1].append( process[1][-1] - 1 )
      if process[1][-1] == 0:
        process[0].append( end_time )
        process[1].append( process[1][-1] )
return process
