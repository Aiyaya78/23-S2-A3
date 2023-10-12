from dataclasses import dataclass
from random_gen import RandomGen

# Islands can have names other than this. This is just used for random generation.
ISLAND_NAMES = [
    "Dawn Island",
    "Shimotsuki Village",
    "Gecko Islands",
    "Baratie",
    "Conomi Islands",
    "Drum Island",
    "Water 7"
    "Ohara",
    "Thriller Bark",
    "Fish-Man Island",
    "Zou",
    "Wano Country",
    "Arabasta Kingdom",
    # 13 🌞 🏃‍♀️
    "Loguetown",
    "Cactus Island",
    "Little Garden",
    "Jaya",
    "Skypeia",
    "Long Ring Long Land",
    "Enies Lobby",
    "Sabaody Archipelago",
    "Impel Down",
    "Marineford",
    "Punk Hazard",
    "Dressrosa",
    "Whole Cake Island",
]

@dataclass
class Island:

    name: str
    money: float
    marines: int
    

    def value(self) -> float:
        """
        Calculate the loot-to-marine ratio for the island.
        Complexity: O(1)
        """
        return (self.money / self.marines)
            
    def __lt__(self, other: 'Island') -> bool:
        """
        Check if the current island's value is less than the other island's value.
        Complexity: O(1)
        """
        return self.value() < other.value()

    def __le__(self, other: 'Island') -> bool:
        """
        Check if the current island's value is less than or equal to the other island's value.        
        Complexity: O(1)
        """
        return self.value() <= other.value()

    def __gt__(self, other: 'Island') -> bool:
        """
        Check if the current island's value is greater than the other island's value.
        Complexity: O(1)
        """
        return self.value() > other.value()

    def __ge__(self, other: 'Island') -> bool:
        """
        Check if the current island's value is greater than or equal to the other island's value.
        Complexity: O(1)
        """
        return self.value() >= other.value()
    
    @classmethod
    def random(cls):
        return Island(
            RandomGen.random_choice(ISLAND_NAMES),
            RandomGen.random() * 500,
            RandomGen.randint(0, 300),
        )
