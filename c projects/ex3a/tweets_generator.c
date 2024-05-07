//
// Created by orin levi on 19/08/2022.
//
#include "markov_chain.h"
#include <string.h>

#define SEED_IND 1
#define NUM_OF_TWEETS_IND 2
#define PATH_IND 3
#define NUM_OF_WORDS_FROM_FILE_IND 4
#define VALID_MAX_ARGS 5
#define VALID_MIN_ARGS 4
#define MAX_NUM_FOR_TWEET 20
#define SIZE_OF_BUFFER 1002
#define DECIMAL 10
#define ZERO 0
#define DELIMITERS " \n"
#define INVALID_NUM_OF_ARGS_MSG "Usage: seed, num_of_tweets, num_of_words, \
num_of_words_to_read_from_file (not mendatory) "
#define INVALID_PATH "Error: The given file is invalid.\n"

static void fill_database(FILE *pt, int word_to_read, MarkovChain
*markov_chain){
    bool loop_continue = false;
    if(word_to_read == 0){
        loop_continue = true;
    }

    char buffer[SIZE_OF_BUFFER];
    while(fgets(buffer, SIZE_OF_BUFFER, pt) != NULL && (word_to_read > 0 ||
    loop_continue)){
        Node *prev_node = NULL;
        char *token = strtok (buffer, DELIMITERS);
        while (token && (word_to_read > 0 || loop_continue)){
            Node *cur_node = add_to_database(markov_chain, token);
            if(!cur_node){
                free_linked_list(&(markov_chain->database));
                return;
            }
            if(prev_node){
               bool ok = add_node_to_counter_list(prev_node->data,
                                               cur_node->data);
               if(!ok){
                   free_linked_list(&(markov_chain->database));
                   return;
               }
            }
            if(!is_last(cur_node->data)){
                prev_node = cur_node;
            }
            else{
                prev_node = NULL;
            }
            token = strtok (NULL, DELIMITERS);
            if(!loop_continue){
                word_to_read -= 1;
            }
        }
    }
    return;
}

static int test_of_args(int argc, char *argv[]){
    if(argc != VALID_MAX_ARGS && argc != VALID_MIN_ARGS) {
        printf(INVALID_NUM_OF_ARGS_MSG);
        return EXIT_FAILURE;
    }
    FILE *text_corpus = fopen(argv[PATH_IND], "r");
    if(text_corpus == NULL) {
        printf(INVALID_PATH);
        return EXIT_FAILURE;
    }
    fclose(text_corpus);
    return EXIT_SUCCESS;
}

static int tweets_maker(int argc, char *argv[]){
    unsigned long num_of_tweets = strtol(argv[NUM_OF_TWEETS_IND], NULL,
                                         DECIMAL);

    unsigned long num_of_words_from_file = 0;
    if(argc == VALID_MAX_ARGS){
        num_of_words_from_file = strtol(argv[NUM_OF_WORDS_FROM_FILE_IND],
                                        NULL, DECIMAL);
    }

    MarkovChain *markov_chain = malloc(sizeof(MarkovChain));
    if(!markov_chain){
        printf(ALLOC_FAILURE);
        return EXIT_FAILURE;
    }

    LinkedList *linked_List = malloc(sizeof(LinkedList));
    if(!linked_List){
        free(markov_chain);
        printf(ALLOC_FAILURE);
        return EXIT_FAILURE;
    }
    linked_List->first = linked_List->last = NULL;
    linked_List->size = ZERO;
    markov_chain->database = linked_List;

    FILE *text_corpus = fopen(argv[PATH_IND], "r");

    fill_database(text_corpus, (int)num_of_words_from_file, markov_chain);
    fclose(text_corpus);
    if(markov_chain->database == NULL){
        free_markov_chain(&markov_chain);
        return EXIT_FAILURE;
    }

    for(unsigned long i = 0; i < num_of_tweets; i++){
        printf("tweet %lu: ", i);
        generate_random_sequence(markov_chain, NULL, MAX_NUM_FOR_TWEET);
        printf("\n");
    }
    free_markov_chain(&markov_chain);
    return EXIT_SUCCESS;
}

int main (int argc, char *argv[]){
    if(test_of_args(argc, argv)){
        return EXIT_FAILURE;
    }

    long seed_long = strtol(argv[SEED_IND], NULL, DECIMAL);
    unsigned int seed = (unsigned int) seed_long;
    srand(seed);

    if(tweets_maker(argc, argv)){
        return EXIT_FAILURE;
    }

    return EXIT_SUCCESS;
}