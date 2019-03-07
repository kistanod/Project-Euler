/*
 * solution for first problem of Project Euler
 * link : https://www.hackerrank.com/contests/projecteuler/challenges/euler001
*/

#include <stdio.h>


int main(){

    int t; 
    scanf("%d",&t);
    
    for(int trial = 0; trial < t; trial++){
        int n; 
        scanf("%d",&n);
        
        long three = (n-1)/3;
        long five = (n-1)/5;
        long fifteen = (n-1)/15;
        
        long up_to_three = (three*(three+1))/2;
        long up_to_five = (five*(five+1))/2;
        long up_to_fifteen = (fifteen*(fifteen+1))/2;
        
        long result = (3*up_to_three)+(5*up_to_five)-(15*up_to_fifteen);
        
        printf("%ld \n", result);
        
    }
    
    return 0;
}
