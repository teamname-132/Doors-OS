from tkinter import Label,Entry,Tk,Button
import signinScreen
import homeScreen
from time import sleep

signinScreen.screen()

user = signinScreen.getStuff("user")
users = signinScreen.getStuff("users")
username = signinScreen.getStuff("username")