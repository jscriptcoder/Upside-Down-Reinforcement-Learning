import gym
import gym.spaces
import rocket_lander_gym

env = gym.make("LunarLander-v2") # RocketLander-v0 | LunarLander-v2 | MountainCar-v0 | CartPole-v0
env.reset()
step = 0

PRINT_DEBUG_MSG = True


while True:
    env.render()
    action = env.action_space.sample()
    observation, reward, done, info = env.step(action)
    step += 1

    if PRINT_DEBUG_MSG:
        print("Step          ", step)
        print("Action Taken  ", action)
        print("Observation   ", observation)
        print("Reward Gained ", reward)
        print("Info          ", info, end='\n\n')

    if done:
        print("Simulation done.")
        break
env.close()
