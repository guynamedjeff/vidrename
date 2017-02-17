# Development Breakdown

The focus in early development has been to exploit regex to identify types of files that could benefit from cleaving at certain markers. While initially operating on whether or not these titles were classified as TV or movies, the better solution to this problem was to loop through a list of patterns and not segregate based on category.

This had the downside of limiting any future ability to solve corner cases based on classification, but at the same time offered the opportunity to have cleaner, less redundant code. The primary benefit to this will be the ease of implementing new features as the application grows.

# Update 2/16:

Flask's template inheritance model was added to the application as well as Bootstrap. Organization of the site's design is still on-going as of this update, but the bulk of all formatting on index.html has been complete and additional features have already been identified for that design. Those include modal images and a nav bar leading to About and Contact pages.

In regards to further back-end development for VidRename, today's update included an earlier desire to implement extension choice. That was simple as the feature merely required posting a series of checkboxes, putting them in a list, and passing that list to rename.py's run_it function.