#include <stdio.h>

char *residence(int x, int y, int n, int m) {
  if (x == n || y == m) {
    return "divisa";
  }
  char left = 1, up = 1;
  if (n - x < 0) {
    left = 0;
  }

  if (m - y > 0) {
    up = 0;
  }
  
  if (left) {
    if (up) {
      return "NO";
    }
    else {
      return "SO";
    }
  }
  else {
    if (up) {
      return "NE";
    }
    else {
      return "SE";
    }
  }
}

int main() {
  int k;
  while(scanf("%d", &k) && k != 0) {
    int n,m; 
    scanf("%d %d", &n, &m);
    int x,y;
    for(; k > 0; k--) {
      scanf("%d %d", &x, &y);
      printf("%s\n", residence(x, y, n, m));
    }
  }
}
