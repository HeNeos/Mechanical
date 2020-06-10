#pragma GCC optimize("Ofast")
#pragma GCC target("sse,sse2,sse3,ssse3")

#include <bits/stdc++.h>
#include </home/heneos/Sparse-Matrix/src/SparseMatrix/SparseMatrix.cpp>
using namespace std;
#define mp make_pair
#define pb push_back
#define FIFO ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0)
#define MOD 1000000007
typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll,ll> pll;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<pii> vii;
typedef vector<pll> vll;

vector <double> K;
vector <double> A;
vector <int> NodesCondition;
vector <int> ForcesCondition;
int NumberOfElement;
int Nodes;
#define vvd vector < vector <double> >


vvd multiply(vvd &a, vvd &b){
	vvd x;
	int r = a.size();
	int c = b[0].size();
	for(int i=0; i<r; i++){
		vector <double> aux;
		for(int j=0; j<c; j++) aux.pb(0);
		x.pb(aux);
	}
	for(int i=0; i<r; i++){
		for(int j=0; j<c; j++){
			double ac = 0;
			for(int k=0; k<b.size(); k++) ac += a[i][k]*b[k][j];
			x[i][j] = ac;
		}
	}
	return x;
}

vvd conjugate_grad(vvd A, vvd b){
	int n = b.size();
	int what = A.size();
	int gg = A[0].size();
	vvd x;
	for(int i=0; i<n; i++){
		vector <double> aux;
		aux.pb(0);
		x.pb(aux);
	}
	vvd r = multiply(A, x);
	SparseMatrix <double> nA(what,gg);
	for(int i=0; i<what; i++){
		for(int j=0; j<gg; j++){
			nA.set(A[i][j],i+1,j+1);
		}
	}
	vector <double> p;
	double r_k_norm = 0;
	for(int i=0; i<n; i++){
		r[i][0] -= b[i][0];
		r_k_norm += (r[i][0]*r[i][0]);
		p.pb(-r[i][0]);
	}
	for(int i=0; i<2*n; i++){
		vector <double> Ap = nA*p;
		double aux = 0;
		for(int i=0; i<n; i++) aux += p[i]*Ap[i];
		double alpha = r_k_norm/aux;
		for(int i=0; i<n; i++){
			x[i][0] += alpha*p[i];
			r[i][0] += alpha*Ap[i];
		}
		double r_kplus_norm = 0; 
		for(int i=0; i<n; i++){
			r_kplus_norm += (r[i][0]*r[i][0]);
		}
		if(sqrt(r_kplus_norm) < 1e-6){
			break;
		}
		double beta = r_kplus_norm/r_k_norm;
		r_k_norm = r_kplus_norm;
		for(int i=0; i<n; i++){
			p[i] = beta*p[i]-r[i][0];
		}
	}
	return x;
}




void UBoundaryCondition(vvd &nU, double u, int i){
	nU[i][0] = u;
	NodesCondition.pb(i);
}

void FBoundaryCondition(vvd &nF, double f, int i){
	nF[i][0] = f;
	ForcesCondition.pb(i);
}

void AssemblyStiffness(vvd &nS, double k, int i){
	int j = i+1;
	nS[i][i] += k;
	nS[i][j] += -k;
	nS[j][i] += -k;
	nS[j][j] += k;
}


void Initialize(vvd  &nS, vvd &nU, vvd &nF){
	for(int i=0; i<Nodes; i++){
		nU[i][0] = -1;
		nF[i][0] = -1;
	}
	for(int i=0; i<NumberOfElement; i++){
		AssemblyStiffness(nS, K[i], i);
		
	}
}

vvd PreSolvingS(vvd &S){
	int nsize = Nodes-NodesCondition.size();
	vvd newS;
	for(int i=0; i<nsize; i++){
		vector <double> aux;
		for(int j=0; j<nsize; j++) aux.pb(0);
		newS.pb(aux);
	}
	int contr = -1;
	for(int i=0; i<Nodes; i++){
		int contc = -1;
		bool flagr = false;
		for(int k=0; k < NodesCondition.size(); k++){
			if(i == NodesCondition[k]){
				flagr = true;
				break;
			}
		}
		if(flagr) continue;
		contr += 1;
		for(int j=0; j<Nodes; j++){
			bool flagc = false;
			for(int k=0; k<NodesCondition.size(); k++){
				if(j == NodesCondition[k]){
					flagc = true;
					break;
				}
			}
			if(flagc) continue;
			contc += 1;
			newS[contr][contc] = S[i][j];
		}
	}
	return newS;
}

vvd PreSolvingF(vvd nF, vvd &nS, vvd &nU){
	int nsize = Nodes-NodesCondition.size();
	vvd newF;
	for(int i=0; i<nsize; i++){
		vector <double> aux;
		aux.pb(0);
		newF.pb(aux);
	}
	int contr = -1;
	for(int i=0; i<Nodes; i++){
		bool flagr = false;
		for(int k=0; k<NodesCondition.size(); k++){
			if(i == NodesCondition[k]){
				flagr = true;
				break;
			}
		}
		if(flagr){
			for(int k=0; k<Nodes; k++) nF[k][0] = nF[k][0] - nS[k][i]*nU[i][0];
			continue;
		}
	}
	for(int i=0; i<Nodes; i++){
		bool flagr = false;
		for(int k=0; k<NodesCondition.size(); k++){
			if(i == NodesCondition[k]){
				flagr = true;
				break;
			}
		}
		if(flagr) continue;
		contr++;
		newF[contr][0] = nF[i][0];
	}
	return newF;
}

void Solve(vvd &nS, vvd &nU, vvd &nF){
	vvd newS = PreSolvingS(nS);
	vvd newF = PreSolvingF(nF,nS,nU);
	
	vvd u = conjugate_grad(newS, newF);
	
	int contr = -1;

	for(int i=0; i<Nodes; i++){
		bool flagr = false;
		for(int k=0; k<NodesCondition.size(); k++){
			if(i == NodesCondition[k]){
				flagr = true;
				break;
			}
		}
		if(flagr) continue;
		contr++;
		nU[i][0] = u[contr][0];
	}
	nF.clear();
	nF = multiply(nS,nU);
}

int main(){
	Nodes = 100;
	Nodes = 2*Nodes+1;
	double E = 2*1e5;
	double L = 1500;
	double b0 = 1000;
	double bf = 0;
	double e = 120;
	double P = 50000;
	double y = 0.0764532e-3;


	double dL = L/(Nodes-1);

	for(int i=0; i<Nodes; i++){
		double b = b0-i*((b0-bf)/(Nodes-1));
		double nb = b0-(i+1)*(b0-bf)/(Nodes-1);
		b = ((b+nb)*e)/2.0;
		
		A.pb(b);
	}
	
	for(int i=0; i<Nodes-1; i++) K.pb(E*A[i]/dL);

	
	NumberOfElement = Nodes-1;

	vvd StiffnessMatrix;

	for(int i=0; i<Nodes; i++){
		vector <double> aux;
		for(int j=0; j<Nodes; j++) aux.pb(0);
		StiffnessMatrix.pb(aux);
	}
	
	
	vvd U;
	vvd F;
	for(int i=0; i<Nodes;i++){
		vector <double> aux;
		aux.pb(0);
		U.pb(aux);
		F.pb(aux);
	}
	
	Initialize(StiffnessMatrix,U,F);
	UBoundaryCondition(U,0,0);
	
	for(int i=1; i<Nodes; i++){
		if(i%2 == 1){
			double W = y*(A[i]+A[i-1])*(dL);
			FBoundaryCondition(F,W,i);
		}
		else{
			FBoundaryCondition(F,0,i);
		}
	}
	
	
	if((NumberOfElement/2)%2 == 1){
		double W = y*(A[NumberOfElement/2]+A[NumberOfElement/2-1])*dL;
		FBoundaryCondition(F,W+P,NumberOfElement/2);
	}
	else{
		FBoundaryCondition(F,P,NumberOfElement/2);
	}

	
	Solve(StiffnessMatrix, U, F);
	for(int i=0; i<U.size(); i++){
		for(int j=0; j<U.size(); j++) printf("%+.5e\t",StiffnessMatrix[i][j]);
		cout << '\n';
	}	
	cout << "Displacements:\n";
	for(int i=0; i<U.size(); i++) printf("%+.12e\n",U[i][0]);
	cout << "Forces:\n";
	for(int i=0; i<F.size(); i++) printf("%+.12e\n",F[i][0]);
	
	return 0;
}
