#include<bits/stdc++.h>
using namespace std;
/*
INPUT:
BEG01: ECONOMIA GENERAL
A T SA 08-10 A2-159 BRAVO, Cesar
A P SA 10-12 A2-259 BRAVO, Cesar
B T SA 13-15 A2-159 BRAVO, Cesar
B P SA 15-17 A2-239 BRAVO, Cesar

BIC01: INTRODUCCION A LA COMPUTACIÓN
A T VI 14-15 CCLAB-2A CASTAÑEDA, Ricardo
A P VI 15-17 CCLAB-3A CASTAÑEDA, Ricardo
B T JU 14-15 CCLAB-3A ORTIZ, Jorge
B P JU 15-17 CCLAB-3A ORTIZ, Jorge
C T LU 14-15 CCLAB-A MORENO, Carlos
C P LU 15-17 CCLAB-2A MORENO, Carlos
D T MA 16-17 CCLAB-A MORENO, Carlos
D P MA 17-19 CCLAB-2B MORENO, Carlos

BRN01: REALIDAD NACIONAL, CONSTITUCIÓN
A T LU 17-19 A2-239 COGORNO, Carlos
A P MA 17-19 A2-360 COGORNO, Carlos
*/
vector <vector <int> > answ;
vector <pair <int,int> > comparador;
unordered_map <string,int> days;
bool cmp(pair <int,int> a, pair<int,int> b){
	if(a.first >= b.first) return false;
	else return true;
}
int main(){
  ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	days["LU"] = 0,days["MA"] = 1, days["MI"]=2,days["JU"]=3,days["VI"]=4, days["SA"]=5;	
	unordered_map <string, unordered_map<string, unordered_map<string, int[24] > > > ALL;
	vector <pair<string,int> > AUXCursos;
	while(true){
		string Cursos;
		getline(cin,Cursos);
		if(Cursos.size() == 0) break;
		AUXCursos.push_back(make_pair(Cursos,0));
		unordered_map <string, unordered_map<string,int[24]> > mm;
		set <string> cantSec;
		while(true){
			string Secciones = "";
			string tst;
			getline(cin,tst);
			int posx = 0;
			if(tst.size() == 0) break;
			if(tst == "*") break;
			for(int i=posx; i<tst.size(); i++){
				if(tst[i] == ' '){
					posx = i+1;
					break;
				}
				Secciones += tst[i];
			}
			bool DetectMultiSecciones = false;
			string MultiSecciones = "";
			if(Secciones.size() > 1){
				DetectMultiSecciones = true;
				for(int i=0; i<Secciones.size(); i++){
					if(i%2 == 1) continue;
					MultiSecciones += Secciones[i];
					string sx = "";
					sx += Secciones[i];
					cantSec.insert(sx);
				}
			}
			else cantSec.insert(Secciones);
			for(int i=posx; i<tst.size(); i++){
				if(tst[i] == ' '){
					posx = i+1;
					break;
				}
			}
			string Dia = "";
			for(int i=posx; i<tst.size(); i++){
				if(tst[i] == ' '){
					posx = i+1;
					break;
				}
				Dia += tst[i];
			}
			string Hora = "";
			for(int i=posx; i<tst.size(); i++){
				if(tst[i] == ' '){
					posx = i;
					break;
				}
				Hora += tst[i];
			}
			string aux = "";
			for(int i=0; i<2; i++) aux += Hora[i];
			int l = stoi(aux);
			aux = "";
			for(int i=3; i<5; i++) aux += Hora[i];
			int r = stoi(aux);
			if(DetectMultiSecciones){
				for(int j=0; j<MultiSecciones.size(); j++){
					for(int i=l; i<=r-1; i++){
						string SectionC = "";
						SectionC += MultiSecciones[j];
						mm[SectionC][Dia][i] = 1;
					}
				}
			}
			else{
				for(int i=l; i<=r-1; i++){
					mm[Secciones][Dia][i] = 1;
				}
			}
		}
		AUXCursos[AUXCursos.size()-1].second = cantSec.size();
		ALL[Cursos] = mm;		
	}
	int it[AUXCursos.size()-1];
	for(int i=0; i<AUXCursos.size(); i++) it[i] = 0;
	while(true){
		int contc = 0;
		int horario[24][7];
		for(int i=0; i<24; i++){
			for(int j=0;j<7; j++) horario[i][j] = 0;
		}
		for(int k=0; k<AUXCursos.size(); k++){
			string CurrentCourse = AUXCursos[k].first;
			int contk = 0;
			string CurrentSection = "";
			for(auto ll:ALL[CurrentCourse]){
				if(contk == it[k]){
					CurrentSection += ll.first;
					break;
				}
				contk++;
			}
			for(auto i:ALL[CurrentCourse][CurrentSection]){
				string CurrentDay = i.first;
				for(int x=0; x<24; x++) horario[x][days[CurrentDay]] += i.second[x];
			}
			for(int i=0;i<24;i++){
				for(int j=0; j<7; j++){
					if(horario[i][j] != 0) contc += horario[i][j]-1;	
				}
			}
		}
		vector <int> awa;
		for(int i=0; i<AUXCursos.size(); i++) awa.push_back(it[i]);
		answ.push_back(awa);
		comparador.push_back(make_pair(contc,answ.size()-1));
		it[0]++;
		for(int i=1; i<AUXCursos.size(); i++){
			if(it[i-1] >= AUXCursos[i-1].second){
				it[i]++;
				it[i-1] = 0;	
			}
			else break;
		}
		if(it[AUXCursos.size()-1] >= AUXCursos[AUXCursos.size()-1].second) break;
	}
	sort(comparador.begin(), comparador.end(), cmp);
	for(int i=0; i<comparador.size(); i++){
		cout << "Cruces = " << comparador[i].first << '\n';
		int posix = comparador[i].second;
		for(int j=0; j<answ[posix].size(); j++){
			cout << AUXCursos[j].first << ":";
			string answsec = "";
			int contb = 0;
			for(auto k:ALL[AUXCursos[j].first]){
				if(contb == answ[posix][j]){
					answsec += k.first;
					break;
				}
				contb++;
			}
			cout << answsec << '\n';
		}
		cout << '\n';
	}
	return 0;
}
