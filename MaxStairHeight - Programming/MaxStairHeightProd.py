import random
import string
import hashlib

def maxStairHeight(startHeight, endHeight, length):
    ## Your Code Here
        
    return height

## Driver code, do not meddle with the code below
assert(maxStairHeight(5,6,6)) == 9
assert(maxStairHeight(3,0,8)) == 6
assert(maxStairHeight(20, 25, 22)) == 34

sha256 = hashlib.sha256()
sha256.update((str(maxStairHeight(634, 513, 116)) + str(maxStairHeight(650, 219, 90)) + str(maxStairHeight(129, 512, 68)) + str(maxStairHeight(951, 395, 121)) + str(maxStairHeight(264, 353, 200)) + str(maxStairHeight(0, 0, 0)) + str(maxStairHeight(497, 739, 69)) + str(maxStairHeight(245, 42, 110)) + str(maxStairHeight(799, 28, 186)) + str(maxStairHeight(86, 679, 182)) + str(maxStairHeight(374, 792, 161)) + str(maxStairHeight(187, 719, 61)) + str(maxStairHeight(129, 1293, 153)) + str(maxStairHeight(944, 486, 31)) + str(maxStairHeight(998, 88, 205)) ).encode())
seed = sha256.hexdigest()

random.seed(seed)
randomLocations = random.sample(range(1, 500), 19)
# print(randomLocations)

jumbledLetters = ['K', 'g', 'b', 'd', 'b', 'O', 'm', 'S', 'P', 'T', 'B', 'M', 'h', 'o', 'Q', 'p', 'J', 'e', 'S', 'B', 'A', 'N', 'l', 'T', 'C', 'L', 'O', 'y', 'c', 'c', 'h', 'G', 'W', 'H', 'z', 'T', 'G', 'n', 'a', 'H', 'h', 'p', 'x', 'a', 'O', 'z', 'e', 'a', 'n', 'z', 'x', 'g', 'j', 'n', 'x', 'n', 'f', 'D', 'o', 'r', 'c', 't', 'f', 'Y', 'J', 'X', 'D', 'M', 'V', 'b', 'k', 'J', 'j', 'A', 'x', 'H', 'I', 'V', 'j', 'e', 'n', 'E', 'Y', 'T', 'R', 'l', 'u', 'O', 'L', 'c', 'o', 'h', 'o', 'l', 'S', 'v', 'N', 'v', 'b', 'm', 'R', 't', 's', 'Z', 'q', 'e', 'g', 'D', 'M', 'H', 'c', 'h', 'P', 'U', 'd', 'i', 'q', 'R', 'y', 'f', 'b', 'O', 'y', 'E', 'w', 's', 'W', 'X', 'm', 's', 'x', 'i', 'i', 'd', 'S', 'A', 'Y', 'h', 'i', 'M', 'q', 'R', 'b', 'M', 'r', 'z', 'm', 'J', 'f', 'l', 'W', 'd', 'K', 's', 'f', 'H', 'T', 'j', 'd', 'p', 'z', 'S', 'V', 'q', 'A', 'N', 'C', 'J', 'M', 'p', 'M', 'R', 'g', 'A', 'p', 's', 'S', 'c', 'O', 'd', 'k', 's', 'I', 'l', 'V', 'H', 'l', 'q', 'x', 't', 'V', 'j', 'Z', 'T', 'H', 'T', 'y', 'g', 'q', 'T', 'G', 'R', 'f', 'l', 'F', 'j', 'T', 'z', 'y', 'M', 'g', 's', 'H', 'd', 'h', 'G', 'K', 'B', 'n', 'd', 'J', 'g', 'a', 'h', 'M', 'A', 't', 'K', 'Q', 'T', 'G', 'V', 'N', 'T', 'q', 'e', 'o', 'E', 'D', 'B', 'g', 'U', 'k', 'd', 'O', 'l', 'z', 'd', 'J', 'P', 'a', 'I', 'K', 'Q', 'b', 'm', 'u', 'R', 'w', 'C', 'g', 'X', 'P', 'y', 'v', 'w', 'F', 'g', 'Y', 'F', 'R', 'S', 'e', 'w', 'W', 'Q', 'L', 'V', 'q', 'y', 'i', 'r', 'G', 'L', 'v', 't', 'W', 'a', 'n', 'N', 'H', 'C', 'B', 'p', 'e', 'c', 'I', 'd', 'y', 'J', 'F', 'w', 'f', 'O', 'S', 'Q', 'y', 'C', 'M', 'G', 'g', 'U', 'R', 'Y', 'z', 'R', 'C', 'M', 'K', 'X', 'A', 'p', 'k', 'd', 'Y', 'i', 'P', 'N', 'u', 'f', 'M', 'K', 'y', 'H', 'D', 'x', 'p', 'a', 'L', 's', 'F', 'c', 'X', 't', 'L', 'P', 'L', 'Y', 's', 'g', 'Z', 'z', 't', 'd', 'R', 't', 't', 'o', 'z', 'h', 'e', 'X', 'y', 'f', 'f', 'W', 'M', 'f', 'b', 'h', 't', 't', 'z', 'L', 'H', 'j', 'M', 'k', 'V', 'm', 'W', 't', 'n', 'h', 'e', 'E', 'b', 'c', 'w', 'd', 'w', 'b', 'P', 'D', 'n', 'T', 'N', 'c', 'b', 'E', 'd', 't', 'C', 'b', 'h', 'd', 'M', 'l', 'p', 'p', 'c', 'x', 'g', 'U', 'Z', 'F', 'y', 'k', 'I', 'O', 'h', 'O', 'a', 'B', 'f', 'R', 'B', 'H', 'l', 'g', 'S', 'p', 'T', 'y', 'H', 'L', 'l', 'T', 'u', 'l', 'y', 'Y', 'G', 'l', 'v', 'k', 'q', 'k', 'K', 'y', 'v', 'L', 'b', 'X', 'k', 'Q', 'Z', 'd', 'P', 'C', 'U', 'g', 'l', 'c', 'U', 'S', 'S', 'C', 'g', 'U', 'f', 'K', 'r', 'M', 'k', 'T', 'A', 'E', 'g', 'p', 'Q', 'w', 'j', 'Y', 'F', 'd', 'S', 'R', 'j', 'I', 'r', 'e', 'd', 'f', 'P', 'w', 'b', 's', 'g', 'M']

returnFlag = "FLAG{"
for i in range(11):
    returnFlag += jumbledLetters[randomLocations[i]]
returnFlag += "}"

print(returnFlag)