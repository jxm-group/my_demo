#include<X11/Xlib.h> 
#include <stdio.h>

int main(int argc , char * argv[])
{
		Display *dsp = XOpenDisplay(NULL); // 与Xserver 建立连接

		if(!dsp) {
				return 1;
		}
		int screenNumber = DefaultScreen(dsp);
		unsigned long white = WhitePixel(dsp,screenNumber);
		unsigned long black = BlackPixel(dsp,screenNumber);

		Window win = XCreateSimpleWindow(   dsp,
											DefaultRootWindow(dsp),
											0, 0,   // origin
											500, 400, // 长度，高度 
											50, 
											black, // 窗口边框的颜色 
											white );  //  背景色 


/* this variable will store the handle of the newly created child window. */
Window child_win;

/* these variables will store the window's width and height. */
int child_win_width = 100;   // 宽度
int child_win_height = 100;

/* these variables will store the window's location.         */
/* position of the child window is top-left corner of the    */
/* parent window. - 0,0.                                     */
int child_win_x = 20;   //位置
int child_win_y = 30;

/* create the window, as specified earlier. */
child_win = XCreateSimpleWindow(dsp,
                                win,
                                child_win_x, child_win_y,
                                child_win_width, child_win_height,
                                10,             //边框宽度
                                black,//BlackPixel(dsp, screenNumber),
                                white/*WhitePixel(dsp, screenNumber)*/);


		XMapWindow( dsp, win ); // map(内存到显存 映射)
		XMapWindow( dsp, child_win ); // map(内存到显存 映射)
#if 1
    	long eventMask = StructureNotifyMask;
    	XSelectInput( dsp, win, eventMask );

		XEvent evt;
    	do{
       		XNextEvent( dsp, &evt );   // XNexT内部调用 XFlush()
	    }while( evt.type != MapNotify );  // 等待server完成map通知


		//绘图
		GC gc = XCreateGC(dsp, win, 0, NULL );
		//XSetForeground( dsp, gc, black );  // 设置画笔颜色
		XSetForeground( dsp, gc, 0xff00003 );  // 设置画笔颜色  // reg红色

    	XDrawLine(dsp, win, gc, 10, 10,190,190); // 画一条线
		XDrawArc(dsp,win,gc,60-(40/2), 10-(15/2),45,15,1,100009); // 
		XDrawArc(dsp, win, gc, 50-(15/2), 100-(15/2), 15, 15, 0, 360*64); //画圆

		XMoveWindow(dsp, win, 300, 500); // 移动窗口
		XStoreName(dsp, win, "Hello XWindow"); //窗口标题
		XDrawString(dsp, win, gc, 70, 30, "this a xWindow", 14); // 在窗口画字符串

		XDrawRectangle(dsp, win, gc, 120, 150, 50, 60); // 画矩形
		XFillRectangle(dsp, win, gc, 60, 150, 50, 60);  // 画矩形，内部填充 gc色

		XFlush(dsp);

		eventMask =		KeyPressMask | KeyReleaseMask | 
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
    	XSelectInput(dsp,win,eventMask); //选择事件信息  

		do {
			XNextEvent(dsp, &evt);   // calls XFlush()
			switch(evt.type){
				case Expose:
					printf("Expose\n"); fflush(stdout);
					break;
				case ButtonPress:
					printf("x = %d , y = %d\n",evt.xbutton.x,evt.xbutton.y);fflush(stdout);
				default:break;
			}
		}while (1);

		XDestroyWindow(dsp, win);
    	XCloseDisplay(dsp);
#endif
	//while(1);
    	return 0;
}

