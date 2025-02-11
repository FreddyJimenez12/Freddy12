// lab 10.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
using namespace std;

class binaryTree {
public: 
	binaryTree() : data(0), left(nullptr), right(nullptr){}
	binaryTree(int d) : data(d), left(nullptr), right(nullptr) {}
	~binaryTree() {}
	int data;
	binaryTree* left;
	binaryTree* right;
	string item;
	

};

bool checkTree(binaryTree* root, string item) {
	binaryTree* runner;
	runner = root;
	while (true) {
		if (runner == NULL) {
			return false;
			cout << "no leaf" << endl;
		}
		else if (item == runner->item) {
			return true;//found leaf
		}
		else if (item < runner->item) {
			runner = runner->left;//go left if found
		}
		else { 
			runner = runner->right;//go right if found
		}
	}
}
void insert(binaryTree* root, int data) {
	if (root == NULL) {
		root = new binaryTree(data);
	}
	else {
		binaryTree* current;
		if (data <= root->data) {
			insert(root->left, data);
			root->left = root;
		}
		else {
			insert(root->right, data);
			root->right = root;

		}
	}
	cout << root << endl;
}//insert as a recursive
void insertRecursive(binaryTree*& root, int data) {
	if (root == nullptr) {
		root = new binaryTree(data);
	}
	else if (root->data == data) {
		cout << "value is already regester." << endl;
	}
	else if (data < root->data) {
		insertRecursive(root->left, data);
	}
	else {
		insertRecursive(root->right, data);
	}
}
//insert as a iterative
void insertIterative(binaryTree*& root, int data) {
	if (root == nullptr) {
		root = new binaryTree(data);
	}
	else {
		binaryTree* current = root;
		binaryTree* patent = nullptr;
		int direction = 0;
		while(current != nullptr){
			patent = current;
			if (data < current->data) {
				current = current->left;
			}
			else {
			current = current->right;
			}
			if (patent == NULL) {
				patent = root;
			}
			else if (data < patent->data) {
				patent->left = root;
			}
			else { patent->right = root; }
		}
		
	}
}





//check for children
int checkChildren(binaryTree* root, int data) {
	data = 0;
	if (root == NULL) {
		return 0;
	}
	if (root->left != NULL) {
		data++;
	}
	if (root->right != NULL) {
		data++;
	}
	return data;
}
//search as a recursive
bool searchRecursive(binaryTree* root, int data) {
	if (root == nullptr)
		return false;
	else if (root->data == data) {
		return true;
	}
	else if (data < root->data) {
		searchRecursive(root->left, data);
	}
	else { searchRecursive(root->right, data); }

}
//search as a iterative
bool searchIterative(binaryTree* root, int data) {
	if (root == nullptr) {
		return false;
	}
	else {
		binaryTree* current = root;
		bool found = false;
		while ((!found) && (current != nullptr)) {
			if (current->data == data) {
				found == true;
			}
			else if (data < current->data) {
				current = current->left;
			}
			else { current = current->right; }
		}
	}
}
//delete children and node
binaryTree* deleteAll(binaryTree* root, int data) {
	if (root == nullptr) {
		return nullptr;

	 }
	if (data < root->data) {
		root->left = deleteAll(root->left, data);
	}
	else if (data > root->data) {
		root->right = deleteAll(root->right, data);
	}
	else {
		if (root->left == nullptr && root->right == nullptr) {
			delete root;
			root = nullptr;
		}
		else if (root->left == nullptr) {
			binaryTree* temp = root;
			root == root->right;
			delete temp;
		}
		else if (root->right == nullptr) {
			binaryTree* temp = root;
			root = root->left;
			delete temp;
		}
		else {
			binaryTree* temp = (root = root->right);
			root->data = temp->data;
			root->right = deleteAll(root->right, temp->data);

		}
	}
	return root;
	
}
//delete all tree
void destroyTree(binaryTree* root) {
	if (root != NULL) {
		destroyTree(root->left);
		destroyTree(root->right);
		delete root;
	}
}

int main() {
	binaryTree* l = nullptr;
	insert(l, 30);
	insert(l, 60);
	insert(l, 50);
	insert(l, 30);
	insert(l, 80);
	insert(l, 90);
	insert(l, 10);
	cout << insert << endl;
	checkChildren(l, 60);
	deleteAll(l, 30);
	insertIterative(l, 100);
	insertRecursive(l, 20);
	searchIterative(l, 30);
	searchRecursive(l, 90);
	destroyTree(l);


	return 0;


	
	



};
	

// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
