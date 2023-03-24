#include <iostream>
#include <vector>
#include <list>
#include <forward_list>
#include <set>

using namespace std;

int main()
{
   // vector <int> v = {10, 20, 30, 40};
   // list<int> v = {10, 20, 30, 40};
    //forward_list<int> v = {10, 20, 30, 40}; // This is a singly linked list
    set<int> v = {10, 20, 30, 40}; // This is a unique set of values and values cannot be modified but only displayed

    // change to these functions while using the list and vectors
   // v.push_back(50);
   // v.push_back(60);
   // v.pop_back();

   // change to these functions while using the forward list
   //  v.push_front(50);
   //  v.push_front(60);

   // change to these functions while using set
   v.insert(50);
   v.insert(60);


///////////////////////////////////////////////////////////////////////

    //vector<int>::iterator itr;
    //list<int>::iterator itr;
    //forward_list<int>::iterator itr;
    set<int>::iterator itr;

    cout << "Displaying value using Iterator" << endl;

    for (itr=v.begin(); itr!=v.end(); itr++)
        //cout << ++*itr << endl;
        cout << *itr << endl; // sets have unique elements and value of sets cannot be modified

///////////////////////////////////////////////////////////////////////

    cout << "Displaying value using For-each loop" << endl;
    for (int x: v)
        cout << x << endl;


/* Notice how by one simple class change the container is converted to doubly linked list */
/* Notice that Iterators are capable of modifying the values */
/* Sets have unique elements and value of sets cannot be modified */

    return 0;
}
