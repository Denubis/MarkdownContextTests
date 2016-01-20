--- 
title: 
  long: Sample Academic Workflow
  short: Sample Workflow
  crossref: SAW
author: 
- name: Brian Ballsun-Stanton
  affiliation: Macquarie University
  email: brian@faims.edu.au
- name: Alex Gil
  affiliation: Twitter
  email: \@elotroalex
date: 12 December 2015
abstract: Suspendisse gravida faucibus mollis. 
keywords: Fake Latin, Wibbling, Image, Citation, Unit Testing
bibliography: citations
---


# Section 1  

\input knuth

## Subsection 1.1  
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.

Next paragraph should start like this. Do not indent.

Can we refer to Figure [@fig:01] and Table [@tab:01]?

## Subsection 1.2
Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque  ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo.

# Section 2

\input knuth

## Subsection 2.1
A sentence that needs a note.[^1] 

# Images

![{fig:01}This is the crossref](https://www.fedarch.org/wordpress/wp-content/uploads//2014/03/faimsLogoNoBorder1.png)

\input knuth

![This no has crossref](https://www.fedarch.org/wordpress/wp-content/uploads//2014/03/faimsLogoNoBorder1.png)

\input knuth

# Tables

   Right     Left       Center     Default
--------     ------- -----------   -------
      12     12          12            12
     123     123         123          123
       1     1            1             1

Table:  Demonstration of simple table syntax.

\input knuth

  Right     Left     Center     Default
-------     ------ ----------   -------
     12     12        12            12
    123     123       123          123
      1     1          1             1

Table:  {tab:01}Demonstration of simple table syntax.

\input knuth

# No heads 

-------     ------ ----------   -------
     12     12        12            12
    123     123       123          123
      1     1          1             1
-------     ------ ----------   -------

Table: No headers!      

\input knuth



# Citations

Does this work? [@ballsun2010asking]

\input knuth

Does this also work? [@ballsun2010asking]


[^1]: my first footnote! And a [link](https://www.eff.org/).