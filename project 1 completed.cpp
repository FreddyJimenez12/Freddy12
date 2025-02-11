// Project 1.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <string>
#include <chrono>
#include <ctime>
//#include <sysinfoapi.h>
#include <vector>

using namespace std;
//starting vector
vector <int> InirtV;

//sub vector
vector <int> twoTh;
vector <int> fourTh;
vector <int> sixTh;
vector <int> eightTh;
vector <int> oneM;




//generate number sort
void numberStore() {
    InirtV.reserve(10000000);
    for (int i = 0; i < 5; i++) {
        for (int v = 0; v < 10000000; v++) {
            int const numberList = (rand() * rand()) % 1000000;
            InirtV.push_back(numberList);

        }
    }
}

//put all element into vector
void twoth(vector <int>& twoTh) {
    twoTh.reserve(200000);

    for (int i = 0; i < twoTh.capacity(); i++) {
        twoTh.push_back(InirtV[i]);
    }

}
void fourth(vector <int>& fourTh) {
    fourTh.reserve(400000);
    for (int i = 0; i < fourTh.capacity(); i++) {
        fourTh.push_back(InirtV[i]);
    }
}

void sixth(vector <int>& sixTh) {
    sixTh.reserve(600000);
    for (int i = 0; i < sixTh.capacity(); i++) {
        sixTh.push_back(InirtV[i]);
    }
}
void eightth(vector <int>& eightTh) {
    eightTh.reserve(800000);
    for (int i = 0; i < eightTh.capacity(); i++) {
        eightTh.push_back(InirtV[i]);
    }
}
void onem(vector <int>& oneM) {
    oneM.reserve(1000000);
    for (int i = 0; i < oneM.capacity(); i++) {
        oneM.push_back(InirtV[i]);
    }
}



//first algorthim
//check for the max of the heap
class Heap {
public:
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

    //heapify the random array number
    void buildSort(vector<int>& a, int n) {
        for (int i = n / 2 - 1; i >= 0; i--) {
            maxHeap(a, i, n);
        }
    }
    //heeapsort the vector
    void heapSort(vector<int>& a, int n) {

        buildSort(a, n);
        for (int i = n - 1; i > 0; i--) {
            swap(a[0], a[i]);
            maxHeap(a, 0, i);
        }
      
    }
    void disp100(vector<int>& a) {

        for (int i = 0; i < 100; i++) {
            cout << a[i] << " ";
        }
        cout << endl;
    }
private:
    int n = 0;
};

void swapsort(vector<int>& a, int loc1, int loc2) {
    int temp = a[loc1];
    a[loc1] = a[loc2];
    a[loc2] = temp;
}
//selective sort
    void selectSort(vector<int>& a) {

        int asize = sizeof(a) / sizeof(a[0]);
        for (int i = 0; i < asize - 1; i++) {
            int minloc = i;
            for (int j = i + 1; j < asize; j++) {
                if (a[j] < a[minloc]) {
                    minloc = j;
                }

            }
            if (minloc != i) {
                swapsort(a, i, minloc);
            }
        }
    }
// insert sort
    void insertSort(vector<int>& a) {
        int asize = sizeof(a) / sizeof(a[0]);
        for (int i = 1; i < asize; i++) {
            int j = i;
            while (j > 0 && a[j - 1] > a[j]) {
                swapsort(a, j, j - 1);
                j = -1;
            }
        }
    }



//bubble sort
void bubbleSort(vector<int>& a) {
     int asize = sizeof(a) / sizeof(a[0]);
        for (int i = 1; i < asize; i++) {
            for (int j = 0; j < asize - 1; j++) {
                if (a[j] > a[j + 1]) {
                    swapsort(a, j, j + 1);
                    
                }
            }
        }
    }


//quick sort
int partition(vector<int>& a, int low, int high) {
    int pivot = a[high];
    int pindex = (low - 1);
    for (int j = low; j <= high - 1; j++) {
        if (a[j] <= pivot) {
            pindex++;
            swap(a[pindex], a[j]);
            for (int i = low; i <= high - 1; i++)
            {
                cout << a[i] << endl;
            }
            cout << endl;
        }
        swap(a[pindex + 1], a[high]);
        
    }
    swap(a[pindex + 1], a[high]);
    return(pindex + 1);
}

//quick sort
void quickSort(vector<int>& a, int low, int high) {

    for (int i = low; i < high; i++) {
        cout << a[i] << endl;
    }
    if (low < high) {
        int pindex = partition(a, low, high);
        for (int i = low; i < pindex; i++) {
        }
    }
}



//display the first 100 element in the vector
void disp100(vector<int>& a) {
 
    for (int i = 0; i < 100; i++) {
        cout << a[i] << " ";
    }
    cout << endl;
}
//display the whole element
void disp(vector<int>& a) {
    for (int i = 0; i < a.size(); i++) {
        cout << a[i] << " ";
    }
    cout << endl;
}

//start the heapsort
void algo1(vector<int>& a) {
    
    cout << "Heap Sort: " << endl;
        Heap* H = new Heap();
        H->disp100(a);
        auto start = chrono::system_clock::now();
        H->buildSort(a, 100);
        H->heapSort(a, 100);
        auto end = chrono::system_clock::now();
        cout << "*************" << endl;
        chrono::duration<float> second = end - start;
        cout << "run time is: " << second.count() << endl;
    
}
//start the select sort
void algo2(vector<int>& a) {
    cout << "selective sort: " << endl;
        disp100(a);
        auto start = chrono::system_clock::now();
        selectSort(a);
        auto end = chrono::system_clock::now();
        cout << "*******************" << endl;
        chrono::duration<float> second = end - start;
        cout << "run time is: " << second.count() << endl;

    
}
//start the insert sort
void algo3(vector<int>& a) {
    cout << "Insert sort: " << endl;
        disp100(a);
        auto start = chrono::system_clock::now();
        insertSort(a);
        auto end = chrono::system_clock::now();
        cout << "*******************" << endl;
        chrono::duration<float> second = end - start;
        cout << "run time is: " << second.count() << endl;

    
}
//start the bubble sort
void algo4(vector<int>& a) {
    cout << "Bubble sort: " << endl;
        disp100(a);
        auto start = chrono::system_clock::now();
        bubbleSort(a);
        auto end = chrono::system_clock::now();
        cout << "*******************" << endl;
        chrono::duration<float> second = end - start;
        cout << "run time is: " << second.count() << endl;

    
}
//start the quick sort
void algo5(vector<int>& a) {

    cout << "quick sort: " << endl;
        
        disp100(a);
        auto start = chrono::system_clock::now();
        quickSort(a, 0, 0);
        auto end = chrono::system_clock::now();

        cout << "**********************" << endl;
        chrono::duration<float> second = end - start;
        cout << "run time is: " << second.count() << endl;
}





int main() {
    //calling vector function to insert number
    numberStore();
    twoth(twoTh);
    fourth(fourTh);
    sixth(sixTh);
    eightth(eightTh);
    onem(oneM);

    //first algroithm
    algo1(twoTh); 
    cout <<  endl;
    algo1(fourTh);
    cout << endl;
    algo1(sixTh);
    cout << endl;
    algo1(eightTh);
    cout << endl;
    algo1(oneM);
    cout << endl;

    //second algroithm
    algo2(twoTh);
    cout << endl;
    algo2(fourTh);
    cout << endl;
    algo2(sixTh);
    cout << endl;
    algo2(eightTh);
    cout << endl;
    algo2(oneM);
    cout << endl;

    //thrid algroithm
    algo3(twoTh);
    cout << endl;
    algo3(fourTh);
    cout << endl;
    algo3(sixTh);
    cout << endl;
    algo3(eightTh);
    cout << endl;
    algo3(oneM);
    cout << endl;

    //fourth algroithm
    algo4(twoTh);
    cout << endl;
    algo4(fourTh);
    cout << endl;
    algo4(sixTh);
    cout << endl;
    algo4(eightTh);
    cout << endl;
    algo4(oneM);
    cout << endl;

    //fifth algroithm
    algo5(twoTh);
    cout << endl;
    algo5(fourTh);
    cout << endl;
    algo5(sixTh);
    cout << endl;
    algo5(eightTh);
    cout << endl;
    algo5(oneM);
    cout << endl;



    //update vector
    /*for (int i : InirtV) {
        cout << i << endl;
    }
    */
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
