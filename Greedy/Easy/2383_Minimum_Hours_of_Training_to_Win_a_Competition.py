class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:

        total_training = 0

        # Simulates a series of competitions using a loop.
        for i in range(len(energy)):

            # If the specified energy is strictly greater than the opponent's energy, 
            # we participate in the competition and reduce our energy.
            if initialEnergy > energy[i]:
                initialEnergy -= energy[i]

            # If energy is insufficient, training hours must be used; to determine the required number of hours, 
            # calculate the difference between the opponent's energy and your own, 
            # then add one to satisfy the strict inequality.
            else:
                need_energy = energy[i] - initialEnergy + 1
                total_training += need_energy

                # After the training sessions, we participate in a competition and determine the new amount of energy 
                initialEnergy += need_energy
                initialEnergy -= energy[i]

            # If the given experience is strictly greater than the opponent's experience, 
            # we participate in the competition and increase the amount of experience.
            if initialExperience > experience[i]:
                initialExperience += experience[i]

            # If experience is insufficient, training hours must be utilized; to determine the required number of hours, 
            # calculate the difference between the opponent's experience and your own, 
            # then add one to satisfy the strict inequality.
            else:
                need_experience = experience[i] - initialExperience + 1
                total_training += need_experience

                # After the training sessions, we participate in a competition and determine the new amount of experience
                initialExperience += need_experience
                initialExperience += experience[i]

        return total_training