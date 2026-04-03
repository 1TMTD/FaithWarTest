from diffusers import StableDiffusionPipeline
import torch, os
from datetime import datetime

# Завантажуємо модель
pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5").to("cuda")

# Читаємо промти
with open("prompts/artifacts.txt", "r", encoding="utf-8") as f:
    prompts = [line.strip() for line in f if line.strip()]

# Папка для результатів
os.makedirs("results", exist_ok=True)

# Генерація
for i, prompt in enumerate(prompts, start=1):
    img = pipe(prompt).images[0]
    filename = os.path.join("results", f"ref_{i}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png")
    img.save(filename)
    print(f"✅ Збережено {filename}")
