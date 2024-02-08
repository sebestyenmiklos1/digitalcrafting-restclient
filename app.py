import tkinter as tk
import requests
import json

def send_request():
    response_area.delete(1.0, tk.END)
    url = url_entry.get()
    payload = json.dumps(payload_entry.get("1.0","end-1c"))
    try:
        response = requests.post(url, data=json.loads(payload))
        response_area.insert(tk.END, json.dumps(response.json(), indent=4))
    except Exception as e:
        response_area.insert(tk.END, str(e))

width=200
root_border=10

root = tk.Tk()
root.title("DigitalCrafting API Tester")
root.configure(border=root_border)

url_label = tk.Label(root, text="URL")
url_label.pack()
url_entry = tk.Entry(root)
url_entry.configure(width=width)
url_entry.insert(0, "http://localhost:11434/api/generate")
url_entry.pack()

payload_label = tk.Label(root, text="Payload")
payload_label.pack()
payload_entry = tk.Text(root)
payload_entry.insert(tk.END, '{\n  "model": "mistral",\n  "prompt": "Why is the sky blue?",\n  "stream": false\n}')
payload_entry.pack()

send_button = tk.Button(root, text="Send", command=send_request)
send_button.pack()

response_area = tk.Text(root)
response_area.pack()

root.mainloop()
