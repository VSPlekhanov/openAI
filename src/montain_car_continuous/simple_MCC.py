if __name__ == '__main__':
    import gym

    env = gym.make('MountainCarContinuous-v0')
    next_step = [0.0]
    env.reset()
    for i in range(1000):
        env.render()
        obs, reward, done, info = env.step(next_step)
        print(obs)
        print(reward)
        print(info)
        # if i % 10 == 0 :
        #     next_step = [float(input())]
        if 0.001 > obs[1] > 0 or obs[1] < -0.001:
            next_step = [-1.0]
        else:
            if obs[1] > 0.04 and obs[0] > 0.10:
                next_step = [0.0]
            else:
                next_step = [1.0]
        if done:
            print("success!")
            break
    env.close()