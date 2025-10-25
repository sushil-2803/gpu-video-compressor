import os
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox

def select_files():
    files = filedialog.askopenfilenames(
        title="Select Video Files",
        filetypes=[("Video Files", "*.mp4;*.mkv;*.avi;*.mov")]
    )
    if files:
        file_list.set("\n".join(files))
        selected_files.clear()
        selected_files.extend(files)

def select_output_dir():
    folder = filedialog.askdirectory(title="Select Output Folder")
    if folder:
        output_dir.set(folder)

def compress_videos():
    if not selected_files:
        messagebox.showwarning("No Files", "Please select at least one video.")
        return

    out_folder = output_dir.get().strip()
    if not out_folder:
        # Default: "Output" folder next to first file
        first_file_dir = os.path.dirname(selected_files[0])
        out_folder = os.path.join(first_file_dir, "Output")
        os.makedirs(out_folder, exist_ok=True)

    bitrate = bitrate_var.get()
    codec = codec_var.get()

    for file in selected_files:
        filename = os.path.basename(file)
        name, ext = os.path.splitext(filename)
        out_file = os.path.join(out_folder, f"{name}_{codec}{ext}")

        if codec == "h264":
            ffmpeg_cmd = [
                "ffmpeg", "-hwaccel", "cuda", "-i", file,
                "-c:v", "h264_nvenc",
                "-b:v", bitrate, "-maxrate", bitrate, "-bufsize", str(int(int(bitrate[:-1]) * 2)) + "k",
                "-vf", "scale=1280:-2,fps=30",
                "-c:a", "aac", "-b:a", "64k",
                out_file
            ]
        else:  # h265
            ffmpeg_cmd = [
                "ffmpeg", "-hwaccel", "cuda", "-i", file,
                "-c:v", "hevc_nvenc",
                "-b:v", bitrate, "-maxrate", bitrate, "-bufsize", str(int(int(bitrate[:-1]) * 2)) + "k",
                "-vf", "scale=1280:-2,fps=30",
                "-c:a", "aac", "-b:a", "64k",
                out_file
            ]

        try:
            subprocess.run(ffmpeg_cmd, check=True)
        except subprocess.CalledProcessError as e:
            messagebox.showerror("FFmpeg Error", f"Error compressing {file}\n\n{e}")
            return

    messagebox.showinfo("Done", f"Videos compressed and saved to:\n{out_folder}")

# --- GUI Setup ---
root = tk.Tk()
root.title("Video Compressor (GPU Accelerated)")

selected_files = []
file_list = tk.StringVar()
output_dir = tk.StringVar()

# Compression options
bitrate_var = tk.StringVar(value="1000k")  # default 1 Mbps
codec_var = tk.StringVar(value="h264")

# File selection
tk.Button(root, text="Select Videos", command=select_files).pack(pady=5)
tk.Label(root, textvariable=file_list, wraplength=400, justify="left").pack()

# Output folder
tk.Button(root, text="Select Output Folder", command=select_output_dir).pack(pady=5)
tk.Entry(root, textvariable=output_dir, width=50).pack()

# Compression settings
tk.Label(root, text="Choose Codec:").pack(pady=5)
tk.Radiobutton(root, text="H.264 (WhatsApp-style, max compatibility)", variable=codec_var, value="h264").pack(anchor="w")
tk.Radiobutton(root, text="H.265 (Smaller size, newer devices)", variable=codec_var, value="h265").pack(anchor="w")

tk.Label(root, text="Target Bitrate (e.g., 800k, 1000k, 1500k):").pack(pady=5)
tk.Entry(root, textvariable=bitrate_var).pack()

# Start button
tk.Button(root, text="Compress Videos", command=compress_videos, bg="green", fg="white").pack(pady=15)

root.mainloop()
