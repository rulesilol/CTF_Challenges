#include<iostream>
#include <tuple>
#include<string>
#include<cmath>

// #include <bits/stdc++.h>

class LittlePRNG {
    private:
        int seedA, seedB, seedC;
        std::tuple<int, int, int, int> myprng(int seedA, int seedB, int seedC) {
        
            int a = (seedA << 13) * 11;
            // std::cout << "a is " << a << std::endl;
            int b = (seedB >> 12) ^ (seedC << 22) + 852145;
            // std::cout << "b is " << b << std::endl;
            int c = (seedA << 3 | seedC >> 18);
            // std::cout << "c is " << c << std::endl;
            int randomNumber  = ((a ^ b) * 7 ) ^ c;
            // std::cout << "r is " << r << std::endl;

            seedA = b ^ c;
            seedB = a ^ c;
            seedC = a ^ b;

            return {randomNumber, seedA, seedB, seedC};
        };
    
    public:
        void setSeed(int A, int B, int C) {
            seedA = A, seedB = B, seedC = C;
        }

        int next() {
            auto [randomNumber, nextSeedA, nextSeedB, nextSeedC] = myprng(seedA, seedB, seedC);
            seedA = nextSeedA;
            seedB = nextSeedB;
            seedC = nextSeedC;

            return randomNumber;
        }
};
    
char decryptor(std::string encryptedChar, int key) {
    char decodedChar;
    key = std::abs(key);

    decodedChar = std::stoi(encryptedChar) ^ (key % 1000);
    return decodedChar;
};


int main() {
    LittlePRNG my_prng;
    my_prng.setSeed(811878287, 502635199, 1723710779);
    // std::string plaintext = "The flag is FLAG{Dont_Roll_Your_Own_Crypto}";
    std::string encryptedText = "915066730242344700629617451930536631439876192487610047514988717581037147488731737653619857039798455381397973353253753096668315063";
    std::string plaintext;
    for (int i = 0; i < encryptedText.length(); i += 3) {
        plaintext += decryptor(encryptedText.substr(i, 3), my_prng.next());

    };
    std::cout << plaintext;
    return 0;
};