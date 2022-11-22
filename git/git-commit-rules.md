# Git commit rules
## Separate subject from body with a blank line
* Begin the commit message with a single short (less than 50 character) line summarizing the change, followed by a blank line and then a more thorough description.
* Not every commit requires both a subject and a body (especially simple ones).

## Limit the subject line to 50 characters
* 50 characters is not a hard limit, just a rule of thumb.
* Ensures Readability and forces the author to think of a concise way to write things

## Capitalize the subject line
* Begin all subject lines with a capital letter.

## Do not end the subject line with a period
* Trailing punctuation is unnecessary in subject lines.

## Use the imperative mood in the subject line
* spoken or written as if giving a command or instruction
* Git itself uses the imperative whenever it creates a commit on your behalf.
	* Example: Merge branch 'feature'
* A properly formed Git commit subject line should always be able to complete the sentence: "If applied, this commit will, *your subject line here*"

## Wrap the body at 72 characters
* Git never wraps text automatically. When you write the body of a commit message, you must mind its right margin, and wrap text manually.
* The recommendation is to do this at 72 characters

## Use the body to explain *what* and *why* vs. *how*
* Just focus on making clear the reasons why you made the change in the first place
	* i.e the way things worked before the change (and what was wrong with that), the way they work now, and why you decided to solve it the way you did.

# Git commit Messages
The commit type can include the following:

* feat – a new feature is introduced with the changes
* fix – a bug fix has occurred
* chore – changes that do not relate to a fix or feature and don't modify src or test files (for example updating dependencies)
* refactor – refactored code that neither fixes a bug nor adds a feature
* docs – updates to documentation such as a the README or other markdown files
* style – changes that do not affect the meaning of the code, likely related to code formatting such as white-space, missing semi-colons, and so on.
* test – including new or correcting previous tests
* perf – performance improvements
* ci – continuous integration related
* build – changes that affect the build system or external dependencies
* revert – reverts a previous commit

<hr>

## Sources
* https://cbea.ms/git-commit/
* https://www.freecodecamp.org/news/how-to-write-better-git-commit-messages/

<hr>

Related to: [git](git)