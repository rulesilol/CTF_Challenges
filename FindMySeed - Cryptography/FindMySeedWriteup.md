**Solution Writeup**\
Reference the FindMySeed.py file\
For this problem, we mainly use Z3. As we can see in the Python script, we first recreate 
the PRNG generator in the function *myprng*. Note the '& 0xFFFFFFFF' after every calculation.
This ensures that only 32-bit numbers are used. Then we initialize the BitVecs using 32 bits and 
set the next random numbers (*xrand*) and next seeds (*state*) to the previous seed. Next is 
setting the random numbers generated to the ones given in the problem statement. Finally we 
solve for these random numbers. Note that the initial seeds that Z3 generates is not unique. 
However, they will still work.\
Now that we know the initial seeds, we move on to writing the decryption function. The encryption
function takes one character from the plaintext and a randomly generated number. It then XORs the 
decimal representation of that character and the last three digits of the randomly generated number, adding "0"
padding to the front to ensure the length of the return string is 3 digit number.\
To decrypt the ciphertext, we just to the opposite. We take the first three digits in the ciphertext
and XOR it with the randomly generated number. Then we return the ASCII character of that number. We continue
this through the ciphertext, giving us the flag.