
#include <iostream>
#include <vector>
using namespace std;

class Myheap {
public:
	vector<int> a1;
	//check the for max heap from left to right.
	void maxHeap(vector<int>& a, int loc, int size) {
		int left, right, largest;
		left = 2 * loc + 1;
		right = 2 * loc + 2;
		largest = loc;
		if (left < size && a[left]> a[largest]) {
			largest = left;

		}
		if (right < size && a[right] > a[largest]) {
			largest = right;
		}
		if (largest != loc) {
			swap(a[loc], a[largest]);
			maxHeap(a, loc, size);
		}
	}
	//check for the min of heap.
	void minHeap(vector<int>& a, int loc) {
		int parent = (loc - 1) / 2;
		if (loc != 0 && a[parent] < a[loc]) {
			swap(a[loc], a[parent]);
			minHeap(a, parent);
		}
	}
	//randomize the heap
	void random(vector<int>&a) {
		for (int i = (a.size() - 1) / 2; i >= 0; i--) {
			maxHeap(a, i, a.size());
			disp(a);
		}
	
	}
	//heapify the random array number
	void buildSort(vector<int>& a) {
		int n = 0;
		for (int i = n / 2 - 1; i >= 0; i--) {
			maxHeap(a, i, n);
		}
	}
	//heeapsort the vector
	void heapSort(vector<int>& a) {
		int n = 0;
		buildSort(a);
		for (int i = n - 1; i > 0; i--) {
			swap(a[0], a[i]);
			maxHeap(a, 0, i);
		}
		disp(a);
		

	}//delete element from heap
	void deleteHeap(vector<int>& a) {
		swap(a[a.size() - 1], a[0]);
		disp(a);
		a.pop_back();
		disp(a);
		maxHeap(a, 0, a.size());
		disp(a);

	}
	
	//insert element into heap
	void insertHeap(vector<int>& a, int n) {
		a.push_back(n);
		disp(a);
		minHeap(a, a.size() - 1);
		disp(a);

	}
	//display element in heap
	void disp(vector<int>& a) {
		for (int i = 0; i < a.size(); i++) {
			cout << a[i] << " ";
		}
		cout << endl;
	}

private:
	int n = 0;
};

int main(){
	vector<int> a1 = { 10, 30, 40, 50, 60, 90, 100 };

	Myheap* H = new Myheap();
	
	H->random(a1);
	H->insertHeap(a1, 4);
	H->deleteHeap(a1);
	H->buildSort(a1);
	H->heapSort(a1);
};

   

