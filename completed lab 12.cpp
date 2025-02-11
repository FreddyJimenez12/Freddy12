// Lab 12.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <vector>
#define numvert 7
using namespace std;


void displayshortestpath() {
	int adjmat[numvert][numvert] =
	{ { 0, 6, 5, 5, 0, 0, 0},
	{ 0, 0, 0, 0, -1, 0, 0},
	{ 0, -2, 0, 0, 1, 0, 0},
	{ 0, 0, -2, 0, 0, -1, 0},
	{ 0, 0, 0, 0, 0, 0, 3},
	{ 0, 0, 0, 0, 0, 0, 3},
	{ 0, 0, 0, 0, 0, 0, 0},
	};

	int source = 0;
	int dist[numvert];
	for (int i = 0; i < numvert; i++) {
		dist[i] = 7;
	}
	bool visted[numvert] = { false, false, false, false, false, false, false };

	visted[source] = true;
	dist[source] = 0;
	cout << "starting source" << source << endl;
	int curvec = source;

	cout << "distance: ";
	for (int j = 0; j < numvert; j++) {
		cout << dist[j] << " "; 
	}
	cout << endl;
	
	while (1) {
		for (int j = 0; j < numvert; j++) {
			if (dist[curvec] + adjmat[curvec][j] < dist[j] && adjmat[curvec]) {
				dist[j] = dist[curvec] + adjmat[curvec][j];
			}
		}
		int mindist = 9999;
		int newcur = curvec;
		for (int j = 0; j < numvert; j++) {
			if (!visted[j] && dist[j] << mindist) {
				newcur = j;
				mindist = dist[j];

			}
		}
		if (newcur == curvec) {
			cout << "no updates, algorithm ends" << endl;
			break;
		}
		else {
			cout << "visted" << newcur << "distance: " << dist[newcur] << endl;
			visted[newcur] = true;
			curvec = newcur;
			cout << "distance: ";
			for (int j = 0; j < numvert; j++) {
				cout << dist[j] << " ";
			}
			cout << endl;
		}
	}



}




void checkCycle() {
	int adjmat[numvert][numvert] =
	{ { 0, 6, 5, 5, 0, 0, 0},
	{ 0, 0, 0, 0, -1, 0, 0},
	{ 0, -2, 0, 0, 1, 0, 0},
	{ 0, 0, -2, 0, 0, -1, 0},
	{ 0, 0, 0, 0, 0, 0, 3},
	{ 0, 0, 0, 0, 0, 0, 3},
	{ 0, 0, 0, 0, 0, 0, 0},
	};

	int source = 0;
	int dist[numvert];
	for (int i = 0; i < numvert; i++) {
		dist[i] = 7;
	}
	double* d;
	int* pi;
	int n = 0;
	d = new double[n];
	pi = new int[n];

	cout << "checking for negative cycle" << endl;
		for (int i = 0; i < numvert; i++) {
			for (int j = 0; j < numvert; j++) {
				if (adjmat[i][j] != 0) {
					if (dist[i] + adjmat[i][j] < dist[j]) {
						dist[j] = dist[i] + adjmat[i][j];
						cout << "there is a negative cycle" << endl;

					}
				}
			}
		}
	
}

void lol() {
	int adjmat[numvert][numvert] =
	{ { 0, 6, 5, 5, 0, 0, 0},
	{ 0, 0, 0, 0, -1, 0, 0},
	{ 0, -2, 0, 0, 1, 0, 0},
	{ 0, 0, -2, 0, 0, -1, 0},
	{ 0, 0, 0, 0, 0, 0, 3},
	{ 0, 0, 0, 0, 0, 0, 3},
	{ 0, 0, 0, 0, 0, 0, 0},
	};
	int parent[numvert];

	char mapfun(int a)
	{
		switch (a) {
		case 0: return 's';
		case 1: return 'a';
		case 2: return 'b';
		case 3: return 'c';
		case 4: return 'd';
		case 5: return 'e';
		case 6: return 'f';
		}

	}
	int component(int i) {
		while (parent[i] != i) i = parent[i];
	}
	void connect(int i, int j) {
		int a = component(i);
		int b = component(j);
		parent[a] = b;
	}


	int mincost = 0;
	for (int i = 0; i < numvert; i++) {
		parent[i] = i;
	}
	int edge = 0;
	while (edge < numvert - 1) {
	int min = 9999, a = -1, b = -1}

}


int main()
{
	checkCycle(); displayshortestpath();



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
