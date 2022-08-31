# Thanks For The Code!

[GitHub Copilot](https://copilot.github.com) helps us write buggy code faster than ever! It was trained on public code on GitHub (and more). It is really nice and [you should try it](https://github.blog/2022-07-14-research-how-github-copilot-helps-improve-developer-productivity/).

In rare cases, [it copies code literally](https://www.theverge.com/2021/7/7/22561180/github-copilot-legal-copyright-fair-use-public-code). In the old days, we used to copy code from public repositories by hand. We would *manually* read the LICENSE file and do the polite thing:
1. Say thanks.
1. Include a copy of the license and copyright notice.
1. Apply the [GPL](https://www.cnet.com/tech/tech-industry/microsofts-hand-forced-on-open-source-driver-release/) to the entire codebase.

Some of us still want to be polite now that AI overlords lend us an automated hand. The problem is: there are more than 140 million public repositories on GitHub, with all kinds of licenses. Which repositories should we give attribution to? And how? We propose a simple solution:


## Say thanks to ALL public GitHub repositories[^2]

This is the easy way of doing attribution [^1], with or without using Copilot! No more tracking what code you stole from what source [^3].  

> When you are not sure what you did wrong, apologize to everyone you encounter.

This repository contains a *tiny* 1.8GB zipped list of repositories that you may or may not have unwittingly borrowed code from. Don't be a stranger! Feel free to distribute it with all your applications, libraries and websites.


## I can't add a 1.8GB file to my website/library/application!!

Fear not! There are even lazier ways of doing attribution. 

Just link to [thanksforthecode.com](http://thanksforthecode.com) which will (eventually) thank all GitHub repositories[^2]. Your users can casually browse the list like they would their favorite EULA. You can give it a personal touch by providing a parameter: [thanksforthecode.com?name=PROJECT_NAME](http://thanksforthecode.com?name=PROJECT_NAME). This website is free of ads and cookies.


## I don't want to link to [thanksforthecode.com](http://thanksforthecode.com)!!

Worry not, as there are still ways to do attribution. As Nasreddin said:

> The sound of coins is payment for the smell of soup.

If you are already using GitHub Copilot, you can have it generate attribution on demand. Just add a comment saying something like "Copyright notice", and let the AI work her magic. For example:
```python
# Copyright notice
print('Copyright (c) 2020, The Regents of the University of California. All Rights Reserved.')
```
Copilot donated my copyright to [a non-fictional entity](https://en.wikipedia.org/wiki/Regents_of_the_University_of_California)[^4], and put it in a print statement so the world will know. Very cool.

For those who don't like generating (fake?) attribution; I included a script that randomly samples a few very lucky repositories. Some of you may ask; what attribution probability can compensate being 1-in-140-millionth of the training data? I asked Copilot that question by giving it a function signature:

```python
def chance_of_attribution(fraction_of_training_data:float) -> float:
    return 1 - (1 - fraction_of_training) ** 2
```

For the average repository we have `fraction_of_training_data = 1/140e6`. With the above formula, we get `chance_of_attribution = 1.4e-8`. By multiplying that by the total number of repositories, we learn that we need to attribute exactly 2 random repositories[^5].


## This is horrible / great

In case you are pleased/offended by Thanks For The Code, I'd like to preemptively say "You're welcome!" and "I'm sorry!" to all sentient beings. Finding a list of names of all sentient beings is left as an exercise for the reader.

Feel free to create an Issue.


[^1]: I read Tom Sawyer, I like to eat rice. I'm not a lawyer, this is not legal advice.

[^2]: Or maybe 99.9% of all public repositories, and a bunch of repositories that have gone private over the last few weeks.

[^3]: Write your employer, tell them they are nice. I'm not a lawyer, this is not legal advice.

[^4]: I'm not affiliated with (The Regents of) the University of California, and they do not have copyright over this document. I'm not a lawyer, this is not legal advice.

[^5]: ok it was `2.00000001`, which makes sense because `(1 - (1 - 1/N)²) * N = N - N * (1 - 2/N + 1/N²) = 2 - 1/N` which was bigger than 2 for `N=140e6` because of a freak accident in floating point arithmetic.
