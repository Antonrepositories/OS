#include <iostream>
#include <thread>
#include <mutex>

std::mutex mtx;
int shared_variable = 0;

void thread_function_with_mutex() {
    for (int i = 0; i < 10000; ++i) {
        mtx.lock();
        shared_variable++;
        shared_variable--;
        mtx.unlock();
    }
}

void thread_function_without_mutex() {
    for (int i = 0; i < 10000000; ++i) {
        shared_variable++;
        shared_variable--;
    }
}

int main() {
    std::thread thread1(thread_function_with_mutex);
    std::thread thread2(thread_function_with_mutex);

    thread1.join();
    thread2.join();

    std::cout << "Shared variable value with mutex: " << shared_variable << std::endl;

    shared_variable = 0; 

    std::thread thread3(thread_function_without_mutex);
    std::thread thread4(thread_function_without_mutex);

    thread3.join();
    thread4.join();

    std::cout << "Shared variable value without mutex: " << shared_variable << std::endl;

    return 0;
}
