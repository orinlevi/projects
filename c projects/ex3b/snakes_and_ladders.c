#include <string.h> // For strlen(), strcmp(), strcpy()
#include "markov_chain.h"

#define MAX(X, Y) (((X) < (Y)) ? (Y) : (X))

#define EMPTY -1
#define BOARD_SIZE 100
#define LAST_CELL 100
#define MAX_GENERATION_LENGTH 60

#define DICE_MAX 6
#define NUM_OF_TRANSITIONS 20

#define VALID_ARGS_NUM 3
#define SEED_IND 1
#define NUM_OF_SENTENCES_IND 2
#define INVALID_NUM_OF_ARGS_MSG "Usage: seed, num_of_sentences"
#define ZERO 0
#define DECIMAL 10

/**
 * represents the transitions by ladders and snakes in the game
 * each tuple (x,y) represents a ladder from x to if x<y or a snake otherwise
 */
const int transitions[][2] = {{13, 4},
                              {85, 17},
                              {95, 67},
                              {97, 58},
                              {66, 89},
                              {87, 31},
                              {57, 83},
                              {91, 25},
                              {28, 50},
                              {35, 11},
                              {8,  30},
                              {41, 62},
                              {81, 43},
                              {69, 32},
                              {20, 39},
                              {33, 70},
                              {79, 99},
                              {23, 76},
                              {15, 47},
                              {61, 14}};

/**
 * struct represents a Cell in the game board
 */
typedef struct Cell {
    int number; // Cell number 1-100
    int ladder_to;  // ladder_to represents the jump of the ladder in case
    // there is one from this square
    int snake_to;  // snake_to represents the jump of the snake in case
    // there is one from this square
    //both ladder_to and snake_to should be -1 if the Cell doesn't have them
} Cell;

static bool snakes_and_ladders_is_last(void * object){
    Cell *cell = (Cell *) object;
    if(cell->number == LAST_CELL){
        return true;
    }
    return false;
}

static void snakes_and_ladders_print_data(void *data){
    Cell *cell = (Cell *) data;
    if(snakes_and_ladders_is_last(cell)){
        printf("[%d]", cell->number);
        return;
    }
    if(cell->ladder_to == EMPTY && cell->snake_to == EMPTY){
        printf("[%d] -> ", cell->number);
    }
    else{
        if(cell->ladder_to != EMPTY){
            printf("[%d]-ladder to %d -> ", cell->number, cell->ladder_to);
        } else{
            printf("[%d]-snake to %d -> ", cell->number, cell->snake_to);
        }
    }
}

static void snakes_and_ladders_free_data(void *data){
    free(data);
}

static int snakes_and_ladders_is_even(void *a, void* b){
    Cell *first_data = a;
    Cell *second_data = b;
    if((second_data->number == first_data->number) &&
    (second_data->ladder_to == first_data->ladder_to) &&
    (second_data->snake_to == first_data->snake_to)){
        return 0;
    }
    if(second_data->number < first_data->number){
        return 1;
    }
    else{
        return -1;
    }
}

static void* snakes_and_ladders_copy_func(void *data){
    Cell *data_to_copy = data;
    Cell *new_data = malloc(sizeof(Cell));
    new_data->number = data_to_copy->number;
    new_data->ladder_to = data_to_copy->ladder_to;
    new_data->snake_to = data_to_copy->snake_to;
    return new_data;
}

/** Error handler **/
static int handle_error(char *error_msg, MarkovChain **database)
{
    printf("%s", error_msg);
    if (database != NULL)
    {
        free_markov_chain(database);
    }
    return EXIT_FAILURE;
}


static int create_board(Cell *cells[BOARD_SIZE])
{
    for (int i = 0; i < BOARD_SIZE; i++)
    {
        cells[i] = malloc(sizeof(Cell));
        if (cells[i] == NULL)
        {
            for (int j = 0; j < i; j++) {
                free(cells[j]);
            }
            handle_error(ALLOCATION_ERROR_MASSAGE,NULL);
            return EXIT_FAILURE;
        }
        *(cells[i]) = (Cell) {i + 1, EMPTY, EMPTY};
    }

    for (int i = 0; i < NUM_OF_TRANSITIONS; i++)
    {
        int from = transitions[i][0];
        int to = transitions[i][1];
        if (from < to)
        {
            cells[from - 1]->ladder_to = to;
        }
        else
        {
            cells[from - 1]->snake_to = to;
        }
    }
    return EXIT_SUCCESS;
}

/**
 * fills database
 * @param markov_chain
 * @return EXIT_SUCCESS or EXIT_FAILURE
 */
static int fill_database(MarkovChain *markov_chain)
{
    Cell* cells[BOARD_SIZE];
    if(create_board(cells) == EXIT_FAILURE)
    {
        return EXIT_FAILURE;
    }
    MarkovNode *from_node = NULL, *to_node = NULL;
    size_t index_to;
    for (size_t i = 0; i < BOARD_SIZE; i++)
    {
        add_to_database(markov_chain, cells[i]);
    }

    for (size_t i = 0; i < BOARD_SIZE; i++)
    {
        from_node = get_node_from_database(markov_chain,cells[i])->data;

        if (cells[i]->snake_to != EMPTY || cells[i]->ladder_to != EMPTY)
        {
            index_to = MAX(cells[i]->snake_to,cells[i]->ladder_to) - 1;
            to_node = get_node_from_database(markov_chain, cells[index_to])
                    ->data;
            add_node_to_counter_list(from_node, to_node, markov_chain);
        }
        else
        {
            for (int j = 1; j <= DICE_MAX; j++)
            {
                index_to = ((Cell*) (from_node->data))->number + j - 1;
                if (index_to >= BOARD_SIZE)
                {
                    break;
                }
                to_node = get_node_from_database(markov_chain, cells[index_to])
                        ->data;
                add_node_to_counter_list(from_node, to_node, markov_chain);
            }
        }
    }
    // free temp arr
    for (size_t i = 0; i < BOARD_SIZE; i++)
    {
        free(cells[i]);
    }
    return EXIT_SUCCESS;
}

static int sentences_maker(char *argv[]){
    LinkedList *linked_list = malloc(sizeof(LinkedList));
    if(!linked_list){
        return EXIT_FAILURE;
    }

    MarkovChain *markov_chain = malloc(sizeof(MarkovChain));
    if(!markov_chain){
        free(linked_list);
        return EXIT_FAILURE;
    }

    linked_list->first = linked_list->last = NULL;
    linked_list->size = ZERO;
    markov_chain->database = linked_list;
    markov_chain->is_last = &snakes_and_ladders_is_last;
    markov_chain->copy_func = &snakes_and_ladders_copy_func;
    markov_chain->comp_func = &snakes_and_ladders_is_even;
    markov_chain->free_data = &snakes_and_ladders_free_data;
    markov_chain->print_func = &snakes_and_ladders_print_data;

    if(fill_database(markov_chain)) {
        free_markov_chain(&markov_chain);
        return EXIT_FAILURE;
    }

    unsigned long num_of_sentences = strtol(argv[NUM_OF_SENTENCES_IND], NULL,
                                            DECIMAL);
    for(unsigned long i = 1; i <= num_of_sentences; i++){
        printf("Random Walk %lu: ", i);
        generate_random_sequence(markov_chain,
                                 markov_chain->database->first->data,
                                 MAX_GENERATION_LENGTH);
        printf("\n");
    }
    free_markov_chain(&markov_chain);
    return EXIT_SUCCESS;
}

/**
 * the function checks if the given args are valid
 * @param argc
 * @param argv
 * @return exit_success or exit_failure
 */
static int test_of_args(int argc){
    if(argc != VALID_ARGS_NUM) {
        printf(INVALID_NUM_OF_ARGS_MSG);
        return EXIT_FAILURE;
    }
    return EXIT_SUCCESS;
}

/**
 * @param argc num of arguments
 * @param argv 1) Seed
 *             2) Number of sentences to generate
 * @return EXIT_SUCCESS or EXIT_FAILURE
 */
int main(int argc, char *argv[])
{
    if(test_of_args(argc)){
        return EXIT_FAILURE;
    }

    long seed_long = strtol(argv[SEED_IND], NULL, DECIMAL);
    unsigned int seed = (unsigned int) seed_long;
    srand(seed);

    if(sentences_maker(argv)){
        return EXIT_FAILURE;
    }

    return EXIT_SUCCESS;
}
