from nlp import transcribeVideo

if __name__ == "__main__":
    link = input("Enter the link of the YouTube video: ")
    title = input("What do you want to name the file? ")
    transcribeVideo(link, title)