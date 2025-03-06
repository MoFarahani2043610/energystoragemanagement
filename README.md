# **Energy Storage Management - Reinforcement Learning Environment**

## **Overview**
This project implements a custom **Reinforcement Learning (RL)** environment designed to manage an energy storage system using the **Gym** library. The environment simulates an agent making energy trading decisions—such as buying, selling, or holding energy—based on fluctuating market prices. The goal is to **maximize profit** by making optimal energy trading decisions over time.

---

## **Features**
- **Custom Gym Environment:** Models energy storage and decision-making related to trading.
- **Action-Based Decision Making:** The agent can choose to buy, sell, or hold energy.
- **Dynamic Energy Pricing:** Utilizes a 199-day dataset containing daily minimum and maximum prices.
- **State Representation:** Tracks energy storage levels and price fluctuations.
- **Reinforcement Learning Ready:** Facilitates the development of optimized trading strategies.
- **Colab Compatibility:** Designed to run seamlessly in Google Colab with minimal setup.

---

## **Components of the Environment**



### **1. State and Action Spaces**
#### **State Space:**
- Represents the current energy storage level (**continuous values**).
- Includes the **current energy price**.

#### **Action Space:**
- `0 → Hold:` Do nothing.
- `1 → Buy:` Increase storage (pay the current price).
- `2 → Sell:` Decrease storage (earn the current price).

---

### **2. Dataset Explanation**
The dataset consists of **199 rows**, each representing a day.

Each row includes:
- **Minimum price** for the day.
- **Maximum price** for the day.

These prices simulate realistic energy market fluctuations.

**Colab Note:** The dataset can be uploaded to Colab using **Google Drive** or directly loaded from a **URL**.

---

### **3. Environment Initialization**
The environment begins with:
- A **random energy level** within defined storage capacity limits.
- A **random energy price** taken from the dataset.
- Defined constraints on **max storage capacity** and **price range**.

---

### **4. Reset Function**
- Resets the environment to an **initial state**.
- Randomizes the **starting energy level** and **price**.
- Resets the **total accumulated reward**.

**Colab Note:** The `reset()` function is called at the start of each episode.

---

### **5. Step Function**
- Processes the **agent's action** and updates the environment state.
- Implements the logic for **buying**, **selling**, or **holding** energy.
- Calculates **rewards** based on **profit/loss** from the transaction.
- Updates the **energy storage level** and selects a new random price from the dataset.
- Ends the **episode** if the **total reward** drops below a defined threshold.

**Colab Note:** The `step()` function is called for each action taken by the agent.

---

### **6. Reward System**
- **Buying energy:** Results in a **negative reward** (cost).
- **Selling energy:** Generates a **positive reward** (profit).
- **Holding energy:** Results in **no immediate reward**.

The agent's goal is to **maximize cumulative reward** over multiple episodes.

## **Results**

## Total Reward per Episode Plot

- The cumulative reward represents the sum of all rewards accumulated by the agent in a single episode.This metric reflects the overall performance of the agent.

- A higher cumulative reward indicates better decision-making (buying at low prices, selling at high prices, or holding strategically).

## Actions Taken in the Last Episode Plot

- Displays the specific actions (Hold, Buy, Sell) taken by the agent in the final episode.

- These actions are influenced by the agent's learned policy (Q-table) and exploration strategy (epsilon-greedy).

- A good strategy typically involves buying energy when prices are low and selling when prices are high.
