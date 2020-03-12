#pragma once
#include "creator.h"
#include "ConcreteProductB.h"

class ConcreteCreatorB : public Creator
{
public:

  ConcreteCreatorB(void)
  {
    cout << "constructor ConcreteCreatorB" << endl;    
  }

  ~ConcreteCreatorB(void)
  {
    cout << "destructor ConcreteCreatorB" << endl;    
  }

protected:
  Product* FactoryMethod()
  {
    cout << "ConcreteCreatorB creates ConcreteProductB by FactoryMethod()" << endl;
    return new ConcreteProductB;
  }
};

