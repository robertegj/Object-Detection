import AvAtfdraw as avt

from PIL import Image, ImageTk
import tkinter as tk
from tkinter import Button
from tkinter import filedialog
from tkinter import simpledialog
import argparse
import datetime
import cv2
import os




class tkwindow:
    def __init__(self, output_path = "./"):
        """ Initialize application which uses OpenCV + Tkinter. It displays
            a video stream in a Tkinter window and stores current snapshot on disk """
        self.video_source = None         
        self.output_path = output_path  # store output path
        self.current_image = None  # current image from the camera


        self.root = tk.Tk()  # initialize root window
        screen_width = self.root.winfo_screenwidth() # calculate screen size
        screen_height = self.root.winfo_screenheight() 
        self.root.minsize(int(screen_width/2),int(screen_height/2))
        self.root.title("AvA 0.0.1")  # set window title
        # self.destructor function gets fired when the window is closed
        self.root.protocol('WM_DELETE_WINDOW', self.destructor)

        self.panel = tk.Label(self.root)  # initialize image panel
        self.panel.grid(row=0,column=0,columnspan=1,rowspan=2,padx=20,pady=20,sticky="se")

        # create a button, that when pressed, will take the current frame and save it to file
        self.ico_cam = tk.PhotoImage(file="camera-512.png")
        btn = tk.Button(self.root,image=self.ico_cam, command=self.take_snapshot)
        btn.grid(row=3, column=0,sticky="s")

        #buttons on right side to select video source
        self.vidfile = Button(self.root, text='Run from File')
        self.vidfile.bind("<Button-1>", self.vs_file)
        self.vidcam = Button(self.root, text='Run on Local Webcam')
        self.vidcam.bind("<Button-1>", self.vs_cam)
        self.vidip = Button(self.root, text='Run on IP Camera')
        self.vidip.bind("<Button-1>", self.vs_ip)


        #video source button layout
        self.vidfile.grid(row=0, column=2)
        self.vidcam.grid(row=1, column=2)
        self.vidip.grid(row=2, column=2)




    def vs_cam(self,*args):
        self.camnumber = 1
        self.vsource = cv2.VideoCapture(self.camnumber)

        # start a self.video_loop that constantly pools the video
        # for the most recently read frame
        self.video_loop(self)
        


    def vs_file(self,*args):
        self.filename = filedialog.askopenfilename()
        self.vsource = cv2.VideoCapture(self.filename)
        # start a self.video_loop that constantly pools the video
        # for the most recently read frame
        self.video_loop(self)

    
    def vs_ip(self,*args):
        self.camip = simpledialog.askstring("Enter the Video IP:",self.root)
        print(str(self.camip))
        self.vsource = cv2.VideoCapture(self.camip)
        # start a self.video_loop that constantly pools the video
        # for the most recently read frame
        self.video_loop(self)


    def looper(self):
        self.video_loop()
        

    def video_loop(self,vsource=None):
        """ Get frame from the video stream and show it in Tkinter """
        
        
        frame = avt.videoloop(self.vsource)
        

##        ok, frame = self.video_source.read()  # read frame from video stream

##        if ok:  # frame captured without any errors
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # convert colors from BGR to RGB
        self.current_image = Image.fromarray(cv2image)  # convert image for PIL
        imgtk = ImageTk.PhotoImage(image=self.current_image)  # convert image for tkinter
        self.panel.imgtk = imgtk  # anchor imgtk so it does not be deleted by garbage-collector
        self.panel.config(image=imgtk)  # show the image

        self.root.after(30, self.looper)  # call the looper function, which in turn calls this.
        #This is a hacky workaround, please fix






    def take_snapshot(self):
        """ Take snapshot and save it to the file """
        ts = datetime.datetime.now() # grab the current timestamp
        filename = "{}.jpg".format(ts.strftime("%Y-%m-%d_%H-%M-%S"))  # construct filename
        p = os.path.join(self.output_path, filename)  # construct output path
        self.current_image.save(p, "JPEG")  # save image as jpeg file
        print("[INFO] saved {}".format(filename))

    def destructor(self):
        """ Destroy the root object and release all resources """
        print("[INFO] closing...")
        self.root.destroy()
        if self.video_source != None:
            self.video_source.release()  # release web camera
        cv2.destroyAllWindows()  # it is not mandatory in this application

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-o", "--output", default="./",
    help="path to output directory to store snapshots (default: current folder")
args = vars(ap.parse_args())

# start the app
print("[INFO] starting...")
pba = tkwindow(args["output"])
pba.root.mainloop()
