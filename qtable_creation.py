# Create an instance of the environment
from constants import NUM_BINS_ENERGY, NUM_BINS_PRICE
from energystorageclass import EnergyStorageEnv
import numpy as np
from upload import time_series_data

env = EnergyStorageEnv(max_storage_capacity=100, time_series_data=time_series_data)

# Define action space size
action_space_size = env.action_space.n  # This will give 3 (for 0, 1, 2)

# Discretize the state space
def discretize_state(state, num_bins_energy, num_bins_price, max_storage_capacity, max_price):
        energy, price = state
        energy_bin = np.digitize(energy, np.linspace(0, max_storage_capacity, num_bins_energy)) - 1
        price_bin = np.digitize(price, np.linspace(0, max_price, num_bins_price)) - 1
        state_index = energy_bin * num_bins_price + price_bin
        return state_index

def get_state_space_size():
        return NUM_BINS_ENERGY * NUM_BINS_PRICE

def get_action_space_size():
        return env.action_space.n

def q_table():
        return np.zeros((get_state_space_size(), get_action_space_size()))
# Initialize Q-table
print("Q-table shape:", q_table().shape)