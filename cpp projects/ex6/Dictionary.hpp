//
// Created by orin levi on 19/09/2022.
//

#ifndef EX6_ORIN_LEVI_DICTIONARY_H
#define EX6_ORIN_LEVI_DICTIONARY_H

#include "HashMap.hpp"

using std::string;

class InvalidKey: public std::invalid_argument{

public:
    InvalidKey(): std::invalid_argument(NO_SUCH_KEY){}
    explicit InvalidKey(const string& error_msg): std::invalid_argument
    (error_msg){}
};

class Dictionary: public HashMap<string, string>{

public:
    typedef std::vector<string> string_vec;
    Dictionary() = default;
    Dictionary(const string_vec &vector_of_keys, const string_vec
    &vector_of_vals): HashMap<string, string>(vector_of_keys,
                                               vector_of_vals){}

    bool erase(const string &key_to_remove) {
        if(!(HashMap::erase(key_to_remove))){
            throw InvalidKey();
        }
        return true;
    }

    template<class IteratorT>
    void update(const IteratorT &begin, const IteratorT &end){
        for(auto i = begin; i != end; i++){
            (*this)[i->first] = i->second;
        }
    }
};

#endif //EX6_ORIN_LEVI_DICTIONARY_H
