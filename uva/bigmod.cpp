#include <stdio.h>

long long bigmod(long long b, long long p, long long m) {
	if (p == 0) {
		return 1;
	}
	if (p == 1) {
		return b % m;
	}
	if (p % 2 == 1) {
		return ((b % m) * (bigmod(b, p - 1, m))) % m;
	}
	long long res = bigmod(b, p / 2, m);
	return res * res % m;
}

int main() {
	long long b, p, m;
	while(scanf("%lld\n%lld\n%lld", &b, &p, &m) == 3) {
		printf("%lld\n", bigmod(b, p, m));		
	}
}
