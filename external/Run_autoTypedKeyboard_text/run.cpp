#include <cstdlib>

int main() {
	const char* command = "py ../../app/main.py";
	int result = system(command);
	
	if (result == -1){
		return -1;
	}
	
	return 0;
}
