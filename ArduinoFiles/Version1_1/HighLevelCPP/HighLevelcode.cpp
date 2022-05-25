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

char reed[10];
using namespace std;
int i = 1;
int serial_port;


int main(int argc, char *argv[])
{
   	// signal()  
	// ofstream outfile;
   	// outfile.open("example.txt");
   	serial_port=open(argv[1],O_RDWR);
    cout<<argv[1]<<" ";
    if(serial_port<0)
    {
		printf("Error %i from open: %s\n", errno, std::strerror(errno));
		return EXIT_FAILURE;
	}	
    
    struct termios tty;
    	if(tcgetattr(serial_port, &tty) != 0) {
    		printf("Error %i from tcgetattr: %s\n", errno, std::strerror(errno));
    	}
	tty.c_cflag &= ~PARENB; // Clear parity bit, disabling parity (most common)
	tty.c_cflag &= ~CSTOPB; // Clear stop field, only one stop bit used in communication (most common)
	tty.c_cflag &= ~CSIZE; // Clear all the size bits, then use one of the statements below
	tty.c_cflag |= CS8; // 5 bits per byte
	tty.c_cflag &= ~CRTSCTS; // Disable RTS/CTS hardware flow control (most common)
	tty.c_cflag |= CREAD | CLOCAL; // Turn on READ & ignore ctrl lines (CLOCAL = 1)
	tty.c_lflag &= ~ICANON;
	tty.c_lflag &= ~ECHO; // Disable echo
	tty.c_lflag &= ~ECHOE; // Disable erasure
	tty.c_lflag &= ~ECHONL; // Disable new-line echo
	tty.c_lflag &= ~ISIG; // Disable interpretation of INTR, QUIT and SUSP
	tty.c_iflag &= ~(IXON | IXOFF | IXANY); // Turn off s/w flow ctrl
	tty.c_iflag &= ~(IGNBRK|BRKINT|PARMRK|ISTRIP|INLCR|IGNCR|ICRNL); // Disable any special handling of received bytes
	tty.c_oflag &= ~OPOST; // Prevent special interpretation of output bytes (e.g. newline chars)
	tty.c_oflag &= ~ONLCR; // Prevent conversion of newline to carriage return/line feed
   
	tty.c_cc[VTIME] = 0;   // This will make read() always wait for bytes (exactly how many is determined by VMIN), so read() could block indefinitely.
	tty.c_cc[VMIN] = 1;
//B0,  B50,  B75,  B110,  B134,  B150,  B200, B300, B600, B1200, B1800, B2400, B4800, B9600, B19200, B38400, B57600, B115200, B230400, B460800
//

	cfsetispeed(&tty, B115200);
	cfsetospeed(&tty, B115200);
	if (tcsetattr(serial_port, TCSANOW, &tty) != 0) 
    		printf("Error %i from tcsetattr: %s\n", errno, strerror(errno));
	sleep(1);
    for (int p = 0; p<10;p++)
    {
		write(serial_port,"12",2); // Starts both motor at degfault speed. 
		sleep(1);
		cout<< p << endl;
		// write(serial_port,"E",1);
		// cout << read(serial_port,reed,10) << endl;
		// break;
    }   
	close(serial_port);
    return EXIT_SUCCESS;
}