# Unit Testing

## AAA pattern for unit testing
* Arrange: initializes objects and sets the value of the data that is passed to the method under test.
* Act: invokes the method under test with the arranged parameters.
* Assert: verifies that the action of the method under test behaves as expected.

## Unit Test good practices
* Automatic
	* Test invocation and verification should be automatic.
* Repeatable
	* Tests should be repeatable.
	* Tests should only rely on stable parameter that don't change between test executions.
* Independent
	* Each test covers one functionality.
	* Tests should be isolated.
* Thorough
	* Ensure that tests have good coverage.
	* Test all corner cases.
* Readable
	* Tests should be designed for people to understand.
	* Use appropriate test names.
	* Follow patters (e.g. AAA pattern).

<hr>

## Sources
* https://learn.microsoft.com/en-us/visualstudio/test/unit-test-basics?view=vs-2022

<hr>

Related to: 
- [software-engineering](../software-engineering.md)