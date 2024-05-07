#include "cipher.h"
#include "tests.h"
#include "stdio.h"
#include "string.h"
#include "stdlib.h"

#define NUM_OF_ARGS_FOR_ENCODE_PLUS_DEFAULT_ARG 5
#define NUM_OF_ARGS_FOR_TESTING_PLUS_DEFAULT_ARG 2
#define PLACE_OF_COMMAND 1
#define PLACE_OF_K 2
#define PLACE_OF_INPUT_FILE 3
#define PLACE_OF_OUTPUT_FILE 4
#define TEST_COMMAND "test"
#define ENCODE_COMMAND "encode"
#define DECODE_COMMAND "decode"
//size of buffer according to the max length of line in the input file + 2
// for the '\0' and '\n' signs
#define SIZE_OF_BUFFER 1026
#define DECIMAL 10
#define NUM_10 10

//the function checks the length of the num including '-' sign
int len(long num);
//the function runs the test (the functions) in the test.c file and checks
// if all of them returns 0 (EXIT_SUCCESS).
int test();
//the function checks if all the arguments that received from the user are
// valid.
int test_of_args(int argc, char *argv[]);
//the function encode or decode (according to the user choice-given argument)
// the input file content and write it into the output file.
void encode_and_decode(int k, char *argv[]);


int test(){
    if(test_encode_non_cyclic_lower_case_positive_k ()){
        return 1;
    }
    if(test_encode_cyclic_lower_case_special_char_positive_k ()){
        return 1;
    }
    if(test_encode_non_cyclic_lower_case_special_char_negative_k ()){
        return 1;
    }
    if(test_encode_cyclic_lower_case_negative_k ()){
        return 1;
    }
    if(test_encode_cyclic_upper_case_positive_k ()){
        return 1;
    }
    if(test_decode_non_cyclic_lower_case_positive_k ()){
        return 1;
    }
    if(test_decode_cyclic_lower_case_special_char_positive_k ()){
        return 1;
    }
    if(test_decode_non_cyclic_lower_case_special_char_negative_k ()){
        return 1;
    }
    if(test_decode_cyclic_lower_case_negative_k ()){
        return 1;
    }
    if(test_decode_cyclic_upper_case_positive_k ()){
        return 1;
    }
    return 0;

}


int len(long num){
    int len = 0;
    if(num == 0){
        return 1;
    }
    if(num < 0){
        len += 1;
        num *= -1;
    }
    while(num>0){
        num = (long) num / NUM_10;
        len += 1;
    }
    return len;
}


int test_of_args(int argc, char *argv[]){
    if(argc != NUM_OF_ARGS_FOR_ENCODE_PLUS_DEFAULT_ARG && argc !=
    NUM_OF_ARGS_FOR_TESTING_PLUS_DEFAULT_ARG){
        fprintf(stderr, "The program receives 1 or 4 arguments only.\n");
        return 1;
    }
    if(argc == NUM_OF_ARGS_FOR_TESTING_PLUS_DEFAULT_ARG){
        if(strcmp(argv[PLACE_OF_COMMAND], TEST_COMMAND) != 0){
            fprintf(stderr, "Usage: cipher test\n");
            return 1;
        }
    }
    if(argc == NUM_OF_ARGS_FOR_ENCODE_PLUS_DEFAULT_ARG){
        if(strcmp(argv[PLACE_OF_COMMAND], ENCODE_COMMAND) != 0 && strcmp
        (argv[PLACE_OF_COMMAND], DECODE_COMMAND) != 0){
            fprintf(stderr, "The given command is invalid.\n");
            return 1;
        }
        long k_long = strtol(argv[PLACE_OF_K], NULL, DECIMAL);
        if(len(k_long) != (int) strlen(argv[PLACE_OF_K])){
            fprintf(stderr, "The given shift value is invalid.\n");
            return 1;
        }
        FILE *input_file = fopen(argv[PLACE_OF_INPUT_FILE], "r");
        if(input_file == NULL){
            fprintf(stderr, "The given file is invalid.\n");
            fprintf(stderr, "%s", argv[PLACE_OF_INPUT_FILE]);
            return 1;
        }
        fclose(input_file);
        FILE *output_file = fopen(argv[PLACE_OF_OUTPUT_FILE], "w");
        if(output_file == NULL){
            fprintf(stderr, "The given file is invalid.\n");
            fprintf(stderr, "%s", argv[PLACE_OF_OUTPUT_FILE]);
            return 1;
        }
        fclose(output_file);
    }
    return 0;
}


void encode_and_decode(int k, char *argv[]){
    FILE *input_file = fopen(argv[PLACE_OF_INPUT_FILE], "r");
    FILE *output_file = fopen(argv[PLACE_OF_OUTPUT_FILE], "w");
    char buffer[SIZE_OF_BUFFER];
    while(fgets(buffer, SIZE_OF_BUFFER, input_file) != NULL){
        if (strcmp(argv[PLACE_OF_COMMAND], ENCODE_COMMAND) == 0){
            encode(buffer, k);
        }
        if (strcmp(argv[PLACE_OF_COMMAND], DECODE_COMMAND) == 0){
            decode(buffer, k);
        }
        fprintf(output_file, "%s", buffer);
    }
    fclose(input_file);
    fclose(output_file);
}



int main (int argc, char *argv[]){
    if(test_of_args(argc, argv)){
        return EXIT_FAILURE;
    }
    if(strcmp(argv[PLACE_OF_COMMAND], TEST_COMMAND) == 0){
        if(test()){
            return EXIT_FAILURE;
        }
    }
    else{
        long k_long = strtol(argv[PLACE_OF_K], NULL, DECIMAL);
        int k = (int) k_long;
        encode_and_decode(k, argv);
    }
    return EXIT_SUCCESS;
}