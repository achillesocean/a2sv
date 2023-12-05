class Solution(object):
    def wateringPlants(self, plants, capacity):
        # on taking each step, increment your steps counter
        # you can water a plant if you have enough to water
        step_count = 0
        #keep track of actual capacity
        act_capacity = capacity
        for p in range(len(plants)):
            if plants[p] <= capacity:
                step_count += 1
                capacity -= plants[p]
            
            else:
                capacity = act_capacity
                step_count += (p + p + 1)#p for going back to river, p + 1 for coming back
                capacity -= plants[p]# when you water

        return step_count
        """
        :type plants: List[int]
        :type capacity: int
        :rtype: int
        """
        