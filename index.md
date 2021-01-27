## NotGate's SFB Minimized Layout

My dislike of Same Finger Bigrams in typing is what led me to create my first layouts. QWERTY is full of SFBs, and most people don't realize because they've either developed a flexible style of typing that involves alternative fingers or they're not fast enough for it to really annoy them. 

The first iteration of this layout invovled brute-forcing the lowest SFB count possible, using the corpus used by the DH and Carpalx creators. The result is an SFB percentage of 0.473. For reference, MTGAP, DH, and QWERTY have 1.118, 1.521, 6.556, respectively.  
![Image](https://media.discordapp.net/attachments/548799170765389834/802674935268638776/unknown.png?width=492&height=675)

The first thing to notice on this layout is the very low index usage. If I enforce a minimum of 15% or higher usage on the index fingers (Colemak has 18+%) then I end up with something better, but people complained that the pinky movement was too high, since there were columns like `cwg` that might've had low usage and low SFB but would have a decent amount of up and down movement. Therefore, the final layout is a result of the lowest SFB possible, given the constraints of *high index usage* and *low pinky movement*. 

What I eneded up with scored better than all other layouts by a decent amount on the DH analyzer and the stevep analyzer:  
https://colemakmods.github.io/mod-dh/analyze.html  
https://stevep99.github.io/keyboard-layout-analyzer/#/main  

Keep in mind that I think the actual positions of keys on a finger, and even the placement of those fingers on left or right, is subjective and flexible. I can max out the DH score even further by appealing to its effort grid, but I end up with something that might be worse. As long as you don't change the SFB count by moving a key from its finger, feel free to swap around the keys and columns to get something that makes more sense to you.   

Interestingly, this layout has up to 12 keys in common with DH, based on how you want to arrange things, so you could consider it a convoluted DH mod if you want.   

The matrix version scores 1.660 on the DH analyzer, while the lowest scoring layout listed on the `compare` page (DH) gets 1.665. Mine also has half or less of the SFB count of most of the others. I've achieved 1.64, but the result really wasn't that good and scored worse on the stevep analyzer:  
![Image](https://i.imgur.com/juz9GsB.png)  
![Image](https://i.imgur.com/A09WSY5.png)  

I compared my layout to Colemak, Colemak DH, and MTGAP on the layout analyzer using ergo thumbshift variants for everything. A couple swaps gets the score to 76. I typically beat MTGAP by 1+ points and DH by 2+ points. Layouts like QWERTY score up to 30 points lower than these, so we're still very much in the realm of diminishing returns. 
![Image](https://i.imgur.com/dPZIob0.png)  

The scores on layout analyzers don't mean everything, and I came across quite a few aspects of them that I disgreed with. However, the metrics of SFB and distance are much more objective (if they're calculated correctly) and ISRT has lower than any other layout I could find in both of those metics:  
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

Here's a very simple AHK script you can use to try it out: https://pastebin.com/mpsdfVc4

I'll include EPKL information for it eventually, although I'm not very familiar with that world. 

If you end up including it in any of your QMK layouts, I can link those here too, if you want. 
