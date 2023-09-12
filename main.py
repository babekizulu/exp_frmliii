import physics
# solve a problem using an equation from on of the libraries
# since 5 divided by 2 is 2.5, should return 2.5
result1 = physics.Physics.velocity(5, 2)  # 2.5
result2 = physics.Physics.acceleration(5, 2)  # 2.5
result3 = physics.Physics.momentum(4, 3)  # 12
data = [str(result1), str(result2), str(result3)]
dataStr = ','.join(data)
columnHeaders = ['velocity', 'acceleration', 'momentum']

# write result data to csv file
with open('results.csv', 'w') as f:
    for dataLine in dataStr:
        f.write(dataLine)
