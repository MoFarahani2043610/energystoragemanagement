import gymnasium as gym
import numpy as np
from gymnasium import spaces
from upload import time_series_data


class EnergyStorageEnv(gym.Env):
    def __init__(self, max_storage_capacity=100, time_series_data=None):
        super(EnergyStorageEnv, self).__init__()

        # Define environment parameters
        self.max_storage_capacity = max_storage_capacity
        self.time_series_data = time_series_data  # Real data (max_price and min_price)
        
        # Normalize max_price values (NEW)
        self.time_series_data[:, 0] = (self.time_series_data[:, 0] - np.min(self.time_series_data[:, 0])) / (
            np.max(self.time_series_data[:, 0]) - np.min(self.time_series_data[:, 0]))

        self.current_step = 0  # To track the current time step in the data

        # Define action space (0 = Hold, 1 = Buy, 2 = Sell)
        self.action_space = spaces.Discrete(3)

        # Define state space (energy in storage, normalized max_price) (MODIFIED)
        self.observation_space = spaces.Box(
            low=np.array([0, 0]),  # [energy, min(normalized max_price)]
            high=np.array([max_storage_capacity, 1]),  # [energy, max(normalized max_price)]
            dtype=np.float32
        )

        # Define maximum steps per episode (NEW)
        self.max_steps_per_episode = 1000  # Adjust this value as needed

    def reset(self, seed=None):
        """
        Resets the environment to an initial state.
        """
        super().reset(seed=seed)  # Required for Gymnasium
        self.current_step = 0  # Reset to the first time step
        self.energy_storage = self.max_storage_capacity / 2  # Start with half storage
        self.energy_price = self.time_series_data[self.current_step, 0]  # Initial max_price
        self.state = np.array([self.energy_storage, self.energy_price], dtype=np.float32)  # Initial state
        self.total_reward = 0  # Reset total reward

        return self.state, {}

    def step(self, action, debug=False):  # Added debug parameter (NEW)
        """
        Take the action and update the environment accordingly.
        """
        reward = 0

        if action == 1:  # Buy energy
            if self.energy_storage < self.max_storage_capacity:
                self.energy_storage += 1
                reward = -self.time_series_data[self.current_step, 1] * 0.01  # Reduced buying cost
            else:
                reward = -0.01  # Penalty for overbuying

        elif action == 2:  # Sell energy
            if self.energy_storage > 0:
                self.energy_storage -= 1
                reward = self.time_series_data[self.current_step, 0] * 15  # increase selling reward
            else:
                reward = -1  # Penalty for overselling

        elif action == 0:  # Hold
            reward = 0.001  # # Small positive reward for holding

        # Update state
        self.current_step += 1
        if self.current_step >= len(self.time_series_data) or self.current_step >= self.max_steps_per_episode:  # MODIFIED
            done = True  # End of data or max steps reached
            next_state = self.state  # No further state updates
        else:
            done = False
            self.energy_price = self.time_series_data[self.current_step, 0]  # Update max_price
            next_state = np.array([self.energy_storage, self.energy_price], dtype=np.float32)

        # Update total reward
        self.total_reward += reward

        # Debugging (NEW)
        if debug:
            print(f"Step {self.current_step}: Action = {self._get_action_name(action)}, Reward = {reward}, Total Reward = {self.total_reward}")

        return next_state, reward, done, {}

    def display_state(self, action, done, reward):
        """
        Displays the current environment state, action, and reward.
        """
        print(f"State: [Energy Storage = {self.energy_storage:.2f} kWh, Energy Price = {self.energy_price:.2f}]")
        print(f"Action: {self._get_action_name(action)}")
        print(f"Reward: {reward:.2f}")
        print(f"Total Reward: {self.total_reward:.2f}")
        print(f"Done: {done}")
        print("-" * 40)

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
        else:
            return "Unknown"
