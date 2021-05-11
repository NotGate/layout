# NotGate's SFB Minimized Layout [🛠️](https://github.com/NotGate/layout) [🧪](https://notgate.github.io/layout/experimental)
*TLDR: The ISRT layout is a comfortable layout for both ortho and ansi boards, and it has lower SFB count and distance than most modern layouts.*

My dislike of Same Finger Bigrams (using the same finger twice in a row) in typing is what led me to create my first layouts. QWERTY is full of SFBs (ed ec fr gr rt br sw hu hy nu mu ju ki lo, etc), and most people don't realize because they've either developed a flexible style of typing that involves alternative fingers or they're not fast enough for it to really annoy them. 

The first iteration of this layout involved brute-forcing the lowest SFB count possible, using the corpus used by the DH and Carpalx creators. The result is an SFB percentage of 0.473. For reference, Colemak, Dvorak, and QWERTY have 1.521%, 2.570%, 6.556%, respectively.  
![Image](https://media.discordapp.net/attachments/548799170765389834/802674935268638776/unknown.png?width=492&height=675)

The first thing to notice about this layout is the very low index usage. If I enforce a minimum of 15% or higher usage on the index fingers (Colemak has 18+%) then I end up with something better, but people complained that the pinky movement was too high, since there were columns like 'cwg' that might've had low usage and low SFB but would have a decent amount of up and down movement. Therefore, **the final layout is a result of the lowest SFB possible, given the constraints of *high index usage* and *low pinky movement***. 

What I ended up with scored better than all other layouts by a decent amount on the DH analyzer and the stevep analyzer:  
<https://colemakmods.github.io/mod-dh/analyze.html>  
<https://stevep99.github.io/keyboard-layout-analyzer/#/main>  

Keep in mind that I think the actual positions of keys on a finger, and even the placement of those fingers on left or right, is subjective and flexible. I can max out the DH score even further by appealing to its effort grid, but I end up with something that might be worse. As long as you don't change the SFB count by moving a key from its finger, feel free to swap around the keys and columns to get something that makes more sense to you.   

Interestingly, this layout has up to 12 keys in common with DH, based on how you want to arrange things, so you could consider it a convoluted DH mod if you want.   

The matrix version scores 1.662 on the DH analyzer, while the lowest scoring layout listed on the [compare page](https://colemakmods.github.io/mod-dh/compare.html) (DH) gets 1.665. Mine also has half or less of the SFB count of most of the others. I've achieved 1.64, but the result really wasn't that good and scored worse on the stevep analyzer - the scores on this analyzer are questionable:  
![Image](https://i.imgur.com/Zilfkpz.png)  
![Image](https://i.imgur.com/A09WSY5.png)  

According to a more recent analysis by DreymaR, using a newer version of the site, ISRT wins by an even larger margin:  
"So bottom line, the comparable numbers for Colemak-DH vs ISRT on a 3×10 matrix on this analyzer are 1.687 (Cmk-DH) vs 1.659 (IndyRad/ISRT). You beat DH by a healthy 0.028 points in this analysis." - DreymaR  

I compared my layout to Colemak, Colemak DH, and MTGAP on the layout analyzer using ergo thumbshift variants for everything. A couple swaps gets the score to 76. I typically beat MTGAP by 1+ points and DH by 2+ points. Layouts like QWERTY score up to 30 points lower than these, so we're still very much in the realm of diminishing returns.  
![Image](https://i.imgur.com/dPZIob0.png)  

The scores on layout analyzers don't mean everything, and I came across quite a few aspects of them that I disagreed with. However, the metrics of SFB and distance are much more objective (if they're calculated correctly) and ISRT has lower than any other layout I could find in both of those metrics:  
![Image](https://i.imgur.com/HQkDF6B.png)  
![Image](https://i.imgur.com/4Syztbn.png)  

Here are the final ortho, ansi, and ansi angle modded versions that I'll be using:
```
y c l m k    z f u , '
i s r t g    p n e a o ;
q v w d j    b h / . x

y c l m k z f u , '
 i s r t g p n e a o ;
  q v w d j b h / . x

y c l m k z f u , '
 i s r t g p n e a o ;
  v w d j q b h / . x
```

Thanks to the MonkeyType Discord and Colemak Discord servers for helping me with the creation of this layout and putting up with the dozens of variations I posted that were the "final design I promise". In a world of compromise, it's hard to have something you're happy with. I hope you enjoy it if you decide to use it. 

There are AHK and XKB files available for the layout as well as full installs using MSKLC and [EPKL](https://github.com/DreymaR/BigBagKbdTrixPKL/tree/master/Layouts/_Test/Cmk-eD-NotGate_ANS_CurlAngleSym). Thank you ze_or, DreymaR and Semi!    
<https://github.com/NotGate/layout/releases/tag/1.0>  

Current/Future Learners 😄 (16):
+ NotGate  
+ juice  
+ neidan   
+ fortissim
+ Matthew Hinton
+ Renato
+ Semi
+ boo
+ Buzz
+ Solsthiem
+ AIVV73
+ morpheus
+ aftersome
+ ze_or  
+ blender
+ Technobald

Feel free to DM me on discord about the layout or to get your name added to the users list!  
NotGate#7317


## Bonus  
I'll be learning this layout using an AHK script (you can do this in QMK too) which provides:  
1) One Shot Shift: Omits the need to hold down shift in order to capatilize something. You tap shift and whether it releases before the next key or after doesn't matter. No more typing 'THe'! This really frees up the pinky and is a superior version to Window's Sticky Keys.   
2) Repeat Key: Bound to right alt (by default) and repeats the last key pressed. I suggest you try to use the thumb that doesn't press space for this. The repeat key fits the theme of reducing SFBs by as much as possible and has the bonus of including the 10th finger. Words like follow become 'fol[rep]ow' so your flow is never broken by the speed of a single finger. It might seem overkill but you quickly get used to it and it's great for keeping a steady pace. There are actually far more double letters than SFBs in typing, so technically this matters more for preserving flow than the layout's SFB minimization 🙃.    
 
AHK (thank you AHK discord helpers!):  
<https://gist.github.com/NotGate/74a5993307424ddb5c9edb87b6280728>  
QMK (thank you Apsu and precondition for the improvements!):  
<https://gist.github.com/NotGate/3e3d8ab81300a86522b2c2549f99b131>  
