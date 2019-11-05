import random
from tkinter import *
from tkinter.ttk import *
from captcha.image import ImageCaptcha


class MathCaptcha:
    def __init__(self):
        root = Tk()
        self.actual = str(random.randint(0, 9)) + \
            self.randOps()+str(random.randint(0, 9))
        print(self.actual)
        image = ImageCaptcha(fonts=['captcha.ttf'])
        data = image.generate(self.actual)
        image.write(self.actual, "out.png")
        photo = PhotoImage(file=r"out.png")
        Button(root, text="Submit", image=photo).pack(side=TOP)
        Label(root, text="Enter the captcha:").pack(side=TOP)
        self.captchaInput = Entry(root)
        self.captchaInput.pack(side=TOP)
        Button(root, text="Submit", command=self.submit).pack(side=TOP)
        mainloop()

    def randOps(self):
        ops = ('+', '-', '*', '/')
        return random.choice(ops)

    def submit(self):
        if(int(self.captchaInput.get()) == eval(self.actual)):
            print("Captcha Verified")
        else:
            print("Incorrect Captcha")


c = MathCaptcha()