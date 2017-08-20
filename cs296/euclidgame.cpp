#include <stdio.h>
#include <vector>
#include <cmath>
using namespace std;

char *euclid_game(int x, int y) {
  vector<int> vec; 
  int z;
  if (x < y) {
    z = x;
    x = y;
    y = z;
  }
  while (y != 0) {
    z = x % y;
    vec.push_back(floor((double) x / y));
    x = y;
    y = z;
  }
  char first_win = 1; 
  for (vector<int>::iterator i = vec.end() - 1; i != vec.begin() - 1; i--) {
    if (i == vec.end() - 1) continue;
    if (first_win) {
      if (*i == 1) {
        first_win = 0;
      }
    }
    else {
      first_win = 1;
    }
  }
  if (first_win) {
    return "Stan wins";
  }
  return "Ollie wins";
}

int main() {
  int x, y;
  while(scanf("%d %d", &x, &y) == 2) {
    if (x == 0 && y == 0) return 0;
    printf("%s\n", euclid_game(x, y));
  }
  return 0;
}
