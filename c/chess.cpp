#include <iostream>

int main(int argc, char * argv[])
{
	char board[15][15]={0};
	for(int i=0; i<15; i++)
	{
		for(int j=0; j<15; j++)
			std::cin>>board[i][j];
	}
}


