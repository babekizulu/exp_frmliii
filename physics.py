# formuliii
# @author: Lwandle Babekizulu Dlamini
# @desc: A physics library

class Physics:
    # velocity
    def velocity(distance, time):
        return distance/time
    # acceleration

    def acceleration(velocity, time):
        return velocity/time
    # equations of motion

    # 1. Velocity
    def velocityEOM(initialVelocity, acceleration, time):
        return initialVelocity + (acceleration*time)
    # 2. Displacement

    # def displacementEOM(initialDisplacement, initialVelocity, time, acceleration):
    #     return initialDisplacement + (initialVelocity*time) + (0.5(acceleration*time))**2
    # 3. Velocity Squared

    def velocitySquaredEOM(initialVeloicty, acceleration, finalDisplacement, initialDisplacement):
        return (initialVeloicty**2) + (2*acceleration)*(finalDisplacement-initialDisplacement)
    # 4. Average Velocity

    def averageVelocity(velocity, initialVelocity):
        return 0.5 * (velocity + initialVelocity)
    # newtons second law

    def newtonsSecondLaw(mass, acceleration):
        return mass * acceleration
    # weight
    # @constants: gravitationalAcceleration - 9.8m/s
    #

    def weight(mass, gravitationalAcceleration):
        return mass * gravitationalAcceleration
    # dry friction

    def dryFriction(coefficientOfFriction, normalForce):
        return coefficientOfFriction * normalForce
    # centripetal acceleration
    # @params:
    # - r: distance from the center of the circle to the moving body

    def centripetalAcceleration(velocity, r):
        return velocity**2/r
    # momentum

    def momentum(mass, velocity):
        return mass*velocity

    # impulse
    def impulse(averageForce, finalTime, initialTime):
        return averageForce*(finalTime - initialTime)
    # impulse-momentum

    def impulseMomentum(mass, changeInVelocity):
        return mass * changeInVelocity

    # work
    def work(averageForce, displacement):
        return averageForce * displacement
    # work-energy

    def workEnergy(finalKineticEnergy, initialKineticEnergy):
        return finalKineticEnergy - initialKineticEnergy
