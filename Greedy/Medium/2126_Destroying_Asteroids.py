class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        '''
        Since a planet does not lose its mass when colliding with an asteroid, 
        but only accumulates the mass of asteroids, 
        it is not necessary to start with small asteroids and accumulate mass for larger asteroids.
        '''

        # sort the asteroid array to start with the smallest ones
        asteroids.sort()

        for i in range(len(asteroids)):

            # We start checking each asteroid. 
            # If the planet's mass is equal to or greater than the asteroid's mass, 
            # then we can shoot down this asteroid and take some of its mass for ourselves.
            if mass >= asteroids[i]:
                mass += asteroids[i]

            # If the planet's mass is less than the asteroid's mass, 
            # then it cannot be shot down and we immediately return false
            elif mass < asteroids[i]:
                return False

        # If all asteroids are destroyed, return true.
        return True