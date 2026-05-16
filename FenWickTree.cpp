#include <bits/stdc++.h>
using namespace std;

class FenwickTree {
    vector<long long> bit;
    int n;

public:
    FenwickTree(int size) {
        n = size;
        bit.assign(n + 1, 0);
    }

    FenwickTree(vector<int>& a) {
        n = a.size();
        bit.assign(n + 1, 0);

        for (int i = 0; i < n; i++) {
            update(i, a[i]);
        }
    }

    // add val at index idx (0-based)
    void update(int idx, long long val) {
        idx++;

        while (idx <= n) {
            bit[idx] += val;
            idx += (idx & -idx);
        }
    }

    // prefix sum [0 ... idx]
    long long prefixSum(int idx) {
        idx++;

        long long sum = 0;

        while (idx > 0) {
            sum += bit[idx];
            idx -= (idx & -idx);
        }

        return sum;
    }

    // range sum [l ... r]
    long long query(int l, int r) {
        if (l > r) return 0;

        return prefixSum(r) - prefixSum(l - 1);
    }
};
int main(){
    vector<int> a = {1,2,3,4,5};

    FenwickTree ft(a);

    cout << ft.query(1,3) << endl; // 2+3+4 = 9

    ft.update(2,10); // add +10 at index 2

    cout << ft.query(1,3) << endl; // 19
    return 0;
}