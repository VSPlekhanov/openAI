if __name__ == '__main__':
    import gym

    env = gym.make('MountainCar-v0')
    min_velocity = 0.001
    avg = 0
    for i in range(10000):
        done = False
        total_reward = 0
        next_step = 0
        env.reset()

        while not done:
            # env.render()
            obs, reward, done, info = env.step(next_step)
            if min_velocity > obs[1] > 0 or obs[1] < -min_velocity:
                next_step = 0
            else:
                next_step = 2
            total_reward += reward
        avg += total_reward

    print("average reward {}".format(avg / 10000))
    env.close()
