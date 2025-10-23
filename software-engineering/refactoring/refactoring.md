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

## Refactoring and Performance
- Most programs spend most of their time in a small fraction of the code
- To optimize for performance, one should focus on the part of the programs that is slow, leaving everything else unchanged
	- Profilers help identify potential performance issues
	- For every change made to the code, run the profiler again. If there are no performance benefits, roll back the changes and start the process again.

## Duplicate Code
- Duplication means that every time you read copies of the same code, you need to read them carefully to see if there is any difference
- Unifying these copies means simplifying the code and saving time in understanding what the code does.
	- If the code is in the same class, then extracting it into one function is enough
	- If it is in different subclasses, then pulling it up to the base class and creating a common function is a possible solution

## Long parameter lists
- When creating functions, we are commonly told to pass all required data as parameters
	- The alternative would be to rely on global data, which has many downsides (e.g. one of the more prominent ones is making things harder to test)
- When considering whether to add a new parameter to a function, always consider whether it is better to pass an object that encapsulates all required parameters
	- This is especially useful if the function we are developing will require many changes in the future.
	- We can avoid a large refactoring by just passing an object (sometimes called a context) to functions

## Polymorphism instead of conditional statements
- There are often times where repeated switch statements are used throughout the code to implement logic.
	- This becomes a problem when we want to add new clauses to the conditional statement, as we need to find all the positions in the code and change them
- The solution is to instead rely on polymorphism and replace conditional statements
	- For instance, instead of having a switch-case statement that returns some value for a given parameter, have subclasses that each extend a method from the base class (or interface) to return the required value.

# Some nice quotes
- _"For each desired change, make the change easy (warning: this may be hard) then make the easy change"_ - Kent Beck
- _"The difference between a poison and something benign is the dose"_ - Paracelsus maxim
	- Meaning in the book: It was used to explain how global data can actually make your code worse. You can get away with small doses of global data, but it gets exponentially harder to deal with the more you have.

<hr>

Related to: 
- [software-engineering](../software-engineering.md)
