// Matrix.h
#ifndef MATRIX_H
#define MATRIX_H
#include <iostream>

#define LEN_ERROR "invalid len"
#define RUN_TIME_ERROR "run time error"
#define OUT_OF_RANGE "out of range"
#define MIN_NUM_TO_SHOW 0.1

/**
 * @struct matrix_dims
 * @brief Matrix dimensions container. Used in MlpNetwork.h and main.cpp
 */
typedef struct matrix_dims
{
	int rows, cols;
} matrix_dims;

// Insert Matrix class here...
class Matrix{
public:
    Matrix(int rows, int cols);
    Matrix();
    Matrix(const Matrix &m);
    ~Matrix();

    int get_rows() const;
    int get_cols() const;

    Matrix& transpose();
    Matrix &vectorize();
    void plain_print() const;
    Matrix dot(Matrix const& m);
    float norm() const;

    Matrix operator+(Matrix const &m) const;
    Matrix& operator=(Matrix const &m);
    Matrix operator*(Matrix const &m) const;
    Matrix operator*(float f) const;
    friend Matrix operator*(float f, Matrix const &m);
    Matrix operator+=(Matrix const &m);
    float& operator()(int i, int j);
    float operator()(int i, int j) const;
    float operator[](int n) const;
    float& operator[](int n);
    friend std::ostream& operator<<(std::ostream &os, Matrix const &m);
    friend std::istream& operator>>(std::istream &is, Matrix &m);

private:
    int _rows, _cols;
    float *arr;

};

#endif //MATRIX_H