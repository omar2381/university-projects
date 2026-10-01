#include<stdio.h>
#include<stdlib.h>

struct board_structure {
 int rows;
 char **data;
};


int main(int argc, char const *argv[])
{

int rows = 6;
int cols = 9-1;

char **data = malloc(rows*cols*sizeof(char));
for(int i = 0; i < rows; i++)
  data[i] = malloc(cols * sizeof(char));


  for(int i = 0; i < rows; i++){
     for(int j = 0; j <cols+1; j++){
       data[i][j] = '.';
	   if (j == cols){
		   data[i][j] = '\n';
	   }
       printf("%c",data[i][j]);
     }
  }
  for(int i = 0; i < rows; i++){
  	fwrite(data[i],sizeof(char),(cols),stdout);
	fwrite("\n",sizeof(char),1,stdout);
  }
}

