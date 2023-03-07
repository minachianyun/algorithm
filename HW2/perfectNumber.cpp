#include<iostream>

using namespace std;

int main(){
    int num;
    cin >> num;
    
    for(int i = 0; i < num; i++){
        int test;
        int sum = 0;
        cin >> test;
        for(int i = 1 ; i < test ; i++){
            if(test % i == 0){
                sum = sum + i;
            }
        }
        if(test == sum){
            cout << test << " ";
        }
    }
     return 0;
}
