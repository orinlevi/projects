#include "cipher.h"

#define NUM_OF_LETTERS_IN_THE_ABC 26
#define UPPER_A_ASCII 65
#define UPPER_Z_ASCII 90
#define LOWER_A_ASCII 97
#define LOWER_Z_ASCII 122


/// IN THIS FILE, IMPLEMENT EVERY FUNCTION THAT'S DECLARED IN cipher.h.

//the function encode/decode (change the given char) a single lower case char
// according to the given "net_to_move" argument.
char move_lower_case(int c, int net_to_move);
//the function encode/decode (change the given char) a single upper case char
// according to the given "net_to_move" argument.
char move_upper_case(int c, int net_to_move);
//the function return the modulo of the given k by
// "NUM_OF_LETTERS_IN_THE_ABC" (26).
int find_net_to_move(int k);


int find_net_to_move(int k){
    int net_to_move = k;
    if(k<0){
        net_to_move *= -1;
    }
    net_to_move %= NUM_OF_LETTERS_IN_THE_ABC;
    if(k<0){
        net_to_move *= -1;
    }
    return net_to_move;
}


char move_lower_case(int c, int net_to_move){
    char new_char = (char) c;
    int dest = c + net_to_move;
    if(LOWER_A_ASCII<= dest && dest<= LOWER_Z_ASCII) {
        new_char = (char) dest;
    }
    if(dest < LOWER_A_ASCII){
        new_char = (char) (dest + NUM_OF_LETTERS_IN_THE_ABC);
    }
    if(LOWER_Z_ASCII < dest){
        new_char = (char) (dest - NUM_OF_LETTERS_IN_THE_ABC);
    }
    return new_char;
}


char move_upper_case(int c, int net_to_move){
    char new_char = (char) c;
    int dest = c + net_to_move;
    if(UPPER_A_ASCII<= dest && dest<= UPPER_Z_ASCII) {
        new_char = (char) dest;
    }
    if(dest < UPPER_A_ASCII){
        new_char = (char) (dest + NUM_OF_LETTERS_IN_THE_ABC);
    }
    if(UPPER_Z_ASCII < dest){
        new_char = (char) (dest - NUM_OF_LETTERS_IN_THE_ABC);
    }
    return new_char;
}


// See full documentation in header file
void encode (char s[], int k)
{
    int net_to_move = find_net_to_move(k);

    for(int i = 0; s[i] != '\0'; i++){
        if(LOWER_A_ASCII <= (int) s[i] && (int) s[i] <= LOWER_Z_ASCII){
            s[i] = move_lower_case(s[i], net_to_move);
        }
        if(UPPER_A_ASCII <= (int) s[i] && (int) s[i]<= UPPER_Z_ASCII){
            s[i] = move_upper_case(s[i], net_to_move);
        }
    }
}

// See full documentation in header file
void decode (char s[], int k)
{
    encode (s, -k);
}
