# 🎬 GPU Accelerated Video Compressor (WhatsApp-Style)

A simple **Python GUI app** that compresses one or more videos — just like WhatsApp does — using **FFmpeg** and your **GPU** for high speed and efficiency.  

It lets you:
- Pick one or more video files.
- Choose output folder (defaults to an `Output` folder).
- Select compression quality and codec (H.264 or H.265).
- Get fast GPU-based compression with minimal visible quality loss.

---

## 🚀 Features

✅ **WhatsApp-like compression** — reduces size drastically while keeping videos sharp enough for phones and social media.  
✅ **GPU accelerated** — uses NVENC (NVIDIA), AMF (AMD), or QSV (Intel) for 5–10× faster compression.  
✅ **Simple GUI** — built using Tkinter. No need to use terminal commands.  
✅ **Batch processing** — compress multiple videos in one go.  
✅ **Automatic output folder** — if you don’t specify one, an `Output` folder is created automatically beside the source files.  

---

## 🖥️ Preview

A minimal Tkinter interface:

- **Select Videos:** choose one or more `.mp4`, `.mkv`, `.mov`, or `.avi` files.  
- **Select Output Folder:** optional — defaults to `Output/`.  
- **Choose Codec:**  
  - **H.264** → WhatsApp-style compression (max compatibility).  
  - **H.265 (HEVC)** → smaller size, modern device compatibility.  
- **Set Target Bitrate:** control output size/quality (e.g., `800k`, `1000k`, `1500k`).  
- **Click "Compress Videos"** → fast, GPU-powered encoding.  

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/gpu-video-compressor.git
cd gpu-video-compressor
```

### 2. Install Python Dependencies

Make sure you have Python 3.8+ installed.
```bash
pip install tk
```

💡 Tkinter is usually included with Python. If not, install via sudo apt install python3-tk (Linux).

### 3. Install FFmpeg
🪟 Windows

Download and install from Gyan.dev FFmpeg builds
.
After extracting, add the bin/ folder to your system PATH so ffmpeg is recognized globally.

🐧 Linux
sudo apt update
sudo apt install ffmpeg

🍎 macOS
brew install ffmpeg

### 4. Verify FFmpeg

Run this in your terminal:

ffmpeg -version


If you see FFmpeg details, setup is correct.

### 5. GPU Requirements

Depending on your GPU vendor:

GPU	Encoder Used	Requirements
NVIDIA	h264_nvenc, hevc_nvenc	Latest NVIDIA drivers & CUDA support
AMD	h264_amf	AMD Adrenalin driver (Windows only)
Intel	h264_qsv, hevc_qsv	Intel QuickSync-enabled CPU (driver required)

⚠️ If GPU encoding fails, FFmpeg will show “encoder not found.” Check driver installation or switch codec.

## ▶️ Usage

Run the app:
```bash
python video_compressor.py
```

You’ll see the GUI window appear.
Steps:

- Click Select Videos → pick one or more videos.

- (Optional) Click Select Output Folder → choose where to save results.

- Choose codec (H.264 or H.265).

- Enter target bitrate (e.g., 1000k for good balance).

- Click Compress Videos.

All output videos are saved in your chosen folder, or automatically under Output/ in the source directory.

📉 Recommended Bitrate Settings
Quality Level	Bitrate	Description
Very Small	700k	Tiny size, noticeable drop in quality
Balanced	1000k	WhatsApp-like, small size, good clarity
High Quality	1500k	Slightly larger files, very clean video
Near-Lossless	2000k+	Best quality, still compressed
🧠 How It Works

Internally, the script uses FFmpeg commands like:

ffmpeg -hwaccel cuda -i input.mp4 \
  -c:v h264_nvenc -b:v 1M -maxrate 1M -bufsize 2M \
  -vf "scale=1280:-2,fps=30" -c:a aac -b:a 64k output.mp4


For H.265:

ffmpeg -hwaccel cuda -i input.mp4 \
  -c:v hevc_nvenc -b:v 800k -maxrate 800k -bufsize 1600k \
  -vf "scale=1280:-2,fps=30" -c:a aac -b:a 64k output.mp4


This mirrors WhatsApp’s compression pipeline:

Resizes to max 1280px width (≈720p).

Limits to 30 FPS.

Uses 1 Mbps or less bitrate.

Audio compressed to 64 kbps AAC.

📦 Folder Structure
gpu-video-compressor/
│
├── video_compressor.py     # Main GUI app
├── README.md               # Documentation
└── Output/                 # Default export folder (auto-created)

🧩 Future Enhancements

 Add “Target File Size” option (e.g., <16 MB WhatsApp limit).

 Add progress bar during compression.

 Add drag & drop file support.

 Support AV1 codec for modern GPUs.

🐞 Troubleshooting
Issue	Fix
ffmpeg: not found	Add FFmpeg to PATH or reinstall it
Encoder not found	Update GPU drivers or switch codec to H.264
App closes instantly	Run via terminal to see Python traceback
Output too big	Reduce bitrate (e.g., 800k) or switch to H.265
💡 Tips

For fastest encoding, use H.264.

For smallest file sizes, use H.265 (HEVC).

GPU compression is 5–10× faster than CPU (libx264).

Bitrate directly affects size → halving bitrate ≈ halving size.

🧑‍💻 Author

Sushil Dubey
Software Engineer • Backend Developer • Tech Enthusiast
