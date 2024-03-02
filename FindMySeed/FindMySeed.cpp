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
            int b = (seedB >> 12) ^ (seedC << 22) + 852145;
            int c = ((seedA << 3 | seedC >> 18));
            int randomNumber  = ((a ^ b) * 7 ) ^ c;

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

std::string encryptor(char character, int key) {
    std::string encodedString;
    key = std::abs(key);
    encodedString += std::to_string(int(character) ^ (key % 1000));

    if (encodedString.length() == 2) {
        encodedString.insert(0, "0");
    } else if (encodedString.length() == 1) {
        encodedString.insert(0, "00");
    };
    return encodedString;
};


int main() {
    LittlePRNG my_prng;

    my_prng.setSeed(X, Y, Z);
    std::string plaintext = "XXX XXXX XX XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX";
    
    int key;

    for (int i = 0; i < plaintext.length(); i++) {
        key = my_prng.next();
        std::cout << '\n' << key <<'\n';
        std::cout << encryptor(plaintext[i], key); 
    };


    return 0;
}