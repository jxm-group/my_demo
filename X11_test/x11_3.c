#include <stdio.h> 
 #include <stdlib.h> 
 #include <X11/Xlib.h> 
 #include <X11/XKBlib.h> 

 #define WINDOW_SIZE 500 
 int main (int argc, char *argv[]) 
 { 
  Display              *dpy; 
  XSetWindowAttributes attributes; 
  Window               win; 
  GC                   gc; 
  XEvent evt; 
  int   i; 

  // 连接到 X Server，创建到 X Server 的套接字连接
  dpy = XOpenDisplay(NULL); 

int	screen_number = DefaultScreen(dpy);
Screen *	screen = ScreenOfDisplay(dpy, screen_number);

  // 创建 200X200 的白色背景窗口
  attributes.background_pixel = 10024;//BlackPixelOfScreen(screen);//XWhitePixel(dpy, 0);  
  attributes.border_pixel     = WhitePixelOfScreen(screen);
  attributes.backing_store = NotUseful;
  attributes.override_redirect = False;

  attributes.bit_gravity = NorthWestGravity;
  attributes.win_gravity = NorthWestGravity;

  win = XCreateWindow(dpy, 
					  XRootWindow(dpy, 0), 
					  0, 0, 
					  WINDOW_SIZE, 
					  WINDOW_SIZE, 
					  1, 
					  0,//DefaultDepth(dpy, 0), 
					  InputOutput, 
					  DefaultVisual(dpy, 0), 
					  CWBackPixel,
					  &attributes); 
 long  eventMask =		KeyPressMask | KeyReleaseMask | 
		ButtonPressMask | ButtonReleaseMask |
		EnterWindowMask | LeaveWindowMask |
		PointerMotionMask | 
		Button1MotionMask | Button2MotionMask | Button3MotionMask | 
		Button4MotionMask | Button5MotionMask |
		ButtonMotionMask | KeymapStateMask | 
		ExposureMask |
		VisibilityChangeMask | 
		StructureNotifyMask | 
		SubstructureNotifyMask |
		SubstructureRedirectMask | 
		FocusChangeMask | 
		PropertyChangeMask |
		ColormapChangeMask |
		OwnerGrabButtonMask;
	  // 选择输入事件。
	  XSelectInput(dpy, win, eventMask ); 
	  // 创建绘图上下文
	  gc = XCreateGC(dpy, win, 0, NULL); 
	  //Map 窗口
	  XMapWindow(dpy, win); 
	  XLockDisplay(dpy);
	  XUnlockDisplay(dpy);

	  XUngrabPointer(dpy, CurrentTime);
	  // 事件主循环。主要处理 Expose 事件和 KeyPress 事件
	  while(1) 
	  { 
			XNextEvent(dpy,(XEvent *)&evt); 
			printf("type = %d\n",evt.type);
#if 0
			switch(evt.type) 
			{
				case 22:
					printf("evt.type = %d\n",evt.type); fflush(stdout);
					break;
				case Expose:
					printf("Expose = %d \n",evt.type); fflush(stdout);
					break;
				case VisibilityNotify:
					printf("VisibilityNotify = %d \n",evt.type); fflush(stdout);
					break;
				case MotionNotify:  //  鼠标移动
					printf("MotionNotify = %d \n",evt.type); fflush(stdout);
					break;
				case ButtonPress: 
					break;
//				case OwnerGrabButton: 
//					printf("====\n");fflush(stdout);
//					break;
				default:break;
			} 
#endif
	  } 
	  return(0); 
 }
