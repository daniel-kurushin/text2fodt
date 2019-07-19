# text2fodt
Very minimalistic text to fodt parser aimed to convert m|l native editable text into M$ word docs

# Usage

The main file should be placed somewhere.
In the same dir folders */img, /code, /tbl, /bib* and */include*
have to be created to use images, code, tables or multipart documents.
Code and Tables can also be placed into the text.

The *in.fodt* file can be used to setup formatting and so on.

# syntax

Normal text
can be
splitted to lines

New para

New para

@ --- Heading w/o number

\# --- Heading w number

\## --- Heading 2-nd and so on

Рис. or Fig. Name of the figure --- figure

/p Name of the figure/ --- link
/р Name of the figure/ --- same for russian

Форм. or Form. Name y = f(x) = x^2 + 2x + b

/f Name/ --- link to fromula

paragraph text /if y = f(x) = x^2 + 2x + b/ with inline formula

Лист. or List. Name of the listing
program code goes here
for(i;i<1;i++)
{
  cout << i;
}
END.
It will search for the file with name "Name of the listing.\*" first,
if no file found - look up to 20 lines of text for the END. kw.
If no END. found - an error is raised.

/l Name of the listing/ link (or /л Name of the listing/

Табл. or Tabl. or Table Name of the table --- table.
a, b, c, d
d, e, f, g
END.
Parser will look for .cvs file with the name of a table and put
it into the doc. If no file found, it will look for csv data
below Tabl., searching for the END. keyword. If more than 20 lines collected 
and no END. is found, exception is raised.

Program will try to guess the separator character.

/t Table name/ reference.

\[ident\] bibliography link. If \[\] found parser will try to guess
citation from the internet. Bibiliiography items are stored in files under
*/bib* dir. Files can have multiple records in bibtex or GOST format.

bib file example:

luckaya Луцкая И. К. Проявления на слизистой оболочке полости рта заболеваний внутренних органов и СПИДа // Международные обзоры: клиническая практика и здоровье. 2013. №6 (6). 

Use \[luckaya\] to cite.

{Page99thepagerank,
    author = {Lawrence Page and Sergey Brin and Rajeev Motwani and Terry Winograd},
    title = {The PageRank Citation Ranking: Bringing Order to the Web},
    year = {1999}
}

Use \[Page99thepagerank\] to cite.

text: "...Bibiliiography items are stored \[\]" will cause lokup for the previous 
2 sentences, extraction of terms w rutermextract, searching of 'em in citeseer
in case of english or in cyberleninka in case of russian.
