import tkinter as tk
from tkinter import messagebox, simpledialog
import tweepy

class TwitterApp:

    def __init__(self):
        # Initialize the TwitterApp class
        self.api = None  # Initialize the Twitter API object
        self.create_login_window()  # Create the login window when the app starts

    def create_login_window(self):
        # Create the login window with entry fields for username and password
        self.login_window = tk.Tk()
        self.login_window.title("Twitter Login")

        tk.Label(self.login_window, text="Please log in to Twitter!").pack(pady=10)

        self.user_entry = tk.Entry(self.login_window)
        self.pass_entry = tk.Entry(self.login_window, show="*")

        tk.Label(self.login_window, text="User:").pack()
        self.user_entry.pack()

        tk.Label(self.login_window, text="Password:").pack()
        self.pass_entry.pack()

        login_button = tk.Button(self.login_window, text="Log In", command=self.login)
        login_button.pack(pady=10)

    def create_tweeting_window(self):
        # Create the tweeting window with an entry field for composing tweets
        self.tweeting_window = tk.Tk()
        self.tweeting_window.title("Twitter")

        tk.Label(self.tweeting_window, text="Compose Tweet:").pack(pady=10)

        self.tweet_entry = tk.Entry(self.tweeting_window)
        self.tweet_entry.pack()

        tweet_button = tk.Button(self.tweeting_window, text="Tweet!", command=self.tweet)
        tweet_button.pack(pady=10)

    def login(self):
        # Log in to Twitter using the provided credentials
        user = self.user_entry.get()
        password = self.pass_entry.get()

        try:
            # Authenticate using Tweepy and Twitter API
            auth = tweepy.OAuthHandler(user, password)
            api = tweepy.API(auth)
            self.api = api
            self.login_window.destroy()
            self.create_tweeting_window()  # If successful, create the tweeting window
        except tweepy.TweepError:
            messagebox.showerror("Login Error", "Invalid credentials. Please try again.")

    def tweet(self):
        # Post a tweet using the authenticated Twitter API
        if self.api:
            tweet_text = self.tweet_entry.get()
            if tweet_text:
                # Update status with the entered tweet text
                self.api.update_status(tweet_text)
                messagebox.showinfo("Tweet Successful", "Your tweet has been posted successfully.")
                self.tweeting_window.destroy()  # Close the tweeting window after posting
            else:
                messagebox.showwarning("Tweet Warning", "Please enter a tweet before posting.")
        else:
            messagebox.showerror("Tweet Error", "You need to log in before tweeting.")

if __name__ == "__main__":
    app = TwitterApp()
    tk.mainloop()
