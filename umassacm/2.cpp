
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <vector>
using namespace std;

vector<int> makePrime() {
  bool ans[10000];
  vector<int> nums;
  memset(ans, 0, sizeof(bool) * 10000);
  for(int i = 2; i < 10000; i++) {
    if (ans[i] == 0) {
      for(int j = i*i; j < 10000; j = j + i) {
        ans[j] = 1;
      }
      nums.push_back(i);
    }
  }
  return nums;
}

int main() {
  int n, q;
  scanf("%d %d\n", &n, &q);
  vector<int> pile;
  vector<int> primes = makePrime();
  vector<int>::iterator prime = primes.begin();
  vector<vector<int>> b;
  for(int i = 0; i < n; i++) {
    int num;
    scanf("%d", &num);
    pile.push_back(num);
  }
  while (q > 0) {
    int primenum = *prime;
    prime++;
    vector<int> nextA;
    for(vector<int>::reverse_iterator i = pile.rbegin(); i != pile.rend(); i++){
      if (*i % primenum == 0) {
        b.push_back(*i);
      }
      else {
        nextA.push_back(*i);
      }
    }
    q--;
    pile = nextA;
  }
  for(vector<int>::reverse_iterator i = b.rbegin(); i != b.rend(); i++) {
    printf("%d\n", *i);
  }
  for(vector<int>::reverse_iterator i = pile.rbegin(); i != pile.rend(); i++) {
    printf("%d\n", *i);
  }
}
