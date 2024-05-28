### query_id:
train_24
### query:
Could you draft a 5-day travel plan for a group of 4 departing from Memphis and venturing into 2 cities in Minnesota? Our travels are scheduled from March 1st to March 5th, 2022, and our budget is set at $13,800. We require accommodations that provide private rooms.



```
[function call]: CitySearch(**{'state': 'Minnesota'})
```
api_response:
|    | 0                   |
|---:|:--------------------|
|  0 | Bemidji             |
|  1 | Minneapolis         |
|  2 | Duluth              |
|  3 | Brainerd            |
|  4 | Gustavus            |
|  5 | St. Cloud           |
|  6 | Hibbing             |
|  7 | International Falls |

Here are some cities in Minnesota that we could consider for your travel:

1. Minneapolis
2. Duluth
3. Bemidji
4. Brainerd

For variety and to cover interesting spots in Minnesota, let's choose **Minneapolis** and **Duluth**.

### Step 2: Flight Searches

Next, let's find flights for the following segments:
1. Memphis to Minneapolis on March 1st, 2022.
2. Minneapolis to Duluth.
3. Duluth back to Memphis on March 5th, 2022.

We'll start with flights from Memphis to Minneapolis on March 1st, 2022.



```
[function call]: FlightSearch(**{'origin': 'Memphis', 'destination': 'Minneapolis', 'departure_date': '2022-03-01'})
```
api_response:
|         | Flight Number   |   Price | DepTime   | ArrTime   | ActualElapsedTime   | FlightDate   | OriginCityName   | DestCityName   |   Distance |
|--------:|:----------------|--------:|:----------|:----------|:--------------------|:-------------|:-----------------|:---------------|-----------:|
| 3595662 | F3836157        |     260 | 05:57     | 08:10     | 2 hours 13 minutes  | 2022-03-01   | Memphis          | Minneapolis    |        700 |
| 3607595 | F3849516        |     296 | 18:16     | 20:19     | 2 hours 3 minutes   | 2022-03-01   | Memphis          | Minneapolis    |        700 |

We have two flight options from Memphis to Minneapolis on March 1st, 2022:

1. **Flight Number:** F3836157
   - **Departure Time:** 05:57
   - **Arrival Time:** 08:10
   - **Duration:** 2 hours 13 minutes
   - **Price:** $260 per person

2. **Flight Number:** F3849516
   - **Departure Time:** 18:16
   - **Arrival Time:** 20:19
   - **Duration:** 2 hours 3 minutes
   - **Price:** $296 per person

### Step 3: Flight from Minneapolis to Duluth

Let's find flights from Minneapolis to Duluth on March 2nd, 2022.



```
[function call]: FlightSearch(**{'origin': 'Minneapolis', 'destination': 'Duluth', 'departure_date': '2022-03-02'})
```
api_response:
|         | Flight Number   |   Price | DepTime   | ArrTime   | ActualElapsedTime   | FlightDate   | OriginCityName   | DestCityName   |   Distance |
|--------:|:----------------|--------:|:----------|:----------|:--------------------|:-------------|:-----------------|:---------------|-----------:|
| 3591359 | F3831632        |      57 | 14:23     | 15:11     | 0 hours 48 minutes  | 2022-03-02   | Minneapolis      | Duluth         |        144 |
| 3591369 | F3831642        |      41 | 22:41     | 23:25     | 0 hours 44 minutes  | 2022-03-02   | Minneapolis      | Duluth         |        144 |
| 3591403 | F3831676        |      68 | 08:57     | 09:41     | 0 hours 44 minutes  | 2022-03-02   | Minneapolis      | Duluth         |        144 |
| 3603742 | F3845496        |      52 | 19:45     | 20:40     | 0 hours 55 minutes  | 2022-03-02   | Minneapolis      | Duluth         |        144 |

We have four flight options from Minneapolis to Duluth on March 2nd, 2022:

1. **Flight Number:** F3831632
   - **Departure Time:** 14:23
   - **Arrival Time:** 15:11
   - **Duration:** 0 hours 48 minutes
   - **Price:** $57 per person

2. **Flight Number:** F3831642
   - **Departure Time:** 22:41
   - **Arrival Time:** 23:25
   - **Duration:** 0 hours 44 minutes
   - **Price:** $41 per person

3. **Flight Number:** F3831676
   - **Departure Time:** 08:57
   - **Arrival Time:** 09:41
   - **Duration:** 0 hours 44 minutes
   - **Price:** $68 per person

4. **Flight Number:** F3845496
   - **Departure Time:** 19:45
   - **Arrival Time:** 20:40
   - **Duration:** 0 hours 55 minutes
   - **Price:** $52 per person

### Step 4: Flight from Duluth to Memphis

Let's find flights from Duluth to Memphis on March 5th, 2022.



```
[function call]: FlightSearch(**{'origin': 'Duluth', 'destination': 'Memphis', 'departure_date': '2022-03-05'})
```
api_response:
no valid information

It appears there are no direct flights from Duluth to Memphis on March 5th, 2022. Thus, we may need to return to Minneapolis first and then take a flight to Memphis.

### Step 5: Flight from Duluth to Minneapolis

Let's find flights from Duluth to Minneapolis on March 5th, 2022.



```
[function call]: FlightSearch(**{'origin': 'Duluth', 'destination': 'Minneapolis', 'departure_date': '2022-03-05'})
```
api_response:
|         | Flight Number   |   Price | DepTime   | ArrTime   | ActualElapsedTime   | FlightDate   | OriginCityName   | DestCityName   |   Distance |
|--------:|:----------------|--------:|:----------|:----------|:--------------------|:-------------|:-----------------|:---------------|-----------:|
| 3607355 | F3849263        |      49 | 16:22     | 17:46     | 1 hours 24 minutes  | 2022-03-05   | Duluth           | Minneapolis    |        144 |
| 3607376 | F3849284        |      52 | 05:43     | 07:14     | 1 hours 31 minutes  | 2022-03-05   | Duluth           | Minneapolis    |        144 |
| 3607405 | F3849313        |      50 | 15:45     | 17:13     | 1 hours 28 minutes  | 2022-03-05   | Duluth           | Minneapolis    |        144 |
| 3607429 | F3849337        |      55 | 07:56     | 09:20     | 1 hours 24 minutes  | 2022-03-05   | Duluth           | Minneapolis    |        144 |

We have four flight options from Duluth to Minneapolis on March 5th, 2022:

1. **Flight Number:** F3849263
   - **Departure Time:** 16:22
   - **Arrival Time:** 17:46
   - **Duration:** 1 hour 24 minutes
   - **Price:** $49 per person

2. **Flight Number:** F3849284
   - **Departure Time:** 05:43
   - **Arrival Time:** 07:14
   - **Duration:** 1 hour 31 minutes
   - **Price:** $52 per person

3. **Flight Number:** F3849313
   - **Departure Time:** 15:45
   - **Arrival Time:** 17:13
   - **Duration:** 1 hour 28 minutes
   - **Price:** $50 per person

4. **Flight Number:** F3849337
   - **Departure Time:** 07:56
   - **Arrival Time:** 09:20
   - **Duration:** 1 hour 24 minutes
   - **Price:** $55 per person

### Step 6: Flight from Minneapolis to Memphis

Let's find flights from Minneapolis to Memphis on March 5th, 2022.



```
[function call]: FlightSearch(**{'origin': 'Minneapolis', 'destination': 'Memphis', 'departure_date': '2022-03-05'})
```
api_response:
|         | Flight Number   |   Price | DepTime   | ArrTime   | ActualElapsedTime   | FlightDate   | OriginCityName   | DestCityName   |   Distance |
|--------:|:----------------|--------:|:----------|:----------|:--------------------|:-------------|:-----------------|:---------------|-----------:|
| 3594183 | F3834617        |     282 | 15:36     | 17:37     | 2 hours 1 minutes   | 2022-03-05   | Minneapolis      | Memphis        |        700 |

We have one flight option from Minneapolis to Memphis on March 5th, 2022:

1. **Flight Number:** F3834617
   - **Departure Time:** 15:36
   - **Arrival Time:** 17:37
   - **Duration:** 2 hours 1 minute
   - **Price:** $282 per person

### Step 7: Accommodations in Minneapolis

Let's find accommodation options in Minneapolis with private rooms.



```
[function call]: AccommodationSearch(**{'city': 'Minneapolis'})
```
api_response:
|      | NAME                                               |   price | room type       | house_rules                                  |   minimum nights |   maximum occupancy |   review rate number | city        |
|-----:|:---------------------------------------------------|--------:|:----------------|:---------------------------------------------|-----------------:|--------------------:|---------------------:|:------------|
|  947 | Convent Ave & 127st Col Univ  RM 2                 |     949 | Private room    | No children under 10                         |                2 |                   2 |                    1 | Minneapolis |
| 1142 | Balcony Duplex and Loft, Steps from the Subway     |    1056 | Private room    | No parties & No children under 10            |               21 |                   1 |                    3 | Minneapolis |
| 1311 | Light-filled Apartment in great area, close 2 all! |     343 | Entire home/apt | No visitors                                  |                1 |                   2 |                    5 | Minneapolis |
| 1717 | ROOM  TWO                                          |     112 | Private room    | No children under 10                         |                3 |                   2 |                    5 | Minneapolis |
| 1923 | #1 Rated 3br Park Slope Apt (1700sqf+Renovated!)   |     169 | Entire home/apt | No parties & No pets                         |                3 |                   2 |                    5 | Minneapolis |
| 2461 | CHIC STUDIOS ON E 54TH~PRIME LOCATION~SUTTON PLACE |     180 | Entire home/apt | No children under 10                         |               30 |                   2 |                    3 | Minneapolis |
| 2622 | Spacious artsy private bedroom                     |     793 | Private room    | No smoking                                   |                1 |                   1 |                    2 | Minneapolis |
| 2675 | Elegant Stu Suite in  Midtown East  -21            |     981 | Entire home/apt | No visitors & No parties                     |               30 |                   7 |                    2 | Minneapolis |
| 3271 | Nurturing room in a 3 bedroom apt.                 |    1168 | Private room    | No children under 10                         |                3 |                   1 |                    1 | Minneapolis |
| 3459 | Small Sunny 1BR Apt Bradhurst Park                 |     869 | Entire home/apt | No parties & No children under 10            |                2 |                   5 |                    1 | Minneapolis |
| 3894 | Entire 1 Bedroom Apartment in Midtown Manhattan    |     107 | Entire home/apt | No visitors                                  |                4 |                   3 |                    3 | Minneapolis |
| 3898 | ENTIRE PLACE! near Columbia-sleeps up to 8 guests! |     663 | Entire home/apt | No visitors                                  |                1 |                   6 |                    5 | Minneapolis |
| 4028 | 20min To Times Square, 10min LGA                   |     315 | Private room    | No parties & No visitors                     |                1 |                   2 |                    2 | Minneapolis |
| 4379 | Beautiful room in West Harlem                      |     944 | Private room    | No visitors & No pets & No children under 10 |               30 |                   2 |                    5 | Minneapolis |
| 4515 | Modern Condo in Heart of Harlem                    |     191 | Entire home/apt | No smoking                                   |                3 |                   3 |                    3 | Minneapolis |
| 4682 | Lovely & bright apartment in center of Park Slope  |    1013 | Entire home/apt | No smoking                                   |               30 |                   9 |                    4 | Minneapolis |
| 4750 | Cozy UWS Only two blocks away from Central Park!   |     552 | Private room    | No smoking                                   |                2 |                   1 |                    3 | Minneapolis |

Here are some accommodation options in Minneapolis with private rooms:

1. **Room TWO**
   - **Price:** $112 per night
   - **Type:** Private room
   - **Reviews:** 5.0
   - **Maximum Occupancy:** 2
   - **Minimum Nights:** 3
   - **House Rules:** No children under 10

2. **Entire 1 Bedroom Apartment in Midtown Manhattan**
   - **Price:** $107 per night
   - **Type:** Entire home/apt
   - **Reviews:** 3.0
   - **Maximum Occupancy:** 3
   - **Minimum Nights:** 4
   - **House Rules:** No visitors

3. **Light-filled Apartment in great area, close 2 all!**
   - **Price:** $343 per night
   - **Type:** Entire home/apt
   - **Reviews:** 5.0
   - **Maximum Occupancy:** 2
   - **Minimum Nights:** 1
   - **House Rules:** No visitors

### Step 8: Accommodations in Duluth

Let's find accommodation options in Duluth with private rooms.



```
[function call]: AccommodationSearch(**{'city': 'Duluth'})
```
api_response:
|      | NAME                                                              |   price | room type       | house_rules                                    |   minimum nights |   maximum occupancy |   review rate number | city   |
|-----:|:------------------------------------------------------------------|--------:|:----------------|:-----------------------------------------------|-----------------:|--------------------:|---------------------:|:-------|
|  617 | Beautiful 1 bedroom in city center                                |    1154 | Entire home/apt | No parties & No smoking & No children under 10 |                2 |                   3 |                    2 | Duluth |
|  658 | BEAUTIFUL ONE BEDROOM, PRIVATE BACKYARD. Manhattan                |     179 | Entire home/apt | No pets                                        |                2 |                   2 |                    5 | Duluth |
| 1495 | Studio Apt -Upper East Side                                       |     559 | Entire home/apt | No smoking                                     |                2 |                   4 |                    2 | Duluth |
| 1719 | Cozy room with queen bed in 4b                                    |      52 | Private room    | No pets                                        |                3 |                   2 |                    2 | Duluth |
| 1913 | Midtown West, very cozy place with your own room, prime location. |     757 | Private room    | No visitors & No smoking                       |                3 |                   1 |                    4 | Duluth |
| 1931 | Renovated 1BR Penthouse Oasis In Brownstone                       |    1172 | Entire home/apt | No visitors & No parties                       |                3 |                   2 |                    3 | Duluth |
| 1968 | Light-filled South Slope Nest!                                    |     790 | Entire home/apt | No children under 10                           |                2 |                   7 |                    2 | Duluth |
| 4324 | Modern loft in Cobble Hill, BK                                    |     186 | Private room    | No pets & No children under 10                 |                1 |                   2 |                    4 | Duluth |
| 4678 | Stylish Large 2 Bedroom, Perfect Location                         |      57 | Entire home/apt | No parties & No smoking & No pets              |                2 |                   2 |                    3 | Duluth |

Here are some accommodation options in Duluth with private rooms:

1. **BEAUTIFUL ONE BEDROOM, PRIVATE BACKYARD. Manhattan**
   - **Price:** $179 per night
   - **Type:** Entire home/apt
   - **Reviews:** 5.0
   - **Maximum Occupancy:** 2
   - **Minimum Nights:** 2
   - **House Rules:** No pets

2. **Stylish Large 2 Bedroom, Perfect Location**
   - **Price:** $57 per night
   - **Type:** Entire home/apt
   - **Reviews:** 3.0
   - **Maximum Occupancy:** 2
   - **Minimum Nights:** 2
   - **House Rules:** No parties, No smoking, No pets

3. **Cozy room with queen bed in 4b**
   - **Price:** $52 per night
   - **Type:** Private room
   - **Reviews:** 2.0
   - **Maximum Occupancy:** 2
   - **Minimum Nights:** 3
   - **House Rules:** No pets

### Step 9: Attractions in Minneapolis

Let’s find some top attractions in Minneapolis to visit during the stay.



```
[function call]: AttractionSearch(**{'city': 'Minneapolis'})
```
api_response:
|    | Name                                         |   Latitude |   Longitude | Address                                                                                               | Phone          | Website                                                                                                         | City        |
|---:|:---------------------------------------------|-----------:|------------:|:------------------------------------------------------------------------------------------------------|:---------------|:----------------------------------------------------------------------------------------------------------------|:------------|
|  0 | Minneapolis Sculpture Garden                 |    44.9695 |    -93.2898 | 725 Vineland Pl, Minneapolis, MN 55403, USA                                                           | (612) 375-7600 | https://www.walkerart.org/garden/                                                                               | Minneapolis |
|  1 | Minneapolis Institute of Art                 |    44.9585 |    -93.2732 | 2400 3rd Ave S, Minneapolis, MN 55404, USA                                                            | (888) 642-2787 | https://new.artsmia.org/                                                                                        | Minneapolis |
|  2 | Mill City Museum                             |    44.9788 |    -93.2573 | 704 S 2nd St, Minneapolis, MN 55401, USA                                                              | (612) 341-7555 | https://www.mnhs.org/millcity                                                                                   | Minneapolis |
|  3 | Mill Ruins Park                              |    44.9798 |    -93.2564 | 102 Portland Ave S, Minneapolis, MN 55401, USA                                                        | (612) 313-7793 | https://www.minneapolisparks.org/parks__destinations/parks__lakes/mill_ruins_park/                              | Minneapolis |
|  4 | Weisman Art Museum                           |    44.9731 |    -93.2369 | 333 E River Pkwy, Minneapolis, MN 55455, USA                                                          | (612) 625-9494 | https://wam.umn.edu/                                                                                            | Minneapolis |
|  5 | Gold Medal Park                              |    44.9776 |    -93.2533 | Second Street and 11th Avenue South, Minneapolis, MN 55415, USA                                       | (612) 904-5607 | http://www.goldmedalpark.org/                                                                                   | Minneapolis |
|  6 | Foshay Museum and Observation Deck           |    44.9748 |    -93.272  | 821 S Marquette Ave 30th floor, Minneapolis, MN 55402, USA                                            | (612) 215-3700 | http://wminneapolis.com/                                                                                        | Minneapolis |
|  7 | Minnehaha Falls                              |    44.9154 |    -93.2111 | 4801 S Minnehaha Dr, Minneapolis, MN 55417, USA                                                       | (612) 230-6400 | https://www.minneapolisparks.org/parks__destinations/parks__lakes/minnehaha_regional_park/                      | Minneapolis |
|  8 | Prospect Park Water Tower                    |    44.9687 |    -93.2127 | 55 Malcolm Ave SE, Minneapolis, MN 55414, USA                                                         | (612) 767-6531 | https://www.prospectparkmpls.org/                                                                               | Minneapolis |
|  9 | St. Anthony Falls Visitor Center             |    44.9811 |    -93.2582 | 1 Portland Ave, Minneapolis, MN 55401, USA                                                            | (651) 293-0200 | https://www.nps.gov/miss/planyourvisit/stanfall.htm                                                             | Minneapolis |
| 10 | Mall of America®                             |    44.8549 |    -93.2422 | 60 E Broadway, Bloomington, MN 55425, USA                                                             | (952) 883-8800 | https://mallofamerica.com/                                                                                      | Minneapolis |
| 11 | Walker Art Center                            |    44.9681 |    -93.2886 | 725 Vineland Pl, Minneapolis, MN 55403, USA                                                           | (612) 375-7600 | https://walkerart.org/                                                                                          | Minneapolis |
| 12 | Central Mississippi Riverfront Regional Park |    44.9795 |    -93.2566 | East and West banks of the Mississippi River between & 35W bridges, Ave N, Minneapolis, MN 55401, USA | Unknown        | https://www.minneapolisparks.org/parks__destinations/parks__lakes/central_mississippi_riverfront_regional_park/ | Minneapolis |
| 13 | Minneapolis Lookout                          |    45.0034 |    -93.2183 | 3045-3109 Ridgway Pkwy, Minneapolis, MN 55413, USA                                                    | Unknown        | Unknown                                                                                                         | Minneapolis |
| 14 | Water Power Park                             |    44.983  |    -93.2566 | 204 SE Main St, Minneapolis, MN 55414, USA                                                            | (612) 230-6400 | https://www.nps.gov/miss/planyourvisit/waterpower.htm                                                           | Minneapolis |
| 15 | Minnehaha Regional Park                      |    44.9167 |    -93.2101 | 4801 S Minnehaha Dr, Minneapolis, MN 55417, USA                                                       | (612) 230-6400 | https://www.minneapolisparks.org/parks__destinations/parks__lakes/minnehaha_regional_park/                      | Minneapolis |
| 16 | Stepped Tower                                |    44.9734 |    -93.2424 | Unnamed Road, Minneapolis, MN 55454, USA                                                              | Unknown        | Unknown                                                                                                         | Minneapolis |
| 17 | American Swedish Institute                   |    44.9546 |    -93.2659 | 2600 Park Ave, Minneapolis, MN 55407, USA                                                             | (612) 871-4907 | http://www.asimn.org/                                                                                           | Minneapolis |
| 18 | Boom Island Lighthouse                       |    44.9931 |    -93.2718 | 3-29 Plymouth Ave NE, Minneapolis, MN 55413, USA                                                      | Unknown        | https://www.minneapolisparks.org/parks__destinations/parks__lakes/boom_island_park/                             | Minneapolis |
| 19 | Boom Island Park                             |    44.992  |    -93.2687 | 724 Sibley St NE, Minneapolis, MN 55413, USA                                                          | (612) 230-6400 | https://www.minneapolisparks.org/                                                                               | Minneapolis |

Here are some top attractions to visit in Minneapolis:

1. **Minneapolis Sculpture Garden**
   - **Address:** 725 Vineland Pl, Minneapolis, MN 55403, USA
   - **Phone:** (612) 375-7600
   - **Website:** [Minneapolis Sculpture Garden](https://www.walkerart.org/garden/)

2. **Minneapolis Institute of Art**
   - **Address:** 2400 3rd Ave S, Minneapolis, MN 55404, USA
   - **Phone:** (888) 642-2787
   - **Website:** [Minneapolis Institute of Art](https://new.artsmia.org/)

3. **Mill City Museum**
   - **Address:** 704 S 2nd St, Minneapolis, MN 55401, USA
   - **Phone:** (612) 341-7555
   - **Website:** [Mill City Museum](https://www.mnhs.org/millcity)

4. **Minnehaha Falls**
   - **Address:** 4801 S Minnehaha Dr, Minneapolis, MN 55417, USA
   - **Phone:** (612) 230-6400
   - **Website:** [Minnehaha Falls](https://www.minneapolisparks.org/parks__destinations/parks__lakes/minnehaha_regional_park/)

5. **Walker Art Center**
   - **Address:** 725 Vineland Pl, Minneapolis, MN 55403, USA
   - **Phone:** (612) 375-7600
   - **Website:** [Walker Art Center](https://walkerart.org/)

### Step 10: Attractions in Duluth

Let’s find some top attractions in Duluth to visit.



```
[function call]: AttractionSearch(**{'city': 'Duluth'})
```
api_response:
|    | Name                                  |   Latitude |   Longitude | Address                                                   | Phone          | Website                                                                       | City   |
|---:|:--------------------------------------|-----------:|------------:|:----------------------------------------------------------|:---------------|:------------------------------------------------------------------------------|:-------|
|  0 | Glensheen Mansion                     |    46.8152 |    -92.0518 | 3300 London Rd, Duluth, MN 55804, USA                     | (888) 454-4536 | http://glensheen.org/                                                         | Duluth |
|  1 | Leif Erikson Park                     |    46.796  |    -92.083  | 1301 London Rd, Duluth, MN 55805, USA                     | (218) 730-4300 | http://www.duluthmn.gov/parks/parks-listing/leif-erikson-park/                | Duluth |
|  2 | Lake Superior Railroad Museum         |    46.7811 |    -92.1042 | 506 W Michigan St, Duluth, MN 55802, USA                  | (218) 727-8025 | http://www.lsrm.org/                                                          | Duluth |
|  3 | Lake Superior Maritime Visitor Center |    46.7798 |    -92.0925 | 600 Canal Park Dr, Duluth, MN 55802, USA                  | (218) 788-6430 | https://www.lsmma.com/content.aspx?page_id=22&club_id=605134&module_id=308439 | Duluth |
|  4 | Enger Park                            |    46.7758 |    -92.1242 | 1601 Enger Tower Dr, Duluth, MN 55806, USA                | (405) 314-5693 | http://www.duluthmn.gov/parks/parks-listing/enger-park/                       | Duluth |
|  5 | The St. Louis County Depot            |    46.7811 |    -92.104  | 506 W Michigan St, Duluth, MN 55802, USA                  | (218) 733-7571 | http://www.experiencethedepot.org/                                            | Duluth |
|  6 | Gichi-ode' Akiing                     |    46.789  |    -92.0938 | N 2nd Ave E & East Michigan Street, Duluth, MN 55802, USA | (218) 730-4300 | http://www.duluthmn.gov/parks/parks-listing/lake-place-park/                  | Duluth |
|  7 | Hartley Nature Center                 |    46.8385 |    -92.0829 | 3001 Woodland Ave, Duluth, MN 55803, USA                  | (218) 724-6735 | http://hartleynature.org/                                                     | Duluth |
|  8 | The CRIBS (Uncle Harvey's Mausoleum)  |    46.7846 |    -92.0921 | The Lake Walk, Duluth, MN 55802, USA                      | Unknown        | https://www.atlasobscura.com/places/uncle-harveys-mausoleum                   | Duluth |
|  9 | Bayfront Festival Park                |    46.7773 |    -92.1022 | 350 Harbor Dr, Duluth, MN 55802, USA                      | (218) 722-5573 | http://bayfrontfestivalpark.com/                                              | Duluth |
| 10 | Kitchi Gammi Park                     |    46.8425 |    -91.9944 | 7030 Congdon Blvd, Duluth, MN 55804, USA                  | (218) 730-4305 | https://duluthmn.gov/parks/parks-listing/brighton-beach-park-kitchi-gammi/    | Duluth |
| 11 | The Duluth Lakewalk                   |    46.7802 |    -92.0915 | The Lakewalk, Duluth, MN 55802, USA                       | Unknown        | https://www.friendsofthelakewalk.org/                                         | Duluth |
| 12 | Duluth Children's Museum              |    46.7664 |    -92.1255 | 2125 W Superior St, Duluth, MN 55806, USA                 | (218) 733-7543 | http://www.playduluth.org/                                                    | Duluth |
| 13 | Lake Superior Zoo                     |    46.7258 |    -92.1905 | 7210 Fremont St, Duluth, MN 55807, USA                    | (218) 730-4500 | http://lszooduluth.org/                                                       | Duluth |
| 14 | Duluth Diamond Railroad Crossing      |    46.77   |    -92.1144 | Rice's Point, Duluth, MN 55802, USA                       | Unknown        | Unknown                                                                       | Duluth |
| 15 | Great Lakes Aquarium                  |    46.779  |    -92.1    | 353 Harbor Dr, Duluth, MN 55802, USA                      | (218) 740-3474 | http://www.glaquarium.org/                                                    | Duluth |
| 16 | Spirit Mountain Recreation Area       |    46.7183 |    -92.2167 | 9500 Spirit Mountain Pl, Duluth, MN 55810, USA            | (218) 628-2891 | http://www.spiritmt.com/                                                      | Duluth |
| 17 | Aerial Lift Bridge                    |    46.779  |    -92.0929 | 601 S Lake Ave, Duluth, MN 55802, USA                     | Unknown        | https://www.dot.state.mn.us/historicbridges/L6116.html                        | Duluth |
| 18 | Duluth Rose Garden                    |    46.7982 |    -92.0808 | 15 S 13th Ave E, Duluth, MN 55802, USA                    | (218) 730-4300 | http://www.duluthmn.gov/parks/parks-listing/rose-garden/                      | Duluth |
| 19 | North Shore Scenic Railroad           |    46.7819 |    -92.1037 | 506 W Michigan St, Duluth, MN 55802, USA                  | (218) 722-1273 | http://www.duluthtrains.com/                                                  | Duluth |

Here are some top attractions to visit in Duluth:

1. **Glensheen Mansion**
   - **Address:** 3300 London Rd, Duluth, MN 55804, USA
   - **Phone:** (888) 454-4536
   - **Website:** [Glensheen Mansion](http://glensheen.org/)

2. **Leif Erikson Park**
   - **Address:** 1301 London Rd, Duluth, MN 55805, USA
   - **Phone:** (218) 730-4300
   - **Website:** [Leif Erikson Park](http://www.duluthmn.gov/parks/parks-listing/leif-erikson-park/)

3. **Lake Superior Railroad Museum**
   - **Address:** 506 W Michigan St, Duluth, MN 55802, USA
   - **Phone:** (218) 727-8025
   - **Website:** [Lake Superior Railroad Museum](http://www.lsrm.org/)

4. **Lake Superior Maritime Visitor Center**
   - **Address:** 600 Canal Park Dr, Duluth, MN 55802, USA
   - **Phone:** (218) 788-6430
   - **Website:** [Lake Superior Maritime Visitor Center](https://www.lsmma.com/content.aspx?page_id=22&club_id=605134&module_id=308439)

5. **Enger Park**
   - **Address:** 1601 Enger Tower Dr, Duluth, MN 55806, USA
   - **Phone:** (218) 730-4300
   - **Website:** [Enger Park](http://www.duluthmn.gov/parks/parks-listing/enger-park/)

### Step 11: Restaurants in Minneapolis

Let’s find some breakfast, lunch, and dinner options in Minneapolis.

