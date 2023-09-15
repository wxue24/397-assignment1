# 397-assignment1

## Marketing RL Loop Design

Agent: Marketing bot

Action space: 
- Choose medium of content (ie commercial, short form video, post, etc)
- Choose platform to advertise on (ie social media, TV, radio, etc)
  
State:
- Costs (ie production, platform costs, etc)
- Successfulness of past marketing campaigns (ie type of advertisement, cost, revenue)
- Metrics (ie number of viewers, customer conversion rate, etc)
  
Reward: The higher the viewer to cost ratio, the higher the reward

Challenges: 
- This is a very complicated loop:
    - large action space and actions are non-binary
    - state is complex and difficult to observe (ie how to determine if revenue is caused by marketing) 

## Dynamic Programming Problem

Run program using `python3 dp.py`. Prints out either "passed" or "failed" for each test case.
