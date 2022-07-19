#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int n, q; // First 2 LOC
    cin >> n >> q;
    
    int *a[n];
    
    
    int sub_arr_size, query;
    int *sub_arr;
    
    // Filling in data for array a ("n subsequent LOC")
    for (int i = 0; i < n; ++i)
    {
        cin >> sub_arr_size;
        sub_arr = new int[sub_arr_size];
        
        for (int j = 0; j < sub_arr_size; ++j)
        {
            cin >> query; // Value for a[i][j]
            sub_arr[j] = query;
        }
        
        a[i] = sub_arr;
    }
    
    
    // Last q queries
    int first, second;
    
    for (int k = 0; k < q; ++k)
    {
        cin >> first >> second;
        cout << a[first][second] << endl;
    }

    return 0;
}