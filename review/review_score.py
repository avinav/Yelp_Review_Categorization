from review import reviews_df

# accepts id hash and returns Series object
def get_reviews(bus_id):
    return reviews_df[reviews_df.business_id == bus_id].text

    
