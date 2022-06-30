#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
 
bool is_sorted(int *a, int n)
{
  while ( --n >= 1 ) {
    if ( a[n] < a[n-1] ) return false;
  }
  return true;
}
 
void shuffle(int *a, int n)
{
  int i, t, r;
  for(i=0; i < n; i++) {
    t = a[i];
    r = rand() % n;
    a[i] = a[r];
    a[r] = t;
  }
}
 
void bogosort(int *a, int n)
{
  while ( !is_sorted(a, n) ) shuffle(a, n);
}

int main(int argc, char *argv[])
{
  int numbers[argc];
  for ( int i = 0; i < argc; i++){
    int n = atoi(argv[i]);
    numbers[i] = n;
  }
 
  bogosort(numbers, argc);
  for (int i=0; i < argc; i++) printf("%d ", numbers[i]);
  printf("\n");
}
