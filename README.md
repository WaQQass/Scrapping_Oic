"# Scrapping_Oic" 


<!-- Remarks -->
1. The hot news are spot on and are correctly scrapped
2. The other articles are correctly scrapped.
3. The calendar events and departments are correctly displayed.

<!-- The structure needs to be updated. Please do follow the structure where the data must be shown on the console in excat same way -->
Hot News => {Heading is required}
[MainHeading]
[Paragraph]

Other News => {Heading is requred}
1. [Main Heading]
   [Pararaph]
   .
   .
   .
   .
n. [Main Heading]
   [Paragraph]

Calendar Events => {Heading is required}
1. [Event Text]
   .
   .
   .
   .
n. [Event Text]

Department Events => {Heading is required}
1. [Heading]
   [Link] 
   .
   .
   .
   .
   .
   .
n. [Heading]
   [Link]

<!-- When you print the link, they must be accessible. You can acheive the following with concatenating withe base url with the links you fetched.-->