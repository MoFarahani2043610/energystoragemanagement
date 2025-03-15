# learning parameters
ALPHA = 0.1  # Learning rate
GAMMA = 0.9  # Discount factor
EPSILON = 1.0  # Initial exploration rate
EPSILON_DECAY = 0.995   # Epsilon decay for more exploration
EPSILON_MIN = 0.2 # Minimum value for epsilon

# Discretize the state space
NUM_BINS_ENERGY = 100  # Number of bins for energy in storage
NUM_BINS_PRICE = 200  # Number of bins for energy price