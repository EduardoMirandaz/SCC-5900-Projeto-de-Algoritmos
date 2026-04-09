#include <bits/stdc++.h>

using namespace std;

const int MAX = 10;

void gera(char *p, int ind){
	// condicao de parada: uma solucao foi encontrada
	if (ind == MAX){
		//cout << p << endl;
		return;
	}

	// usa todas as letras
	for (char c = 'a'; c <= 'z'; c++){
		p[ind] = c;
		gera(p, ind+1);
	}


}

int main(int argc, char const *argv[])
{

	char palavra[MAX+1];
	palavra[MAX] = '\0';


	gera(palavra, 0); // 0 corresponde ao indice da palavra
	return 0;
}