#include <stdio.h>
#include <stdint.h>

uint32_t get_bit(uint32_t data, int k)
{
	return (data & (((uint32_t)0x01)<<k))>>k;
}

bool check(uint32_t n, int k)
{
        if(get_bit(n, k)==1 && get_bit(n, k+1)==1 && get_bit(n, k+3)==1 && get_bit(n, k+4)==1)
	{
		printf("%d : ", n);
		for(int i=0; i<9; i++)
		{
			printf("%d ", get_bit(n, i));
		}
        	printf("\n");
		printf("true\n");
		return true;
	}
        else
	{
		return false;
	}
}

int count(uint32_t n)
{
	int bits = 0;
	for(int i=0; i<9; i++)
	{
		if(get_bit(n, i)>0)
			bits++;
	}
	return bits;
}

int main(int argc, char * argv[])
{
	int n = 0;
	for(uint32_t i=0; i<512; i++)
	{
		if(count(i)==6)
		{
		if (check(i, 0) || check(i, 1) || check(i, 3) || check(i, 4))
		{
			n++;
		}
		}
	}
	printf("n = %d\n", n);
	return 0;
}
