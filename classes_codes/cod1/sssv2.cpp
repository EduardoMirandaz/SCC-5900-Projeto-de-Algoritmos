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

bool sss(vi &conj, vi subc, int ind, int valor, int soma){
	// condicao de parada: consumi todos os elementos do conjuno
	if (soma == valor){
		imprime(subc);
		return true;
	}

	// vamos fazer uma poda: OU a soma > valor OU esgotei todos elementos
	//if (soma > valor || ind == conj.size())
	//   return;

	// itera para todos os elemetos
	for (int i = ind; i < conj.size(); ++i){
		if (soma <= valor || ind < conj.size()){
			subc.push_back(conj[i]);
			if (sss(conj, subc, i+1, valor, soma+conj[i]) == true  )
				return true;
			subc.pop_back();
		}
		
	}

	return false;

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