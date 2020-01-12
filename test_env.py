import gym
import gym.spaces
import rocket_lander_gym

env = gym.make("RocketLander-v0")
env.reset()

PRINT_DEBUG_MSG = True


while True:
    env.render()
    action = env.action_space.sample()
    observation, reward, done, info = env.step(action)

    if PRINT_DEBUG_MSG:
        print("Action Taken  ", action)
        print("Observation   ", observation)
        print("Reward Gained ", reward)
        print("Info          ", info, end='\n\n')

    if done:
        print("Simulation done.")
        break
env.close()
