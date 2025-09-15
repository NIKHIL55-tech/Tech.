import webbrowser
from googlesearch import search
from speak_engine import speak


def play_youtube_video(url):
    try:
        speak("Now playing the YouTube video.")
        webbrowser.open(url)  
    except Exception as e:
        speak(f"Sorry, I couldn't play the YouTube video. Error: {str(e)}")


def search_youtube(query):
    try:
        speak("Searching YouTube for " + query)
        
        search_results = list(search(query + " site:youtube.com", num_results=5))  
        if search_results:
            first_result = search_results[0] 
            
            video_title = first_result.split("https://www.youtube.com/watch?v=")[-1]  
            speak(f"Found a YouTube video titled: {video_title}")
           
            play_youtube_video(first_result)
        else:
            speak("No results found on YouTube.")
    except Exception as e:
        speak(f"Sorry, I couldn't perform the YouTube search. Error: {str(e)}")


def search_google(query):
    try:
        speak(f"Searching Google for {query}")
        search_results = list(search(query, num_results=5))  
        if search_results:
            first_result = search_results[0]  
            
            clean_result = first_result.replace("https://", "").replace("www.", "")
            speak(f"Here is the top result: {clean_result.split('/')[0]}")  
            webbrowser.open(first_result)
        else:
            speak("No results found on Google.")
    except Exception as e:
        speak(f"Sorry, I couldn't search Google. Error: {str(e)}")


def search_wikipedia(query):
    try:
        speak(f"Searching Wikipedia for {query}")
        search_results = list(search(f"{query} site:en.wikipedia.org", num_results=5))  
        if search_results:
            first_result = search_results[0] 
            
            clean_result = first_result.replace("https://", "").replace("www.", "")
            speak(f"Here is the top result: {clean_result.split('/')[0]}")  
            webbrowser.open(first_result)
        else:
            speak("No results found on Wikipedia.")
    except Exception as e:
        speak(f"Sorry, I couldn't search Wikipedia. Error: {str(e)}")
