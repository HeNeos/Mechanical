#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pii;
typedef pair<double,double> pdd;
typedef vector<double> vd;
#define u_map unordered_map
#define pb push_back
#define mp make_pair
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
vector <vi> answ;
vector <pii> cross;
u_map <string,int> days;
u_map <string, u_map <string, u_map <string, int[24] > > > ALL;
vector <pair<string,int> > data_courses;

bool cmp(pii a, pii b){
	if(a.first >= b.first) return false;
	else return true;
}

bool Read_input(string &line){
	getline(cin,line);
	if(!line.size()) return false;
	else return true;
}

void Read_section(int &posx, string &tst, string &s_p_c){
	for(int i=posx; i<(int)tst.size(); i++){
		if(tst[i] == ' '){
			posx = i+1;
			break;
		}
		s_p_c += tst[i];
	}
}

void Read_day(int &posx, string &tst, string &Day){
	for(int i=posx; i<(int)tst.size(); i++){
		if(tst[i] == ' '){
			posx = i+1;
			break;
		}
		Day += tst[i];
	}
}

void Read_hour(int &posx, string &tst, string &Hour){
	for(int i=posx; i<(int)tst.size(); i++){
		if(tst[i] == ' '){
			posx = i;
			break;
		}
		Hour += tst[i];
	}
}
void Read_SE(int &l, int &r, string &Hour){
	string aux = "";
	for(int i=0; i<2; i++) aux += Hour[i];
	l = stoi(aux);
	aux = "";
	for(int i=3; i<5; i++) aux += Hour[i];
	r = stoi(aux);
}

void Insert_MultiSections(string &SPC, bool &DM, string &MS, set <string> &AS){
	if(SPC.size() > 1){
		DM = true;
		for(int i=0; i<(int)SPC.size(); i+=2){
			MS += SPC[i];
			string aux = "";
			aux += SPC[i];
			AS.insert(aux);
		}
	}
	else AS.insert(SPC);
}

void Add_sections(bool &DMS, string &MS, int &l, int &r, string &Day, string &SPC, u_map <string, u_map <string,int[24]> > &m){
	if(DMS){
		for(int j=0; j<(int)MS.size(); j++){
			for(int i=l; i<=r-1; i++){
				string current_section = "";
				current_section += MS[j];
				m[current_section][Day][i] = 1;
			}
		}
	}
	else{
		for(int i=l; i<=r-1; i++){
			m[SPC][Day][i] = 1;
		}
	}
}

void Fill_schedule(int &contc, vi &it){
	int current_schedule[24][7];
	for(int i=0; i<24; i++){
		for(int j=0; j<7; j++) current_schedule[i][j] = 0;
	}
	for(int k=0; k<(int)data_courses.size(); k++){
		string current_course = data_courses[k].first;
		int contk = 0;
		string current_section = "";
		for(auto i:ALL[current_course]){
			if(contk == it[k]){
				current_section += i.first;
				break;
			}
			contk++;
		}	
		for(auto i:ALL[current_course][current_section]){
			string current_day = i.first;
			for(int x=0; x<24; x++) current_schedule[x][days[current_day]] += i.second[x];
		}
		for(int i=0; i<24; i++){
			for(int j=0; j<7; j++){
				if(current_schedule[i][j] != 0) contc += current_schedule[i][j]-1;
			}
		}
	}
}

void output(){
	sort(cross.begin(), cross.end(), cmp);
	for(int i=0; i<(int)cross.size(); i++){
		cout << "Cruces = " << cross[i].first << '\n';
		int _posid = cross[i].second;
		for(int j=0; j<(int)answ[_posid].size(); j++){
			cout << data_courses[j].first << ":";
			string course_section = "";
			int contb = 0;
			for(auto k:ALL[data_courses[j].first]){
				if(contb == answ[_posid][j]){
					course_section += k.first;
					break;
				}
				contb++;
			}
			cout << course_section << '\n';
		}
		cout << '\n';
	}
}

int main(){
  	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	days["LU"] = 0,days["MA"] = 1, days["MI"]=2,days["JU"]=3,days["VI"]=4, days["SA"]=5;		
	while(true){
		string line;
		if(!Read_input(line)) break;
		
		data_courses.pb(mp(line,0));
		u_map <string, u_map<string,int[24]> > schedule;
		set <string> amount_of_sections;
		while(true){
			string sections_per_course = "";
			string tst;
			if(!Read_input(tst)) break;
			if(tst == "*") break;
			
			int posx = 0;
			Read_section(posx,tst,sections_per_course);
			bool DetectMultiSections = false;
			
			string MultiSections = "";
			Insert_MultiSections(sections_per_course, DetectMultiSections, MultiSections, amount_of_sections);

			for(int i=posx; i<(int)tst.size(); i++){
				if(tst[i] == ' '){
					posx = i+1;
					break;
				}
			}

			string Day = "";
			Read_day(posx, tst, Day);
			string Hour = "";
			Read_hour(posx, tst, Hour);

			int _start_hour, _end_hour;
			Read_SE(_start_hour,_end_hour,Hour);
			
			Add_sections(DetectMultiSections, MultiSections, _start_hour, _end_hour, Day, sections_per_course, schedule);
		}
		data_courses[data_courses.size()-1].second = amount_of_sections.size();
		ALL[line] = schedule;		
	}
	vi it(data_courses.size());
	while(true){
		int contc = 0;
		Fill_schedule(contc, it);
		answ.pb(it);
		cross.pb(mp(contc,answ.size()-1));
		it[0]++;
		for(int i=1; i<(int)data_courses.size(); i++){
			if(it[i-1] >= data_courses[i-1].second){
				it[i]++;
				it[i-1] = 0;	
			}
			else break;
		}
		if(it[data_courses.size()-1] >= data_courses[data_courses.size()-1].second) break;
	}

	output();	
	return 0;
}
