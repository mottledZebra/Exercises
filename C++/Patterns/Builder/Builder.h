#pragma once

#include <iostream>

using namespace std;

class Builder
{
public:

  Builder(void)
  {
    cout << "constructor Builder" << endl;    
  }

  virtual ~Builder(void)
  {
    cout << "destructor Builder" << endl;    
  }

  virtual void reset() = 0;
  virtual void addPartA(int number) = 0;
  virtual void addPartB(char option) = 0;
  virtual void addPartC() = 0;
};

