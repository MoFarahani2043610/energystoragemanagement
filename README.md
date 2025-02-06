# Energy Storage Management

Purpose of This Code

This code creates a custom reinforcement learning environment for an energy storage system using the Gym library. The environment simulates a system where an agent can buy, sell, or hold energy based on fluctuations in energy prices. The goal of the agent is to maximize its total reward (profit) by making optimal decisions regarding energy transactions.

The agent interacts with the environment, selects different actions, and the environment responds accordingly. Over time, the agent learns to develop an effective strategy to maximize profit or minimize losses.

What is Needed to make an envirnment in Gymnasim envirnment?

1- Import Libraries (Gym, NumPy)

2- Create a Class inheriting from gym.Env

3- Define init() (State space, Action space, Parameters)

4- Define reset() (Reset state)

5- Define step(action) (Update state, reward, and termination)

6- Define render() (Show current state)

Sets up a Gym environment in Google Colab

Importing Libraries

Imports NumPy, a library used for numerical operations and random number generation.
Imports Gym, an OpenAI toolkit used to create and train reinforcement learning environments.
Imports spaces, which defines the state space (possible conditions of the environment) and the action space (possible actions the agent can take).

# Importing Libraries

Imports NumPy, a library used for numerical operations and random number generation.
Imports Gym, an OpenAI toolkit used to create and train reinforcement learning environments.
Imports spaces, which defines the state space (possible conditions of the environment) and the action space (possible actions the agent can take).

# Defining the Custom Environment Class

Why Do We Define a Class for an Environment? In Gym, every custom environment must be defined as a class that inherits from gym.Env. This ensures that the environment follows a standard structure that reinforcement learning (RL) algorithms can interact with.

By defining a class, we:

Encapsulate the environment’s behavior : The class stores all relevant data, such as energy levels and price fluctuations.

Ensure modularity and reusability : The environment can be easily modified and reused in different RL applications.

Allow interaction with RL agents : The agent interacts with the environment by taking actions and receiving feedback.

What Happens Here?

✅ Creates a new environment called EnergyStorageEnv

✅ Inherits from gym.Env to ensure compatibility with RL algorithms

✅ Simulates an energy storage system where the agent must decide:

Buy energy (increase storage, pay price)
Sell energy (decrease storage, earn price)
Hold energy (no change) This environment is useful for training an agent to optimize energy storage decisions based on price fluctuations.
Initializing the Environment
1- Defines the constructor method (init) to initialize the environment. It takes three parameters:

max_storage_capacity : The maximum amount of energy (in kWh) that can be stored.

max_price : The maximum energy price (in $/kWh).

min_price : The minimum energy price (in $/kWh).

2- Calls the constructor of the parent class gym.Env to properly initialize the environment.

3-Stores the maximum storage capacity and energy price range as environment attributes.

Defining State and Action Spaces

Defines state space:

The energy level in storage can range from 0 to 100 kWh.

continuous state space (spaces.Box).

Defines the price space, meaning energy prices can range from 0 to 100.

Defines the action space:

The agent has three possible actions:

0 → Hold (do nothing)

1 → Buy energy

2 → Sell energy

Initializing the State

The initial state is randomly generated:

The energy level is randomly set between 0 and max_storage_capacity. The energy price is randomly set between min_price and max_price. Initializes self.total_reward to 0, which will track the agent’s cumulative earnings.