VidRename
https://github.com/guynamedjeff/vidrename

Development Autopsy:

The focus in early development has been to exploit regex to identify types of
files that could benefit from cleaving at certain markers. While initially
operating on whether or not these titles were classified as TV or movies, the
better solution to this problem was to loop through a list of patterns and
not segregate based on category.

This had the downside of limiting any future ability to solve corner cases
based on classification, but at the same time offered the opportunity to
have cleaner, less redundant code. The primary benefit to this will be the
ease of implementing new features as the application grows.

Next Steps:

VidRename should feature an interface to allow for directory changes via
explorer. It should also allow for additional formats i.e. the ability to
rename a file with hyphens or spaces instead of periods.