#include <iostream>
#include <stack>
using namespace std;

void print(int result[], int n)
{
	for(int i=0; i<n; i++)
	{
		cout<<result[i]+1;
	}
	cout<<endl;
}

void permutation(int mask[], int n, int result[], int depth){
	if(depth>=n)
		print(result, n);
	for(int i=0; i<n; i++)
	{
		if(mask[i]==0)
		{
			mask[i] = 1;
			result[depth]=i;
			permutation(mask, n, result, depth+1);
			mask[i] = 0;
		}
	}
}

int main()
{
	int mask[5]={0};
	int result[5]={0};
	permutation(mask, 5, result, 0);
	return 0;
}
