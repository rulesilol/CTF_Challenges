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
            int c = ((seedA << 3 | seedC >> 18));
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
    
// char decryptor(int encryptedChar, int key) {

// };


int main() {
    LittlePRNG my_prng;
    my_prng.setSeed(811878287, 502635199, 1723710779);
    std::string plaintext = "The flag is FLAG{Dont_Roll_Your_Own_Crypto}";
    std::string ciphertext = "";
    int key;

    for (int i = 0; i < plaintext.length(); i++) {
        key = my_prng.next();
        std::cout << key <<'\n';
        ciphertext += encryptor(plaintext[i], key); 
    };
    std::cout << ciphertext;


    return 0;
}