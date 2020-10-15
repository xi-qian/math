#include <iostream>
#include <unistd.h>
using namespace std;
////

void locateCursor(const int row, const int col){    
    printf("%c[%d;%dH",27,row,col);
}

int main()
{
    printf("\e[?25l");
    int i=0;
    int n=50;
    cout << "Nice to meet you."<<"请做好作战准备"<<endl;
    
    while(i<n)
    {
        usleep(1000*100);
        i=i+1;
        printf("\r\e[K\e[%dC三 ————>", i);
    }
    
    cout <<endl;
    
    cout <<"请选择模式"<<endl;
    
    return 0;
}
