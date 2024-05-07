#ifndef _MARKOV_CHAIN_H
#define _MARKOV_CHAIN_H
#define ALLOC_FAILURE "Allocation failure: memory allocation attempt failed."

#include "linked_list.h"
#include <stdio.h>  // For printf(), sscanf()
#include <stdlib.h> // For exit(), malloc()
#include <stdbool.h> // for bool



/**
 * insert MarkovChain struct
 */

typedef struct MarkovChain{
    LinkedList *database;
} MarkovChain;

typedef struct MarkovNode{
    char *data;
    struct NextNodeCounter *counter_list;
    int num_of_all_sec_words;
    int num_of_optional_words;
    int counter_list_capacity;
} MarkovNode;

typedef struct NextNodeCounter{
    MarkovNode *markov_node;
    int frequency;
} NextNodeCounter;

/**
 * get a random number between 0 and max number [0, max number).
 * @param max_number maximal number to return (not including).
 * @return a random number.
 */
int get_random_number(int max_number);

/**
 * Get one random state from the given markov_chain's database.
 * @param markov_chain
 * @return
 */
MarkovNode* get_first_random_node(MarkovChain *markov_chain);

/**
 * Choose randomly the next state, depend on it's occurrence frequency.
 * @param state_struct_ptr MarkovNode to choose from
 * @return MarkovNode of the chosen state
 */
MarkovNode* get_next_random_node(MarkovNode *state_struct_ptr);

/**
 * Receive markov_chain, generate and print random sentence out of it. The
 * sentence most have at least 2 words in it.
 * @param markov_chain
 * @param first_node markov_node to start with,
 *                   if NULL- choose a random markov_node
 * @param  max_length maximum length of chain to generate
 */
void generate_random_sequence(MarkovChain *markov_chain, MarkovNode *
first_node, int max_length);

/**
 * the function frees linked list and all of it's content from memory
 * @param ptr_linked_list
 */
void free_linked_list(LinkedList ** ptr_linked_list);

/**
 * Free markov_chain and all of it's content from memory
 * @param markov_chain markov_chain to free
 */
void free_markov_chain(MarkovChain ** ptr_chain);

/**
 * Add the second markov_node to the counter list of the first markov_node.
 * If already in list, update it's counter value.
 * @param first_node
 * @param second_node
 * @param markov_chain
 * @return success/failure: true if the process was successful, false if in
 * case of allocation error.
 */
bool add_node_to_counter_list(MarkovNode *first_node, MarkovNode *second_node);

/**
* Check if data_ptr is in database. If so, return the markov_node wrapping
 * it in the markov_chain, otherwise return NULL.
 * @param markov_chain the chain to look in its database
 * @param data_ptr the state to look for
 * @return Pointer to the Node wrapping given state, NULL if state not in
 * database.
 */
Node* get_node_from_database(MarkovChain *markov_chain, char *data_ptr);

/**
* If data_ptr in markov_chain, return it's markov_node. Otherwise, create new
 * markov_node, add to end of markov_chain's database and return it.
 * @param markov_chain the chain to look in its database
 * @param data_ptr the state to look for
 * @return markov_node wrapping given data_ptr in given chain's database,
 * returns NULL in case of memory allocation failure.
 */
Node* add_to_database(MarkovChain *markov_chain, char *data_ptr);

/**
 * the function checks if the data in the MarkoNode ends in '.'- its means
 * its an "end data" its finish the tweet.
 * @param markov_node
 * @return true or false
 */
bool is_last(MarkovNode * markov_node);

#endif /* markovChain_h */
