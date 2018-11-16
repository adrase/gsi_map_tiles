### Simple script for collecting map tile from japanese gsi map service
Idea was simple - collect japanese map tiles and join them into one, big fancy map. If you have enough disk space and time you can make a detailed, kanji labelled, wall size map of Mount Fuji ;) However, I limited myself to A1 size picture.

Single map tile looks like this: 
![](https://maps.gsi.go.jp/xyz/std/15/29265/12345.png)

and it's size is 256px.
At the begining you have to specify area of interest and know coordinates of lower left and upper right corners of it. These are input parameters for the script.

The script translates geographic coordinates to tiles' numbers, downloads them and join into one picture you can print out.

There is many versions of this map. You can find corresponding services addresses [here](https://gist.github.com/minorua/7654132). If you want different map, just replace url in the script.

This is mine
![](http://mapowy.pl/IMG_20181116_211309.jpg)



