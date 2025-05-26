# Packages
* Packages are the construct that is used in Scala to introduce new namespaces. By default, each file in scala does not introduce its own namespace. This can potentially lead to name clashes when importing external Scala files.
* Scala allows the creation of multiple packages within the same file

Self-explanatory example from docs:
```
package users:

  package administrators:  // users.administrators
    class AdminUser        // users.administrators.AdminUser

  package normalusers:     // users.normalusers
    class NormalUser       // users.normalusers.NormalUser
```

# Import statements

```
import users.*                            // import everything package `users`
import users.User                         // import class `User`
import users.{User, UserPreferences}      // import two members
import users.{UserPreferences as UPrefs}  // rename a member
import java.util.{List as _, *}           // hides List member
import A.given                            // import the given instance
import A.{given TC}                       // by-type imports
```

An important aspect, is that it’s not possible to hide imported `given`s in a long list of other wildcard (`*`) imports.

Default imported packages:
* java.lang.*
* scala.*

<hr>

## Sources
* https://docs.scala-lang.org/scala3/book/packaging-imports.html

<hr>

Related to: [scala](scala)