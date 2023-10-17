from dataclasses import dataclass

@dataclass
class DataClassCard:
    rank: str
    suit: str
    
def main():
    queen_of_hearts = DataClassCard('Q', 'Hearts')
    return queen_of_hearts.rank

if __name__ == '__main__':
    print(main())