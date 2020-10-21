# sqlcomp: An SQL Converter

`sqlcomp` is a converter library for the rare case where you might need to store some simple SQL in a very small amount of space, so you can retrieve it and execute it later.

Currently, the library only supports very basic conditionals (x=y, x<y, x like y, things like that) and INSERT/UPDATE/DELETE.