#include <stdlib.h>
#include <vector>
#include <unordered_map>
using namespace std;

int minarrays(vector<int> a, vector<int> b, vector<int> c) {
	unordered_map<int, int> m;
	for (auto i = a.begin(); i != a.end(); i++) {
		if (m.find(*i) == m.end()) {
			m[*i] = 1;
		}
	}
	for (auto i = b.begin(); i != b.end(); i++) {
		auto num = m.find(*i);
		if (num != m.end() && num->second == 1) {
			m[*i] = 2;
		}
	}

	int min = 1 << 31 - 1;
	for (auto i = c.begin(); i != c.end(); i++) {
		auto num = m.find(*i);
		if (num != m.end() && num->second == 2 && min > *i) {
			min = *i;
		}
	}
	return min;
}

int main()
{
	vector<int> a, b, c;
	int max = 5;
	int num;
	for (int i = 0; i < 10; i++) {
		num = rand() % max;
		a.push_back(num);
		num = rand() % max;
		b.push_back(num);
		num = rand() % max;
		c.push_back(num);
	}

	printf("%d\n", minarrays(a, b, c));
}

