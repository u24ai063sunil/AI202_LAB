#include <bits/stdc++.h>
using namespace std;

class SegmentTree {
    vector<long long> seg;
    int n;
    
public:
    SegmentTree(vector<int>& arr) {
        n = arr.size();
        seg.resize(4 * n);
        build(0, 0, n - 1, arr);
    }
  
    void build(int node, int low, int high, vector<int>& arr) {
        if (low == high) {
            seg[node] = arr[low];
            return;
        }

        int mid = (low + high) / 2;

        build(2 * node + 1, low, mid, arr);
        build(2 * node + 2, mid + 1, high, arr);

        seg[node] = seg[2 * node + 1] + seg[2 * node + 2];
    }

    long long query(int node, int low, int high, int l, int r) {
        if (r < low || high < l)
            return 0;

        if (l <= low && high <= r)
            return seg[node];

        int mid = (low + high) / 2;

        long long left = query(2 * node + 1, low, mid, l, r);
        long long right = query(2 * node + 2, mid + 1, high, l, r);

        return left + right;
    }

    void update(int node, int low, int high, int idx, int val) {
        if (low == high) {
            seg[node] = val;
            return;
        }

        int mid = (low + high) / 2;

        if (idx <= mid)
            update(2 * node + 1, low, mid, idx, val);
        else
            update(2 * node + 2, mid + 1, high, idx, val);

        seg[node] = seg[2 * node + 1] + seg[2 * node + 2];
    }
};

int main() {
    int n;
    cin >> n;

    vector<int> a(n);

    for (int i = 0; i < n; i++)
        cin >> a[i];

    SegmentTree sg(a);

    cout << sg.query(0,0,n-1,3, 5) << endl;

    return 0;
}