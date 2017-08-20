#include <iostream>
using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
      int ans = 0;
      if (prices.size() == 0) {
        return 0;
      }
      int stock = *(prices.begin());
      for(auto i = prices.begin()++; i != prices.end(); i++) {
        int nextStock = *i;
        if (nextStock > stock) {
          ans += nextStock - stock;
          stock = nextStock;
        }
        else {
          stock = nextStock;
        }
      }
      return ans;
    }
};

