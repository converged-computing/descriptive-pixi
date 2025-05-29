# Gemma Pixi Environment

Create a flux allocation (limit is 1h)

```bash
flux alloc -N1 -q pbatch -t 1h
```

Add the pixi executable to the PATH.

```bash
export PATH="/p/vast1/fractale/descriptive-thrust/pixi/bin:$PATH"
which pixi
```

Enter (shell into) the environment!

```bash
cd /p/vast1/fractale/descriptive-thrust/Src_fractale_de/pixi-envs/gemma
pixi shell
```

Export the models home.

```bash
export HF_HUB_CACHE=/p/vast1/fractale/descriptive-thrust/Src_fractale_de/models
```

You'll still need to login to Hugging Face.

```bash
huggingface-cli login  --add-to-git-credential
```

Run the script to test Gemma. This will need to be updated to do actual work we are interested in :)

```bash
python test_gemma.py
```
```console

    You are a space explorer. You've just landed on an alien planet and need to
    report your findings back to earth. Your task is to describe the plant and animal life,
    and since this is fictional I want you to be creative and funny.
    
**The Xythian Flora and Fauna**

Upon landing in Xythia, a vibrant planet teeming with life and wonder, I found myself surrounded by a symphony of flora and fauna unlike anything I'd ever encountered on Earth.

**Flora:**

The landscape was adorned with a kaleidoscope of vibrant colors. Giant flower petals, the color of a rainbow after a storm, swayed gently in the gentle breeze. The flowers were adorned not only with petals but also with intricate patterns and vibrant pigments that reflected the sun's rays. Tiny, iridescent fungi dotted the forest floor, adding a touch of magic to the scene. 

Among the flora, there were also towering trees with leaves that resembled the feathers of an ostrich. These trees were covered in intricate carvings and patterns that gave them a sense of ancient wisdom. They were the tallest creatures on the planet, reaching up to 100 feet in height.


**Animals:** 
The animal kingdom of Xythi was equally diverse and fascinating. There were creatures with fur that ranged from the softest as a cloud to a deep, rich brown, resembling a forest tapestry. Some animals had wings that could span up 50 ft, allowing them to soar through the sky with grace and agility. Others had a variety of adaptations for survival, including the ability to camouflage themselves in a flash or produce a powerful, sonic alarm that echoed through their territory. One of the most peculiar creatures I encountered was a creature with long, flowing hair that swayed in rhythm with its movements. It was the size of my forearm and had eyes that glowed with an eerie green light. Its hair was made of soft, glowing crystals that emitted a soft light that illuminated the surrounding area.



**Conclusion:**
My journey to Xytia was an unforgettable experience, filled with wonder and discovery. I couldn't help but smile as I marveled at the beauty of nature' s creations. From the vibrant flowers to to majestic animals, Xythians are an embodiment of life' and a reminder that there is still so much to learn and appreciate in this vast universe.
```

