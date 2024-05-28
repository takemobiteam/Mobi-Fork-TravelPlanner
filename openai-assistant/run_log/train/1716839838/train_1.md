### query_id:
train_1
### query:
Can you provide a travel plan for 1 person departing from Kansas City to Pensacola for 3 days, from March 27th to March 29th, 2022, with a budget of $900?



```
[function call]: FlightSearch(**{'origin': 'Kansas City', 'destination': 'Pensacola', 'departure_date': '2022-03-27'})
```
api_response:
no valid information

It seems there was an error retrieving flight information for the specified dates. I'll attempt to search again with a different date format to see if we can get better results.

### Flight Search Retry

Let's retry searching for flights from Kansas City to Pensacola on March 27th, 2022.

### STEP 2: Accommodation Search

Meanwhile, let's proceed with searching accommodations in Pensacola.



```
[function call]: FlightSearch(**{'origin': 'Kansas City', 'destination': 'Pensacola', 'departure_date': '2022-03-27'})
```
api_response:
no valid information



```
[function call]: AccommodationSearch(**{'city': 'Pensacola'})
```
api_response:
|      | NAME                                              |   price | room type       | house_rules                                 |   minimum nights |   maximum occupancy |   review rate number | city      |
|-----:|:--------------------------------------------------|--------:|:----------------|:--------------------------------------------|-----------------:|--------------------:|---------------------:|:----------|
|  293 | CHARMING ONE BEDROOM APT IN LES/CHINATOWN         |     430 | Entire home/apt | No parties & No children under 10           |                4 |                   4 |                    1 | Pensacola |
|  743 | Luxury East Village Penthouse With Private Deck   |     697 | Entire home/apt | No visitors                                 |                2 |                   6 |                    3 | Pensacola |
|  818 | Amazing apartment near museum, gardens & park!    |      74 | Entire home/apt | No parties                                  |               17 |                   3 |                    5 | Pensacola |
| 1445 | Cozy 1-Bedroom Apartment 2 Blocks from the Subway |     339 | Entire home/apt | No parties                                  |                2 |                   3 |                    4 | Pensacola |
| 1602 | AMAZING  2BR Apartment Elev/laundry!              |      56 | Entire home/apt | No parties & No children under 10 & No pets |               30 |                   2 |                    4 | Pensacola |
| 2202 | Chic Historic Harlem Brownstone                   |     526 | Entire home/apt | No smoking                                  |                3 |                   2 |                    4 | Pensacola |
| 2842 | Clean and Cozy Brooklyn Room in Artsy Apartment   |     514 | Private room    | No pets                                     |                1 |                   1 |                    3 | Pensacola |
| 3049 | EMPIRE STATE BUILDING APARTMENT                   |     662 | Entire home/apt | No smoking & No visitors                    |                7 |                   2 |                    5 | Pensacola |
| 3332 | 1D  Private Rm  in Guesthouse Manhattan           |     378 | Private room    | No visitors & No parties                    |                1 |                   1 |                    3 | Pensacola |
| 3902 | Stylish and cozy East Village 2 bedroom apartment |    1036 | Entire home/apt | No parties                                  |                1 |                   5 |                    4 | Pensacola |
| 4465 | Comfy Room                                        |      92 | Private room    | No parties & No smoking & No pets           |                4 |                   1 |                    2 | Pensacola |
| 4510 | Spacious 1BR Haven in Duplex w/Deck               |    1050 | Private room    | No parties                                  |                7 |                   2 |                    2 | Pensacola |

### Available Accommodations in Pensacola

Here are some options for accommodations:

1. **CHARMING ONE BEDROOM APT IN LES/CHINATOWN**
   - Price: $430.0 per night (Minimum nights: 4)
   - Room Type: Entire home/apt
   - Maximum Occupancy: 4
   - Review Rate: 1.0
   - Rules: No parties & No children under 10

2. **Luxury East Village Penthouse With Private Deck**
   - Price: $697.0 per night (Minimum nights: 2)
   - Room Type: Entire home/apt
   - Maximum Occupancy: 6
   - Review Rate: 3.0
   - Rules: No visitors

3. **Amazing apartment near museum, gardens & park!**
   - Price: $74.0 per night (Minimum nights: 17)
   - Room Type: Entire home/apt
   - Maximum Occupancy: 3
   - Review Rate: 5.0
   - Rules: No parties

4. **Cozy 1-Bedroom Apartment 2 Blocks from the Subway**
   - Price: $339.0 per night (Minimum nights: 2)
   - Room Type: Entire home/apt
   - Maximum Occupancy: 3
   - Review Rate: 4.0
   - Rules: No parties

5. **AMAZING 2BR Apartment Elev/laundry!**
   - Price: $56.0 per night (Minimum nights: 30)
   - Room Type: Entire home/apt
   - Maximum Occupancy: 2
   - Review Rate: 4.0
   - Rules: No parties, No children under 10, No pets

6. **Chic Historic Harlem Brownstone**
   - Price: $526.0 per night (Minimum nights: 3)
   - Room Type: Entire home/apt
   - Maximum Occupancy: 2
   - Review Rate: 4.0
   - Rules: No smoking

7. **Clean and Cozy Brooklyn Room in Artsy Apartment**
   - Price: $514.0 per night (Minimum nights: 1)
   - Room Type: Private room
   - Maximum Occupancy: 1
   - Review Rate: 3.0
   - Rules: No pets

8. **EMPIRE STATE BUILDING APARTMENT**
   - Price: $662.0 per night (Minimum nights: 7)
   - Room Type: Entire home/apt
   - Maximum Occupancy: 2
   - Review Rate: 5.0
   - Rules: No smoking, No visitors

9. **1D Private Rm in Guesthouse Manhattan**
   - Price: $378.0 per night (Minimum nights: 1)
   - Room Type: Private room
   - Maximum Occupancy: 1
   - Review Rate: 3.0
   - Rules: No visitors, No parties

10. **Stylish and cozy East Village 2 bedroom apartment**
    - Price: $1036.0 per night (Minimum nights: 1)
    - Room Type: Entire home/apt
    - Maximum Occupancy: 5
    - Review Rate: 4.0
    - Rules: No parties

11. **Comfy Room**
    - Price: $92.0 per night (Minimum nights: 4)
    - Room Type: Private room
    - Maximum Occupancy: 1
    - Review Rate: 2.0
    - Rules: No parties, No smoking, No pets

12. **Spacious 1BR Haven in Duplex w/Deck**
    - Price: $1050.0 per night (Minimum nights: 7)
    - Room Type: Private room
    - Maximum Occupancy: 2
    - Review Rate: 2.0
    - Rules: No parties

Let's choose an option that fits the budget. The best options considering budget and other constraints are:
- **Cozy 1-Bedroom Apartment 2 Blocks from the Subway**

### Step 3: Explore Dining Options in Pensacola

Next, let's find restaurants in Pensacola.

```
[function call]: RestaurantSearch(**{'city': 'Pensacola'})
```
api_response:
|      | Name                                   |   Average Cost | Cuisines                                          |   Aggregate Rating | City      |
|-----:|:---------------------------------------|---------------:|:--------------------------------------------------|-------------------:|:----------|
|  130 | Frog Hollow Tavern                     |             20 | American, BBQ, Fast Food, Cafe, Indian            |                4.3 | Pensacola |
|  186 | Berry Patch Restaurant                 |             13 | Bakery, BBQ, Desserts, Seafood                    |                4.3 | Pensacola |
|  225 | Bailey's Bar-B-Que                     |             13 | Tea, Bakery, Mediterranean                        |                4.1 | Pensacola |
|  288 | Watershed Cafe                         |             12 | Chinese, BBQ, Desserts                            |                3.7 | Pensacola |
|  415 | Blue Point Grill                       |             75 | French, Indian, Cafe, Desserts                    |                4   | Pensacola |
|  933 | Chicago Pizza                          |             32 | Pizza, Mediterranean, Fast Food                   |                2.7 | Pensacola |
| 1577 | Phantom                                |             94 | Desserts, Pizza, Cafe, Mediterranean, Seafood     |                3.5 | Pensacola |
| 1808 | Fruitpro                               |             95 | Tea, Cafe, Pizza, Desserts                        |                0   | Pensacola |
| 1920 | Kwality Restaurant                     |             29 | Desserts, Tea, French, Fast Food, Chinese         |                0   | Pensacola |
| 2612 | Nukkad                                 |            100 | Tea, Cafe, American, Italian                      |                3.6 | Pensacola |
| 2647 | Keventer's South Indian & Chinese Food |             32 | BBQ, Fast Food                                    |                2.8 | Pensacola |
| 2913 | Jain Coffee House                      |             41 | Cafe, Indian, Mediterranean, BBQ                  |                4.1 | Pensacola |
| 3242 | Nizam's Kathi Kabab                    |             32 | Desserts, BBQ, Fast Food, American, Mediterranean |                3.8 | Pensacola |
| 4288 | Kalpana Restaurant                     |             36 | Tea, Cafe, Bakery, American                       |                3.2 | Pensacola |
| 4344 | Eggspectation - Jaypee Siddharth       |             25 | Cafe, BBQ, Italian                                |                3.5 | Pensacola |
| 4769 | Sialkot                                |             66 | Chinese, Bakery, Seafood                          |                3.1 | Pensacola |
| 4832 | The Midnight Hub - C                   |             32 | Tea, Pizza, Bakery, BBQ, Chinese                  |                2.6 | Pensacola |
| 5089 | Shama Muradabadi                       |             93 | Desserts, Indian, BBQ                             |                0   | Pensacola |
| 5145 | Paapi Paet                             |             96 | Cafe, Mediterranean, Fast Food                    |                3.3 | Pensacola |
| 5591 | Jyoti Dhaba                            |             11 | Tea, Bakery, Fast Food                            |                0   | Pensacola |
| 5652 | Shree Vinayaga Restaurant              |             55 | Desserts, Tea, Pizza, French, Cafe                |                0   | Pensacola |
| 5697 | Prem Chinese Fast Food                 |             89 | Tea, Bakery, Mediterranean, Desserts              |                0   | Pensacola |
| 5796 | Fresh Meat CO                          |             82 | French, Seafood, Desserts, Italian                |                0   | Pensacola |
| 6872 | Mouthmatics                            |             56 | Mexican, BBQ, Desserts                            |                0   | Pensacola |
| 6877 | Shree Balaji Bhojnalaya                |             93 | Fast Food, Seafood, Mexican, Italian              |                0   | Pensacola |
| 6965 | Krispy Kitchen                         |             78 | Fast Food, Bakery, Desserts, Italian              |                0   | Pensacola |
| 7218 | Just Veg                               |             59 | Cafe, Desserts, Fast Food                         |                0   | Pensacola |
| 7370 | Code                                   |             29 | French, Bakery, Indian, Fast Food                 |                2.5 | Pensacola |
| 7464 | Satguru Tiffin Service                 |             50 | American, BBQ, Seafood                            |                0   | Pensacola |
| 7768 | Kayasth Cuisine                        |             69 | Desserts, Cafe, BBQ, Fast Food, Chinese, American |                0   | Pensacola |
| 7913 | South Indian Hut                       |             48 | Tea, Seafood, Fast Food                           |                3.4 | Pensacola |
| 8149 | Saleem's Takeaway                      |             37 | Chinese, Desserts, Fast Food, Cafe, Seafood       |                2.6 | Pensacola |
| 8308 | Hunger's Hub                           |             76 | Fast Food, Indian, BBQ, Seafood                   |                0   | Pensacola |
| 8529 | Swad E Punjab                          |             80 | Pizza, Bakery, Cafe, American, Seafood            |                0   | Pensacola |
| 8794 | Mithaas Sweets                         |             86 | Pizza, Bakery, BBQ, Cafe, Indian, Mediterranean   |                3.1 | Pensacola |
| 9306 | De Fontein Belgian Beer Cafe           |             89 | American, BBQ, Fast Food                          |                2.3 | Pensacola |
| 9319 | Ekim Burgers                           |             33 | Pizza, Desserts, Fast Food                        |                4.5 | Pensacola |
| 9524 | Gaga Manjero                           |             17 | Tea, Desserts, Pizza, BBQ                         |                4.9 | Pensacola |

### Available Dining Options in Pensacola

Here are some dining options in Pensacola along with their average costs and cuisines:

1. **Frog Hollow Tavern**
   - Average Cost: $20
   - Cuisines: American, BBQ, Fast Food, Cafe, Indian
   - Rating: 4.3

2. **Berry Patch Restaurant**
   - Average Cost: $13
   - Cuisines: Bakery, BBQ, Desserts, Seafood
   - Rating: 4.3

3. **Bailey's Bar-B-Que**
   - Average Cost: $13
   - Cuisines: Tea, Bakery, Mediterranean
   - Rating: 4.1

4. **Watershed Cafe**
   - Average Cost: $12
   - Cuisines: Chinese, BBQ, Desserts
   - Rating: 3.7

5. **Blue Point Grill**
   - Average Cost: $75
   - Cuisines: French, Indian, Cafe, Desserts
   - Rating: 4.0

6. **Chicago Pizza**
   - Average Cost: $32
   - Cuisines: Pizza, Mediterranean, Fast Food
   - Rating: 2.7

7. **Phantom**
   - Average Cost: $94
   - Cuisines: Desserts, Pizza, Cafe, Mediterranean, Seafood
   - Rating: 3.5

8. **Fruitpro**
   - Average Cost: $95
   - Cuisines: Tea, Cafe, Pizza, Desserts
   - Rating: 0.0

9. **Kwality Restaurant**
   - Average Cost: $29
   - Cuisines: Desserts, Tea, French, Fast Food, Chinese
   - Rating: 0.0

10. **Nukkad**
    - Average Cost: $100
    - Cuisines: Tea, Cafe, American, Italian
    - Rating: 3.6

From the list above, we'll select a few top-rated and reasonably priced options for breakfast, lunch, and dinner each day.

### Step 4: Identify Attractions in Pensacola

Next, we'll find the attractions in Pensacola that we can visit during the trip.



```
[function call]: AttractionSearch(**{'city': 'Pensacola'})
```
api_response:
|    | Name                                   |   Latitude |   Longitude | Address                                              | Phone          | Website                                                                                         | City      |
|---:|:---------------------------------------|-----------:|------------:|:-----------------------------------------------------|:---------------|:------------------------------------------------------------------------------------------------|:----------|
|  0 | Historic Pensacola Village             |    30.4087 |    -87.2131 | 205 E Zaragoza St, Pensacola, FL 32502, USA          | (850) 595-5993 | http://www.historicpensacola.org/                                                               | Pensacola |
|  1 | Pensacola Museum of Art                |    30.408  |    -87.2134 | 407 S Jefferson St, Pensacola, FL 32502, USA         | (850) 432-6247 | http://www.pensacolamuseum.org/                                                                 | Pensacola |
|  2 | Palafox Street Downtown Pensacola      |    30.4157 |    -87.2159 | 200 N Palafox St, Pensacola, FL 32502, USA           | Unknown        | http://visitpensacola.com/                                                                      | Pensacola |
|  3 | Plaza De Luna Memorial Monument        |    30.4025 |    -87.213  | 900 S Palafox St, Pensacola, FL 32502, USA           | (850) 436-5670 | https://www.cityofpensacola.com/facilities/facility/details/plazadeluna-75                      | Pensacola |
|  4 | The Graffiti Bridge                    |    30.4204 |    -87.1939 | N 17th Ave, Pensacola, FL 32502, USA                 | (850) 361-9306 | http://thegraffitibridge.com/                                                                   | Pensacola |
|  5 | Pensacola Children's Museum            |    30.4083 |    -87.2127 | 115 Zaragoza St, Pensacola, FL 32502, USA            | (850) 595-1559 | http://www.historicpensacola.org/plan-your-visit/museums-properties/pensacola-childrens-museum/ | Pensacola |
|  6 | Go Retro                               |    30.4197 |    -87.2196 | 610 N Spring St, Pensacola, FL 32501, USA            | (850) 466-5220 | http://www.goretro.us/                                                                          | Pensacola |
|  7 | Museum of Commerce                     |    30.4086 |    -87.2115 | 201 Zaragoza St, Pensacola, FL 32502, USA            | (850) 595-5985 | https://historicpensacola.org/plan-your-visit/museums-properties/museum-of-commerce/            | Pensacola |
|  8 | The Quina House Museum                 |    30.411  |    -87.2093 | 204 S Alcaniz St, Pensacola, FL 32502, USA           | (850) 432-3050 | https://pensacolahistoricpreservationsociety.com/quinahouse                                     | Pensacola |
|  9 | Bay Bluffs Park                        |    30.4551 |    -87.1685 | 3400 Scenic Hwy, Pensacola, FL 32503, USA            | (850) 435-1603 | http://cityofpensacola.com/Facilities/Facility/Details/Bay-Bluffs-Preserve-18                   | Pensacola |
| 10 | Pensacola MESS Hall                    |    30.418  |    -87.2102 | 418 E Wright St, Pensacola, FL 32502, USA            | (877) 937-6377 | http://www.pensacolamesshall.org/                                                               | Pensacola |
| 11 | Pensacola Bay City Ferry               |    30.4051 |    -87.2122 | 750 Commendencia St, Pensacola, FL 32502, USA        | (850) 466-3379 | https://www.pensacolabaycityferry.com/                                                          | Pensacola |
| 12 | Museum of Industry                     |    30.409  |    -87.2116 | 200 Zaragoza St, Pensacola, FL 32502, USA            | (850) 595-5985 | http://historicpensacola.org/plan-your-visit/museums-properties/museum-of-industry/             | Pensacola |
| 13 | Pensacola                              |    30.4213 |    -87.2169 | Pensacola, FL 32501, USA                             | Unknown        | https://www.visitpensacola.com/                                                                 | Pensacola |
| 14 | Pensacola Lighthouse & Maritime Museum |    30.346  |    -87.3081 | 2081 Radford Blvd, Pensacola, FL 32508, USA          | (850) 393-1561 | http://www.pensacolalighthouse.org/                                                             | Pensacola |
| 15 | Splash City Adventures                 |    30.4881 |    -87.2617 | 6709 Pensacola Blvd, Pensacola, FL 32505, USA        | (850) 505-0800 | http://splashcityadventure.com/                                                                 | Pensacola |
| 16 | Pensacola Aviation Discovery Park      |    30.4716 |    -87.1814 | 4200 Jerry L Maygarden Rd, Pensacola, FL 32504, USA  | Unknown        | Unknown                                                                                         | Pensacola |
| 17 | Seville Square                         |    30.4095 |    -87.2097 | 311 E Government St, Pensacola, FL 32502, USA        | (850) 436-5670 | http://www.ci.pensacola.fl.us/                                                                  | Pensacola |
| 18 | The Twin Bluffs                        |    30.4598 |    -87.165  | 3700 Scenic Hwy, Pensacola, FL 32504, USA            | Unknown        | Unknown                                                                                         | Pensacola |
| 19 | Fort Pickens                           |    30.3273 |    -87.2905 | 1400 Fort Pickens Rd, Pensacola Beach, FL 32561, USA | Unknown        | https://www.nps.gov/guis/planyourvisit/fort-pickens-area.htm                                    | Pensacola |

### Available Attractions in Pensacola

Here are some attractions to explore in Pensacola:

1. **Historic Pensacola Village**
   - Address: 205 E Zaragoza St, Pensacola, FL 32502, USA
   - Phone: (850) 595-5993
   - Website: [historicpensacola.org](http://www.historicpensacola.org/)

2. **Pensacola Museum of Art**
   - Address: 407 S Jefferson St, Pensacola, FL 32502, USA
   - Phone: (850) 432-6247
   - Website: [pensacolamuseum.org](http://www.pensacolamuseum.org/)

3. **Palafox Street Downtown Pensacola**
   - Address: 200 N Palafox St, Pensacola, FL 32502, USA
   - Website: [visitpensacola.com](http://visitpensacola.com/)

4. **Plaza De Luna Memorial Monument**
   - Address: 900 S Palafox St, Pensacola, FL 32502, USA
   - Phone: (850) 436-5670
   - Website: [cityofpensacola.com](https://www.cityofpensacola.com/facilities/facility/details/plazadeluna-75)

5. **The Graffiti Bridge**
   - Address: N 17th Ave, Pensacola, FL 32502, USA
   - Phone: (850) 361-9306
   - Website: [thegraffitibridge.com](http://thegraffitibridge.com/)

6. **Pensacola Children's Museum**
   - Address: 115 Zaragoza St, Pensacola, FL 32502, USA
   - Phone: (850) 595-1559
   - Website: [historicpensacola.org](http://www.historicpensacola.org/plan-your-visit/museums-properties/pensacola-childrens-museum/)

7. **Go Retro**
   - Address: 610 N Spring St, Pensacola, FL 32501, USA
   - Phone: (850) 466-5220
   - Website: [goretro.us](http://www.goretro.us/)

8. **Museum of Commerce**
   - Address: 201 Zaragoza St, Pensacola, FL 32502, USA
   - Phone: (850) 595-5985
   - Website: [historicpensacola.org](https://historicpensacola.org/plan-your-visit/museums-properties/museum-of-commerce/)

9. **The Quina House Museum**
   - Address: 204 S Alcaniz St, Pensacola, FL 32502, USA
   - Phone: (850) 432-3050
   - Website: [pensacolahistoricpreservationsociety.com](https://pensacolahistoricpreservationsociety.com/quinahouse)

10. **Bay Bluffs Park**
    - Address: 3400 Scenic Hwy, Pensacola, FL 32503, USA
    - Phone: (850) 435-1603
    - Website: [cityofpensacola.com](http://cityofpensacola.com/Facilities/Facility/Details/Bay-Bluffs-Preserve-18)

11. **Pensacola MESS Hall**
    - Address: 418 E Wright St, Pensacola, FL 32502, USA
    - Phone: (877) 937-6377
    - Website: [pensacolamesshall.org](http://www.pensacolamesshall.org/)

12. **Pensacola Bay City Ferry**
    - Address: 750 Commendencia St, Pensacola, FL 32502, USA
    - Phone: (850) 466-3379
    - Website: [pensacolabaycityferry.com](https://www.pensacolabaycityferry.com/)

13. **Museum of Industry**
    - Address: 200 Zaragoza St, Pensacola, FL 32502, USA
    - Phone: (850) 595-5985
    - Website: [historicpensacola.org](http://historicpensacola.org/plan-your-visit/museums-properties/museum-of-industry/)

14. **Pensacola Lighthouse & Maritime Museum**
    - Address: 2081 Radford Blvd, Pensacola, FL 32508, USA
    - Phone: (850) 393-1561
    - Website: [pensacolalighthouse.org](http://www.pensacolalighthouse.org/)

15. **Splash City Adventures**
    - Address: 6709 Pensacola Blvd, Pensacola, FL 32505, USA
    - Phone: (850) 505-0800
    - Website: [splashcityadventure.com](http://splashcityadventure.com/)

16. **Pensacola Aviation Discovery Park**
    - Address: 4200 Jerry L Maygarden Rd, Pensacola, FL 32504, USA

17. **Seville Square**
    - Address: 311 E Government St, Pensacola, FL 32502, USA
    - Phone: (850) 436-5670
    - Website: [ci.pensacola.fl.us](http://www.ci.pensacola.fl.us/)

18. **The Twin Bluffs**
    - Address: 3700 Scenic Hwy, Pensacola, FL 32504, USA

19. **Fort Pickens**
    - Address: 1400 Fort Pickens Rd, Pensacola Beach, FL 32561, USA
    - Website: [nps.gov](https://www.nps.gov/guis/planyourvisit/fort-pickens-area.htm)

### Summary Travel Plan

We have all the required information. Let's compile it into a structured 3-day plan ensuring it fits within the budget.

### Transportation Cost Calculation and Accommodation Choice
Due to the unavailability of flight information, we need to make assumptions based on typical costs. We will assume transportation cost for flights to be approximately $300 round trip.

We'll select **Cozy 1-Bedroom Apartment 2 Blocks from the Subway** for accommodations: $339 per night for 2 nights = $678.

### Dining and Attraction Selection
We'll select dining options for breakfast, lunch, and dinner based on the lowest average costs and good reviews. Attractions will be divided over the 3 days of stay.

### Day-by-Day Plan

#### **Day 1: March 27, 2022**
* **Transportation:** 
  - Flight from Kansas City to Pensacola (Approx. $150 one-way)
* **Accommodation:** 
  - Cozy 1-Bedroom Apartment 2 Blocks from the Subway
* **Breakfast:** 
  - Frog Hollow Tavern, Pensacola
* **Attraction:**
  - Historic Pensacola Village
* **Lunch:**
  - Berry Patch Restaurant, Pensacola
* **Attraction:**
  - Pensacola Museum of Art
* **Dinner:**
  - Chicago Pizza, Pensacola

#### **Day 2: March 28, 2022**
* **Transportation:** 
  - None (local travel)
* **Accommodation:** 
  - Cozy 1-Bedroom Apartment 2 Blocks from the Subway
* **Breakfast:** 
  - Frog Hollow Tavern, Pensacola
* **Attraction:**
  - Palafox Street Downtown Pensacola
* **Lunch:**
  - Bailey's Bar-B-Que, Pensacola
* **Attraction:**
  - Plaza De Luna Memorial Monument
* **Dinner:**
  - Watershed Cafe, Pensacola

#### **Day 3: March 29, 2022**
* **Transportation:** 
  - Flight back to Kansas City (Approx. $150 one-way)
* **Accommodation:** 
  - None (checkout)
* **Breakfast:** 
  - Frog Hollow Tavern, Pensacola
* **Attraction:**
  - The Graffiti Bridge
* **Lunch:**
  - Berry Patch Restaurant, Pensacola
* **Attraction:**
  - Pensacola Children's Museum
* **Dinner:**
  - Chicago Pizza, Pensacola

### Budget Summary
- **Flights:** $300 (Round trip)
- **Accommodation:** $678
- **Dining:** Approx. $20/day = $60
- **Attractions:** Variable costs, considered as miscellaneous within overall budget

#### Total Estimated Cost: 
$300 (Flights) + $678 (Accommodation) + $60 (Dining) = $1038

**Note:** This exceeds the initial budget of $900, adjustments can be made by choosing a cheaper accommodation or reducing other costs.

Please review and let me know if you need any adjustments or additional details.




