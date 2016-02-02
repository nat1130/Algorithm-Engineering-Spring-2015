#include <chrono>
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

string * readingFile(int size)
{
	ifstream myfile;
	myfile.open("beowulf.txt");

	string word = "";
	
	string *content = new string[size];

	for (int index = 0; index < size; index++)
	{
		myfile >> word;
		content[index] = word;
	}

	myfile.close();

	return content;
}

void in_place_selection_sort(string * content, int size) {

	int least;
	string temp;

	// waste time...
	for (int i = 0; i < (size -1) ; ++i)
	{
		least = i;
		for (int j = i + 1; j < size; ++j)
		{
			if (content[j] < content[least])
				least = j;
		}
		temp = content[i];
		content[i] = content[least];
		content[least] = temp;
	}

}

string * request(string user_input)
{
	string output = "loaded " + user_input + " lines from 'bewulf.txt'";
	cout << output << endl;
	int value = stoi(user_input);
	return readingFile(value);

}


void print(string * content)
{
	string current_content = "";
	int size = 0;
	for (int index = 0; index < 10; index++)
	{
		current_content += "[" + content[index] + "] ";
		size++;
	}
	cout << current_content << endl;
}

int main(int argc, char** argv) {
	
	string user_input = "";
	cout << "requested n = ";
	cin >> user_input;
	cin.clear();

	// Read file
	string *file = request(user_input);

	// View Unsorted
	cout << "first 10 words : " << endl;
	
	//print contents
	print(file);
	
	cout << "in place selection sort..." << endl;

	auto start = chrono::high_resolution_clock::now();
	// Run algorithm
	in_place_selection_sort(file, stoi(user_input));
	auto end = chrono::high_resolution_clock::now();

	//print contents
	print(file);

	int microseconds = chrono::duration_cast<chrono::microseconds>(end - start).count();
	double seconds = microseconds / 1E6;
	cout << "elapsed time: " << seconds << " seconds" << endl;

	cin.ignore(99, '\n');
	cin.ignore(99, '\n');

	return 0;
}


