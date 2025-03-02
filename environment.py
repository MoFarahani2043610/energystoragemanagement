#example usage
from energystorageclass import EnergyStorageEnv

env = EnergyStorageEnv()
state,_ = env.reset()
        
randomAction = env.action_space.sample()

step = env.step(randomAction)

energyStep = step[0]
reward = step[1]
done = step[2]

print("energyStep - Energy Storage:", energyStep[0], "kWh, Energy Price:", energyStep[1])
print("reward", reward)
print("done", done)
print ("Action",env._get_action_name(randomAction))

    
            

            
    