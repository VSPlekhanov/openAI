if __name__ == '__main__':
    import gym

    env = gym.make('MountainCar-v0')
    next_step = 1
    env.reset()
    for i in range(1000):
        env.render()
        obs, reward, done, info = env.step(next_step)
        if 0.0001 > obs[1] > 0 or obs[1] < -0.0001:
            next_step = 0
        else:
            next_step = 2
        if done:
            print("success!")
            print(obs)
            print(reward)
            print(info)
            break
    env.close()
