#include <bits/stdc++.h>
using namespace std;

typedef struct subset {
  int parent;
  int rank;
} subset;

void initSet(subset* sets, int i, int id) {
    sets[i].parent = i;
    sets[i].rank = 0;
}

int find(subset* sets, int i) {
  if (sets[i].parent != i) {
    sets[i].parent = find(sets, sets[i].parent);
  }
  return sets[i].parent;
}

void unionSet(subset* sets, int u, int v) {
  u = find(sets, u);
  v = find(sets, v);
  if (sets[u].rank < sets[v].rank) {
    sets[u].parent = v;
  }
  else if (sets[u].rank > sets[v].rank) {
    sets[v].parent = u;
  }
  else {
    sets[u].parent = v;
    sets[v].rank += 1;
  }
}

int main() {
  ios_base::sync_with_stdio(0);cin.tie(0);
  int n, m, k;
  cin >> n >> m >> k;
  int socks[n];
  subset* sets = (subset*) malloc(n * sizeof(subset));
  for (auto i = 0; i < n; i++) {
    initSet(sets, i, i);
    cin >> socks[i];
  }

  int l, r;
  for (auto i = 0; i < m; i++) {
    cin >> l >> r;
    l--;
    r--;

    int u = find(sets, l);
    int v = find(sets, r);
    if (u != v) {
      unionSet(sets, u, v);
    }
  }

  unordered_map<int, int> counts[n];
  int maxVal[n], setSize[n];
  memset(maxVal, -1, sizeof(maxVal));
  memset(setSize, 0, sizeof(setSize));

  for(auto i = 0; i < n; i++) {
    int u = find(sets, i);
    if (counts[u].find(socks[i]) == counts[u].end()) {
      counts[u].insert(make_pair(socks[i], 1));
    }
    else {
      counts[u][socks[i]]++;
    }
    setSize[u]++;
    if (maxVal[u] == -1 || counts[u][socks[i]] > counts[u][maxVal[u]])  {
      maxVal[u] = socks[i];
    }
  }

  int ans = 0;
  for (auto i = 0; i < n; i++) {
    if (sets[i].parent != i) continue;
    ans += setSize[i] - counts[i][maxVal[i]];
  }
  cout << ans;
  return 0;
}
