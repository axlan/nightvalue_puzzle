//
//  main.cpp
//  nighttest
//
//  Created by Jonathan Diamond on 2/2/16.
//  Copyright © 2016 CoreLocation. All rights reserved.
//

#include <iostream>
#include <fstream>
#include "MarkovGen.hpp"

int main(int argc, const char * argv[]) {
	// insert code here...
	std::ifstream test("/Users/jdiamond/personal/nightvale/combined");
	MarkovGen gen(test);

	std::string msg = gen.GenerateText(1000);
	
	std::cout << msg << std::endl;
    return 0;
}
