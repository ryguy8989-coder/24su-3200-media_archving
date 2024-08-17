# Summer 2024 CS 3200 Project Template Repository

## Project Name: Media Archiving
## Team Members: Ryan Jiang (ryguy8989-coder), Hersh Joshi (hershjoshii), Martin Celo (Cajmali), Moses Yawe (mosyawe1), Santiago Arango(LuchotheCat)



## About

The Media Archive application has the goal of providing a centralized location for the organization of various types of media, including books, movies, articles, and images, and other media literature. A lot of similar services are either too disparate in media typing or optimally organized and this app intends to solve that. Its intended users would be the likes of avid movie watchers, classical book readers, analysts in media companies, journalists, and content curators. The app will allow a great deal of customization and optimization for the user to decide how to organize their media. This will include a crowdsourced method of media tagging that will allow better descriptions.

To achieve our goals of accessible media– books, movies, articles, and images– we organized our data into three main categories: media, videos, and images. Each of these categories all revolve around a common attribute: tags. These tables are as such broken into separate tables, or relations, where there is a certain amount of criteria, its respective attributes, in each of these categories to be met that can identify its value and henceforth make it useful for any users of our app. 


**Relations**

This entity is characterisized by the attributes description, title, genre, ISBN, Page Count, Budget, Publisher, Publication Date, Literature Video Type (book, article, etc), Literature Link for where we can find this piece of writing, and the Author. This relation is mainly characterized by its Media ID, since this category value cannot be repeated for any two different pieces of literature. Similarly, the Media Video relation, and the Media Images relations are also described by their Media_ID attribute. 

Unlike the Mideo Literature relation, the Media Video relation only includes nine attributes: Media ID, Length, Quality, Director, Description, Video Type (Movie, show, etc.), Name, Size, and Genre. This relation is where all the information about finding videos is stored and if a user wants to add another video reference for others to find, they must provide a value that satisfies each of these traits. 

Whenever a particular user frequently references a specific type of visual content, it is often observed that to search for related Media Videos and Images together, as seen with the Jouranlist and Analytics users. This suggests that the formats of these two relations ought to be closely aligned, as the search requirements would need to be similar. As such, like the Mideo Video relation, the Media Images relation includes nine attributes as well: Media ID, Resolution, Image Link, Date Taken, Image Type (jpg, png, hrec, etc), Photographer, Title, File Format, and the Description. In this table as well, if a Value is to be added to this table, it would need to have a sub-value for each of the attributes for this table.

Two more smaller components to this app include the Users and Tags. The Users relation on this app only consists of the User ID and Media ID, both of which contain values that uniquely identify each row in a table. With this table the amount of users can be changed as per needed. These users then have power to create, delete of modify the tags in this app. This tags table is characterized by TagID and the TagName, where the uniquely identifiable column is the TagID. Together, all these components make up this media archiving app.

## How to View The App:
Clone this repository to your device, type docker compose up -d in your terminal, then type localhost:8501 in your browser


Link to Video: https://drive.google.com/file/d/1kNKKPa5JKZTMFgcW3jf1HzBIbw4flFEc/view?usp=sharing





 
