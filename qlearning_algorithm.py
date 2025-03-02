# Create an instance of the environment
from constants import ALPHA, EPSILON_DECAY, EPSILON_MIN, GAMMA, NUM_BINS_ENERGY, NUM_BINS_PRICE
from energystorageclass import EnergyStorageEnv
import numpy as np

from qtable_creation import discretize_state, get_action_space_size, get_state_space_size

env = EnergyStorageEnv()

# Q-learning update rule
def update_q_table(q_table, state, action, reward, next_state, alpha, gamma):
    current_q_value = q_table[state, action]
    max_future_q_value = np.max(q_table[next_state, :])
    new_q_value = (1 - alpha) * current_q_value + alpha * (reward + gamma * max_future_q_value)
    q_table[state, action] = new_q_value
    return q_table

# Train the agent
num_episodes = 1000
epsilon = 1.0  # Initialize epsilon
q_table = np.zeros((get_state_space_size(), get_action_space_size()))  # Initialize Q-table

for episode in range(num_episodes):
    state, _ = env.reset()
    state_index = discretize_state(state, NUM_BINS_ENERGY, NUM_BINS_PRICE, env.max_storage_capacity, env.max_price)
    done = False

    while not done:
        # Epsilon-greedy action selection
        if np.random.rand() < epsilon:
            action = np.random.randint(0, get_action_space_size())  # Explore: random action
        else:
            action = np.argmax(q_table[state_index, :])  # Exploit: best known action

        # Take the action and observe the next state and reward
        next_state, reward, done, _ = env.step(action)
        next_state_index = discretize_state(next_state, NUM_BINS_ENERGY, NUM_BINS_PRICE, env.max_storage_capacity, env.max_price)

        # Update Q-table
        q_table = update_q_table(q_table, state_index, action, reward, next_state_index, ALPHA, GAMMA)

        # Move to the next state
        state_index = next_state_index

    # Decay epsilon
    epsilon = max(EPSILON_MIN, epsilon * EPSILON_DECAY)

    # Print progress
    if (episode + 1) % 100 == 0:
        print(f"Episode {episode + 1}, Epsilon: {epsilon:.3f}")

print("Training complete!")
