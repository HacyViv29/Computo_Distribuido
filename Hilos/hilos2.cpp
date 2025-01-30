#include <iostream>
#include <thread>
using namespace std;
#include <string>
#include <thread>

/*void thread_proc(int num, int hilo)
{
    while(num < 1000)
    {
        std::cout << "Numero de inicio: " << num << std::endl;
        num++;
        hilo++;
        std::cout << "Numero de final: " << num << std::endl;
        std::cout << "Hilo: " << hilo << std::endl;
    }
}*/

void thread_proc(int num, int hilo)
{
    while(num < 1000)
    {
        std::cout << "Numero de inicio: " << num << std::endl;
        num++;
        hilo++;
        std::cout << "Numero de final: " << num << std::endl;
        std::cout << "Hilo: " << hilo << std::endl;
    }
}

int main()
{
    int num = 500;
    int hilo = 1;

    std::thread t(thread_proc, num, hilo);
    t.join();
    
}