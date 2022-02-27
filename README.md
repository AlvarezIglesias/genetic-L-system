# genetic-L-system
L-system implementation with 'cross-breeding' option. This demo creates two plants and then a third one based on the previous two following basic genetic rules. The offspring will share some of it's parents rules. 

To allow this, rules can have multiple 'deffinitions' that will be chosen at random. 

Note that in the following example, the rule 'X' has 5 possible outcomes. One will be chosen randomly each time.

```
rules1 = {}
rules1["F"] = ["FF"]
rules1["X"] = ["AF-[[X]+X]+F[+FX]-X","BF-[[X]+X]+F[+FX]X","CF[[X]+X]-X","DF-[X+[X]][+X]-X","EF[X]+F[+X.]-X"]
```

This demo was made a long time ago but it did give some impressive ressults.

![example](https://github.com/AlvarezIglesias/genetic-L-system/blob/main/example.png)
