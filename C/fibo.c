// #include <stdio.h>
// int main()
// {
//     int n,fibo=0,a=0,b=1;
//     scanf("%d",&n);

//     for(int i = 1;i<=n;i++){
//         printf("%d\n",fibo);
//         fibo = a+b;
//         a=b;
//         b=fibo;
//     }

    
//     return 0;
// }

#include <stdio.h>

int fibo(int n) {
    if (n == 0) {
        return 0;
    }

    if (n == 1) {
        return 1;
    }

    return fibo(n - 1) + fibo(n - 2);
}

int main() {
    int n = 20; // You can adjust this value as needed
    for (int i = 0; i < n; i++) {
        printf("%d\n", fibo(i)); // Print each Fibonacci number
    }
    return 0;
}
