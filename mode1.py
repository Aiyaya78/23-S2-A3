from island import Island
from data_structures.heap import MaxHeap

class Mode1Navigator:
    """
    Student-TODO: short paragraph as per https://edstem.org/au/courses/12108/lessons/42810/slides/294117
    """

    def __init__(self, islands: list[Island], crew: int) -> None:
        """
        Student-TODO: Best/Worst Case
        """
        self.crew = crew
        self.islands = islands[:]
        self.local_heap = MaxHeap(len(islands))
        self.value_to_island = {}
        for island in islands:
            value = island.value()
            self.local_heap.add(value)
            self.value_to_island[value] = island

    @staticmethod
    def loot_potential(island: Island, crew: int) -> float:
        if crew >= island.marines:
            return island.money
        else:
            return island.value() * crew
        
    
    def select_islands(self) -> list[tuple[Island, int]]:
        available_crew = self.crew
        loot_plan = []
        local_islands = self.islands[:]

        while available_crew > 0:
        
            if self.local_heap.length == 0:
                break
            top_value = self.local_heap.get_max()
            top_island = self.value_to_island[top_value]

            pirates_to_send = min(available_crew, top_island.marines)


            if pirates_to_send > 0:
                loot_plan.append((top_island, pirates_to_send))
                available_crew -= pirates_to_send
                
        self.local_heap = self.build_heap(local_islands)
        return loot_plan

    

    def build_heap(self, islands: list[Island]) -> MaxHeap:
        new_heap = MaxHeap(len(islands))
        self.value_to_island = {}
        for island in islands:
            value = island.value()
            new_heap.add(value)
            self.value_to_island[value] = island
        return new_heap


    def select_islands_from_crew_numbers(self, crew_numbers: list[int]) -> list[float]:
        """
        Student-TODO: Best/Worst Case
        """
        results = []

        for crew in crew_numbers:
            self.crew = crew
            islands_selected = self.select_islands()
            total_money = sum([Mode1Navigator.loot_potential(island, crew_sent) for island, crew_sent in islands_selected])
            results.append(total_money)
        return results

    def update_island(self, island: Island, new_money: float, new_marines: int) -> None:
        """
        Student-TODO: Best/Worst Case
        """
        # Assuming self.islands is a list storing all islands:
        index = self.islands.index(island)
        self.islands[index].money = new_money
        self.islands[index].marines = new_marines