#include <stdio.h>
int main()
{
	int n,r;
	int rev=0;
	

	printf("Enter the number");
	scanf("%d",&n);
	int m=n;

	while(n>0){
		r=n%10;
		n=n/10;
		rev=rev*10+r;
	}

	if(rev==m){
		printf("palindrome");
	}else{
		printf("not a palindrome");
	}

	return 0;
}
