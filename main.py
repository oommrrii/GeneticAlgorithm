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
      if DEBUG: print(f'\nThe following population of {self.creatures_amount} creatures was created:\n')
      for index in range(self.creatures_amount):
         state = self.creature_gen() 

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
         self.creatures[index].selected_flag = 0
      
      sortedCreatures = sorted(self.creatures, key=lambda x: x.fitness, reverse=True)  # Using lambda function
      for creature in range(NUM_SELECTED): sortedCreatures[creature].selected_flag = 1
      self.creatures = sortedCreatures
      
      if DEBUG:
         print('state | fitness| selected_flag')
         for creature in sortedCreatures:
            print(f'{creature.state} : {creature.fitness} : {creature.selected_flag}')
   
   # crossover function

   def crossover_fun(self,index): # use index and index+1
      pass

      creature1 = self.creatures[index]
      creature2 = self.creatures[index+1]
      if DEBUG: print(f'The state value were:\n{creature1.state}\n{creature2.state}')
      bitsAmount = CROSSOVER_BITS
      bitValues1 = creature1.state[-bitsAmount:]
      bitValues2 = creature2.state[-bitsAmount:]

      charList = list(creature1.state)
      charList[-bitsAmount:] = bitValues2
      creature1.state = ''.join(charList)
      charList = list(creature2.state)
      charList[-bitsAmount:] = bitValues1
      creature2.state = ''.join(charList)
      if DEBUG: print(f'The state value after crossover is:\n{creature1.state}\n{creature2.state}')

   # Evolve Generations

   def evolve(self):
      for generation in range(self.allowed_generations):
         self.selection_fun()
      
         for index in range(NUM_SELECTED,self.creatures_amount):
            if not index % 2:
               if index < self.creatures_amount-1:
                  self.crossover_fun(index)
            
            self.creatures[index].mutate()

         self.generation += 1 # progress generations count

   def get_result(self):
      binRep = self.creatures[0].state
      intRep = self.bin2int(binRep)
      print(f'### Result ###\n\nbin: {binRep}\nint: {intRep}\n')







class Creature:
   def __init__(self,input):
      self.state = input # a string of ones and zeros
      self.selected_flag = 0
      self.length = len(input)
      self.fitness = 0
      if DEBUG: print(f'A creature created with input value: {input}')

   # mutation function    
      
   def mutate(self):
      if DEBUG: print(f'The state value was: {self.state}\n')
      index = random.randint(1,self.length) # choose a bit position from a uniformly distributed range
      bitValue = self.state[index-1]
      if (bitValue == '1'):
         bitValue = '0'
      else:
         bitValue = '1'
      charList = list(self.state)
      charList[index-1] = bitValue
      self.state = ''.join(charList)
      if DEBUG: print(f'The mutation state value is: {self.state} with a change in index: {index}\n')



# Global Parameters
DEBUG = 0
CROSSOVER_BITS = 2
NUM_SELECTED = 2

def main():
   print('\nInitiating a Genetic Algoritm solver\n') 
   Evolution = Genetica(creatures_amount = 10, creature_size = 4, allowed_generations=4)
   print('\nGenerating a population')
   Evolution.population_gen()
   print('\nEvolving the generations')
   Evolution.evolve()
   Evolution.get_result()

   #cr1 = Creature(input='1111')
   #cr1.mutate()
   pass
     
   

if __name__ == '__main__':
    # execute
    main()
