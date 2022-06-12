#include <list>
#include <iostream>
using namespace std;

int main(int argc, char * argv[])
{
  list<int> data;
  int m, n;
  cin>>n;
  cin>>m;

  for(int i=0; i<n; i++)
    data.push_back(i+1);
  auto it = data.begin();
  for(int k=0; k<n; k++)
  {
    for(int i=0; i<m-1; i++)
    {
      it++;
      if(it==data.end()){
        it = data.begin();
      }
    }
    cout<<*it<<" ";
    it = data.erase(it);
    if(it==data.end())
      it = data.begin();
  }
  cout<<endl;
  return 0;
}
