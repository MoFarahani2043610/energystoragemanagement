
# Import necessary libraries
import gymnasium as gym
import numpy as np
from gymnasium import spaces

class EnergyStorageEnv(gym.Env):
    def __init__(self, max_storage_capacity=100, max_price=100, min_price=0):
        super(EnergyStorageEnv, self).__init__()

        # Define environment parameters
        self.max_storage_capacity = max_storage_capacity
        self.max_price = max_price
        self.min_price = min_price

        # Define action space (0 = Hold, 1 = Buy, 2 = Sell)
        self.action_space = spaces.Discrete(3)

        # Define state space (energy in storage, energy price)
        self.observation_space = spaces.Box(
            low=np.array([0, min_price], dtype=np.float32),
            high=np.array([max_storage_capacity, max_price],dtype=np.float32),
            dtype=np.float32
        )

        # Initialize state variables
        self.reset()

    def reset(self, seed=None):
        """
        Resets the environment to an initial state, randomizing initial conditions.
        """
        super().reset(seed=seed)  #required for Gymnasium
        self.energy_storage = self.np_random.uniform(0, self.max_storage_capacity)  # Random initial storage
        self.energy_price = self.np_random.uniform(self.min_price, self.max_price)  # Random initial price
        self.total_reward = 0  # Reset total reward

        return np.array([self.energy_storage, self.energy_price], dtype=np.float32), {}

    def step(self, action):
        """
        Take the action and updates the envirnment accordingly.
        """
        reward = 0
        
        if action == 1 : #buy energy
            if self.energy_storage < self.max_storage_capacity:
                self.energy_storage += 1
                reward = -self.energy_price  #paying for energy
            else:
                reward = 0 # No storage left , no action taken
                
        elif action == 2: #sell energy
            if self.energy_storage > 0 :
                self.energy_storage -= 1
                reward = self.energy_price  # earning money
            else : 
                reward = 0 # no energy to sell 
                
        elif action == 0:  # hold
             reward = 0    # no change 
             
        # Update state
        self.energy_price = self.np_random.uniform(self.min_price, self.max_price)  # Generate new price
        self.total_reward += reward

        # Define termination condition
        done = self.energy_storage >= self.max_storage_capacity or self.energy_storage <= 0

        return np.array([self.energy_storage, self.energy_price], dtype=np.float32), reward, done
          
    def display_state(self, action, done, reward):      
        # Displays the current Envirnment State,Action and Reward.
         
        print(f"state: [Energy Storage = {self.energy_storage:.2f} kWh, Energy Price ={self.energy_price:.2f}]")
        print(f"Action:{self._get_action_name(action)}")
        print(f"Reward:{reward :.2f}")
        print(f"Total Reward : {self.total_reward:.2f}")
        print(f"Done:{done}")
        print("-" * 40) #seprator for clarity
        
    def _get_action_name(self, action):
         """
        Helper function to convert action index to a readable name.
         """
         if action == 0:
             return "Hold"
         elif action == 1:
             return "Buy"
         elif action == 2:
             return "Sell"
         else :
             return "Unknown"
         
#example usage
env = EnergyStorageEnv()
state,_ = env.reset()
        
randomAction = env.action_space.sample()

step = env.step(randomAction)

energyStep = step[0]
reward = step[1]
done = step[2]

print("energyStep - Energy Storage:", energyStep[0], "kWh, Energy Price:", energyStep[1])
print("reward", reward)
print("done", done)
print ("Action",env._get_action_name(randomAction))

    
            

            
    