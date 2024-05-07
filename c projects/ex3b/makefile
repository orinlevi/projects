tweets: tweets_generator.o markov_chain.o linked_list.o
	gcc  markov_chain.o tweets_generator.o linked_list.o -o tweets_generator

snake: snakes_and_ladders.o markov_chain.o linked_list.o
	gcc markov_chain.o snakes_and_ladders.o linked_list.o -o snakes_and_ladders

tweets_generator.o: tweets_generator.c
	gcc -Wall -Wextra -Wvla -std=c99 -c tweets_generator.c

snakes_and_ladders.o: snakes_and_ladders.c
	gcc -Wall -Wextra -Wvla -std=c99 -c snakes_and_ladders.c

markov_chain.o: markov_chain.h markov_chain.c
	gcc -Wall -Wextra -Wvla -std=c99 -c markov_chain.c

linked_list.o: linked_list.c linked_list.h
	gcc -Wall -Wextra -Wvla -std=c99 -c linked_list.c

clean:
	rm -f *.o