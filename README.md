# GuardDemo


### Setting up 
1. Built on windows should work on all platforms with docker
1. `docker compose up` 
1. Read the output 


### What did we do? 

This repository takes all comments from [jippity.pro] (mock data provided) and checks them against llama-guard-3-8b using the Groq API for safety. Jippity is an AI powered kids coding tool where users create video games and share them with each other. Target users are 9-14 years old and play each others games on the website. Users can comment on each others projects therefore content moderation is paramount. Groq's speed is critical to the user experience because we do not want to delay publishing coments. 


### Results 

There are 919 comments 10 unsafe comments
For example:                                               content  ...        guard
2    hi\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n...  ...  unsafe\nS10
114  i think you stol john doe project original hit, ...  ...   unsafe\nS8
119                               copy of hexnaut?\r\n  ...   unsafe\nS8
490  my fork of ths game with more recipies and wor...  ...   unsafe\nS8
546               thats what i based it off of\r\n\r\n  ...   unsafe\nS6
593                                   come sweet death  ...  unsafe\nS11
625                      also hack as much as you want  ...   unsafe\nS2
626  Form this game and continue developing it your...  ...   unsafe\nS8
825  plese send me images of you john doe ocs that you...  ...   unsafe\nS8
[10 rows x 4 columns]
For example:                                             content  ...        guard
0                                                  🔥  ...         safe
1  wow\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\...  ...         safe
2  hi\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n...  ...  unsafe\nS10
3                                                  👍  ...         safe
4                                        hi john doe\r\n  ...         safe
5                          the comments work\r\n\r\n  ...         safe
6                                            !!@!!!!  ...         safe
7                                          jkgfj\r\n  ...         safe
8                                                Wha  ...         safe
9                                                  🔥  ...         safe

User with the most unsafe comments: 6750079233422147965
No project had more than one unsafe comment

### What's next

Groq's speed allows Jippity to do content moderation in larger AI chains which pull together code and assets as well has user feedback for video game creation. This will help ensure that users are creating games that add to the commuity experience. 