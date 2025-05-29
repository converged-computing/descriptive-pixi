# LLAMA Pixi Environment

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
python test_llama.py
```
```console

Setting `pad_token_id` to `eos_token_id`:128001 for open-end generation.

    You are a word wizard. Come up with a list of pairs of words, at least 10, where each pair
    rhymes and the other word means the opposite. An example is an "adorer" vs an "abhorrer."
     Here are some pairs: 
    *   Adorer vs AbhorrER
     *  Luminous vs Dim
      *    Bountiful vs Meager
        *     Radiant vs Dull
       *      Luxuriant vs SparsE
         *       Vibrant   vs Muted
          *        Glowing vs Fading
           *         Eloquent vs Inarticulate
            *          Vivacious vs Apathetic
             *           Radiating vs Secluded
              *            Exuberant  vs  Inhibited
               *             Splendid vs Mediocre
                *              Dazzling vs Unimpressive
                 *               Energetic vs Lethargic
                  *                Lively vs Lifeless
                   *                 Resplendent vs Dreary
                    *                  Enthusiastic vs Disinterested
                     *                   Exotic vs Familiar
                      *                    Brilliant vs Mundane
                       *                     Bubbly vs Flat
                        *                      Sizzling vs Chilly
                         *                       Slick vs Rough
                          *                        Vibratory vs Stationary

Here is a more extensive list, 20 pairs, of rhyming words with opposing meanings:

    1.   *Adorer  (one who loves) vs *Abhorer (One who hates)
   	2.  *Luminus (light)  VS *Dim (little or no light)
	3. *Bountifull (generous) VS Meagre (insufficient)
    	*   4. Radiance (glowing)   VS Dulls (not glowing)
     	5. Luxurious (lavish)     VS Sparse (bare)
        6. Vibrating (moving)      VS Mute (silent)
         7. Glows (shining)       VS Fades (losing light) 
          8. Elocution (speaking well)    VS Inart (unskilled speaking)
           9. Vivacity (lively)        VS Apathe (apathetic)
            0. Radians (spreading)         VS Seclude (isolating)
             11. Exubrant (abundant)          VS inhibit (restraining)
              12. Splendour (beautiful)           VS Mediocr (average)
               13. Dazling (bright)                VS UnImpress (no effect)
                14. Enrgic (full of energy)             VS Ltharg (lazy)
                 15. Liveliness (alive)                  VS Lifeles (dead)
                  16. Resplen (glimmering)                 VS Drear (sad)
                   17. Entusiasm (enthusiast)               VS Disinterest (indifferent)
                    18. exot (unique)                     VS Familar (known)
                     19. Brill (excellent)                    VS Mundan (ordinary)
                      21. Bubly (cheerful)                      VS Flat (boring)
                       22. Sizzle (hot)                         VS Chily (cold)
                        23. slick (smooth)                        VS Rough (harsh)
                         24. Vibrate (move)                       VS Station (fixed)
                          25. Flair (talent)                          VS dull (lack of skill)

This list is extensive, with 26 pairs. Each pair consists of a rhyme and an antonym.

1  AdorER (who loves)
2  LumINUS ( light ) vs DIM ( little or none)
3  BOUNTIFUL ( generous) meager ( insufficient)
4  RADIANT ( shining) dull  not glowing
5  LuxURIOUS ( lavish) sparse ( bare)
6  VIBRATING ( moving) mute ( silent)
7  GLOW ( shinin) fade ( losing)
8  ELOQUENT ( speaking well ) inartic ( unskil)
9  VivACIty ( lively) apathe ( apath)
10  RADIAN ( spreading) seclude  isolate
11  EXUBRANT  abundant) inhibit restr
12  SPLENDOR ( beautiful) mediocr average
13  DAZLING ( bright) unimpress no effect
14  ENERGETIC ( full of) letharg lazy
15  LIVE ( alive) lifeless dead
16  RESPLEND ( glimmer) drear sad
17  EnTHUSIASM ( entus) disinterest indifferent
18  exOT ( unique) familiar known
19  BRILLIANT excellent) mundane ordinary
20  BUbbly cheerful) flat boring
21  SIZZLE ( hot) chilly cold
22  SLICK ( smooth) rough harsh

```

