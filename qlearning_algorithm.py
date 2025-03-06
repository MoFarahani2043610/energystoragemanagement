from constants import ALPHA, EPSILON_DECAY, EPSILON_MIN, GAMMA, NUM_BINS_ENERGY, NUM_BINS_PRICE
from energystorageclass import EnergyStorageEnv
import numpy as np
import matplotlib.pyplot as plt
from upload import time_series_data
from qtable_creation import discretize_state, get_action_space_size, get_state_space_size

env = EnergyStorageEnv(max_storage_capacity=100, time_series_data=time_series_data)

# Q-learning update rule
def update_q_table(q_table, state, action, reward, next_state, alpha, gamma):
    current_q_value = q_table[state, action]
    max_future_q_value = np.max(q_table[next_state, :])
    new_q_value = (1 - alpha) * current_q_value + alpha * (reward + gamma * max_future_q_value)
    q_table[state, action] = new_q_value
    return q_table

# Initialize list to store rewards per episode
episode_rewards = [] 
action_log = []  # To log actions taken in each episode

# Train the agent
num_episodes = 1000
epsilon = 1.0  
q_table = np.zeros((get_state_space_size(), get_action_space_size()))  # Initialize Q-table

# Action mapping
action_names = {0: "Hold", 1: "Buy", 2: "Sell"}

for episode in range(num_episodes):
    state, _ = env.reset()
    state_index = discretize_state(state, NUM_BINS_ENERGY, NUM_BINS_PRICE, env.max_storage_capacity, np.max(time_series_data[:, 0]))
    done = False
    total_reward = 0
    episode_actions = []  # To log actions for this episode

    while not done:
        # Epsilon-greedy action selection
        if np.random.rand() < epsilon:
            action = np.random.randint(0, get_action_space_size())  # Explore: random action
        else:
            action = np.argmax(q_table[state_index, :])  # Exploit: best known action
            
        # Log the action
        episode_actions.append(action)

        # Take the action and observe the next state and reward
        next_state, reward, done, _ = env.step(action)
        next_state_index = discretize_state(next_state, NUM_BINS_ENERGY, NUM_BINS_PRICE, env.max_storage_capacity, np.max(time_series_data[:, 0]))

        # Update Q-table
        q_table = update_q_table(q_table, state_index, action, reward, next_state_index, ALPHA, GAMMA)

        # Move to the next state
        state_index = next_state_index
        total_reward += reward
          
    # Store total reward for this episode
    episode_rewards.append(total_reward)  
    action_log.append(episode_actions)  

    # Decay epsilon
    epsilon = max(EPSILON_MIN, epsilon * EPSILON_DECAY)

    # Print progress
    if (episode + 1) % 100 == 0:
        print(f"Episode {episode + 1}, Epsilon: {epsilon:.3f}, Total Reward: {total_reward:.2f}")

print("Training complete!")

# Plot total reward per episode
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(episode_rewards)
plt.xlabel("Episode")
plt.ylabel("Total Reward")
plt.title("Total Reward per Episode")

# Plot actions taken in the last episode
plt.subplot(2, 1, 2)
plt.plot(action_log[-1], label="Actions")
plt.yticks([0, 1, 2], [action_names[0], action_names[1], action_names[2]])  # Map action numbers to names
plt.xlabel("Step")
plt.ylabel("Action")
plt.title("Actions Taken in each Episode")
plt.legend()
plt.tight_layout()
plt.show()

# Analyze action distribution
action_counts = np.zeros(get_action_space_size())
for episode_actions in action_log:
    for action in episode_actions:
        action_counts[action] += 1

print("Action Distribution:")
for action, count in enumerate(action_counts):
    print(f"Action {action} ({action_names[action]}): {count} times")
