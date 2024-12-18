#include<iostream>
using namespace std;

class que{
	public:
		int max;
		int job[5];
		int f,r;
		
		que(){
			f=0;
			r=-1;
			max=5;
		}
		
		int Is_Empty();
		int Is_full();
		void enque();
		void deque();
		 
};

int que::Is_Empty(){
	if(f==-1&&r==-1){					
	return 1;
	}
	else{
		return 0;
	}
}
		
int que::Is_full(){
	if(f==0&&r==max-1){
		return 1;
	}
	else{
		return 0;
	}
}
		
void que::enque(){
	char choice;
	do{	
		int e;
		cout<<"Enter job number to be added:";
		cin>>e;
		if(Is_full()){
		cout<<"Queue is full.. cannot enter element.";
		}
		else{
			r++;
			cout<<"Job added"<<endl;
			job[r]=e;
		}
		cout<<"do you want to enter more job(y/n):";
		cin>>choice;	
    }while(choice=='y');
}
		
void que::deque(){
	char choice;
	do{	
		if(Is_full()){
			cout<<"Queue is full.. cannot enter element.";
		}
		else{
			cout<<job[f]<<" is deleted."<<endl;
			f++;
		}
		cout<<"do you want to delete more job(y/n):";
		cin>>choice;	
    }while(choice=='y');
}



int main(){	
	que q;
	int ch;
	char choice;
	do{
		cout<<"1.Insert job\n2.Delete job"<<endl;
		cin>>ch;
		switch(ch){
			case 1:
				q.enque();
				break;
			case 2:
				q.deque();
				break;
		}
		cout<<"do you want to operate more job(y/n):";
		cin>>choice;	
    }while(choice=='y');
	cout<<endl;
	cout<<"Job Queue:";
	for(int i=q.f;i<q.r;i++){
		cout<<q.job[i]<<"\t";
	}
}
