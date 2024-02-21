import random
from itertools import cycle
import hashlib

def defang(address: str) -> str:
    defanged = address.replace('.', '[.]')
    return defanged

assert defang("www.reddit.com") == "www[.]reddit[.]com"
assert defang("ftp.google.com") == "ftp[.]google[.]com"
assert defang("facebook.com") == "facebook[.]com"

## Driver code, do not meddle with the code below

sha256 = hashlib.sha256()
sha256.update((defang("ssl.google.com") + defang("youtube.com") + defang("tls.facebook.com") + defang("en.wikipedia.org") + defang("yahoo.com") + defang("www.yandex.ru") + defang("qq.com") + defang("www.netflix.com") + defang("") + defang("mail.google.com") + defang("defence.gov.au") + defang("reddit.com") + defang("www.abc.net.au") + defang("twitch.tv") + defang("imdb.com")).encode())
seed = sha256.hexdigest()

random.seed(seed)
randomLocations = random.sample(range(1, 500), 20)

jumbledLetters = ['q', 'w', 'q', 'q', 'E', 'I', 'c', 'o', 'M', 'w', 'l', 'L', 'v', 'K', 'F', 'R', 'V', 'g', 'h', 'X', 'U', 'V', 'o', 'R', 'k', 'i', 'n', 'W', 'N', 'C', 'G', 'n', 'K', 'H', 'R', 'I', 'B', 'Z', 'q', 'a', 'g', 'O', 'm', 'x', 'Y', 'N', 'v', 'O', 'o', 'V', 'U', 'O', 'K', 'e', 'O', 'V', 'K', 'n', 't', 'm', 'W', 'b', 'j', 't', 'p', 'Z', 's', 'S', 'u', 'g', 'P', 'Z', 'h', 'k', 'F', 't', 'F', 'Y', 'm', 'P', 'o', 'r', 'd', 'K', 'Y', 'h', 'k', 'D', 't', 'u', 'G', 'Q', 'G', 'c', 'l', 'H', 'd', 'g', 'x', 'B', 'B', 'v', 'o', 'm', 'j', 'r', 'Y', 'C', 'y', 't', 'E', 'c', 'F', 'y', 'O', 'J', 's', 'c', 'i', 'a', 'c', 'G', 'E', 'P', 'O', 'R', 'h', 'k', 'K', 'z', 'p', 'T', 'i', 'k', 'M', 'n', 'p', 'l', 'R', 's', 'S', 'N', 'J', 'k', 'x', 'L', 'L', 'v', 'l', 'Z', 'W', 'b', 'N', 'X', 'U', 'u', 'B', 'h', 'f', 'q', 'n', 'w', 'Q', 'W', 'c', 'S', 'n', 'j', 'r', 'Y', 'V', 'a', 'H', 'g', 'W', 's', 'a', 'Y', 'l', 'C', 'N', 'W', 'E', 'O', 'L', 'I', 'a', 'b', 'I', 'L', 'U', 'Z', 's', 'n', 'e', 'R', 'k', 'v', 'S', 'l', 'A', 'A', 'Q', 'X', 'M', 'o', 'r', 'l', 'Q', 'Q', 'O', 'f', 'v', 'q', 'F', 'R', 'e', 'y', 'D', 'B', 'Y', 'k', 'X', 'u', 'd', 'B', 'n', 'H', 'V', 'I', 'u', 'C', 'o', 'y', 's', 'd', 'C', 'R', 'D', 'g', 'I', 'n', 'r', 'B', 'R', 'u', 'c', 'u', 'U', 'a', 'T', 'J', 'Z', 'n', 'd', 'J', 'n', 'H', 'u', 'i', 'V', 'n', 'H', 'S', 'j', 't', 'o', 'n', 'G', 'X', 'D', 'w', 'W', 'E', 'w', 'a', 'd', 'E', 'S', 'q', 'g', 'H', 'h', 'W', 'M', 'I', 'L', 's', 'k', 'Y', 'R', 'a', 'q', 'X', 'I', 'B', 'L', 'c', 'B', 'd', 'Y', 'l', 'f', 'F', 'h', 'H', 't', 'd', 'L', 'o', 'C', 'V', 'l', 'E', 'r', 'Q', 'z', 'O', 'N', 'm', 'Z', 'H', 'I', 'T', 'a', 'o', 'U', 'q', 'b', 'M', 'f', 'P', 'G', 'A', 'C', 'd', 'R', 'A', 'r', 's', 'J', 'X', 'o', 'J', 'K', 'q', 'e', 'A', 'u', 'n', 'w', 'M', 'j', 'W', 'z', 'w', 'U', 's', 'V', 'h', 'k', 'f', 'w', 'W', 'W', 's', 'M', 'b', 'K', 'K', 'j', 'G', 'I', 'n', 'j', 'm', 'y', 'W', 'o', 'm', 'W', 'H', 'U', 'T', 'V', 'd', 'D', 'f', 'd', 'j', 'I', 'E', 'i', 'D', 'A', 'U', 'V', 'G', 'Q', 'q', 'B', 'Q', 'X', 'A', 'R', 'C', 'Z', 'M', 'z', 'u', 'T', 'Z', 'x', 'k', 'f', 'q', 'e', 'y', 'e', 't', 'x', 'G', 'k', 'r', 'L', 'V', 'r', 'x', 'v', 'o', 'h', 'G', 'p', 'p', 'T', 'I', 'a', 'c', 'Y', 'S', 'Q', 'A', 'm', 'Q', 'w', 'r', 'b', 'd', 'r', 'L', 'K', 'q', 'J', 'r', 'H', 'H', 'i', 'K', 'd', 'P', 'Y', 'x', 'x', 'P', 'K', 'w', 'e', 'v', 'u', 'B', 'e', 'w', 'I', 'u', 'g', 'f', 'l', 'Q', 'k', 'E', 'T', 'G', 'U', 'm', 'j', 'e', 'A', 'R', 'l', 'c', 'e', 'u', 'o', 'H', 'k', 'K', 'C', 'S', 't', 'S']

returnFlag = "FLAG{"
for i in range(20):
    returnFlag += jumbledLetters[randomLocations[i]]
returnFlag += "}"

print(returnFlag)