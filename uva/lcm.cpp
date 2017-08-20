#include <stdio.h>
#include <vector>
#include <unordered_map>
#include <math.h> 
using namespace std;
static const int size_max = 1000000;
bool* sieve = new bool[size_max + 1];
vector<long long> primes;
long long* prime_pos = new long long[size_max + 1];
void reduce(long long* n) {
	while(*n % 10 == 0) { *n /= 10; }
}
long long calculate_lcm(vector<long long>* primes, long long prime_pos, long long i) {
	long long res = 1;
	for(long long k = 0; k <= prime_pos; k++) {
		long long p = log(i) / log((*primes)[k]);
		while(p-- > 0) {
			res *= (*primes)[k];
		}
	}
	return res;
}
int calculate(vector<long long>* primes, long long prime_pos, long long i) {
	long long res = 1;
	for(long long k = 0; k <= 2; k++) {
		long long p = log(i) / log((*primes)[k]);
		while(p-- > 0) {
			res *= (*primes)[k];
			reduce(&res);
		}
	}
	for(long long k = 3; k <= prime_pos; k++) {
		long long p = log(i) / log((*primes)[k]);
		while(p-- > 0) {
			res *= (*primes)[k];
			reduce(&res);
			res %= 10;
		}
	}
	return res;
}

void prepare() {
	bool* sieve = new bool[size_max + 1];
	fill(sieve, sieve + size_max + 1, true);
	sieve[0] = false; 
	sieve[1] = false;
	primes.push_back(2);
	prime_pos[2] = 0;
	long long cnt = 0;
	for(long long i = 3; i <= size_max; i += 2) {
		if (sieve[i]) {
			primes.push_back(i);
			cnt += 1;
			if (i * i <= size_max) {
				for(long long j = i*i; j <= size_max; j += 2*i) {
					sieve[j] = false;
				}
			}
		}
		prime_pos[i] = cnt;
	}
	for(long long i = 4; i <= size_max; i += 2) {
		sieve[i] = false;
		prime_pos[i] = prime_pos[i - 1];
	}
}

int main() {
	int i;
	prepare();
	while(scanf("%d", &i), i != 0) {
		printf("%d\n", calculate(&primes, prime_pos[i], i) % 10);
	}
}
