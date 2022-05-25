#include <stdio.h>
#include<iostream>
#include<cstring>
#include <fstream>
#include <unistd.h>
// Linux headers
#include <fcntl.h> // Contains file controls like O_RDWR
#include <errno.h> // Error integer and strerror() function
#include <termios.h> // Contains POSIX terminal control definitions
#define window 150
char dataa[4] = {'1','1','2','\n'};
char reed[100];
using namespace std;
int zzCheck = 0 ;
int serial_port;
// void convert_char_arr(string s,char* p,int& n){
//     	for (int i = 0; i < s.length(); i++) {
						
//         	 if(s[i]=='\n')
// 			break;
// 			cout<<s[i]<<endl;
// 			p[i] = s[i];n++;
// 			// cout<<"\n"<<p[i];
        	
//     		}

// 	}
// void change_parameter(int serial_port,int value){
// 	string val=to_string(value)+'\n';
// 	cout<<"sending the following--->"<<val<<"\n";
// 	int size=0;char* char_array=new char[val.length()];

// 	convert_char_arr(val,char_array,size);
// 	write(serial_port,char_array,size+1);usleep(100000); 
// 	delete char_array;
// 	}
int main(int argc, char *argv[])
{
   	// signal()  
	// ofstream outfile;
   	// outfile.open("example.txt");
   	serial_port=open("/dev/ttyUSB0",O_RDWR| O_NOCTTY);
    //cout<<argv[1]<<" ";
    if(serial_port<0)
    {
		printf("Error %i from open: %s\n", errno, std::strerror(errno));
		return EXIT_FAILURE;
	}	
	struct termios tty;
struct termios tty_old;
memset (&tty, 0, sizeof tty);

/* Error Handling */
if ( tcgetattr ( serial_port, &tty ) != 0 ) {
   std::cout << "Error " << errno << " from tcgetattr: " << strerror(errno) << std::endl;
}

/* Save old tty parameters */
tty_old = tty;

/* Set Baud Rate */
cfsetospeed (&tty, (speed_t)B9600);
cfsetispeed (&tty, (speed_t)B9600);

/* Setting other Port Stuff */
tty.c_cflag     &=  ~PARENB;            // Make 8n1
tty.c_cflag     &=  ~CSTOPB;
tty.c_cflag     &=  ~CSIZE;
tty.c_cflag     |=  CS8;

tty.c_cflag     &=  ~CRTSCTS;           // no flow control
tty.c_cc[VMIN]   =  1;                  // read doesn't block
tty.c_cc[VTIME]  =  5;                  // 0.5 seconds read timeout
tty.c_cflag     |=  CREAD | CLOCAL;     // turn on READ & ignore ctrl lines

/* Make raw */
cfmakeraw(&tty);

/* Flush Port, then applies attributes */
tcflush( serial_port, TCIFLUSH );
if ( tcsetattr ( serial_port, TCSANOW, &tty ) != 0) {
   std::cout << "Error " << errno << " from tcsetattr" << std::endl;
}
/*-------------------------    
//     struct termios tty;
//     	if(tcgetattr(serial_port, &tty) != 0) {
//     		printf("Error %i from tcgetattr: %s\n", errno, std::strerror(errno));
//     	}
// 	tty.c_cflag &= ~PARENB; // Clear parity bit, disabling parity (most common)
// 	tty.c_cflag &= ~CSTOPB; // Clear stop field, only one stop bit used in communication (most common)
// 	tty.c_cflag &= ~CSIZE; // Clear all the size bits, then use one of the statements below
// 	tty.c_cflag |= CS8; // 5 bits per byte
// 	tty.c_cflag &= ~CRTSCTS; // Disable RTS/CTS hardware flow control (most common)
// 	tty.c_cflag |= CREAD | CLOCAL; // Turn on READ & ignore ctrl lines (CLOCAL = 1)
// 	tty.c_lflag &= ~ICANON;
// 	tty.c_lflag &= ~ECHO; // Disable echo
// 	tty.c_lflag &= ~ECHOE; // Disable erasure
// 	tty.c_lflag &= ~ECHONL; // Disable new-line echo
// 	tty.c_lflag &= ~ISIG; // Disable interpretation of INTR, QUIT and SUSP
// 	tty.c_iflag &= ~(IXON | IXOFF | IXANY); // Turn off s/w flow ctrl
// 	tty.c_iflag &= ~(IGNBRK|BRKINT|PARMRK|ISTRIP|INLCR|IGNCR|ICRNL); // Disable any special handling of received bytes
// 	tty.c_oflag &= ~OPOST; // Prevent special interpretation of output bytes (e.g. newline chars)
// 	tty.c_oflag &= ~ONLCR; // Prevent conversion of newline to carriage return/line feed
   
// 	tty.c_cc[VTIME] = 0;   // This will make read() always wait for bytes (exactly how many is determined by VMIN), so read() could block indefinitely.
// 	tty.c_cc[VMIN] = 1;
// //B0,  B50,  B75,  B110,  B134,  B150,  B200, B300, B600, B1200, B1800, B2400, B4800, B9600, B19200, B38400, B57600, B115200, B230400, B460800

// 	cfsetispeed(&tty, B9600);
// 	cfsetospeed(&tty, B9600);
	// for (int reel = 0; reel <10;reel++)
	*/
		zzCheck = write(serial_port,"00000\n",6);
	printf("%d\n",zzCheck);
	if (tcsetattr(serial_port, TCSANOW, &tty) != 0) 
    		printf("Error %i from tcsetattr: %s\n", errno, strerror(errno));
	// change_parameter(serial_port,0); // Starts both motor at degfault speed. 
	printf("I wrote 1\n");
	
	zzCheck = write(serial_port,dataa,sizeof(dataa)-1);
	printf("%d\n",zzCheck);
	zzCheck = 0;
	// for (int p = 0; p<30;p++)
    // {
	// 	// zzCheck = write(serial_port,"12\n",3);
	// 	// sleep(1);
	// 	printf("I AM SLEEPING %d %d \n",zzCheck,p);
	// // 	int enn = read(serial_port,&reed,sizeof(reed));
	// // for (int zz = 0; zz<enn ; zz++)
	// // 	printf("%c",reed[zz]);// break;
	// 	// cout<< p << endl;
    // }
	sleep(8);
	printf("I sent 0\n");
	// write(serial_port,"E",1);
	zzCheck = write(serial_port,"0",1); // Starts both motor at degfault speed.
	printf("%d\n",zzCheck);
	close(serial_port);
    return EXIT_SUCCESS;
}