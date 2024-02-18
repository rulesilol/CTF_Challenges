import random
import hashlib

def maxArea(budget: float, fenceCost: float) -> int:
    # Insert Code Here

    x = budget/(fenceCost * 4)
    y = budget/(fenceCost * 2)
    area = int(x * y )

    return area

assert maxArea(100.0, 3.0) == 138
assert maxArea(640.0, 8.0) == 800
assert maxArea(4433.0, 61.0) == 660

## Driver code, do not meddle with the code below

sha256 = hashlib.sha256()
sha256.update(str(maxArea(4433.0, 61.0) + maxArea(1093.0, 40.0) + maxArea(1974.0, 94.0) + maxArea(975.0, 22.0) + maxArea(1828.0, 16.0) + maxArea(1505.0, 12.0) + maxArea(4816.0, 52.0) + maxArea(308.0, 96.0) + maxArea(4705.0, 81.0) + maxArea(1402.0, 84.0) + maxArea(4375.0, 73.0) + maxArea(1590.0, 93.0) + maxArea(443.0, 50.0) + maxArea(4189.0, 84.0) + maxArea(3113.0, 94.0)).encode())
seed = sha256.hexdigest()

random.seed(seed)
randomLocations = random.sample(range(1, 500), 19)
print(randomLocations)

jumbledLetters = ['X', 'I', 'b', 'k', 'k', 'F', 'c', 'F', 'q', 'k', 'p', 'k', 'c', 'n', 'S', 'i', 'H', 'x', 'W', 'i', 's', 'E', 'L', 'v', 's', 'r', 'p', 's', 'G', 'D', 'V', 'd', 'm', 'Y', 'x', 'k', 'V', 'p', 'o', 'q', 'A', 'W', 'b', 'i', 'h', 'b', 'w', 'e', 'B', 'v', 'B', 'h', 'j', 'r', 'U', 'W', 'H', 'k', 'B', 't', 'e', 'e', 'R', 'e', 'C', 'I', 'D', 'i', 'F', 'n', 'n', 'v', 'l', 'G', 'L', 'j', 'e', 'h', 'U', 'e', 'z', 'y', 'f', 'n', 'R', 'H', 'P', 't', 'W', 'I', 'b', 'X', 'i', 'U', 'S', 's', 'y', 'a', 'T', 'q', 'L', 'f', 'o', 'K', 'e', 'D', 'O', 'P', 'F', 'o', 's', 'W', 'g', 'm', 'q', 'd', 'u', 'V', 'J', 'u', 'c', 'h', 'M', 'g', 'c', 'O', 'j', 'K', 'e', 'H', 'o', 'c', 'l', 'U', 'C', 'q', 'a', 'E', 'G', 'o', 'p', 'z', 'B', 'c', 'F', 'x', 'P', 'g', 'F', 'k', 'J', 'B', 'x', 'B', 'z', 'J', 'W', 'K', 'S', 'X', 'x', 'S', 'D', 'A', 'U', 'O', 'q', 'D', 'g', 'i', 'W', 'm', 'H', 'W', 'c', 'y', 'w', 'H', 'U', 'W', 'u', 'Q', 'F', 'N', 'h', 'D', 'n', 'r', 'Y', 'F', 'w', 'g', 'L', 'q', 'a', 'b', 'q', 'M', 'h', 'w', 'T', 'C', 'w', 'e', 'z', 'f', 'h', 'Z', 'g', 'A', 'R', 'F', 'I', 'p', 'N', 'h', 'G', 'R', 'V', 'T', 'w', 's', 'r', 'y', 'q', 'Y', 'W', 'k', 'n', 's', 'p', 'x', 'K', 'w', 'W', 'J', 'H', 'e', 'x', 'R', 'z', 't', 'w', 'z', 'X', 'R', 'l', 'u', 's', 'j', 'q', 'P', 'B', 'o', 'O', 'D', 'K', 'z', 'F', 'B', 'c', 'R', 'L', 'A', 'X', 'T', 'c', 'q', 'z', 'j', 'B', 'd', 'b', 'q', 'n', 'V', 'T', 'B', 'O', 'i', 'o', 'y', 'e', 'i', 'e', 'P', 'c', 'x', 'V', 'd', 'H', 'a', 'L', 'h', 'O', 'x', 'G', 'L', 'M', 'l', 's', 's', 'H', 'm', 'n', 'N', 'p', 'T', 'c', 'd', 'n', 'K', 'N', 'M', 'l', 'J', 'Q', 'N', 'H', 'U', 'C', 'h', 'S', 'c', 'o', 'T', 'G', 'f', 'B', 'J', 'a', 'm', 'c', 'e', 'i', 'y', 'w', 'x', 'u', 'V', 'n', 'M', 'e', 'O', 'O', 'S', 'l', 's', 'R', 'D', 'I', 'p', 'G', 'F', 'N', 'b', 'p', 'l', 'E', 'v', 't', 'y', 'e', 'c', 'r', 'O', 'Q', 'q', 'm', 'O', 'w', 'w', 'C', 'C', 'i', 'r', 'E', 'b', 'B', 'f', 's', 'F', 'H', 'D', 'G', 'h', 'p', 'a', 'u', 'L', 'a', 'X', 'S', 'r', 'l', 's', 'S', 'V', 'l', 'K', 'P', 'q', 'J', 'Y', 'P', 'B', 'S', 'u', 'n', 'j', 'e', 'v', 'I', 'o', 'V', 'o', 'O', 'L', 't', 'o', 'x', 'U', 'C', 'j', 'L', 'R', 'E', 'l', 'e', 'v', 'D', 'B', 'r', 'X', 'Y', 'H', 'S', 'g', 'G', 'q', 'C', 'V', 'c', 'M', 'C', 'O', 'v', 'l', 'Q', 'z', 'm', 'i', 'P', 'q', 'y', 'w', 'J', 'Q', 'o', 'g', 'q', 'c', 'a', 'h', 'm', 'W', 'p', 'd', 'W', 'a', 'V', 'u', 'L', 'T', 's', 'O', 'T', 'q', 'p', 'k', 'n', 'j', 'n', 'O', 't', 'a', 'u', 'T', 'J', 'R', 'u', 'F', 'm', 'E', 'M', 'X', 'C', 'l', 'F', 'F']

returnFlag = "FLAG{"
for i in range(19):
    returnFlag += jumbledLetters[randomLocations[i]]
returnFlag += "}"

print(returnFlag)