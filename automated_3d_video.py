import os
import torch
from diffusers import StableDiffusionPipeline
from PIL import Image
import imageio
import numpy as np

# ---------- CONFIG ----------
OUTPUT_DIR = "output"
PROMPT = "ultra realistic 3D cinematic animation of a human brain floating in space, dramatic lighting, science film style"
TOTAL_FRAMES = 24
FPS = 12

os.makedirs(OUTPUT_DIR, exist_ok=True)

# ---------- FIND RESUME POINT ----------
existing_frames = sorted([
    f for f in os.listdir(OUTPUT_DIR)
    if f.startswith("frame_") and f.endswith(".png")
])
START_FRAME = len(existing_frames)

print(f"Resuming from frame {START_FRAME}/{TOTAL_FRAMES}")

# ---------- LOAD MODEL ----------
print("Loading Stable Diffusion...")
pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32
)
pipe = pipe.to("cuda" if torch.cuda.is_available() else "cpu")

# ---------- GENERATE FRAMES ----------
for i in range(START_FRAME, TOTAL_FRAMES):
    prompt = PROMPT + f", cinematic camera rotation {i*5} degrees"
    image = pipe(
        prompt,
        guidance_scale=7.5,
        num_inference_steps=30   # faster + stable
    ).images[0]

    frame_path = f"{OUTPUT_DIR}/frame_{i:03}.png"
    image.save(frame_path)

    print(f"Generated frame {i+1}/{TOTAL_FRAMES}")

print("Frame generation complete.")

# ---------- CREATE VIDEO ----------
print("Creating video...")
frames = []

for i in range(TOTAL_FRAMES):
    img = Image.open(f"{OUTPUT_DIR}/frame_{i:03}.png")
    frames.append(np.array(img))

video_path = f"{OUTPUT_DIR}/final_video.mp4"
imageio.mimsave(video_path, frames, fps=FPS)

print("VIDEO CREATED:", video_path)