int[][] brick;
final int BW = 50;
final int BH = 50;
final int WS = 100;
final int XPOS = BW/2;
final int YPOS = BH/2;
boolean bStart = false;
final int sizeOfBox = sizeOfBox;
boolean[][] trueOrFalse = new boolean[sizeOfBox][sizeOfBox];
trueOrFalse[(sizeOfBox+1)/2][(sizeOfBox+1)/2] = true;

final int RD = 25;
int ballX = 250;
int ballY = 250;
boolean checker = true;

void setup() {
  size(sizeOfBox, sizeOfBox);
  int col = sizeOfBox/BW;
  int row = sizeOfBox/BH;
  rectMode(CENTER);
  brick = new int[row][col];
  frameRate(12);
  fill(0, 0, 255);
  ellipse(ballX, ballY, RD, RD);
}
void draw() {
  background(100);
  if (mousePressed) bStart = true;
  fill(0, 255, 255);
  int col = sizeOfBox/BW;
  int row = sizeOfBox/BH;
  for (int r = 0; r < row; r++) { //initialize the brick value
    for (int i = 0; i < col; i++) {
      brick[r][i]= 1;
      int x = XPOS + i*BW;
      int y = YPOS + r*BH;
      rect(x, y, BW, BH);
    }
  }
  if (bStart&&checker) {
    ballX += 4;
    ballY += 4;
  }
  fill(0, 0, 255);
  ellipse(ballX, ballY, RD, RD);
}
void checkTouch(){
  if (ballX <= 25 || ballY <= 25){
    checker = false;
  }
}
