from island import Island
from algorithms.mergesort import mergesort
from algorithms.binary_search import binary_search


class Mode1Navigator:
    """
    Mode1Navigator strategizes the optimal way to raid a collection of islands to maximize loot potential given a crew count.

    Approach:
    The navigator sorts islands based on a calculated loot-to-marine ratio, such that the most valuable islands are raided 
    first. The process is repeated until all the crew are used up or no more islands are left to raid.
    
    Data Structures Used:
    1. List: To store the islands sorted by their loot-to-marine ratio.
    2. Dictionary: To enable constant time lookups of islands based on their unique value.

    Small Example:
    If we have islands A, B, and C with respective loot-to-marine ratios of 10, 5, and 15 and an available crew of 100, the 
    navigator would first prioritize raiding island C, followed by A, and then B.

    Complexity Reasoning:
    See each method.
    """
    def __init__(self, islands: list[Island], crew: int) -> None:
        """
        Initialize the Mode1Navigator with a list of islands and a given crew count.

        Firstly, the method sorts the islands based on their loot-to-marine ratio to prioritize raiding the 
        most valuable islands first. This sort is performed using a mergesort. 
        Secondly, it sets up a dictionary, `value_to_island`, that maps each island's unique loot-to-marine ratio 
        to the respective island object for quick lookups.

        Complexity Reasoning:
        - Mergesort: 
            Best Case: O(N log N), where the list is already sorted or almost sorted.
            Worst Case: O(N log N), when the list is in reverse order or completely random.
        The complexity remains O(N log N) as mergesort provides a consistent performance for different input cases.
        
        - Dictionary Setup:
            Iterating over the islands and setting up the dictionary is O(N), where N is the number of islands.

        Overall, the worst-case and best-case time complexity of the `__init__` method is O(N log N + N), which simplifies 
        to O(N log N). N represents the number of islands in the provided islands list.

        Parameters:
        - islands (list[Island]): A list of Island objects, each representing an island to potentially raid.
        - crew (int): The total number of pirates available for raiding.

        Attributes:
        - crew (int): Represents the available pirates for raiding.
        - islands (list[Island]): A sorted list of islands based on their loot-to-marine ratio.
        - value_to_island (dict): A mapping from the island's unique value (ratio) to the Island object.
        """
        self.crew = crew
        # Sort the islands using mergesort by their value
        self.islands = mergesort(islands)
        self.value_to_island = {}
        for island in islands:  # O(N)
            # Calculate the unique value (loot-to-marine ratio) for the island
            value = island.value()  
            self.value_to_island[value] = island 

       

    @staticmethod
    def loot_potential(island: Island, crew: int) -> float:
        """
        Calculate the potential loot obtained from raiding an island based on the available crew.

        If the crew count is greater than or equal to the marines on the island, 
        the potential loot is the total money on the island. 
        Otherwise, the potential loot is calculated based on the money-to-marine ratio.

        Complexity Reasoning:
        - Best Case: O(1), as it involves a simple comparison followed by direct attribute access or a multiplication.
        - Worst Case: O(1), same as best case.

        
        Parameters:
        - island (Island): The island to calculate potential loot for.
        - crew (int): The number of pirates available for raiding.

        Returns:
        - float: The potential loot from the island.
        """
        # If we have enough crew to overcome the marines on the island
        if crew >= island.marines:
            return island.money
        # Otherwise, calculate potential loot based on money-to-marine ratio
        else:
            return island.value() * crew
        
    
    
    def select_islands(self) -> list[tuple[Island, int]]:
        """
        Determine the optimal set of islands to raid to maximize loot, given the available crew.

        The function iterates through the sorted list of islands (from the highest loot-to-marine ratio to the lowest) 
        and selects the ones which can be raided with the available crew. The chosen island is then marked as raided 
        and the crew count is updated. The function stops either when there's no more available crew or all islands 
        have been considered.

        Complexity Reasoning:
        - Best Case: O(1) when the first island in the sorted list consumes all available crew or there's no 
                    available crew from the start.
        - Worst Case: O(N) where N is the number of islands. This happens when we need to check every island, either 
                    because the crew is sufficiently large or because not every island can be raided.

        Parameters:
        None

        Returns:
        A list of tuples. Each tuple consists of the Island object and the number of pirates sent to raid it.
        """
        # Set the available crew from the instance variable
        available_crew = self.crew
        # Initialize the loot plan list to keep track of raided islands and the number of pirates sent
        loot_plan = []
        # Iterate through the islands in decreasing order of their loot-to-marine ratio
        for island in reversed(self.islands): # O(N)
            # If there's no available crew, break out of the loop
            if available_crew <= 0:
                break
            # Determine the number of pirates to send to the island. It's either the available crew 
            # or the number of marines on the island, whichever is smaller.
            pirates_to_send = min(available_crew, island.marines)
            # If we're sending pirates (more than 0), append to the loot plan and update the available crew count
            if pirates_to_send > 0:
                loot_plan.append((island, pirates_to_send))
                available_crew -= pirates_to_send

        return loot_plan
    

    def select_islands_from_crew_numbers(self, crew_numbers: list[int]) -> list[float]:
        """
        
        Determine the potential loot obtained when raiding islands for each specified crew size.

        This function evaluates the optimal island raiding strategy for multiple crew sizes, as provided in 
        'crew_numbers'. For each crew size, it determines the islands to be raided and then calculates the 
        potential loot. The results are aggregated in a list which maps to the input crew sizes.

        Complexity Reasoning:
        - Best Case: O(C) where C is the length of crew_numbers. This happens when select_islands (which 
                    internally has a worst-case complexity of O(N)) has a best case complexity of O(1) for 
                    all crew sizes in crew_numbers.
        - Worst Case: O(C * N) where C is the length of crew_numbers and N is the number of islands. This is 
                    when select_islands operates at its worst-case complexity for all crew sizes in crew_numbers.

        Parameters:
        - crew_numbers (list[int]): A list of crew sizes to evaluate.

        Returns:
        A list of floats. Each float represents the potential loot obtained for the corresponding crew size in crew_numbers.
        """
        # Initialize the results list to store the potential loot for each crew size
        results = []

        # Iterate through each specified crew size
        for crew in crew_numbers: # O(C)
            # Update the instance's crew count
            self.crew = crew
            # Determine the islands to raid using the current crew count
            islands_selected = self.select_islands() # BEST:O(1), WORST:O(N)
            # Calculate the total potential loot for the raided island
            total_money = sum([Mode1Navigator.loot_potential(island, crew_sent) for island, crew_sent in islands_selected])
            # Append the result to the results list
            results.append(total_money)

        return results

    def update_island(self, island: Island, new_money: float, new_marines: int) -> None:
        """
        Update the attributes (money and marines) of a particular island. 
        
        Given that the ratio of marines to gold for each island remains unique throughout execution,
        this update does not disrupt the order of the sorted islands list. 
        
        Complexity Reasoning:
        - Best Case: O(1), when the middle index directly points to the island in question.
        - Worst Case: O(log N) where N is the number of islands, due to binary search.

        :param island: The Island object to be updated.
        :param new_money: The new amount of money to set for the island.
        :param new_marines: The new number of marines to set for the island.
        
        """
        # Find the island's position in the list
        index = binary_search(self.islands, island)
        
        # Ensure we found the correct island
        if self.islands[index] != island:
            raise ValueError(f"Island {island.name} not found in the list of islands.")
        
        # Update the attributes of the island
        self.islands[index].money = new_money
        self.islands[index].marines = new_marines