#include <bits/stdc++.h>

using namespace std;

typedef vector<int> vi;

const int MAX = 10;

void imprime(vi &c){
	cout << "{ ";
	for (int i = 0; i < c.size(); ++i)
		cout << c[i] << " ";
	cout << "}" << endl;
}

void gera(vi &conj, vi &subc, int ind){
	// condicao de parada: consumi todos os elementos do conjuno
	if (ind == conj.size()){
		imprime(subc);
		return;
	}

	// primeira acao: considerar o elemento
	subc.push_back(conj[ind]);
	gera(conj, subc, ind+1);

	// segunda acao: despreza o elemento
	subc.pop_back();
	gera(conj, subc, ind+1);


}

int main(int argc, char const *argv[])
{
	int n;
	vi conjunto;
	vi subc;
	cin >> n;
	for (int i = 0; i < n; ++i){
		int v;
		cin >> v;
		conjunto.push_back(v);
	}


	gera(conjunto, subc, 0); // 0 corresponde ao indice dos elementos de conjunto
	return 0;
}