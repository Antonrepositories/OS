#include <iostream>
#include <thread>
#include <vector>
#include <mutex>

std::vector<std::vector<int>> global_result_matrix;

std::mutex mtx;

void multiply_row(int row_index, const std::vector<std::vector<int>>& A, const std::vector<std::vector<int>>& B) {
    std::vector<int> result_row(B[0].size(), 0);
    for (int j = 0; j < B[0].size(); ++j) {
        int result = 0;
        for (int k = 0; k < A[0].size(); ++k) {
            result += A[row_index][k] * B[k][j];
        }
        result_row[j] = result;
        mtx.lock();
        std::cout << "[" << row_index << ", " << j << "] = " << result << std::endl;
        mtx.unlock();
    }
    mtx.lock();
    global_result_matrix[row_index] = result_row;
    mtx.unlock();
}

int main() {
    int n = 5;
    int m = 4;
    int k = 3;

    std::vector<std::vector<int>> A(n, std::vector<int>(m));
    std::vector<std::vector<int>> B(m, std::vector<int>(k));
    std::cout << "Матриця A:" << std::endl;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            A[i][j] = rand() % 10 + 1;
            std::cout << A[i][j] << " ";
        }
        std::cout << std::endl;
    }
    std::cout << "Матриця B:" << std::endl;
    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < k; ++j) {
            B[i][j] = rand() % 10 + 1;
            std::cout << B[i][j] << " ";
        }
        std::cout << std::endl;
    }

    global_result_matrix.resize(n, std::vector<int>(k, 0));

    std::vector<std::thread> threads;
    for (int i = 0; i < n; ++i) {
        threads.push_back(std::thread(multiply_row, i, std::ref(A), std::ref(B)));
    }

    for (std::thread& thread : threads) {
        thread.join();
    }

    std::cout << "Результуюча матриця C:" << std::endl;
    for (const auto& row : global_result_matrix) {
        for (int elem : row) {
            std::cout << elem << " ";
        }
        std::cout << std::endl;
    }

    return 0;
}
