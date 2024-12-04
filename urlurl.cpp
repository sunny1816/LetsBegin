#include <iostream>
#include <cstdlib> 
using namespace std;
int main() {
string url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR5b7QyuBfOf2PgFocJNFYDI2YBkCHXQwarkg&s"; 
cout << "HOW WAS THE SUPRISE ";
string command = "start " + url; 
system(command.c_str());
return 0;
}
