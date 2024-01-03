#include <stdio.h>
#include <time.h>

int main() {
  clock_t starttime = clock();

  int i = 0;
  
  while(i != 1000000000) {
    i++;
  }

  clock_t endtime = clock();
  double timeelapsed = (double)(endtime - starttime) / CLOCKS_PER_SEC;

  printf("Time taken by C: %f secs\n", timeelapsed);

  return 0;
}
