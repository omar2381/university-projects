//You can include any of headers defined in the C11 standard here. They are:
//assert.h, complex.h, ctype.h, errno.h, fenv.h, float.h, inttypes.h, iso646.h, limits.h, locale.h, math.h, setjmp.h, signal.h, stdalign.h, stdarg.h, stdatomic.h, stdbool.h, stddef.h, stdint.h, stdio.h, stdlib.h, stdnoreturn.h, string.h, tgmath.h, threads.h, time.h, uchar.h, wchar.h or wctype.h
//You may not include any other headers.
#include<stdio.h>
#include<stdlib.h>
#include<ctype.h>
#include"connect4.h"

struct board_structure {
 int rows;
 int cols;
 char **data;
 int arrxx[4];
 int arrxy[4];
};

board setup_board(){
  board u = malloc(sizeof(char)*4);
  return u;
}

void cleanup_board(board u){
  free(u);
}

void read_in_file(FILE *infile, board u){
  char cr = 'a';
  int rows = 0;
  int cols = 0;

  while (cr != EOF) {
    cr = fgetc(infile);
    cols++;
    if (cr == '\n'){
      rows++;
    }
  }

  rows = rows;
  cols = (cols/(rows))-1;

  u -> rows = rows;
  u -> cols = cols;

  char **data = malloc(rows*cols*sizeof(char)*4);

  for(int i = 0; i < cols; i++){
    data[i] = malloc(rows * sizeof(char));
  }

  for(int i = 0; i < u->rows; i++){
    for(int j = 0; j < u->cols+1; j++){
      data[i][j] = '.';
      if (j == cols){
		    data[i][j] = '\n';
	    }
    }
  }
  
  u -> data = data;
}

void write_out_file(FILE *outfile, board u){
  printf("\n");
  for(int a = 0; a<4; a++){
    printf("%d", u->arrxx[a]);
  }
  
  for(int i = 0; i < u->rows; i++){
    fwrite(u->data[i],sizeof(char),(u->cols),outfile);
	  fwrite("\n",sizeof(char),1,outfile);
  }
}

char next_player(board u){
  int x = 0;
  int o = 0;
  for(int i = 0; i < u->rows; i++){
    for(int j = 0; j < u->cols; j++){
      if (u->data[i][j] == 'x'){
        x++;
      }
      if (u->data[i][j] == 'o')
      {
        o++;
      }
    }
  }
  if (x > o){ 
    return 'o';
  }
  else{
    return 'x';
  }
}

char current_winner(board u){
  int k = 0;
  int one = 0;
  int two = 0;
  int x = 0;
  int o = 0;
  int arrxx[4];
  int arrxy[4];
  
  for (int i = 0; i < u->rows; i++){
    for (int j = 0; j < u->cols + 3; j++){
      if (u->data[i][j%u->cols]== 'x'){
        arrxx[one] = j%u->cols;
        arrxy[one] = i;
        one++;
        two = 0;
        if (one >= 4){
          for(int a = 0; a < 4; a++){
            u->arrxx[a] = arrxx[a];
            //u->arrxy[a] = arrxy[a];
            printf("%d", u->arrxx[a]);
          }
          x = 4;
        }
      }
      else if (u->data[i][j%u->cols]== 'o'){
        two++;
        one = 0;
        if (two >= 4)
          o = 4;
      }
      else if(u->data[i][j] == '.'){
        two = 0;
        one = 0;
      }
    }
  }

  two = 0;
  one = 0;
  for (int i = 0; i < u->cols; i++){
    for (int j = 0; j < u->rows; j++){
      if (u->data[j][i]== 'x'){
        one++;
        two = 0;
        if (one >= 4)
          x = 4;
      }
      else if (u->data[j][i]== 'o'){
        two++;
        one = 0;
        if (two >= 4)
          o = 4;
      }
      else if(u->data[j][i] == '.'){
        two = 0;
        one = 0;
      }
    }
  }

  two = 0;
  one = 0;
  k = 0;
  for (int i = 0; i < u->cols + 3; i++){
    k = i;
    for (int j = u->rows; j > 0; j--){
      if (u->data[j][k%u->cols]== 'x'){
        one++;
        two = 0;
        if (one >= 4)
          x = 4;
      }
      else if (u->data[j][k%u->cols]== 'o'){
        two++;
        one = 0;
        if (two >= 4)
          o = 4;
      }
      else if(u->data[j][k%u->cols] == '.'){
        two = 0;
        one = 0;
      }
      k++;
    }
  }

  two = 0;
  one = 0;
  k = 0;
  for (int i = u->cols + 3; i > 0; i--){
    k = i;
    for (int j = u->rows; j > 0; j--){
      if (u->data[j][k%u->cols]== 'x'){
        one++;
        two = 0;
        if (one >= 4)
          x = 4;
      }
      else if (u->data[j][k%u->cols]== 'o'){
        two++;
        one = 0;
        if (two >= 4)
          o = 4;
      }
      else if(u->data[j][k%u->cols] == '.'){
        two = 0;
        one = 0;
      }
      k--;
    }
  }

  if (x==4 && o==4)
    return 'd';
  else if(x>=4)
    return 'x';
  else if(o>=4)
    return 'o';
  else
    return '.';
}

struct move read_in_move(board u){
  struct move m;
  int col;
  int row;
  printf("Player %c enter column to place your token: ",next_player(u)); //Do not edit this line
  scanf("%d",&col);
  printf("Player %c enter row to rotate: ",next_player(u)); // Do not edit this line
  scanf("%d",&row);
  m.column = col-1;
  m.row = row;
  return m;
}

int is_valid_move(struct move m, board u){
  if (m.column < 0 || isdigit(m.row) == 1 || isdigit(m.column) == 1 || m.column >= u->cols || m.row > u->rows || m.row < -(u->rows) || u->data[0][m.column] != '.'){
    return 0;
  }
  else{
    return 1;
  }
}

char is_winning_move(struct move m, board u){
  int k = 0;
  int one = 0;
  int two = 0;
  int x = 0;
  int o = 0;
  
  for (int i = 0; i < u->rows; i++){
    for (int j = 0; j < u->cols + 3; j++){
      if (u->data[i][j%u->cols]== 'x'){
        one++;
        two = 0;
        if (one >= 4)
          x = 4;
      }
      else if (u->data[i][j%u->cols]== 'o'){
        two++;
        one = 0;
        if (two >= 4)
          o = 4;
      }
      else if(u->data[i][j] == '.'){
        two = 0;
        one = 0;
      }
    }
  }

  two = 0;
  one = 0;
  for (int i = 0; i < u->cols; i++){
    for (int j = 0; j < u->rows; j++){
      if (u->data[j][i]== 'x'){
        one++;
        two = 0;
        if (one >= 4)
          x = 4;
      }
      else if (u->data[j][i]== 'o'){
        two++;
        one = 0;
        if (two >= 4)
          o = 4;
      }
      else if(u->data[j][i] == '.'){
        two = 0;
        one = 0;
      }
    }
  }

  two = 0;
  one = 0;
  k = 0;
  for (int i = 0; i < u->cols + 3; i++){
    k = i;
    for (int j = u->rows; j > 0; j--){
      if (u->data[j][k%u->cols]== 'x'){
        one++;
        two = 0;
        if (one >= 4)
          x = 4;
      }
      else if (u->data[j][k%u->cols]== 'o'){
        two++;
        one = 0;
        if (two >= 4)
          o = 4;
      }
      else if(u->data[j][k%u->cols] == '.'){
        two = 0;
        one = 0;
      }
      k++;
    }
  }

  two = 0;
  one = 0;
  k = 0;
  for (int i = u->cols + 3; i > 0; i--){
    k = i;
    for (int j = u->rows; j > 0; j--){
      if (u->data[j][k%u->cols]== 'x'){
        one++;
        two = 0;
        if (one >= 4)
          x = 4;
      }
      else if (u->data[j][k%u->cols]== 'o'){
        two++;
        one = 0;
        if (two >= 4)
          o = 4;
      }
      else if(u->data[j][k%u->cols] == '.'){
        two = 0;
        one = 0;
      }
      k--;
    }
  }

  if (x==4 && o==4)
    return 'd';
  else if(x>=4)
    return 'x';
  else if(o>=4)
    return 'o';
  else
    return '.';
}

void play_move(struct move m, board u){
  char player = next_player(u);
  int i = 0;
  while (u->data[i][m.column] == '.'){
    i++;
  }
  u->data[i-1][m.column] = player;

  if (m.row == 0){
    return;
  }
  else if(m.row < 0){
    m.row = -(m.row);
    m.row = u->rows - m.row;
    char temp = u->data[m.row][0]; 
    for (int i = 0; i < u->cols; i++) 
      u->data[m.row][i] = u->data[m.row][i + 1]; 
    u->data[m.row][u->cols-1] = temp; 
  }
  else if(m.row > 0){
    m.row = u->rows - m.row;
    char temp = u->data[m.row][u->cols-1];
    for (int i = u->cols; i > 0; i--)
      u->data[m.row][i] = u->data[m.row][i - 1];
    u->data[m.row][0] = temp;
  }

  char temp;
  int times = (u->rows/2) + 1;
  while(times > 0){
    for (int j=0; j< u->cols; j++){
      for (int i = u->rows ;i > 0 ;i--){
        int z = i;
        while (u->data[z][j]=='.' && z > 0){
          temp = u->data[z][j];
          u->data[z][j]=u->data[z-1][j];
          u->data[z-1][j]=temp;
          z--;
        }
      }
    }
  times --;
  }
}

//You may put additional functions here if you wish.
