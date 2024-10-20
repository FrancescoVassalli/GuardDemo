from guard import check_statement
import logging
import pandas as pd

logger = logging.getLogger("Main")

df = pd.read_csv('data.csv')
df.drop(columns=["id", "created_at", "updated_at"], inplace=True)
i=0
while i<df.shape[0] and i<10000:
    top = df.iloc[i:i+100]
    top['guard'] = top['content'].apply(check_statement)
    i+=100
    top.to_csv(f"topguarded{i}.csv", index=False)

i=i//100
logger.warning(top.tail())

dfs = [0]*i
while i>0:
    dfs[i-1] = pd.read_csv(f'topguarded{i}00.csv')
    i-=1

combined_df = pd.concat(dfs, ignore_index=True)
combined_df.to_csv("guarded.csv")

df = pd.read_csv('guarded.csv')
unsafe_df = df[df["guard"] != "safe"]
logger.warning(f"There are {df.shape[0]} comments {unsafe_df.shape[0]} unsafe comments")
logger.warning(f"For example:{unsafe_df.head(10)}")
logger.warning(f"For example:{df.head(10)}")


logger.warning(f"Job complete, quitting")


'''
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
'''