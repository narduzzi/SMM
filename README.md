# Swiss Music Map Project
> Project of the course Applied Data Analysis, by Michele Catasta
EPFL, November 2016

##Team
Virgile Neu ( @virgileNeu ), IN  
Alexandre Connat ( @AlexConnat ), SC  
Simon Narduzzi ( @Narduzzi ), IN


##Abstract
> Music is an art form and cultural activity whose medium is sound and silence, which exist in time. - Wikipedia  

Music is a way to express and share. It brings people together around a common focus. In ancient Greece, 
music is the most beautifl of the arts. Along with a science, it is the object of high philosophical speculation. The Greeks
are indeed the first people who have established real concerts, which contributed to the developpement of a socially 
conscious public actively participating in the hearing.

Through the ages, genres fall and rised, music has greatly evolved. However, the manner of celebrating and listening to music
 remained the same : the concerts.
 The goal of this project is to study the dynamics of music in Switzerland in recent decades, by studying the evolution of genres
 and number of auditors in concerts and major musical events.


##Data Description
###List of concert places

A first approach will be to use existing event websites to grab informations about the musical scene in Switzerland. We plan to get a list of all locations were we can attend a concert. Using the plateform Resident Advisor, we can a good list of clubs and concerts hall in Switzerland. The website contains all line-ups of the concerts that have been announced through RA since 2006, giving us approximately 10 years of data. As the plateform is mainly electronic music oriented, the data will be mostly related to Techno scenes and Electro clubs.

###Line-ups of Festivals / Concerts

We need to find several website of festival in Switzerland. We will build a dataset of all festival since 1980, and try to get the line-up for each of them. Of course, it will not be possible to get data for 36 years, as some festival just got created 10 or even 5 years ago. But we will try to get as much data as we can in order to perform analysis on genre and attendances of the festival. We will grab the line-up from official websites of festivals, and maybe other plateform, such as Facebook public events.

###Genres Analysis

Once we have the line-up of the concerts and festival, we can link the name of the artist to genre of music. There is a lot of genre possible, we need to select "main genres" that we can link to the data. We will perform a "merge" of subgenres, i.e : Hard Techno and Hardstyle = Electronic Music. If we have the time, we will try to divide our analysis in subgenre, but we will maybe not have enough data to have a viable statistical basis. The goal is to be able to detect rise and fall of music genre in Switzerland across the years.

We will mainly use a Wikipedia bot that will extract genre from artist name. The main challenge will be to try to get the genre of an artist if it does not have a Wikipedia biography.

###Artists Analysis

Using Wikipedia (and other biography pages), we can get the "profile" of an artiste. We can analyse its discography to observe genre change, and try to compare the popularity of an artist with the "trend" at that time in Swtizerland (hit parade, artist reputation).

Using the list of artist, we can also perform an analysis of the "foreign" rate of music : Do Switzerland always invited foreign musicians ? Do we observe a rise of local artists in big festivals ? What is the success of swiss artists abroad ?

##Feasability and Risks

We already know that some data exists for some location, for instance with the new Montreux Jazz Museum in Art Lab we have access to all the artists that performed in the Montreux Jazz Festival for the last 50 years. We should be able to scrap enough data to at least cover the Vaud canton. The risks are the lack of other data or the time it will take to scrap it all the from various festival and concert room websites.
We will focus on the tools learned in the first labs, foc and homeworks using Python,numpy and Panda's dataframes, and using folium for interactive maps like in the third homework.
We also plan to use the Tweeter database or the Facebook API to grab some more data, tweets or comments on musical events to have more inputs in case we don't find as much information as required to have a precise and accurate representation.
We can also try to contact online tickets sellers (like ticketcorner or fnac) to see if they agree to give us some data. This would be a last attempt if we are desparatly in lack of data.
The major goal is to obtain the a big set of data, and we will use all the tools we can to have it. We will to merge the data from different website and plateform in a unique, comparable dataset on which we will perform our analysis. Data Scrapping and Vizualisations will be the two main aspect we will focus on during this project.

##Deliverables

The project with be released with vizualisations using Folium or Javascript. We will create multiple interactive maps that will contain the following informations.

###Attendance Map
The attendance map is a heat-map containing the medium attendance of concert place for each year. The idea is to display the evolution of genre and popularity of festivals in Switzerland (Montreux Jazz, Paléo, Frauenfeld..), as well as the evolution of concert places : number of public institutions per city, size, etc.

The resulting map should look like this :
![Image of Crime Data form Alastaira](https://alastaira.files.wordpress.com/2011/02/image24.png)

###Genre evolution
We can use attendance map to display the number of events of a certain genre in Switzerland. A heat map of colors symbolizing the genre of music will be displayed, and a slider under the map will allow the user to observe the evolution of music in Switzerland across time. Some side options will be available : select only one genre to display (observing the evolution of only one genre), compare two genres, and a "play" button to automatically observe the dynamic of the genres.

###Artist popularity/genre evolution
Using data from the line-up, wikipedia or even twitter, we will be able to observe the popularity of a certain artiste. A search bar will be available to the user to perform search on the artist he/she wants. Using the interactive map, we can observe the evolution of an artiste across the time, if he/she came to Switzerland several times in a year, etc.

More ideas can be explored, such as displaying an pieplot of genres of an artist.

##Timeplan

We hope to achieve the end of scraping by the checkpoint mid december or at most by the end of december. We will first need to get all the website we need, and then create bots that will automatically grab the data for us. Storing all data in CSV or only parsing HTML, we will next create dataframes that will resume all data. 
By the end of december we should have got all data from RA, festivals and wikipedia artist pages.

The next step will be to focus on the visualization (maps). That point shouldn't take more than two weeks. We will try to spare time in order to grab more data or offer more detailed visualisation or more different views on the maps. 

This project is consequent and a planning is difficult to predict, as we are not very aware of the data that are available at the moment. Maybe we will discover interesting informations constructing our dataframe, and discovering more possible comparison. But displaying the result can take a lot of time, that's why we will first develop the two points mentionned above before trying techniques such as Machine Learning on our data to discover new features.

Week 1 (7.11.2016) : Data Search / Data Scrapping for RA  
Week 2 (14.11.2016) : Data Search / Data Scrapping for other plateform  
Week 3 (21.11.2016) : Data Search / Data Scrapping for other plateform  
Week 4 (28.11.2016) : Data Search / Data Scrapping for other plateform (Tweeter, Facebook)  
Week 5 (5.11.2016) : Wikipedia artist extractor development / Data Analysis  
Week 6 (12.11.2016) : Wikipedia artist extractor development / Data Analysis  
Week 7 (19.11.2016) : Wikipedia artist extractor development  
Week 8 (26.11.2016) : Vizualisation developpement  
Week 9 (2.11.2016) : Vizualisation developpement  
Week 10 (9.11.2016) : Vizualisation developpement  
Week 10 (16.11.2016) : Vizualisation developpement  
