//
// Created by orin levi on 19/08/2022.
//
#include "markov_chain.h"

#define FIRST_TIME 1
#define ZERO 0

int get_random_number(int max_number){
    return rand() % max_number;
}

MarkovNode* get_first_random_node(MarkovChain *markov_chain){
    int ind = get_random_number(markov_chain->database->size);
    Node *cur = markov_chain->database->first;
    for(int i = 0; i < ind; i++){
        cur = cur->next;
    }
    return cur->data;
}

MarkovNode* get_next_random_node(MarkovNode *state_struct_ptr){
//    if(!(state_struct_ptr->counter_list)){
//        return NULL;
//    }

    int steps = get_random_number(state_struct_ptr->num_of_all_sec_words);
    const NextNodeCounter *curr = state_struct_ptr->counter_list;
    while (steps >= curr->frequency){
        steps -= curr->frequency;
        curr++;
    }
    return curr->markov_node;
}

void generate_random_sequence(MarkovChain *markov_chain, MarkovNode *
first_node, int max_length){
    if(!first_node){
        bool ok = false;
        while (!ok){
            first_node = get_first_random_node(markov_chain);
            if(!(markov_chain->is_last(first_node->data))){
                ok = true;
            }
        }
    }
    MarkovNode *cur_node = first_node;
    for(int i = 0; i < max_length; i++){
        markov_chain->print_func(cur_node->data);
        if(markov_chain->is_last(cur_node->data)){
            break;
        }
        cur_node = get_next_random_node(cur_node);
    }
}

void free_linked_list(LinkedList ** ptr_linked_list, GenericFunc free_data){
    Node *cur = (*ptr_linked_list)->first;
    while (cur) {
        Node *next_cur = cur->next;
        free_data(cur->data->data);
        free(cur->data->counter_list);
        free(cur->data);
        free(cur);
        cur = next_cur;
    }
    free(*ptr_linked_list);
    *ptr_linked_list = NULL;
}

void free_markov_chain(MarkovChain ** ptr_chain){
    if((*ptr_chain)->database){
        free_linked_list(&((*ptr_chain)->database), (*ptr_chain)->free_data);
    }
    free(*ptr_chain);
    *ptr_chain = NULL;
}

bool add_node_to_counter_list(MarkovNode *first_node, MarkovNode
*second_node, MarkovChain *markov_chain){
    char *new_data = second_node->data;
    bool appears = false;
    for(int i = 0; i < first_node->num_of_optional_words; i++){
        if(markov_chain->comp_func(new_data, (first_node->counter_list[i])
        .markov_node->data)== 0){
            appears = true;
            (first_node->counter_list[i]).frequency++;
            first_node->num_of_all_sec_words++;
            break;
        }
    }
    if(!appears){
        if(first_node->counter_list_capacity ==
           first_node->num_of_optional_words){
            NextNodeCounter *new_counter_list = realloc
                    (first_node->counter_list, sizeof(NextNodeCounter) *
                    (first_node->counter_list_capacity + 1));
            if (!new_counter_list){
                printf(ALLOCATION_ERROR_MASSAGE);
                return false;
            }
            first_node->counter_list = new_counter_list;
            first_node->counter_list_capacity += 1;
        }
        (first_node->counter_list[first_node->num_of_optional_words
        ]).markov_node = second_node;
        (first_node->counter_list[first_node->num_of_optional_words
        ]).frequency = FIRST_TIME;
        first_node->num_of_optional_words += 1;
        first_node->num_of_all_sec_words += 1;
    }
    return true;
}

Node* get_node_from_database(MarkovChain *markov_chain, void *data_ptr){
    if(markov_chain->database->first){
        Node *cur = markov_chain->database->first;
        while (cur){
            if(markov_chain->comp_func(cur->data->data, data_ptr) == 0){
                return cur;
            }
            cur = cur->next;
        }
    }
    return NULL;
}

Node* add_to_database(MarkovChain *markov_chain, void *data_ptr){
    Node *exit_node = get_node_from_database(markov_chain, data_ptr);
    if(exit_node){
        return exit_node;
    }
    Node *new_node = malloc(sizeof(Node));
    if(!new_node){
        printf(ALLOCATION_ERROR_MASSAGE);
        return NULL;
    }
    MarkovNode *new_markov_node = malloc(sizeof(MarkovNode));
    if(!new_markov_node){
        free(new_node);
        printf(ALLOCATION_ERROR_MASSAGE);
        return NULL;
    }

    void *data = markov_chain->copy_func(data_ptr);
    if(!data){
        free(new_node);
        free(new_markov_node);
        printf(ALLOCATION_ERROR_MASSAGE);
        return NULL;
    }

    new_markov_node->data = data;
    new_markov_node->counter_list = NULL;
    new_markov_node->counter_list_capacity = ZERO;
    new_markov_node->num_of_all_sec_words = ZERO;
    new_markov_node->num_of_optional_words = ZERO;
    new_node->data = new_markov_node;
    new_node->next = NULL;
    if(markov_chain->database->first){
        markov_chain->database->last->next = new_node;
        markov_chain->database->last = new_node;
    }
    else{
        markov_chain->database->first = markov_chain->database->last =
                new_node;
    }
    markov_chain->database->size += 1;
    return new_node;
}