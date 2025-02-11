// Project 2 redoing.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
using namespace std;


class Date {

public:
	Date() {}
	Date(int m, int d, int y) {}


		void date(int m, int d, int y) {
			int month, day, year;

			month = m;
			day = d;
			year = y;
			cout << "date: " << month << "/" << day << "/" << year << endl;
		}
	


};

struct node {
	string data; 
	node* next;
	 
};


class DLL {
private: node* head, *tail;

public:

	DLL() : head(nullptr), tail(nullptr) {}
	//addcategory for the netflix category
	void addCategory(string name) {
		node* newname = new node;
		newname->data = name;
		newname->next = nullptr;
		if (head == nullptr) {
			head = newname;
			tail = newname;
		}
		else {
			tail->next = newname;
			tail = newname;
		}

	}
	//remove category by name
	void removerCategory(string name) {
		if (head == nullptr) {
			cout << "no name" << endl;
			return;
		}
		else { 
			node* newname = head;
			newname->data = name;
		if (head->next == nullptr) {
			head = tail = nullptr;
		}
		else {
			while (newname->next->next != nullptr) {
				newname = newname->next;
			}
			tail = newname;
			tail->next = nullptr; 
		}
		}
	}
	//search category
	bool searchCategory(string name) {
		node* newname = head;
		newname->data = name;
		if (head == nullptr) {
			cout << "nothing to search" << endl;
			return false;
		}
		while (newname != nullptr) {
			if (newname->data == name) {
				return true;
				newname = newname->next;
				cout << newname->data << endl;
			}
		}return false;
	}
	//delete movie
	void deleteMovies(Date* date) {
		node* newname = head;
		newname = head;
		head = head->next;
		head->next = nullptr;
		delete newname;

	}
	//print all from category
	void printAll() {
		node* newname = new node;
		newname = head;
		while (newname != nullptr) {
			cout << newname->data << ", ";
			newname = newname->next;
			
		}
	
	}
		
		
		
		
		
		
		/*
		node* newname = nullptr;
		node* new_name = nullptr;

		newname = head;
		while (newname->next != nullptr) {
			new_name = newname;
			newname = newname->next;
		}
		tail = new_name;
		new_name->next = nullptr;
		delete newname;
		*/




};

class category {
private:
	node* head, * tail;
public:
	category(): head(nullptr), tail(nullptr) {}

	//add movie into category
	void addMovie(string name, Date* date) {
		node* newname = new node;
		newname->data = name, date;
		newname->next = nullptr;
	
		if (head == nullptr) {
			head = newname;
			head->next = head;
		}
		else {
			newname->next = head->next;
			head->next = newname;
			head = newname;
			
		}
	
	}
	//search for movie
	bool searchMovie(string name) {
		
		node* newname = new node;
		newname->data = name;
		newname->next = nullptr;

		if (newname == nullptr) {
			return false;
		}
		else { 
			bool found = false;
			while ((!found) && (newname != nullptr)) {
				if (newname->next == newname) {
					found = true;
				}
				else if (newname < newname->next) {
					newname = newname->next;

				}
				else { newname = newname->next; }
			}
		}

		if (newname != nullptr) {
			searchMovie(newname->data);
			cout << newname->data << " ";
			

		}
	}
	//return movie with index
	void getMovie(string name) {
		node* title = tail;
		int index = 0;
		title->data = name;
		title->next = nullptr;
		
		while (title != tail) {
			if (title->next->data == name) {
				index = index + 1;
			}
			index++;
			title = title->next;
		}
	}
	//print all movie 
	void printAllMovie() const{
		node* newname;
		if (head == nullptr) {
			cout << "No name" << endl;
		}
		else {
			newname = head->next;
			cout << "Name of movie: ";
			while (newname != head) {
				cout << newname->data << ", ";
				newname = newname->next;
			}
			cout << newname->data << endl;
		}
	}







};



int main()
{
	Date* time = new Date;
	DLL* netflix = new DLL;
	//set name into category
	netflix->addCategory("children");
	netflix->addCategory("action");
	netflix->addCategory("comedy");
	//search for children in category
	netflix->searchCategory("children");
	//print category
	netflix->printAll();
	cout << endl;
	//delete children from category and print it
	netflix->removerCategory("children");
	netflix->printAll();
	cout << endl;

	//delete movie before date
	netflix->deleteMovies(time);
	netflix->printAll();



	//print movie in category of children
	category* children = new category;
	children->addMovie("Barbie", time);
	time->date(1, 4, 2003);
	children->addMovie("Harry Potter", time);
	time->date(6, 4, 2013);
	children->addMovie("Lion Kind", time);
	time->date(5, 4, 203);
	children->searchMovie("action");
	
	children->printAllMovie();

	//print movie in action
	category* action = new category;
	action->addMovie("Mi 5", time);
	time->date(1, 4, 2003);

	action->addMovie("Rocky", time);
	time->date(1, 4, 2003);

	action->addMovie("Taken", time);
	time->date(1, 4, 2003);


	action->searchMovie("children");

	action->printAllMovie();

	//print out movie in Comedy
	category* Comedy = new category;
	Comedy->addMovie("Harold & Kumar", time);
	time->date(1, 4, 2003);
	Comedy->addMovie("Jerry McGuire", time);
	time->date(1, 4, 2003);

	Comedy->addMovie("Tuxedo", time);
	time->date(1, 4, 2003);


	Comedy->searchMovie("Tuxedo");

	Comedy->printAllMovie();

	




}

// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
