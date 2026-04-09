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

void sss(vi &conj, vi &subc, int ind, int valor, int soma){
	// condicao de parada: consumi todos os elementos do conjuno
	if (soma == valor){
		imprime(subc);
		return;
	}

	// vamos fazer uma poda: OU a soma > valor OU esgotei todos elementos
	if (soma > valor || ind == conj.size())
		return;

	// primeira acao: considerar o elemento
	subc.push_back(conj[ind]);
	sss(conj, subc, ind+1, valor, soma+conj[ind]);

	// segunda acao: despreza o elemento
	subc.pop_back();
	sss(conj, subc, ind+1, valor, soma);


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
	int valor;
	cin >> valor;



	// primeiro 0 >> o indice dos elementos do conh
    // valor: o limite 
    // segundo 0: a soma parcial
	sss(conjunto, subc, 0, valor, 0);
	return 0;
}