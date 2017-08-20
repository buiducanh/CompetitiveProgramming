#include "string.h"
using namespace std

class Solution {
public:
    bool isMatch(string s, string p) {
      return matchRecur(s, p, 0, 0);
    }

    bool matchRecur(string s, string p, int si, int pi) {
      if ((0 > si || si > s.length()) || (0 > pi || pi > p.length())) {
        return false;
      }

      if (si == s.length()) {
        int jumps = 0;
        while ((pi + jumps + 1 < p.length()) && (p[pi + jumps + 1] == '*')) {
          jumps += 2;
        }

        if (pi + jumps == p.length()) {
          return true;
        }

        return false;
      }
      else {
        if (pi == p.length()) {
          return false;
        }

        if (pi + 1 < p.length() && p[pi + 1] == '*') {
          return matchRecur(s, p, si, pi + 2) ||
                 (p[pi] == '.' || s[si] == p[pi]) &&
                 matchRecur(s, p, si + 1, pi);
        }
        else {
          return (p[pi] == '.' || s[si] == p[pi]) &&
                 matchRecur(s, p, si + 1, pi + 1);
        }
      }
    }
};
