#include <iostream>
#include <unistd.h>
#include <sys/wait.h>
using namespace std;

void myFunc(int i){
    cout << "calling myFunc from process n°: " << i << endl;
    for (int j = 0; j<i; ++j){
        cout << "output from myFunc is: " << j << endl;
    }
}

int main(){
    for(int i = 0; i<6; ++i){
        pid_t pid = fork();

        if(pid == 0){
            //Child process
            myFunc(i);
            exit(0);
        }else if (pid > 0){
            //Parent Process
            wait(NULL);
        }else{
            cerr << "Fork failes" << endl;
        }
    }
}
