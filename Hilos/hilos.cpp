#include <iostream>
#include <thread>
#include <string>

using namespace std;

void thread_proc(std::string msg)
{
    std::cout << "Ejecución desde el hilo: " << msg;
}
int main()
{
    std::thread t(thread_proc, "Hello World\n");

    t.join();
}
