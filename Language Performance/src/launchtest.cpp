#include <iostream>
#include <Windows.h>

using namespace std;

int main() 
{
    const char *ctestpath = "build/ctest.exe";
    const char *cpptestpath = "build/cpptest.exe";
    const char *cstestpath = "build/cstest.exe";
    const char *pytestpath = "build/pytest.exe";

    cout << "Welcome! Testing the performance of counting to 1 billion according to how much time was taken for the languages below.\n";
    cout << "Languages to be tested: C, C++, C#, Java, Python\n";

    system("ctest.exe");
    system("cpptest.exe");
    system("cstest.exe");
    system("java javatest");
    system("pytest.exe");

    cout << "Closing in 10 seconds...\n";

    Sleep(10000);
}