//
//  MarkovGen.hpp
//  nighttest
//
//  Created by Jonathan Diamond on 2/2/16.
//  Copyright © 2016 CoreLocation. All rights reserved.
//

#ifndef MarkovGen_hpp
#define MarkovGen_hpp

#include <stdio.h>
#include <stdlib.h>     /* srand, rand */
#include <time.h>       /* time */
#include <map>
#include <vector>
#include <string>
#include <iostream>

class MarkovGen
{
private:
	std::vector<std::string> words;
	std::map<std::tuple<std::string,std::string>,std::vector<std::string>> triples;
public:
	MarkovGen(std::istream & inFile);
	std::string GenerateText(int len);
};

#endif /* MarkovGen_hpp */
