prog: tweets_generator.o markov_chain.o linked_list.o
	gcc markov_chain.o tweets_generator.o -o tweets_generator

tweets_generator.o: markov_chain.h tweets_generator.c
	gcc -Wall -Wextra -Wvla -std=c99 -c tweets_generator.c

markov_chain.o: markov_chain.h markov_chain.c
	gcc -Wall -Wextra -Wvla -std=c99 -c markov_chain.c

linked_list.o: linked_list.c linked_list.h
	gcc -Wall -Wextra -Wvla -std=c99 -c linked_list.c

