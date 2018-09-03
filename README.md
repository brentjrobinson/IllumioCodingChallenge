# IllumioCodingChallenge

I tested my code right at the end of my development using the included rules and an addition of my own rule which included ranges for both port an IP. I also did not test for formatting or other conditions explained in the document. If I had more time for the challenge I would have elected to complete some unit tests. I was able to test if the overall algorithm's functionality was correct.
___

I chose to use a dictionary of dictionaries for fast lookup of the most difficult to check values: port and IP. This is useful because we can quickly access the easier to compare values, direction and protocol, and then create methods to check for ranges in the other two.
Example of structure:

    {'inbound': {'tcp': {}, 'udp': {}},
     'outbound': {'tcp': {}, 'udp': {}}}

This way we can look up a packet quickly by getting to port and ip address in constant time. From there I implemented several method to detect if a port or ip was first, a range and then if the numbers match.

Considering the time restraint of 90 minutes I would refine this solution further by looking into data structures that use less space (nested dict is useful but space costly) but are still efficient. Perhaps some sort of range tree or a map that can simplify the 'decisions' when finding a matching rule.  

---
Team Preference: Data
