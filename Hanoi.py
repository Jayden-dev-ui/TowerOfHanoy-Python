move_count = 0

def hanoi(n, source, auxiliary, target):
    global move_count

    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        move_count += 1
        return

    hanoi(n - 1, source, target, auxiliary)

    print(f"Move disk {n} from {source} to {target}")
    move_count += 1

    hanoi(n - 1, auxiliary, source, target)


n = int(input("Enter the n umber disk: "))

print("\nTower of Hanoi Moves: ")
hanoi(n, "A", "B", "C")

minimum_moves = (2 ** n) - 1

print("\nResults:")
print("Total moves made:", move_count)
print("Minimum moves using formula:", minimum_moves)