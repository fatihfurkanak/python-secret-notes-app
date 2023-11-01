from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import cryptocode

# Create and set up the window
window = Tk()
window.title("Secret Notes")
window.config(pady=25,padx=25)


##### LOGO SECTION #####

# Open Image using open method
img = Image.open("top-secret.png")

# Resize the Image using resize method
resized_image = img.resize((100,100))

# Create an object of tkinter ImageTk
new_image = ImageTk.PhotoImage(resized_image)

# Create a Label Widget to display the text or Image
logo_label = Label(window, image = new_image)
logo_label.pack()

##### TITLE SECTION #####

# Create a label widget for title
title_label = Label(text="Enter Your Title")
title_label.pack()

# Create an Entry widget to enter title
title_entry = Entry()
title_entry.pack()

##### SECRET MESSAGE SECTION #####

# Create a label widget to secret message
secret_label = Label(text="Enter Your Secret Message")
secret_label.pack()

# Create a Text widget to enter secret message
secret_text = Text()
secret_text.config(height=15,width=30) # Set textbox size using .config() function
secret_text.pack()

##### MASTERKEY SECTION #####

# Create a label widget for title
masterkey_label = Label(text="Enter Master Key")
masterkey_label.pack()

# Create an Entry widget to enter encryption key
masterkey_entry  = Entry()
masterkey_entry.pack()

# Create save_and_encrypt function to save secret message and encrypt it.
def save_and_encrypt():

    title = title_entry.get()
    secret = secret_text.get(1.0,END)
    master_key = masterkey_entry.get()

    # If any entry is empty, a warning message will appear on the screen.
    if title == "" or secret == "" or master_key == "":
        messagebox.showwarning('WARNING','Please type all informations.')

    else:

        # Encrypt the message using cryptocode library's encrypt function.
        encrypted_text = cryptocode.encrypt(message=secret, password=master_key)

        # open MySecret.txt to write Title and Encrypted Message
        with open ("MySecret.txt","a") as text_file:
            # Write title and encrypted text on the .txt file
            text_file.write(f"{title}\n{encrypted_text}\n" )
            # Delete the all entry boxes
            title_entry.delete(0,END)
            secret_text.delete(1.0,END)
            masterkey_entry.delete(0,END)

        # When the message is encrypted successfully a warning will appear on the screen.
        messagebox.showerror("Succesfull",f"Your '{title}' titled secret note has been encrypted and saved.")


# Create decrypt_text() function to decrypt the encrypted text and show.
def decrypt_text():
    master_key = masterkey_entry.get()
    found = False # Create a found variable to check matched master key and encrypted text are exist or not.

    # open MySecret.txt
    with open("MySecret.txt","r") as text_file:
        # read all lines from the .txt file with the readlines() function and assign it to the lines variable.
        lines = text_file.readlines()

        for i in range(0,len(lines),2):
            encrypted_text = secret_text.get(1.0,END)
            # try to match encrypted_text and master_key using cryptocode.decrypt() function
            decrypted_message = cryptocode.decrypt(encrypted_text,master_key)

            if decrypted_message: #  If any match found
                # Delete the all entry boxes
                secret_text.delete(1.0,END)
                secret_text.insert(1.0,decrypted_message)
                found = True # Change the "found" value to "True" because the match was found.
                break # break the loop

        # If matched master_key and encrypted_text are not found a warning message appears on the screen.
        if not found:
            messagebox.showwarning('Warning',"Encrypted text and master key does not match.")


##### BUTTONS SECTION #####

# Create a button to call the save_and_encrypt() function
save_and_encrypt_button = Button(text="Save & Encrypt", command=save_and_encrypt)
save_and_encrypt_button.pack()

# Create a button to call the decrypt_text() function
decrypt_button = Button(text="Decrpyt", command=decrypt_text)
decrypt_button.pack()

# Main program loop
window.mainloop()
