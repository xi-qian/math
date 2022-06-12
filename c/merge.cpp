#include <iostream>
#include <vector>
using namespace std;
int main(int argc, char * argv[])
{
  int m, n;
  vector<int> a, b, c;
  int val;
  cin>>m;
  for(int i=0; i<m; i++)
  {
    cin>>val;
    a.push_back(val);
  }
  cin>>n;
  for(int i=0; i<n; i++)
  {
    cin>>val;
    b.push_back(val);
  }
  for(int i=0, u=0, v=0;i<m+n; i++)
  {
    if(v>=n || (u<m && a[u]<=b[v]))
    {
      c.push_back(a[u]);
      u++;
    }else{
      c.push_back(b[v]);
      v++;
    }
    cout<<c[i]<<" ";
  }
  cout<<endl;
}
