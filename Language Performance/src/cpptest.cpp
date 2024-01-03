#include <iostream>
#include <time.h>

using namespace std;

int main() {
  clock_t starttime = clock();

  int i = 0;
  
  while(i != 1000000000) {
    i++;
  }

  clock_t endtime = clock();
  double timeelapsed = (double)(endtime - starttime) / CLOCKS_PER_SEC;

  cout << "Time taken by C++: " << timeelapsed << " secs\n";

  return 0;
}
