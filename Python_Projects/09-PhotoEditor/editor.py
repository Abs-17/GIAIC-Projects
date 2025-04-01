#Libraries
import tkinter as tk
from tkinter import filedialog, simpledialog, Scrollbar, Canvas, Frame, Scale
from PIL import Image, ImageTk, ImageEnhance, ImageFilter, ImageDraw, ImageFont
import numpy as np

class PhotoEditor:
    def __init__(self,root):
        self.root = root
        self.root.title("The Photo Manipulation Tool")
        self.root.configure(bg = "#94105f")

        self.image = None
        self.tk_image = None

        container = Frame(root, bg="#94105f")
        container.pack(fill=tk.BOTH,expand=True)

        canvas = Canvas(container, bg="#94105f")
        scrollbar = Scrollbar(container, orient="vertical", command=canvas.yview)
        self.scrollable_Frame = Frame(canvas, bg="#94105f")

        self.scrollable_Frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        ) 

        window = canvas.create_window((0,0), window=self.scrollable_Frame, anchor="n")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left",fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        center_frame = Frame(self.scrollable_Frame, bg="#94105f")
        center_frame.pack(expand=True, pady=50)

        self.label = tk.Label(center_frame, text="Upload an image to manipulate:", font=("Arial",14,"bold"), fg="white", bg="#94105f")
        self.label.pack(pady=10)

        self.upload_button = tk.Button(center_frame, text="Upload Image", command=self.upload_image, font=("Arial", 12), bg="#610a44", fg="white")
        self.upload_button.pack()

        self.image_canvas = tk.Canvas(center_frame, width=500, height=400, bg="white", highlightthickness=2)
        self.image_canvas.pack(pady=10)

        self.controls_frame = tk.Frame(center_frame, bg="#94105f")
        self.controls_frame.pack(pady=10)

        self.add_controls()

    def add_controls(self):
        self.brightness_scale = Scale(self.controls_frame, from_=0.1, to=3.0, resolution=0.1, orient='horizontal', label='Brightness')
        self.brightness_scale.pack()
        
        self.blur_scale = Scale(self.controls_frame, from_=0, to=10, resolution=1, orient='horizontal', label='Blur')
        self.blur_scale.pack()
        
        self.vignette_scale = Scale(self.controls_frame, from_=0, to=255, resolution=5, orient='horizontal', label='Vignette')
        self.vignette_scale.pack()
        
        self.rotate_scale = Scale(self.controls_frame, from_=0, to=360, resolution=5, orient='horizontal', label='Rotate')
        self.rotate_scale.pack()

        buttons = [
            ("Apply Brightness", self.adjust_brightness),
            ("Apply Blur", self.apply_blur),
            ("Apply Vignette", self.apply_vignette),
            ("Rotate", self.rotate_image),
            ("Grayscale", self.apply_grayscale),
            ("Add Text", self.add_text),
            ("Crop", self.crop_image),
            ("Flip", self.flip_image),
            ("Sepia", self.apply_sepia),
            ("Edge Detection", self.apply_edge_detection)
        ]

        for text, command in buttons:
            btn = tk.Button(self.controls_frame, text=text, command=command, font=("Arial", 10), bg="#530963", fg="white")
            btn.pack(pady=5)   

    def upload_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.image = Image.open(file_path)
            self.display_image()
    
    def display_image(self):
        self.tk_image = ImageTk.PhotoImage(self.image.resize((500, 400)))
        self.image_canvas.create_image(250, 200, image=self.tk_image)
    
    def adjust_brightness(self):
        if self.image:
            enhancer = ImageEnhance.Brightness(self.image)
            self.image = enhancer.enhance(self.brightness_scale.get())
            self.display_image()
    
    def apply_grayscale(self):
        if self.image:
            self.image = self.image.convert("L")
            self.display_image()
    
    def apply_blur(self):
        if self.image:
            self.image = self.image.filter(ImageFilter.GaussianBlur(self.blur_scale.get()))
            self.display_image()
    
    def apply_vignette(self):
        if self.image:
            width, height = self.image.size
            vignette = Image.new("L", (width, height), 0)
            for x in range(width):
                for y in range(height):
                    distance = min(x, y, width-x, height-y)
                    vignette.putpixel((x, y), int(self.vignette_scale.get() * (distance / (width / 2))))
            vignette = vignette.filter(ImageFilter.GaussianBlur(50))
            self.image.putalpha(vignette)
            self.display_image()
    
    def add_text(self):
        if self.image:
            text = simpledialog.askstring("Add Text", "Enter text:")
            if text:
                draw = ImageDraw.Draw(self.image)
                font = ImageFont.load_default()
                draw.text((50, 50), text, fill="red", font=font)
                self.display_image()
    
    def crop_image(self):
        if self.image:
            width, height = self.image.size
            self.image = self.image.crop((50, 50, width-50, height-50))
            self.display_image()
    
    def rotate_image(self):
        if self.image:
            self.image = self.image.rotate(self.rotate_scale.get(), expand=True)
            self.display_image()
    
    def flip_image(self):
        if self.image:
            self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
            self.display_image()
    
    def apply_sepia(self):
        if self.image:
            sepia_filter = np.array(self.image.convert("RGB"))
            tr = np.clip(sepia_filter[:,:,0] * 0.393 + sepia_filter[:,:,1] * 0.769 + sepia_filter[:,:,2] * 0.189, 0, 255)
            tg = np.clip(sepia_filter[:,:,0] * 0.349 + sepia_filter[:,:,1] * 0.686 + sepia_filter[:,:,2] * 0.168, 0, 255)
            tb = np.clip(sepia_filter[:,:,0] * 0.272 + sepia_filter[:,:,1] * 0.534 + sepia_filter[:,:,2] * 0.131, 0, 255)
            self.image = Image.fromarray(np.stack([tr, tg, tb], axis=-1).astype('uint8'))
            self.display_image()
    
    def apply_edge_detection(self):
        if self.image:
            self.image = self.image.filter(ImageFilter.FIND_EDGES)
            self.display_image()
    
if __name__ == "__main__":
    root = tk.Tk()
    editor = PhotoEditor(root)
    root.mainloop()


             
