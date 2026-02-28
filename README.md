# AI 3D Video Pipeline

This project uses **Stable Diffusion** to generate frames and create a 3D cinematic video. The pipeline takes a text prompt, generates image frames, and compiles them into a video.

---

## Features

* Generate realistic 3D-style frames from a text prompt.
* Create a full video from the generated frames.
* Adjustable number of frames and frame rate.
* Uses GPU (CUDA) if available for faster generation.

---

## Installation

1. **Clone the repository**

```bash
git clone <your-repo-url>
cd ai_video_pipeline
```

2. **Create a Python virtual environment**

```bash
python -m venv venv
```

3. **Activate the virtual environment**

* Windows:

```bash
venv\Scripts\activate
```

* Mac/Linux:

```bash
source venv/bin/activate
```

4. **Install dependencies**

```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
pip install diffusers==0.37.0 transformers accelerate imageio imageio-ffmpeg pillow
```

---

## Usage

1. Edit the `automated_3d_video.py` file to change the `PROMPT`, `FRAMES`, and output directory.
2. Run the script:

```bash
python automated_3d_video.py
```

3. Output video will be saved in the `output` folder as `final_video.mp4`.

---

## Configuration

| Variable     | Description                                  |
| ------------ | -------------------------------------------- |
| `PROMPT`     | Text prompt for generating images            |
| `FRAMES`     | Total number of frames to generate           |
| `OUTPUT_DIR` | Directory to save generated frames and video |

---

## Notes

* Make sure your GPU drivers are updated for CUDA support.
* If your laptop goes to sleep during generation, the process will stop. Ensure uninterrupted execution.
* You may need to log in to Hugging Face to access certain models.

---

## License

This project is licensed under the MIT License.
