#include <iostream>
using namespace std;

int main(){
	
	 string a;

	cin >> a;

	for(int i=0; i< a.length(); i++){
		cout << (int)a[i];
		cout << "\n";
	}

	return 0;

}
