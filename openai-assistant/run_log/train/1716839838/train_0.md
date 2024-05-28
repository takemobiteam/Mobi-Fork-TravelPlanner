### query_id:
train_0
### query:
Please help me plan a trip from St. Petersburg to Rockford spanning 3 days from March 16th to March 18th, 2022. The travel should be planned for a single person with a budget of $1,700.



```
[function call]: FlightSearch(**{'origin': 'St. Petersburg', 'destination': 'Rockford', 'departure_date': '2022-03-16'})
```
api_response:
|         | Flight Number   |   Price | DepTime   | ArrTime   | ActualElapsedTime   | FlightDate   | OriginCityName   | DestCityName   |   Distance |
|--------:|:----------------|--------:|:----------|:----------|:--------------------|:-------------|:-----------------|:---------------|-----------:|
| 3349312 | F3573659        |     474 | 15:40     | 17:04     | 2 hours 24 minutes  | 2022-03-16   | St. Petersburg   | Rockford       |       1049 |

The flight information for travel from St. Petersburg to Rockford on March 16th, 2022 is as follows:

- **Flight Number:** F3573659
- **Price:** $474
- **Departure Time:** 15:40
- **Arrival Time:** 17:04
- **Duration:** 2 hours 24 minutes
- **Distance:** 1049 miles

Next, let's look for accommodations in Rockford. I will search for accommodations for two nights, from March 16th to March 18th.

```
[function call]: AccommodationSearch(**{'city': 'Rockford'})
```
api_response:
|      | NAME                                               |   price | room type       | house_rules                                  |   minimum nights |   maximum occupancy |   review rate number | city     |
|-----:|:---------------------------------------------------|--------:|:----------------|:---------------------------------------------|-----------------:|--------------------:|---------------------:|:---------|
|  286 | Spacious 3BDR Prime Location!                      |    1030 | Entire home/apt | No smoking                                   |                2 |                   9 |                    2 | Rockford |
|  458 | Private Room in a two bedroom apt.                 |     210 | Private room    | No visitors & No smoking                     |                1 |                   2 |                    4 | Rockford |
|  514 | Private rooms And Matchless Location               |    1075 | Private room    | No pets & No parties                         |                2 |                   2 |                    2 | Rockford |
| 1349 | Park Side Zen Home - Terrace & next to CentralPark |     250 | Entire home/apt | No children under 10                         |                3 |                   3 |                    3 | Rockford |
| 1426 | Lux 2 Bedroom NYC Apt on the Hudson River!         |     737 | Entire home/apt | No smoking                                   |               30 |                   4 |                    5 | Rockford |
| 1461 | Modern 1-bedroom apartment in Fordham              |     377 | Entire home/apt | No pets                                      |                7 |                   2 |                    5 | Rockford |
| 1811 | Private bedroom in BedStuy!                        |    1107 | Private room    | No smoking                                   |               10 |                   1 |                    4 | Rockford |
| 1841 | Pure luxury one bdrm + sofa bed on Central Park    |     243 | Entire home/apt | No smoking & No parties                      |                2 |                   3 |                    3 | Rockford |
| 2128 | Charming studio in the heart of Astoria            |     519 | Entire home/apt | No parties                                   |                4 |                   4 |                    4 | Rockford |
| 3239 | The heart of Brooklyn                              |     154 | Entire home/apt | No children under 10 & No visitors & No pets |               30 |                   3 |                    2 | Rockford |
| 4167 | Private Stuyvesant Bedroom Madison 1R-2            |     395 | Private room    | No parties & No children under 10            |               30 |                   2 |                    3 | Rockford |
| 4213 | Sunny big bedroom in lively Brooklyn neighborhood  |     440 | Private room    | No pets & No smoking                         |               14 |                   2 |                    3 | Rockford |
| 4917 | Midtown 2 Bed United Nations Loc, Full Kitchen     |     245 | Entire home/apt | No visitors                                  |                3 |                   3 |                    4 | Rockford |

Here are the accommodation options available in Rockford with their respective details:

1. **Spacious 3BDR Prime Location!**
   - Price: $1030 (2-night total)
   - Room Type: Entire home/apt
   - House Rules: No smoking
   - Minimum Nights: 2
   - Max Occupancy: 9
   - Review Rate: 2

2. **Private Room in a two bedroom apt.**
   - Price: $210 (2-night total)
   - Room Type: Private room
   - House Rules: No visitors & No smoking
   - Minimum Nights: 1
   - Max Occupancy: 2
   - Review Rate: 4

3. **Private rooms And Matchless Location**
   - Price: $1075 (2-night total)
   - Room Type: Private room
   - House Rules: No pets & No parties
   - Minimum Nights: 2
   - Max Occupancy: 2
   - Review Rate: 2

4. **Park Side Zen Home - Terrace & next to CentralPark**
   - Price: $250 (2-night total)
   - Room Type: Entire home/apt
   - House Rules: No children under 10
   - Minimum Nights: 3
   - Max Occupancy: 3
   - Review Rate: 3

5. **Lux 2 Bedroom NYC Apt on the Hudson River!**
   - Price: $737 (2-night total)
   - Room Type: Entire home/apt
   - House Rules: No smoking
   - Minimum Nights: 30
   - Max Occupancy: 4
   - Review Rate: 5

6. **Modern 1-bedroom apartment in Fordham**
   - Price: $377 (2-night total)
   - Room Type: Entire home/apt
   - House Rules: No pets
   - Minimum Nights: 7
   - Max Occupancy: 2
   - Review Rate: 5

7. **Private bedroom in BedStuy!**
   - Price: $1107 (2-night total)
   - Room Type: Private room
   - House Rules: No smoking
   - Minimum Nights: 10
   - Max Occupancy: 1
   - Review Rate: 4

8. **Pure luxury one bdrm + sofa bed on Central Park**
   - Price: $243 (2-night total)
   - Room Type: Entire home/apt
   - House Rules: No smoking & No parties
   - Minimum Nights: 2
   - Max Occupancy: 3
   - Review Rate: 3

9. **Charming studio in the heart of Astoria**
   - Price: $519 (2-night total)
   - Room Type: Entire home/apt
   - House Rules: No parties
   - Minimum Nights: 4
   - Max Occupancy: 4
   - Review Rate: 4

10. **Private Stuyvesant Bedroom Madison 1R-2**
    - Price: $395 (2-night total)
    - Room Type: Private room
    - House Rules: No parties & No children under 10
    - Minimum Nights: 30
    - Max Occupancy: 2
    - Review Rate: 3

11. **Sunny big bedroom in lively Brooklyn neighborhood**
    - Price: $440 (2-night total)
    - Room Type: Private room
    - House Rules: No pets & No smoking
    - Minimum Nights: 14
    - Max Occupancy: 2
    - Review Rate: 3

12. **Midtown 2 Bed United Nations Loc, Full Kitchen**
    - Price: $245 (2-night total)
    - Room Type: Entire home/apt
    - House Rules: No visitors
    - Minimum Nights: 3
    - Max Occupancy: 3
    - Review Rate: 4

Given the budget and flexibility, "**Private Room in a two bedroom apt.**" priced at $210 for two nights seems like a reasonable and affordable option. 

Next, let's find restaurants for the three days.

I'll start by looking for dining options in Rockford.

```
[function call]: RestaurantSearch(**{'city': 'Rockford'})
```
api_response:
|      | Name                                      |   Average Cost | Cuisines                                           |   Aggregate Rating | City     |
|-----:|:------------------------------------------|---------------:|:---------------------------------------------------|-------------------:|:---------|
|   39 | Coco Bambu                                |             72 | Tea, French, Bakery, BBQ, Cafe                     |                4.9 | Rockford |
|  251 | Flying Mango                              |             20 | American, BBQ, Seafood                             |                4.5 | Rockford |
| 2470 | Gajalee Sea Food                          |             49 | Bakery, BBQ                                        |                3.9 | Rockford |
| 2861 | Shree Balaji Chaat Bhandar                |             97 | French, Bakery, BBQ, Italian                       |                3.2 | Rockford |
| 3052 | Moets Arabica                             |             43 | Tea, Bakery, Indian, Fast Food                     |                3.5 | Rockford |
| 3163 | Cafe Coffee Day                           |             28 | Chinese, Desserts, Pizza, Cafe, Mediterranean      |                0   | Rockford |
| 3700 | Nutri Punch                               |             34 | Tea, Chinese, Cafe, Desserts                       |                4   | Rockford |
| 4319 | Cafe Southall                             |             56 | Seafood, Pizza, Cafe, Fast Food                    |                4.2 | Rockford |
| 4348 | Eggspectation - Jaypee Vasant Continental |             77 | Tea, Mediterranean, Seafood                        |                3.6 | Rockford |
| 4542 | Aroma Rest O Bar                          |             58 | Bakery, Fast Food, Chinese, American, Seafood      |                3.6 | Rockford |
| 4735 | Advance Bakery                            |            100 | Desserts, Pizza, Mexican, Bakery, Chinese, Seafood |                2.9 | Rockford |
| 4789 | Dial A Cake                               |             29 | Cafe, American, Mediterranean, Desserts            |                0   | Rockford |
| 5309 | U Like                                    |             32 | Tea, French, Desserts                              |                0   | Rockford |
| 5459 | Subway                                    |             42 | Tea, Chinese, Pizza                                |                3.4 | Rockford |
| 5661 | Aggarwal Sweet Centre                     |             81 | Desserts, Tea, Italian, Bakery, Cafe               |                0   | Rockford |
| 6078 | Aggarwal Sweets Centre                    |             73 | Fast Food, Chinese, BBQ, Italian                   |                0   | Rockford |
| 6313 | Giri Momos Centre & Chinese Fast Food     |             44 | Cafe, Indian, Seafood                              |                2.4 | Rockford |
| 6388 | Mr. Confectioner - Pride Plaza Hotel      |             74 | Bakery, Desserts                                   |                0   | Rockford |
| 6507 | Faaso's                                   |             98 | Bakery, Desserts, Seafood                          |                0   | Rockford |
| 6796 | Hangchuaa's Chinese Food Corner           |             64 | Tea, BBQ, Seafood                                  |                3.1 | Rockford |
| 7295 | Grappa - Shangri-La's - Eros Hotel        |             21 | Bakery, Desserts, Italian                          |                3.4 | Rockford |
| 7955 | New Bhappe Di Hatti                       |             76 | Seafood, Mexican, BBQ, Fast Food                   |                0   | Rockford |
| 8095 | Dunkin' Donuts                            |             24 | Cafe, Bakery, BBQ, Seafood                         |                0   | Rockford |
| 8455 | Subway                                    |             26 | Bakery, Pizza, BBQ, Desserts                       |                3.8 | Rockford |
| 8821 | The Gourmet Shack                         |             77 | Tea, Pizza, Indian, Fast Food                      |                3.3 | Rockford |
| 8844 | Mirchievous                               |             64 | American, Indian, BBQ, Seafood                     |                3.1 | Rockford |
| 9340 | Chaophraya                                |             74 | Chinese, Pizza, Cafe, Desserts                     |                3.9 | Rockford |

Here are some restaurant options available in Rockford with their details:

1. **Coco Bambu**
   - Cuisine: Tea, French, Bakery, BBQ, Cafe
   - Average Cost: $72
   - Rating: 4.9

2. **Flying Mango**
   - Cuisine: American, BBQ, Seafood
   - Average Cost: $20
   - Rating: 4.5

3. **Gajalee Sea Food**
   - Cuisine: Bakery, BBQ
   - Average Cost: $49
   - Rating: 3.9

4. **Shree Balaji Chaat Bhandar**
   - Cuisine: French, Bakery, BBQ, Italian
   - Average Cost: $97
   - Rating: 3.2

5. **Moets Arabica**
   - Cuisine: Tea, Bakery, Indian, Fast Food
   - Average Cost: $43
   - Rating: 3.5

6. **Cafe Coffee Day**
   - Cuisine: Chinese, Desserts, Pizza, Cafe, Mediterranean
   - Average Cost: $28
   - Rating: Not Rated

7. **Nutri Punch**
   - Cuisine: Tea, Chinese, Cafe, Desserts
   - Average Cost: $34
   - Rating: 4.0

8. **Cafe Southall**
   - Cuisine: Seafood, Pizza, Cafe, Fast Food
   - Average Cost: $56
   - Rating: 4.2

9. **Eggspectation - Jaypee Vasant Continental**
   - Cuisine: Tea, Mediterranean, Seafood
   - Average Cost: $77
   - Rating: 3.6

10. **Aroma Rest O Bar**
    - Cuisine: Bakery, Fast Food, Chinese, American, Seafood
    - Average Cost: $58
    - Rating: 3.6

11. **Advance Bakery**
    - Cuisine: Desserts, Pizza, Mexican, Bakery, Chinese, Seafood
    - Average Cost: $100
    - Rating: 2.9

12. **Dial A Cake**
    - Cuisine: Cafe, American, Mediterranean, Desserts
    - Average Cost: $29
    - Rating: Not Rated

13. **U Like**
    - Cuisine: Tea, French, Desserts
    - Average Cost: $32
    - Rating: Not Rated

14. **Subway**
    - Cuisine: Tea, Chinese, Pizza
    - Average Cost: $42
    - Rating: 3.4

15. **Aggarwal Sweet Centre**
    - Cuisine: Desserts, Tea, Italian, Bakery, Cafe
    - Average Cost: $81
    - Rating: Not Rated

16. **Aggarwal Sweets Centre**
    - Cuisine: Fast Food, Chinese, BBQ, Italian
    - Average Cost: $73
    - Rating: Not Rated

17. **Giri Momos Centre & Chinese Fast Food**
    - Cuisine: Cafe, Indian, Seafood
    - Average Cost: $44
    - Rating: 2.4

18. **Mr. Confectioner - Pride Plaza Hotel**
    - Cuisine: Bakery, Desserts
    - Average Cost: $74
    - Rating: Not Rated

19. **Faaso's**
    - Cuisine: Bakery, Desserts, Seafood
    - Average Cost: $98
    - Rating: Not Rated

20. **Hangchuaa's Chinese Food Corner**
    - Cuisine: Tea, BBQ, Seafood
    - Average Cost: $64
    - Rating: 3.1

21. **Grappa - Shangri-La's - Eros Hotel**
    - Cuisine: Bakery, Desserts, Italian
    - Average Cost: $21
    - Rating: 3.4

22. **New Bhappe Di Hatti**
    - Cuisine: Seafood, Mexican, BBQ, Fast Food
    - Average Cost: $76
    - Rating: Not Rated

23. **Dunkin' Donuts**
    - Cuisine: Cafe, Bakery, BBQ, Seafood
    - Average Cost: $24
    - Rating: Not Rated

24. **Subway (another location)**
    - Cuisine: Bakery, Pizza, BBQ, Desserts
    - Average Cost: $26
    - Rating: 3.8

25. **The Gourmet Shack**
    - Cuisine: Tea, Pizza, Indian, Fast Food
    - Average Cost: $77
    - Rating: 3.3

26. **Mirchievous**
    - Cuisine: American, Indian, BBQ, Seafood
    - Average Cost: $64
    - Rating: 3.1

27. **Chaophraya**
    - Cuisine: Chinese, Pizza, Cafe, Desserts
    - Average Cost: $74
    - Rating: 3.9

Given these diverse options, we can include Coco Bambu, Flying Mango, and Cafe Coffee Day considering the ratings and average costs for dining during the trip.

Next, let's find some attractions to visit in Rockford. I'll search for attractions in Rockford.

```
[function call]: AttractionSearch(**{'city': 'Rockford'})
```
api_response:
|    | Name                                    |   Latitude |   Longitude | Address                                                          | Phone          | Website                                                                 | City     |
|---:|:----------------------------------------|-----------:|------------:|:-----------------------------------------------------------------|:---------------|:------------------------------------------------------------------------|:---------|
|  0 | Burpee Museum of Natural History        |    42.2773 |    -89.0881 | 737 N Main St, Rockford, IL 61103, USA                           | (815) 965-3433 | http://www.burpee.org/                                                  | Rockford |
|  1 | Midway Village Museum                   |    42.2805 |    -88.9846 | 6799 Guilford Rd, Rockford, IL 61107, USA                        | (815) 397-9112 | https://www.midwayvillage.com/                                          | Rockford |
|  2 | Discovery Center Museum                 |    42.2771 |    -89.0894 | 711 N Main St, Rockford, IL 61103, USA                           | (815) 963-6769 | http://www.discoverycentermuseum.org/                                   | Rockford |
|  3 | Tinker Swiss Cottage Museum and Gardens |    42.2641 |    -89.1028 | 411 Kent St, Rockford, IL 61102, USA                             | (815) 964-2424 | http://www.tinkercottage.com/                                           | Rockford |
|  4 | Anderson Japanese Gardens               |    42.2901 |    -89.0578 | 318 Spring Creek Rd, Rockford, IL 61107, USA                     | (815) 229-9390 | http://andersongardens.org/                                             | Rockford |
|  5 | Nicholas Conservatory & Gardens         |    42.2823 |    -89.0707 | 1354 N 2nd St, Rockford, IL 61107, USA                           | (815) 987-8858 | http://www.nicholasconservatory.com/                                    | Rockford |
|  6 | Erlander Home Museum                    |    42.2641 |    -89.0887 | 404 S 3rd St, Rockford, IL 61104, USA                            | (815) 963-5559 | http://www.swedishhistorical.org/                                       | Rockford |
|  7 | Ethnic Heritage Museum                  |    42.2611 |    -89.1009 | 1129 S Main St, Rockford, IL 61101, USA                          | (815) 962-7402 | https://www.ethnicheritagemuseum.org/                                   | Rockford |
|  8 | Sinnissippi Park                        |    42.2827 |    -89.0641 | 1401 N 2nd St, Rockford, IL 61107, USA                           | (815) 987-8858 | http://rockfordparkdistrict.org/ncg                                     | Rockford |
|  9 | Klehm Arboretum & Botanic Garden        |    42.2445 |    -89.1125 | 2715 S Main St, Rockford, IL 61102, USA                          | (815) 965-8146 | http://www.klehm.org/                                                   | Rockford |
| 10 | Davis Park at Founders Landing          |    42.2683 |    -89.0954 | 320 S Wyman St, Rockford, IL 61101, USA                          | (815) 968-5600 | https://www.gorockford.com/listings/davis-park-at-founders-landing/275/ | Rockford |
| 11 | Frank Lloyd Wright's Laurent House      |    42.2998 |    -89.0244 | 4646 Spring Brook Rd, Rockford, IL 61114, USA                    | (815) 877-2952 | http://www.laurenthouse.com/                                            | Rockford |
| 12 | Sinnissippi Gardens                     |    42.284  |    -89.0679 | 1354 N 2nd St, Rockford, IL 61107, USA                           | (815) 987-8858 | https://nicholasconservatory.com/                                       | Rockford |
| 13 | Riverfront Museum Park                  |    42.2768 |    -89.0889 | Ste 3, 711 N Main St, Rockford, IL 61103, USA                    | (815) 962-0105 | Unknown                                                                 | Rockford |
| 14 | Searls Park                             |    42.3007 |    -89.1241 | 4950 Safford Rd, Rockford, IL 61101, USA                         | (815) 987-8800 | http://rockfordparkdistrict.org/                                        | Rockford |
| 15 | La Paloma Gardens                       |    42.2937 |    -89.0346 | 3622 Brookview Rd, Rockford, IL 61107, USA                       | (815) 399-0324 | http://www.lapalomagardens.com/                                         | Rockford |
| 16 | Rockford Park District                  |    42.2684 |    -89.0972 | 401 S Main St, Rockford, IL 61101, USA                           | (815) 987-8800 | https://rockfordparkdistrict.org/                                       | Rockford |
| 17 | Aldeen Park                             |    42.2741 |    -89.0228 | 623 N Alpine Rd, Rockford, IL 61107, USA                         | Unknown        | https://www.rockfordparkdistrict.org/                                   | Rockford |
| 18 | Blackhawk Springs Forest Preserve       |    42.2047 |    -88.9916 | 5360 Mulford Road &, 5801 Perryville Rd, Rockford, IL 61109, USA | (815) 877-6100 | http://winnebagoforest.org/preserves/blackhawk-springs/                 | Rockford |
| 19 | Ingersoll Centennial Park               |    42.2663 |    -89.0914 | 315 S 1st St, Rockford, IL 61104, USA                            | (815) 987-8800 | http://rockfordparkdistrict.org/                                        | Rockford |

Here are some recommended attractions to visit in Rockford:

1. **Burpee Museum of Natural History**
   - Address: 737 N Main St, Rockford, IL 61103, USA
   - Phone: (815) 965-3433
   - Website: [burpee.org](http://www.burpee.org/)

2. **Midway Village Museum**
   - Address: 6799 Guilford Rd, Rockford, IL 61107, USA
   - Phone: (815) 397-9112
   - Website: [midwayvillage.com](https://www.midwayvillage.com/)

3. **Discovery Center Museum**
   - Address: 711 N Main St, Rockford, IL 61103, USA
   - Phone: (815) 963-6769
   - Website: [discoverycentermuseum.org](http://www.discoverycentermuseum.org/)

4. **Tinker Swiss Cottage Museum and Gardens**
   - Address: 411 Kent St, Rockford, IL 61102, USA
   - Phone: (815) 964-2424
   - Website: [tinkercottage.com](http://www.tinkercottage.com/)

5. **Anderson Japanese Gardens**
   - Address: 318 Spring Creek Rd, Rockford, IL 61107, USA
   - Phone: (815) 229-9390
   - Website: [andersongardens.org](http://andersongardens.org/)

6. **Nicholas Conservatory & Gardens**
   - Address: 1354 N 2nd St, Rockford, IL 61107, USA
   - Phone: (815) 987-8858
   - Website: [nicholasconservatory.com](http://www.nicholasconservatory.com/)

7. **Erlander Home Museum**
   - Address: 404 S 3rd St, Rockford, IL 61104, USA
   - Phone: (815) 963-5559
   - Website: [swedishhistorical.org](http://www.swedishhistorical.org/)

8. **Ethnic Heritage Museum**
   - Address: 1129 S Main St, Rockford, IL 61101, USA
   - Phone: (815) 962-7402
   - Website: [ethnicheritagemuseum.org](https://www.ethnicheritagemuseum.org/)

9. **Sinnissippi Park**
   - Address: 1401 N 2nd St, Rockford, IL 61107, USA
   - Phone: (815) 987-8858
   - Website: [rockfordparkdistrict.org](http://rockfordparkdistrict.org/ncg)

10. **Klehm Arboretum & Botanic Garden**
    - Address: 2715 S Main St, Rockford, IL 61102, USA
    - Phone: (815) 965-8146
    - Website: [klehm.org](http://www.klehm.org/)

11. **Davis Park at Founders Landing**
    - Address: 320 S Wyman St, Rockford, IL 61101, USA
    - Phone: (815) 968-5600
    - Website: [gorockford.com](https://www.gorockford.com/listings/davis-park-at-founders-landing/275/)

12. **Frank Lloyd Wright's Laurent House**
    - Address: 4646 Spring Brook Rd, Rockford, IL 61114, USA
    - Phone: (815) 877-2952
    - Website: [laurenthouse.com](http://www.laurenthouse.com/)

13. **Sinnissippi Gardens**
    - Address: 1354 N 2nd St, Rockford, IL 61107, USA
    - Phone: (815) 987-8858
    - Website: [nicholasconservatory.com](https://nicholasconservatory.com/)

14. **Riverfront Museum Park**
    - Address: Ste 3, 711 N Main St, Rockford, IL 61103, USA

15. **Searls Park**
    - Address: 4950 Safford Rd, Rockford, IL 61101, USA
    - Phone: (815) 987-8800
    - Website: [rockfordparkdistrict.org](http://rockfordparkdistrict.org/)

16. **La Paloma Gardens**
    - Address: 3622 Brookview Rd, Rockford, IL 61107, USA
    - Phone: (815) 399-0324
    - Website: [lapalomagardens.com](http://www.lapalomagardens.com/)

17. **Rockford Park District**
    - Address: 401 S Main St, Rockford, IL 61101, USA
    - Phone: (815) 987-8800
    - Website: [rockfordparkdistrict.org](https://rockfordparkdistrict.org/)

18. **Aldeen Park**
    - Address: 623 N Alpine Rd, Rockford, IL 61107, USA
    - Website: [rockfordparkdistrict.org](https://www.rockfordparkdistrict.org/)

19. **Blackhawk Springs Forest Preserve**
    - Address: 5360 Mulford Road &, 5801 Perryville Rd, Rockford, IL 61109, USA
    - Phone: (815) 877-6100
    - Website: [winnebagoforest.org](http://winnebagoforest.org/preserves/blackhawk-springs/)

20. **Ingersoll Centennial Park**
    - Address: 315 S 1st St, Rockford, IL 61104, USA
    - Phone: (815) 987-8800
    - Website: [rockfordparkdistrict.org](http://rockfordparkdistrict.org/)

With this gathered information, we are ready to summarize the trip plan. Here is the structured plan based on a budget of $1,700:

### Day 1: March 16, 2022
- **Current City:** Traveling from St. Petersburg to Rockford
- **Transportation:** 
  - **Flight:** F3573659 
  - **From:** St. Petersburg 
  - **To:** Rockford 
  - **Departure Time:** 15:40 
  - **Arrival Time:** 17:04 
  - **Cost:** $474
- **Accommodation:** Private Room in a two bedroom apt ($210 for two nights)
- **Dinner:**
  - **Restaurant:** Flying Mango
  - **Cuisine:** American, BBQ, Seafood
  - **Cost:** $20
  - **Rating:** 4.5

### Day 2: March 17, 2022
- **Current City:** Rockford
- **Transportation:** 
  - None
- **Breakfast:**
  - **Restaurant:** Cafe Coffee Day
  - **Cuisine:** Chinese, Desserts, Pizza, Cafe, Mediterranean
  - **Cost:** $28
  - **Rating:** Not Rated
- **Attraction(s):**
  - **Anderson Japanese Gardens**
    - **Address:** 318 Spring Creek Rd, Rockford, IL 61107, USA
    - **Phone:** (815) 229-9390
    - **Website:** [andersongardens.org](http://andersongardens.org/)
  - **Nicholas Conservatory & Gardens**
    - **Address:** 1354 N 2nd St, Rockford, IL 61107, USA
    - **Phone:** (815) 987-8858
    - **Website:** [nicholasconservatory.com](http://www.nicholasconservatory.com/)
- **Lunch:**
  - **Restaurant:** Nutri Punch
  - **Cuisine:** Tea, Chinese, Cafe, Desserts
  - **Cost:** $34
  - **Rating:** 4.0
- **Attraction(s):**
  - **Burpee Museum of Natural History**
    - **Address:** 737 N Main St, Rockford, IL 61103, USA
    - **Phone:** (815) 965-3433
    - **Website:** [burpee.org](http://www.burpee.org/)
  - **Discovery Center Museum**
    - **Address:** 711 N Main St, Rockford, IL 61103, USA
    - **Phone:** (815) 963-6769
    - **Website:** [discoverycentermuseum.org](http://www.discoverycentermuseum.org/)
- **Dinner:**
  - **Restaurant:** Coco Bambu
  - **Cuisine:** Tea, French, Bakery, BBQ, Cafe
  - **Cost:** $72
  - **Rating:** 4.9

### Day 3: March 18, 2022
- **Current City:** Rockford
- **Transportation:**
  - None
- **Breakfast:**
  - **Restaurant:** Shree Balaji Chaat Bhandar
  - **Cuisine:** French, Bakery, BBQ, Italian
  - **Cost:** $97
  - **Rating:** 3.2
- **Attraction(s):**
  - **Tinker Swiss Cottage Museum and Gardens**
    - **Address:** 411 Kent St, Rockford, IL 61102, USA
    - **Phone:** (815) 964-2424
    - **Website:** [tinkercottage.com](http://www.tinkercottage.com/)
  - **Midway Village Museum**
    - **Address:** 6799 Guilford Rd, Rockford, IL 61107, USA
    - **Phone:** (815) 397-9112
    - **Website:** [midwayvillage.com](https://www.midwayvillage.com/)
- **Lunch:**
  - **Restaurant:** Cafe Southall
  - **Cuisine:** Seafood, Pizza, Cafe, Fast Food
  - **Cost:** $56
  - **Rating:** 4.2
- **Final expenditure summary:**
  - **Flight:** $474
  - **Accommodation:** $210 (2 nights in Private Room in a two bedroom apt)
  - **Meals:** $20 + $28 + $34 + $72 + $97 + $56 = $307
  - **Total:** $991

The trip plan is well within the budget of $1,700.

I hope this plan meets your requirements. If there are any adjustments needed, feel free to let me know!



