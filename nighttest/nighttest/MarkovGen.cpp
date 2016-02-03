//
//  MarkovGen.cpp
//  nighttest
//
//  Created by Jonathan Diamond on 2/2/16.
//  Copyright © 2016 CoreLocation. All rights reserved.
//

#include "MarkovGen.hpp"



MarkovGen::MarkovGen(std::istream & inFile)
{
	std::string word1;
	std::string word2;
	std::string word3;
	int count = 0;
	while (inFile >> word3)
	{
		words.push_back(word3);
		if(count>=2)
		{
			triples[std::make_tuple(word1,word2)].push_back(word3);
		}
		count++;
		std::swap(word1,word2);
		std::swap(word2,word3);
	}
}

std::string MarkovGen::GenerateText(int len)
{
	std::string text;
	srand (time(NULL));

	int seed = rand() % (words.size()-3);

	std::string w1 = words[seed];
	std::string w2 = words[seed+1];

	for(int i=0;i<len;i++) {
		text += " " + w1;
		auto matches = triples[std::make_tuple(w1,w2)];
		w1 = w2;
		w2 = matches[rand()%matches.size()];
	}
	return text;
}