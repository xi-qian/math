#include <iostream>

int main(int argc, char * argv[])
{
	using namespace std;
	int a, b, c;
	cin>>a;
	cin>>b;
	cin>>c;
	if(a+b>c && b+c>a && a+c>b)
	{
		if(a==b && b==c)
		{
		       cout<<"Equilateral"; 

		}else if (a*a+b*b==c*c || a*a+c*c==b*b || b*b+c*c==a*a)
		{
			cout<<"Right";
		}else
		{
			cout<<"General";
		}

	}else
	{
		cout<<"NO";
	}
	cout<<endl;
}
