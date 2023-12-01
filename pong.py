import gym
import numpy as np

# Hyperparameters
learning_rate = 0.1
discount_factor = 0.9
exploration_prob = 0.1
num_episodes = 1000

# Initialize the environment
env = gym.make("Pong-v4")

# Define the Q-table
action_space_size = env.action_space.n
state_space_size = env.observation_space.shape[0]
q_table = np.zeros((state_space_size, action_space_size))

# Discretize the state space
def discretize_state(state):
    return tuple(np.round(state, decimals=1))

# Choose an action using epsilon-greedy policy
def choose_action(state):
    if np.random.rand() < exploration_prob:
        return env.action_space.sample()  # Exploration
    else:
        return np.argmax(q_table[state])

# Training loop
for episode in range(num_episodes):
    state = discretize_state(env.reset())
    total_reward = 0

    while True:
        # Choose an action
        action = choose_action(state)

        # Take the chosen action
        next_state, reward, done, _ = env.step(action)
        next_state = discretize_state(next_state)

        # Update Q-value using Q-learning formula
        q_table[state][action] += learning_rate * (
            reward + discount_factor * np.max(q_table[next_state]) - q_table[state][action]
        )

        total_reward += reward
       
