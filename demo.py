from island import Island
from data_structures.heap import MaxHeap
from data_structures.hash_table import LinearProbeTable

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
        print(loot_plan)
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
            print("total money:", total_money)
            results.append(total_money)
        print(results)
        return results

    def update_island(self, island: Island, new_money: float, new_marines: int) -> None:
        """
        Student-TODO: Best/Worst Case
        """
        # Assuming self.islands is a list storing all islands:
        index = self.islands.index(island)
        self.islands[index].money = new_money
        self.islands[index].marines = new_marines
        

def load_basic(self):
        self.a = Island("A", 400, 100)
        self.b = Island("B", 300, 150)
        self.c = Island("C", 100, 5)
        self.d = Island("D", 350, 90)
        self.e = Island("E", 300, 100)
        # Create deepcopies of the islands
        self.islands = [
            Island(self.a.name, self.a.money, self.a.marines),
            Island(self.b.name, self.b.money, self.b.marines),
            Island(self.c.name, self.c.money, self.c.marines),
            Island(self.d.name, self.d.money, self.d.marines),
            Island(self.e.name, self.e.money, self.e.marines),
        ]

def check_solution(self, islands, starting_crew, solution, optimal):
        current_money = 0
        current_crew = starting_crew
        for island, crew_sent in solution:
            self.assertGreaterEqual(crew_sent, 0)
            # This assertIn is written so that we allow copies with the same properties to be considered equal.
            self.assertIn((island.name, island.money, island.marines), [(i.name, i.money, i.marines) for i in islands])
            current_money += min(island.money * crew_sent / island.marines, island.money)
            current_crew -= crew_sent
            self.assertGreaterEqual(current_crew, 0)
        self.assertFalse(current_money < optimal, "Your island selection is suboptimal!")
        if current_money > optimal:
            raise ValueError("ERROR! You somehow made more money than the intended solution")

if __name__ == "__main__":

    a = Island("A", 400, 100)
    b = Island("B", 300, 150)
    c = Island("C", 100, 5)
    d = Island("D", 350, 90)
    e = Island("E", 300, 100)
    
    islands = [
            Island(a.name, a.money, a.marines),
            Island(b.name, b.money, b.marines),
            Island(c.name, c.money, c.marines),
            Island(d.name, d.money, d.marines),
            Island(e.name, e.money, e.marines),
        ]
    
      
    nav = Mode1Navigator(islands, 200)
    # selected = nav.select_islands()
    
    results = nav.select_islands_from_crew_numbers([0, 200, 500, 300, 40])
    # self.assertListEqual(results, [0, 865, 1450, 1160, 240])
