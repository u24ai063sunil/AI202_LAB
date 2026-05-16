#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define mod 1000000007
#define inf 1000000000000000000
#define pb push_back
#define mp make_pair
#define ff first
#define ss second
#define all(x) x.begin(),x.end()
#define rall(x) x.rbegin(),x.rend()
#define fast ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
class SegmentTree {
    vector<long long> seg;
    int n;

    void build(int node, int low, int high, vector<int>& arr,int orr) {
        if (low == high) {
            seg[node] = arr[low];
            return;
        }

        int mid = (low + high) / 2;

        build(2 * node + 1, low, mid, arr,!orr);
        build(2 * node + 2, mid + 1, high, arr,!orr);

        if(orr) seg[node] = seg[2 * node + 1] | seg[2 * node + 2];
        else seg[node] = seg[2 * node + 1] ^ seg[2 * node + 2];
    }

    long long query(int node, int low, int high, int l, int r,int orr) {
        if (r < low || high < l)
            return 0;

        if (l <= low && high <= r)
            return seg[node];

        int mid = (low + high) / 2;

        long long left = query(2 * node + 1, low, mid, l, r,!orr);
        long long right = query(2 * node + 2, mid + 1, high, l, r,!orr);

        if(orr) return left | right;
        return left ^ right;
    }

    void update(int node, int low, int high, int idx, int val,int orr) {
        if (low == high) {
            seg[node] = val;
            return;
        }

        int mid = (low + high) / 2;

        if (idx <= mid)
            update(2 * node + 1, low, mid, idx, val,!orr);
        else
            update(2 * node + 2, mid + 1, high, idx, val,!orr);

        if(orr) seg[node] = seg[2 * node + 1] | seg[2 * node + 2];
        else seg[node] = seg[2 * node + 1] ^ seg[2 * node + 2];
    }

public:
    SegmentTree(vector<int>& arr,int orr) {
        n = arr.size();
        seg.resize(4 * n);
        build(0, 0, n - 1, arr,orr);
    }

    long long query(int l, int r,int orr) {
        return query(0, 0, n - 1, l, r,orr);
    }

    void update(int idx, int val,int orr) {
        update(0, 0, n - 1, idx, val,orr);
    }
};

int main(){
    fast
    int n,m;
    cin>>n>>m;
    int l=pow(2,n);
    vector<int> a(l);
    for(int i=0;i<l;i++) cin>>a[i]; 
    SegmentTree sg(a,n&1);
    for(int i=0;i<m;i++){
        int idx,val;
        cin>>idx>>val;
        sg.update(idx-1,val,n&1);
        a[idx-1]=val;
        cout<<sg.query(0,l-1,n&1)<<endl;
    }
    return 0;
}