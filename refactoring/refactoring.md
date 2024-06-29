# Notes from Martin Fowler's Refactoring Book

## Definition of Refactoring
- Refactoring is the process of changing a software system in a way that does not alter the external behaviour of the code yet improves its internal structure. 
- It is a disciplined way to clean up code that minimizes its internal structure. 
- It is an improvement to code design after it has been written

## First step in Refactoring
- The first step in refactoring is ensuring there is a solid set of tests fot the section of the code being refactored. The larger the program, the more likely it is that a refactoring will casuse something to break inadvertently. 
- The suite of tests must be self-checking
- For every small change, compile and test the code.
- Make changes in small increments, allowing for these changes to be tested individually.

## Rule of Three (When should one refactor)
The first time you do something, you just do it. The second time you do something similar, you wince at the duplication, but you do the duplicate thing anyway. The third time you do something similar, you refactor.
Or for those who like baseball: Three strikes, and you refactor.


## Planned and Opportunistic refactoring
- Most refactoring effort should be the unremarkable, opportunistic kind
- Planned refactoring episodes should be rare
- Refactoring should always come separate from the actual feature work (either as separate commits, or even as separate PRs). 
	- Be careful when doing separate PRs with refactoring, as a refactor by itself may be hard to justify without the actual code that introduces the new feature.
- 

# Some nice quotes
- _"For each desired change, make the change easy (warning: this may be hard) then make the easy change"_ - Kent Beck
- 





