import random

class Genetica:
   def __init__(self,creatures_amount,creature_size,allowed_generations):
        self.generation = 0
        self.creatures = []
        self.creatures_amount = creatures_amount
        self.creature_size = creature_size
        self.allowed_generations = allowed_generations

   # genetic representation of a solution
       
   def bin2int(self, binRep):
      intRep = int(binRep,base=2)
      return intRep
   
   def int2bin(self,intRep):
       binRep = bin(intRep)[2:]
       return binRep
   
   # a function to generate new solutions
   
   def population_gen(self):
      for index in range(self.creatures_amount):
         state = self.creature_gen() 
         print(state)
      print(f'A population of {len(self.creatures)} creatures was created\n')

   def creature_gen(self):
      binary_number = ''.join(random.choice('01') for _ in range(self.creature_size))
      cr = Creature(input = binary_number)
      self.creatures.append(cr)
      return binary_number
      

   # fitness function

   def fitness_fun(self,intRep):
       fitness = 1/abs(intRep-10.5) # higher score to the closest value to 10
       return fitness

   # selection function

   def selection_fun(self):
      for index in range(self.creatures_amount):
         binRep = self.creatures[index].state
         intRep = self.bin2int(binRep)
         fitness = self.fitness_fun(intRep)
         self.creatures[index].fitness = fitness
      
      sortedCreatures = sorted(self.creatures, key=lambda x: x.fitness, reverse=True)  # Using lambda function
      self.creatures = sortedCreatures

      for creature in sortedCreatures:
         print(f'{creature.state}: {creature.fitness}')
   
   # crossover function

   def crossover_fun(self):
      pass

   # Evolve Generations

   def evolve(self):
      for generation in range(self.allowed_generations):
         self.selection_fun()
         self.crossover_fun()
         for index in range(2,self.creatures_amount):
            self.creatures[index].mutate()

         self.generation += 1 # progress generations count

   def get_result(self):
      binRep = self.creatures[0].state
      intRep = self.bin2int(binRep)
      print(f'### Result ###\nbin: {binRep}\nint: {intRep}')







class Creature:
   def __init__(self,input):
      self.state = input # a string of ones and zeros
      self.selected_flag = 0
      self.length = len(input)
      self.fitness = 0
      # print(f'The input value is: {input}\n')

   # mutation function    
      
   def mutate(self):
      print(f'The state value was: {self.state}\n')
      index = random.randint(1,self.length) # choose a bit position from a uniformly distributed range
      bitValue = self.state[index-1]
      if (bitValue == '1'):
         bitValue = '0'
      else:
         bitValue = '1'
      charList = list(self.state)
      charList[index-1] = bitValue
      self.state = ''.join(charList)
      print(f'The mutation state value is: {self.state} with a change in index: {index}\n')





def main():
   print('hello world\n\n') 
   EvolutionObj = Genetica(creatures_amount = 10, creature_size = 4, allowed_generations=4)
   EvolutionObj.population_gen()
   EvolutionObj.evolve()
   EvolutionObj.get_result()

   #cr1 = Creature(input='1111')
   #cr1.mutate()
   pass
     
   

if __name__ == '__main__':
    # execute
    main()
