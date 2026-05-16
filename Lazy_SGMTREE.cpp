#include <bits/stdc++.h>
using namespace std;

class LazySegmentTree {
    vector<long long> seg, lazy;
    int n;
public:
    LazySegmentTree(vector<int>& arr) {
        n = arr.size();

        seg.resize(4 * n);
        lazy.resize(4 * n, 0);

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

    void propagate(int node, int low, int high) {
        if (lazy[node] != 0) {

            // Apply pending update
            seg[node] += (high - low + 1) * lazy[node];

            // Push to children
            if (low != high) {
                lazy[2 * node + 1] += lazy[node];
                lazy[2 * node + 2] += lazy[node];
            }

            lazy[node] = 0;
        }
    }

    void rangeUpdate(int node, int low, int high,
                     int l, int r, int val) {

        propagate(node, low, high);

        // No overlap
        if (r < low || high < l)
            return;

        // Complete overlap
        if (l <= low && high <= r) {

            lazy[node] += val;
            propagate(node, low, high);

            return;
        }

        int mid = (low + high) / 2;

        rangeUpdate(2 * node + 1, low, mid, l, r, val);
        rangeUpdate(2 * node + 2, mid + 1, high, l, r, val);

        seg[node] = seg[2 * node + 1] + seg[2 * node + 2];
    }

    long long query(int node, int low, int high,
                    int l, int r) {

        propagate(node, low, high);

        // No overlap
        if (r < low || high < l)
            return 0;

        // Complete overlap
        if (l <= low && high <= r)
            return seg[node];

        int mid = (low + high) / 2;

        long long left =
            query(2 * node + 1, low, mid, l, r);

        long long right =
            query(2 * node + 2, mid + 1, high, l, r);

        return left + right;
    }
};
int main() {
    int n=6;
    vector<int> a={1,4,3,8,7,6};
    LazySegmentTree sg(a);

    cout << sg.query(0,0,n-1,3, 5) << endl;
    sg.rangeUpdate(0,0,5,0,4,2);
    cout << sg.query(0,0,n-1,3, 5) << endl;

    return 0;
}