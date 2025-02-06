
# Import necessary libraries
import gym
import numpy as np
import matplotlib.pyplot as plt
from gym import spaces

#%matplotlib inline

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
            low=np.array([0, min_price]),
            high=np.array([max_storage_capacity, max_price]),
            dtype=np.float32
        )

        # Initialize state variables
        self.reset()

    def reset(self):
        """
        Resets the environment to an initial state, randomizing initial conditions.
        """
        self.energy_storage = np.random.uniform(0, self.max_storage_capacity)  # Random initial storage
        self.energy_price = np.random.uniform(self.min_price, self.max_price)  # Random initial price
        self.total_reward = 0  # Reset total reward

        return np.array([self.energy_storage, self.energy_price], dtype=np.float32)

    def step(self, action):
        """
        Takes an action and updates the environment accordingly.
        """
        reward = 0

        if action == 1:  # Buy energy
            if self.energy_storage < self.max_storage_capacity:
                self.energy_storage += 1
                reward = -self.energy_price  # Paying for energy
            else:
                reward = -self.energy_price  # No storage left, still loses money

        elif action == 2:  # Sell energy
            if self.energy_storage > 0:
                self.energy_storage -= 1
                reward = self.energy_price  # Earning money
            else:
                reward = 0  # No energy to sell

        elif action == 0:  # Hold
            reward = 0  # No change

        # Update state
        self.energy_price = np.random.uniform(self.min_price, self.max_price)  # Generate new price
        self.total_reward += reward

        # Define termination condition
        done = self.total_reward < -100

        return np.array([self.energy_storage, self.energy_price], dtype=np.float32), reward, done, {}

    def render(self):
        """
        Displays the current environment state with a plot.
        """
        print(f"Energy Storage: {self.energy_storage:.2f} kWh")
        print(f"Energy Price: {self.energy_price:.2f}")
        print(f"Total Reward: {self.total_reward:.2f}")

        # Create a bar plot of the environment state
        plt.figure(figsize=(6, 4))
        labels = ['Energy Storage', 'Energy Price', 'Total Reward']
        values = [self.energy_storage, self.energy_price, self.total_reward]
        plt.bar(labels, values, color=['blue', 'green', 'red'])
        plt.ylim(min(values), max(values))  
        plt.ylabel("Values")
        plt.title("Energy Management Environment State")
        plt.show()

# Example usage
env = EnergyStorageEnv()
state = env.reset()
action = env.action_space.sample()  # Random action
next_state, reward, done, info = env.step(action)
env.render()  # Display the plot