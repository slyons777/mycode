"""Sarina Lyons | sarina.lyons@tlgcohort.com
   range practice CHALLENGE
"""

def main():
    for i in range(99, 0, -1):
        print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
        print(f"Take one down, pass it around, {i-1} bottles of beer on the wall.")
        print()

if __name__ == "__main__":
    main()
