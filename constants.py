# Define learning parameters
ALPHA = 0.1  # Learning rate
GAMMA = 0.9  # Discount factor
EPSILON = 1.0  # Initial exploration rate
EPSILON_DECAY = 0.995  # Decay rate for epsilon
EPSILON_MIN = 0.01 # Minimum value for epsilon
# Discretize the state space
NUM_BINS_ENERGY = 10  # Number of bins for energy in storage
NUM_BINS_PRICE = 10   # Number of bins for energy price