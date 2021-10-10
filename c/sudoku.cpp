#include <iostream>
using namespace std;

int data[9][9]={0};

void init_data()
{
    for(int i=0; i<9; i++)
        for(int j=0; j<9; j++)
            cin>>data[i][j];
}

bool check(int row, int col, int number)
{
    //check row
    for(int i =0; i<9; i++)
        if(data[row][i]==number)
            return false;
    //check col
    for(int i=0; i<9; i++)
        if(data[i][col]==number)
            return false;
    //check block
    int begin_i = row/3*3;
    int begin_j = col/3*3;
    for(int i=begin_i; i<begin_i+3; i++)
        for(int j=begin_j; j<begin_j+3; j++)
            if(data[i][j]==number)
                return false;
    return true;
}

bool dfs(int n)
{
//    cout<<"dfs "<<n<<endl;
    for(int k = n; k<9*9; k++)
    {
        if(data[k/9][k%9]!=0)
        {
            if(k==9*9-1)
                return true;
            else
                continue;
        }
            
        for(int number = 1; number<=9; number++)
        {
            if(check(k/9, k%9, number))
            {
                data[k/9][k%9]=number;
                if(k==9*9-1||dfs(k+1))
                {
                    return true;
                }else
                {
                    data[k/9][k%9]=0;
                }
            }
        }
        return false;
    }        
    return false;
}

void print_data()
{
    for(int i=0; i<9; i++)
    {
        for(int j=0; j<9; j++)
            cout<<data[i][j]<<" ";
        cout<<endl;
    }
}

int main()
{
    init_data();
    if(dfs(0))
    {
        print_data();
    }else
    {
        cout<<"FAIL!"<<endl;
    }
}