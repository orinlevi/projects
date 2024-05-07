//
// Created by orin levi on 19/09/2022.
//

#ifndef EX6_ORIN_LEVI_HASHMAP_H
#define EX6_ORIN_LEVI_HASHMAP_H

#define INITIAL_CAPACITY 16
#define INITIAL_SIZE 0

#define LOWER_LOAD_FACTOR 0.25
#define UPPER_LOAD_FACTOR 0.75

#define UNEQUAL_VEC_SIZES "ERROR: the vectors of keys and vals must be the \
same length"

#define NO_SUCH_KEY "there is no such key is this map"

#define UPPER_LOAD_FACTOR 0.75

#include <iostream>
#include <vector>

template<class KeyT, class ValueT>
class HashMap{

public:
    typedef std::vector<KeyT> keys_vec;
    typedef std::vector<ValueT> vals_vec;
    typedef std::vector<std::pair<KeyT, ValueT>> bucket;
    typedef std::pair<KeyT, ValueT> pair_in_bucket;

    HashMap(): _capacity(INITIAL_CAPACITY), _size(INITIAL_SIZE), _map(new
    bucket[INITIAL_CAPACITY]){}

    HashMap(keys_vec vector_of_keys, vals_vec vector_of_vals) noexcept(false):
    _capacity(INITIAL_CAPACITY), _size(INITIAL_SIZE){
        if(vector_of_vals.size() != vector_of_keys.size()){
            throw std::invalid_argument(UNEQUAL_VEC_SIZES);
        }
        _map = new bucket[INITIAL_CAPACITY];
        for(int i = 0; i < (int) vector_of_keys.size(); i++){
            (*this)[vector_of_keys[i]] = vector_of_vals[i];
        }
    }

    HashMap(const HashMap &hash_map): _capacity(hash_map._capacity), _size
    (hash_map._size), _map(new bucket[hash_map._capacity]){
        for(int i = 0; i < _capacity; i++){
            _map[i] = hash_map._map[i];
        }
    }

    virtual ~HashMap(){
        delete[] _map;
    }

//    int hash_func(const KeyT key_to_hash) const{
//        return ((std::hash<KeyT>()(key_to_hash) % (_capacity)) + _capacity)
//        % _capacity;
//    }
    int hash_func(const KeyT key_to_hash) const{
        return (std::hash<KeyT>()(key_to_hash) & (_capacity - 1));
    }

    int hash_func(const KeyT key_to_hash, int mult) const{
        return (std::hash<KeyT>()(key_to_hash) & ((mult * _capacity) - 1));
    }

    int size() const{return _size;}
    int capacity() const{return _capacity;}
    bool empty() const{ return (_size == 0);}

    bool insert(KeyT key_to_add, ValueT val_to_add){
        try{
            at(key_to_add);
        }
        catch(std::runtime_error &error) {
            _size++;

            if( get_load_factor() > UPPER_LOAD_FACTOR){
                bucket *new_map = new bucket[2 * _capacity];

                for(const_iterator pair_iter = begin(); pair_iter != end();
                pair_iter++){
                    new_map[hash_func(pair_iter->first, 2)].push_back
                    (*pair_iter);
                }
                delete[] _map;
                _map = new_map;
                _capacity *= 2;
            }
            _map[hash_func(key_to_add)].push_back(std::pair<KeyT, ValueT>
            (key_to_add, val_to_add));
            return true;
        }
        return false;
    }

    bool contains_key(const KeyT &key_to_find) const{
        for(auto const &pair: _map[hash_func(key_to_find)]){
            if(key_to_find == pair.first){
                return true;
            }
        }
        return false;
    }

    ValueT at(const KeyT &key_to_get_his_val) const noexcept(false){
        for(const auto &pair: _map[hash_func(key_to_get_his_val)]){
            if(key_to_get_his_val == pair.first){
                return pair.second;
            }
        }
        throw std::runtime_error(NO_SUCH_KEY);
    }

    ValueT& at(const KeyT &key_to_get_his_val) noexcept(false){
        for(auto &pair: _map[hash_func(key_to_get_his_val)]){
            if(key_to_get_his_val == pair.first){
                return pair.second;
            }
        }
        throw std::runtime_error(NO_SUCH_KEY);
    }

    virtual bool erase(KeyT key_to_remove){
        try {
            at(key_to_remove);
            bucket bucket_of_pairs = _map[bucket_index(key_to_remove)];
            _size--;
            for (auto pair_to_rm_iter = bucket_of_pairs.begin();
            pair_to_rm_iter != bucket_of_pairs.end(); pair_to_rm_iter++) {
                if ((*pair_to_rm_iter).first == key_to_remove) {
                    bucket_of_pairs.erase(pair_to_rm_iter);
                    break;
                }
            }

            if (get_load_factor() < LOWER_LOAD_FACTOR) {
                bucket *new_map = new bucket[(_capacity / 2)];

                for(const_iterator pair_iter = begin(); pair_iter != end();
                     pair_iter++) {
                    new_map[hash_func((*pair_iter).first, (1/2))].push_back
                    (*pair_iter);
                }

                delete[] _map;
                _map = new_map;
                _capacity /= 2;
            }
        }
        catch(std::runtime_error &error) { return false; }
        return true;
    }

    double get_load_factor(){return ((double)_size/_capacity);}

    int bucket_size(KeyT key_to_find_his_bucket_size){
        if(contains_key(key_to_find_his_bucket_size)){
            return (_map[hash_func(key_to_find_his_bucket_size)].size());
        }
        throw std::invalid_argument(NO_SUCH_KEY);
    }
    int bucket_index(KeyT key_to_find_his_bucket_index){
        if(contains_key((key_to_find_his_bucket_index))){
            return hash_func(key_to_find_his_bucket_index);
        }
        throw std::invalid_argument(NO_SUCH_KEY);
    }

    void clear(){
        bucket * temp = new bucket[_capacity];
        delete[] _map;
        _map = temp;
        _size = 0;
    }

    HashMap &operator=(const HashMap& map_to_copy){
        if(&map_to_copy == this){
            return *this;
        }
        bucket *temp = new bucket [map_to_copy._capacity];
        delete[] _map;
        _map = temp;
        _capacity = map_to_copy._capacity;
        _size = map_to_copy._size;
        for(int i = 0; i < _capacity; i++){
            _map[i] = map_to_copy[i];
        }
        return *this;
    }

    ValueT &operator[](const KeyT &key){
        try{
            ValueT &val = at(key);
            return val;
        }
        catch(std::runtime_error &error){
            insert(key, ValueT());
            return at(key);

        }
    }

    ValueT operator[](const KeyT &key) const{
        ValueT val = ValueT();
        try{
            val = at(key);
        }
        catch(std::runtime_error &error){
            return val;

        }
        return val;
    }

    bool operator==(const HashMap &rhs) const{
        // compares maps' size
        if(_capacity != rhs._capacity || _size != rhs._size){
            return false;
        }
        // compares buckets' size
        for(int i = 0; i < _capacity; i++){
            if(_map[i].size() != rhs._map[i].size()) {
                return false;
            }
            // compares buckets' content
            for(int j = 0; j < (int) _map[i].size(); j++){
                if(_map[i][j].first != rhs._map[i][j].first || _map[i][j]
                .second != rhs._map[i][j].second){
                    return false;
                }
            }
        }

        return true;
    }

    bool operator !=(const HashMap &rhs) const{
        return !operator==(rhs);
    }

    class ConstIterator {

    public:

        typedef pair_in_bucket value_type;
        typedef const pair_in_bucket &reference;
        typedef const pair_in_bucket *pointer;
        typedef std::ptrdiff_t difference_type;
        typedef std::forward_iterator_tag iterator_category;

        ConstIterator(const HashMap *hash_map, int bucket_ind, int
        pair_ind) : _hash_map(hash_map), _bucket_ind(bucket_ind), _pair_ind
        (pair_ind) {}

        ConstIterator(const ConstIterator &rhs) = default;

        ConstIterator& operator++() {
            _pair_ind++;
            if((int)_hash_map->_map[_bucket_ind].size() > _pair_ind){
                return *this;
            }

            _pair_ind = 0;
            _bucket_ind++;
            bucket *map = _hash_map->_map;
            int map_capacity = _hash_map->capacity();
            while(map_capacity > _bucket_ind && (map[_bucket_ind].size() ==
            0)){
                _bucket_ind++;
            }

            return *this;
        }

        ConstIterator operator++(int) {
            ConstIterator it(*this);
            ++(*this);
            return it;
        }

        bool operator==(const ConstIterator& rhs) const {
            return (rhs._hash_map == _hash_map) && (rhs._bucket_ind ==
            _bucket_ind) && (rhs._pair_ind == _pair_ind);
        }

        bool operator!=(const ConstIterator& rhs) const {
            return !operator==(rhs);
        }

        reference operator*() const {return
        _hash_map->_map[_bucket_ind][_pair_ind]; }

        pointer operator->() const { return &(operator*());}

    private:
        const HashMap *_hash_map;
        int _bucket_ind;
        int _pair_ind;
    };

    using const_iterator = ConstIterator;

    const_iterator cbegin() const{
        int bucket_ind =0;
        while((_map[bucket_ind].size() == 0) && _capacity > bucket_ind){
            bucket_ind++;
        }
        return const_iterator(this, bucket_ind, 0);
    }

    const_iterator begin() const{
        return cbegin();
    }

    const_iterator cend() const{ return const_iterator(this, _capacity, 0); }

    const_iterator end() const{ return const_iterator(this, _capacity, 0); }

private:
    int _capacity;
    int _size;
    bucket *_map;
};

#endif //EX6_ORIN_LEVI_HASHMAP_H
