#Marilyn's CUTE Taskbar Pet <3
#Started: 05/11/2026 
#Finished: 

import pygame
import tkinter as tk 
import os

#--- THIS WILL BE FOR CONFIGURATIONS FOR GOLDIE ---
FRAME_WIDTH = 32
FRAME_HEIGHT = 32
SCALING = 2 #Puppy size, might make bigger
ROW_INDEX = 8

#--- INITIALIZE WINDOW ---
root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight() 
root.destroy() #tkinter to get theee screen size

pygame.init()

# The flag pygame.NOFRAME removes the title bar/close buttons
screen = pygame.display.set_mode((FRAME_WIDTH * SCALING, (FRAME_HEIGHT * SCALING) + 40), pygame.NOFRAME)

import win32gui
import win32con
import win32api
# Making bar on TOP but transparent
import ctypes
hwnd = pygame.display.get_wm_info()['window']
ctypes.windll.user32.SetWindowPos(hwnd, -1 ,0, 0, 0, 0, 0x0001 | 0x0002)
win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                       win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(0,0,0), 0, win32con.LWA_COLORKEY)

TRANS_COLOR = (255, 0, 128)

#--- Cute Sprite ---
sprite_sheet = pygame.image.load("Goldie_v02.png").convert_alpha()

def get_frame(sheet, frame, width, height, scale):
    # Blank surface for the frame
    image = pygame.Surface((width, height), pygame.SRCALPHA)
    # Area to grab: (Left, Top, Width, Height)
    # The 'Top' is calculated by (ROW_INDEX * height)
    image.blit(sheet, (0, 0), (frame * width, (ROW_INDEX * height) - 6, width, height + 6))
    return pygame.transform.scale(image, (width * scale, height * scale))

# --- MAIN LOOP ---
x_pos = 0
y_pos = screen_height - (FRAME_HEIGHT * SCALING) - 40 #will adjust to match taskbar height
frame = 0 
clock = pygame.time.Clock()
running = True

#win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(0,0,0), 0, win32con.LWA_COLORKEY)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update Puppy Position (Walking right)
    x_pos += 3
    if x_pos > screen_width:
        x_pos = -(FRAME_WIDTH * SCALING)

# Use win32gui to move the window (smoother than os.environ)
    win32gui.SetWindowPos(hwnd, -1, x_pos, y_pos, 0, 0, 0x0001)

    # Update Animation Frame (0 to 3, change based on your sheet)
    frame = (frame + 1) % 4 
    
    # Update Window Position
    ##os.environ['SDL_VIDEO_WINDOW_POS'] = f"{x_pos},{y_pos}"
    
    # Draw
    screen.fill((0,0,0)) # Fill with black (which is transparent)
    current_puppy = get_frame(sprite_sheet, frame, FRAME_WIDTH, FRAME_HEIGHT, SCALING)
    screen.blit(current_puppy, (0, 20))
    
    pygame.display.update()
    clock.tick(10) # Adjust speed (frames per second)

pygame.quit()
