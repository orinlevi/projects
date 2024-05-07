//
// Created by orin levi on 02/09/2022.
//
#include "Matrix.h"
#include <cmath>

Matrix::Matrix(int rows, int cols):_rows(rows), _cols(cols) {
    if(!(cols > 0 && rows > 0)){
        throw std::length_error(LEN_ERROR);
    }
    arr = new float[_rows * _cols];
}

Matrix::Matrix(): Matrix(1, 1) {}

Matrix::Matrix(const Matrix &m): Matrix(m._rows, m._cols){
    for (int i = 0; i < _rows * _cols; i++){
        arr[i]  = m.arr[i];
    }
}

Matrix::~Matrix() {
    delete[] arr;
}

int Matrix::get_rows() const {
    return _rows;
}

int Matrix::get_cols() const {
    return _cols;
}

Matrix& Matrix::transpose() {
    auto *new_arr = new float[_cols*_rows];
    for(int i = 0; i < _rows; i++){
        for(int j = 0; j < _cols; j++){
            new_arr[j * _rows + i] = arr[i * _cols + j];
        }
    }
    int temp = _cols;
    _cols = _rows;
    _rows = temp;
    delete[] arr;
    arr = new_arr;
    return *this;
}

Matrix& Matrix::vectorize() {
    _rows *= _cols;
    _cols = 1;
    return *this;
}

void Matrix::plain_print() const{
    for(int i = 0; i < _rows; i++){
        for(int j = 0; j < _cols; j++){
            std::cout << arr[i * _cols + j] << " ";
        }
        std::cout << std::endl;
    }
}

Matrix Matrix::dot(const Matrix &m) {
    if( m._rows != _rows || m._cols != _cols){
        throw std::length_error(LEN_ERROR);
    }
    Matrix new_matrix(*this);
    for( int i = 0; i < _cols * _rows; i++){
        new_matrix.arr[i] = arr[i] * m.arr[i];
    }
    return new_matrix;
}


float Matrix::norm() const {
    float sum = 0;
    for(int i = 0; i< _cols * _rows; i++){
        sum += (float)pow(arr[i], 2);
    }
    return sqrt(sum);
}

Matrix Matrix::operator+(const Matrix &m) const {
    if( m._rows != _rows || m._cols != _cols){
        throw std::length_error(LEN_ERROR);
    }
    Matrix new_matrix(*this);
    for( int i = 0; i < _cols * _rows; i++){
        new_matrix.arr[i] = arr[i] + m.arr[i];
    }
    return new_matrix;
}

Matrix& Matrix::operator=(const Matrix &m) {
    if(this != &m){
        auto *new_arr = new float[m._cols * m._rows];
        for(int i =0; i < m._cols * m._rows; i++){
            new_arr[i] = m.arr[i];
        }
        delete[] arr;
        arr = new_arr;
        _rows = m._rows;
        _cols = m._cols;
    }
    return *this;
}

Matrix Matrix::operator*(const Matrix &m) const {
    if(_cols != m._rows){
        throw std::length_error(LEN_ERROR);
    }
    Matrix new_matrix(_rows, m._cols);
    for( int i = 0; i < new_matrix._rows; i++){
        for( int j = 0; j < new_matrix._cols; j++){
            float sum = 0;
            for( int x = 0; x < _cols; x++){
                sum += (arr[i * _cols + x] * m.arr[j+ x * m._cols]);
            }
            new_matrix.arr[i* new_matrix._cols + j] = sum;
        }
    }
    return new_matrix;
}

Matrix Matrix::operator*(float f) const {
    Matrix new_matrix(_rows, _cols);
    for( int i = 0; i < _cols * _rows; i++){
        new_matrix.arr[i] = (float) f * arr[i];
    }
    return new_matrix;
}

Matrix operator*(float f, const Matrix &m) {
    return (m*f);
}

Matrix Matrix::operator+=(const Matrix &m) {
    if( m._rows != _rows || m._cols != _cols){
        throw std::length_error(LEN_ERROR);
    }
    for( int i = 0; i < _cols * _rows; i++){
        arr[i] += m.arr[i];
    }
    return *this;
}

float& Matrix::operator()(int i, int j){
    if( i >= _rows || i < 0 || j >= _cols || j < 0){
        throw std::out_of_range(OUT_OF_RANGE);
    }
    return arr[i * _cols + j];
}

float Matrix::operator()(int i, int j) const{
    if( i >= _rows || i < 0 || j >= _cols || j < 0){
        throw std::out_of_range(OUT_OF_RANGE);
    }
    return arr[i * _cols + j];
}

float Matrix::operator[](int n) const {
    if( n < 0 || n >= _cols * _rows){
        throw std::out_of_range(OUT_OF_RANGE);
    }
    return arr[n];
}

float& Matrix::operator[](int n) {
    if( n < 0 || n >= _cols * _rows){
        throw std::out_of_range(OUT_OF_RANGE);
    }
    return arr[n];
}

std::ostream& operator<<(std::ostream &os, const Matrix &m) {
    for(int i = 0; i < m._rows; i++){
        for(int j = 0; j < m._cols; j++){
            if(m.arr[i * m._cols + j] > MIN_NUM_TO_SHOW){
                os << "**";
            } else{
                os << "  ";
            }
        }
        os << std::endl;
    }
    return os;
}

std::istream& operator>>(std::istream &is, Matrix &m) {
    if(!is){
        throw std::runtime_error(RUN_TIME_ERROR);
    }
    is.seekg(0, std::istream::end);
    long int file_size_bytes = is.tellg();
    unsigned long file_len = file_size_bytes/sizeof(float);
    is.seekg(0, std::istream::beg);

    for(unsigned long i = 0; i < file_len; i++){
        if(!is.read((char*)&(m.arr[i]), sizeof(float ))){
            throw std::runtime_error(RUN_TIME_ERROR);
        }
    }
    return is;
}
