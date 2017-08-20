#include <bits/stdc++.h>
using namespace std;

double asmall(int n, int m) {
  double dp[n+1][m+1];
  memset(dp, 0, sizeof(dp));
  dp[1][0] = 1;
  for(int i = 2; i < n + 1; i++) {
    for(int j = 0; j < i && j < m + 1; j++) {
      if (i != j + 1) {
        dp[i][j] = dp[i - 1][j] * i
      }
    }
  }
}

int main() {
  int t;
  scanf("%d", tt);
  for(int t = 0; t < tt; t++) {
    printf("Case #%d: %0.6f", t + 1, asmall(n, m));
  }
}
