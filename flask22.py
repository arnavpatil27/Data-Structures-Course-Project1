positive_x = ['Majestic', 'Sir M. Visvesvaraya Station, Central College', 'Dr. B.R. Ambedkar Station, Vidhana Soudha', 'Cubbon Park', 'Mahatma Gandhi Road', 'Trinity', 'Halasuru', 'Indiranagar', 'Swami Vivekananda Road', 'Baiyappanahalli', 'Benniganahalli', 'K.R Pura', 'Singayyanapalya', 'Garudacharapalya', 'Hoodi', 'Seetharampalya', 'Kundalahalli', 'Nallur Halli', 'Sri Sathya Sai Hospital', 'Pattandur Agrahara', 'Kadugodi Tree Park', 'Hopefarm Channasandra', 'Whitefield(Kadugodi)']


positive_y = ['Majestic', 'Mantri Square Sampige Road', 'Srirampura', 'Mahakavi Kuvempu Road', 'Rajajinagar', 'Mahalakshmi', 'Sandal Soap Factory', 'Yeshwanthpur', 'Goragunte Palya', 'Peenya', 'Peenya Industry', 'Jalahalli', 'Dasarahalli', 'Nagasandra']


negative_x = ['Majestic', "Krantivira Sangolli Rayanna Railway Station", "Magadi Road", "Balagangadaranatha Swamiji Station, Hosahalli", "Vijayanagar", "Attiguppe", "Deepanjali Nagar", "Mysuru Road", "Pantharapalya - Nayandahalli", "Rajarajeshwari Nagar", "Jnanabharathi", "Pattanagere", "Kengeri Bus Terminal", "Kengeri", "Challaghatta"]


negative_y = ['Majestic', 'Chickpet', 'Krishna Rajendra Market', 'National College', 'Lalbagh', 'South End Circle', 'Jayanagar', 'Rashtreeya Vidyalaya Road', 'Banashankari', 'Jaya Prakash Nagar', 'Yelachenahalli', 'Konanakunte Cross', 'Doddakallasandra', 'Vajarahalli', 'Thalaghattapura', 'Silk Institute']

def calculate_stops(boarding_station, destination_station):
    def find_index(station, station_list):
        try:
            return station_list.index(station)
        except ValueError:
            return -1
        
# If boarding and destination in single list

    if boarding_station in positive_x and destination_station in positive_x:
        stops = abs(find_index(destination_station, positive_x) - find_index(boarding_station, positive_x))
    
    elif boarding_station in positive_y and destination_station in positive_y:
        stops = abs(find_index(destination_station, positive_y) - find_index(boarding_station, positive_y))

    elif boarding_station in negative_x and destination_station in negative_x:
        stops = abs(find_index(destination_station, negative_x) - find_index(boarding_station, negative_x))

    elif boarding_station in negative_y and destination_station in negative_y:
        stops = abs(find_index(destination_station, negative_y) - find_index(boarding_station, negative_y))  
    
    

# If boarding and destination in diffferent list
    
    # Boarding in Positive X
    
    if boarding_station in positive_x and destination_station in positive_y:  
    
        stops = (abs(find_index(boarding_station, positive_x) - find_index('Majestic', positive_x)) +
                 abs(find_index(destination_station, positive_y) - find_index('Majestic', positive_y)))
    
    elif boarding_station in positive_x and destination_station in negative_y:  
    
        stops = (abs(find_index(boarding_station, positive_x) - find_index('Majestic', positive_x)) +
                 abs(find_index(destination_station, negative_y) - find_index('Majestic', negative_y)))
        
    elif boarding_station in positive_x and destination_station in negative_x:  
    
        stops = (abs(find_index(boarding_station, positive_x) - find_index('Majestic', positive_x)) +
                 abs(find_index(destination_station, negative_x) - find_index('Majestic', negative_x)))
        
    # Boarding in Negative X  

    elif boarding_station in negative_x and destination_station in positive_y:  
    
        stops = (abs(find_index(boarding_station, negative_x) - find_index('Majestic', negative_x)) +
                 abs(find_index(destination_station, positive_y) - find_index('Majestic', positive_y)))

    elif boarding_station in negative_x and destination_station in negative_y:  
    
        stops = (abs(find_index(boarding_station, negative_x) - find_index('Majestic', negative_x)) +
                 abs(find_index(destination_station, negative_y) - find_index('Majestic', negative_y)))
        
    elif boarding_station in negative_x and destination_station in positive_x:  
    
        stops = (abs(find_index(boarding_station, negative_x) - find_index('Majestic', negative_x)) +
                 abs(find_index(destination_station, positive_x) - find_index('Majestic', positive_x)))
        
    # Boarding in Positive Y
     
    elif boarding_station in positive_y and destination_station in positive_x:  
    
        stops = (abs(find_index(boarding_station, positive_y) - find_index('Majestic', positive_y)) +
                 abs(find_index(destination_station, positive_x) - find_index('Majestic', positive_x)))     
    
    elif boarding_station in positive_y and destination_station in negative_x:  
    
        stops = (abs(find_index(boarding_station, positive_y) - find_index('Majestic', positive_y)) +
                 abs(find_index(destination_station, negative_x) - find_index('Majestic', negative_x)))   

    elif boarding_station in positive_y and destination_station in negative_y:  
    
        stops = (abs(find_index(boarding_station, positive_y) - find_index('Majestic', positive_y)) +
                 abs(find_index(destination_station, negative_y) - find_index('Majestic', negative_y)))                                                                                                                    
        

    # Boarding in Negative Y

    elif boarding_station in negative_y and destination_station in positive_x:  
    
        stops = (abs(find_index(boarding_station, negative_y) - find_index('Majestic', negative_y)) +
                 abs(find_index(destination_station, positive_x) - find_index('Majestic', positive_x)))
    
    elif boarding_station in negative_y and destination_station in positive_y:  
    
        stops = (abs(find_index(boarding_station, negative_y) - find_index('Majestic', negative_y)) +
                 abs(find_index(destination_station, positive_y) - find_index('Majestic', positive_y)))

    elif boarding_station in negative_y and destination_station in negative_x:  
    
        stops = (abs(find_index(boarding_station, negative_y) - find_index('Majestic', negative_y)) +
                 abs(find_index(destination_station, negative_x) - find_index('Majestic', negative_x)))
    

    return stops
    
def calculate_ticket_price(stops, city_center_stop=False):
    if stops == 0:
        return 0  
    elif stops == 1:
        price = 9
    elif stops == 2:
        price = 14
    elif stops == 3:
        price = 18
    else:
        price = 18 + 2 * (stops - 3)

    if city_center_stop:
        price += 1

    return price