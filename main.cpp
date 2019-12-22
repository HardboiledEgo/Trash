#include <iostream>
#include <algorithm>
#include <time.h>
#include <std_lib_facilities.h>

class PassGen {


public:
	void displayMessage()
	{
		setlocale(0, "");
		int passLenght;
		int numOfPasswords;
		string filename;

		cout << "¬ведите длину парол€ дл€ генерации: ";
		cin >> passLenght;
		cout << "¬ведите количество паролей дл€ генерации: ";
		cin >> numOfPasswords;
		cout << "Ѕудет сгенерировано паролей: " << numOfPasswords << "." << endl;
		cout << endl;
		cout << "¬ведите им€ файла дл€ записи: ";
		cin >> filename;
		filename += ".txt";

		std::ofstream outFile(filename);

		for (int k = 0; k < numOfPasswords; k++) {
			for (int i = 0; i < passLenght; ++i) {
				numOfChars(passLenght);
				passGenerator(passLenght);
				outFile << password[i];
			}
			outFile << endl;
		}
		outFile.close();

		cout << "ѕароли успешно сгенерированы и записаны в файл " << filename << "" << endl;
	}

	void passGenerator(int passLenght)
	{
		password = new char[passLenght];

		for (int i = 0; i < numOfNumbers; ++i) {
			password[i] = char(rand() % 10 + 48);
		}
		for (int i = numOfNumbers; i < numOfNumbers + numOfBigChars; ++i) {
			password[i] = char(rand() % 26 + 65);
		}
		for (int i = numOfNumbers + numOfBigChars; i < passLenght; ++i) {
			password[i] = char(rand() % 26 + 97);
		}
		std::random_shuffle(password, password + passLenght);
	}

	void numOfChars(int passLenght)
	{
		numOfSmallChars = rand() % passLenght;
		int charRandEnd = passLenght - numOfSmallChars;
		numOfBigChars = rand() % charRandEnd;
		numOfNumbers = passLenght - numOfSmallChars - numOfBigChars;
	}

private:
	int numOfSmallChars;
	int numOfBigChars;
	int numOfNumbers;
	char * password;
};

int main()
{
	srand(time(NULL));
	PassGen * pass = new PassGen;
	pass->displayMessage();
	system("pause");
	return 0;
}