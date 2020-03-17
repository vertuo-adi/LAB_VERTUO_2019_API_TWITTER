import pandas as pd
import json

def tweet_df(tweets):
    
    df = pd.DataFrame()
 
    df['created_at'] = list(map(lambda tweet: tweet['created_at'], tweets))
    df['id'] = list(map(lambda tweet: tweet['id'], tweets))
    df['id_str'] = list(map(lambda tweet: tweet['id'], tweets))
    df['full_text'] = list(map(lambda tweet: tweet['full_text'], tweets))
    df['entities'] = list(map(lambda tweet: tweet['entities'], tweets))
    df['entities_symbols'] = list(map(lambda tweet: tweet['entities']['symbols'], tweets))
    df['entities_url'] = list(map(lambda tweet: tweet['entities']['urls'], tweets))
    df['favorite_count'] = list(map(lambda tweet: tweet['favorite_count'], tweets))
    df['favorited'] = list(map(lambda tweet: tweet['favorited'], tweets))
    df['geo'] = list(map(lambda tweet: tweet['geo'], tweets))
    df['in_reply_to_screen_name'] = list(map(lambda tweet: tweet['in_reply_to_screen_name'], tweets))
    df['in_reply_to_status_id'] = list(map(lambda tweet: tweet['in_reply_to_status_id'], tweets))
    df['in_reply_to_status_id_str'] = list(map(lambda tweet: tweet['in_reply_to_status_id_str'], tweets))
    df['in_reply_to_user_id'] = list(map(lambda tweet: tweet['in_reply_to_user_id'], tweets))
    df['in_reply_to_user_id_str'] = list(map(lambda tweet: tweet['in_reply_to_user_id_str'], tweets))
    df['is_quote_status'] = list(map(lambda tweet: tweet['is_quote_status'], tweets))
    df['lang'] = list(map(lambda tweet: tweet['lang'], tweets))
    df['metadata'] = list(map(lambda tweet: tweet['metadata'], tweets))
    df['place'] = list(map(lambda tweet: tweet['place'], tweets))
    df['place_attributes'] = list(map(lambda tweet: tweet['place']['attributes']
                                  if tweet['place'] != None else '', tweets))
    df['place_contained_within'] = list(map(lambda tweet: tweet['place']['contained_within']
                                  if tweet['place'] != None else '', tweets))  
    df['place_country'] = list(map(lambda tweet: tweet['place']['country']
                                  if tweet['place'] != None else '', tweets))  
    df['place_full_name'] = list(map(lambda tweet: tweet['place']['full_name']
                                  if tweet['place'] != None else '', tweets))  
    df['place_id'] = list(map(lambda tweet: tweet['place']['id']
                                  if tweet['place'] != None else '', tweets))  
    df['place_name'] = list(map(lambda tweet: tweet['place']['name']
                                  if tweet['place'] != None else '', tweets))  
    df['place_place_type'] = list(map(lambda tweet: tweet['place']['place_type']
                                  if tweet['place'] != None else '', tweets))  
    df['place_url'] = list(map(lambda tweet: tweet['place']['url']
                                  if tweet['place'] != None else '', tweets))  
    
    
    #df['possibly_sensitive'] = list(map(lambda tweet: tweet['possibly_sensitive'], tweets))
    
    
    df['retweet_count'] = list(map(lambda tweet: tweet['retweet_count'], tweets))
    df['retweeted'] = list(map(lambda tweet: tweet['retweeted'], tweets))
    df['source'] = list(map(lambda tweet: tweet['source'], tweets))
    df['truncated'] = list(map(lambda tweet: tweet['truncated'], tweets))
    
    df['user_contributors_enabled'] = list(map(lambda tweet: tweet['user']['contributors_enabled']
                                  if tweet['user'] != None else '', tweets))      
    df['user_created_at'] = list(map(lambda tweet: tweet['user']['created_at']
                                  if tweet['user'] != None else '', tweets))  
    df['user_default_profile'] = list(map(lambda tweet: tweet['user']['default_profile']
                                  if tweet['user'] != None else '', tweets))  
    df['user_default_profile_image'] = list(map(lambda tweet: tweet['user']['default_profile_image']
                                  if tweet['user'] != None else '', tweets))  
    df['user_description'] = list(map(lambda tweet: tweet['user']['description']
                                  if tweet['user'] != None else '', tweets))  
    df['user_entities'] = list(map(lambda tweet: tweet['user']['entities']
                                  if tweet['user'] != None else '', tweets))  
    df['user_favourites_count'] = list(map(lambda tweet: tweet['user']['favourites_count']
                                  if tweet['user'] != None else '', tweets))  
    df['user_follow_request_sent'] = list(map(lambda tweet: tweet['user']['follow_request_sent']
                                  if tweet['user'] != None else '', tweets))  
    df['user_followers_count'] = list(map(lambda tweet: tweet['user']['followers_count']
                                  if tweet['user'] != None else '', tweets))          
    df['user_following'] = list(map(lambda tweet: tweet['user']['following']
                                  if tweet['user'] != None else '', tweets))  
    df['user_friends_count'] = list(map(lambda tweet: tweet['user']['friends_count']
                                  if tweet['user'] != None else '', tweets))  
    df['user_geo_enabled'] = list(map(lambda tweet: tweet['user']['geo_enabled']
                                  if tweet['user'] != None else '', tweets))  
    df['user_has_extended_profile'] = list(map(lambda tweet: tweet['user']['has_extended_profile']
                                  if tweet['user'] != None else '', tweets))  
    df['user_id'] = list(map(lambda tweet: tweet['user']['id']
                                  if tweet['user'] != None else '', tweets))  
    df['user_id_str'] = list(map(lambda tweet: tweet['user']['id_str']
                                  if tweet['user'] != None else '', tweets))  
    df['user_is_translation_enabled'] = list(map(lambda tweet: tweet['user']['is_translation_enabled']
                                  if tweet['user'] != None else '', tweets))  
    df['user_is_translator'] = list(map(lambda tweet: tweet['user']['is_translator']
                                  if tweet['user'] != None else '', tweets))  
    df['user_lang'] = list(map(lambda tweet: tweet['user']['lang']
                                  if tweet['user'] != None else '', tweets))  
    df['user_listed_count'] = list(map(lambda tweet: tweet['user']['listed_count']
                                  if tweet['user'] != None else '', tweets))  
    df['user_location'] = list(map(lambda tweet: tweet['user']['location']
                                  if tweet['user'] != None else '', tweets))  
    df['user_name'] = list(map(lambda tweet: tweet['user']['name']
                                  if tweet['user'] != None else '', tweets))  
    df['user_notifications'] = list(map(lambda tweet: tweet['user']['notifications']
                                  if tweet['user'] != None else '', tweets))  
    
    df['user_profile_background_color'] = list(map(lambda tweet: tweet['user']['profile_background_color']
                                  if tweet['user'] != None else '', tweets))  
    df['user_profile_background_image_url'] = list(map(lambda tweet: tweet['user']['profile_background_image_url']
                                  if tweet['user'] != None else '', tweets))  
    df['user_profile_background_image_url_https'] = list(map(lambda tweet: tweet['user']['profile_background_image_url_https']
                                  if tweet['user'] != None else '', tweets))  
    df['user_profile_background_tile'] = list(map(lambda tweet: tweet['user']['profile_background_tile']
                                  if tweet['user'] != None else '', tweets))
    #df['profile_banner_url'] = list(map(lambda tweet: tweet['user']['profile_banner_url']
    #                              if tweet['user'] != None else '', tweets))
    df['user_profile_image_url'] = list(map(lambda tweet: tweet['user']['profile_image_url']
                                  if tweet['user'] != None else '', tweets))  
    df['user_profile_image_url_https'] = list(map(lambda tweet: tweet['user']['profile_image_url_https']
                                  if tweet['user'] != None else '', tweets))  
    df['user_profile_link_color'] = list(map(lambda tweet: tweet['user']['profile_link_color']
                                  if tweet['user'] != None else '', tweets))  
    df['user_profile_sidebar_border_color'] = list(map(lambda tweet: tweet['user']['profile_sidebar_border_color']
                                  if tweet['user'] != None else '', tweets))  
    df['user_profile_sidebar_fill_color'] = list(map(lambda tweet: tweet['user']['profile_sidebar_fill_color']
                                  if tweet['user'] != None else '', tweets))  
    df['user_profile_text_color'] = list(map(lambda tweet: tweet['user']['profile_text_color']
                                  if tweet['user'] != None else '', tweets))  
    df['user_profile_use_background_image'] = list(map(lambda tweet: tweet['user']['profile_use_background_image']
                                  if tweet['user'] != None else '', tweets))  
    df['user_protected'] = list(map(lambda tweet: tweet['user']['protected']
                                  if tweet['user'] != None else '', tweets))  
    df['user_screen_name'] = list(map(lambda tweet: tweet['user']['screen_name']
                                  if tweet['user'] != None else '', tweets))  
    df['user_statuses_count'] = list(map(lambda tweet: tweet['user']['statuses_count']
                                  if tweet['user'] != None else '', tweets))  
    df['user_time_zone'] = list(map(lambda tweet: tweet['user']['time_zone']
                                  if tweet['user'] != None else '', tweets))  
    df['user_translator_type'] = list(map(lambda tweet: tweet['user']['translator_type']
                                  if tweet['user'] != None else '', tweets))  
    df['user_url'] = list(map(lambda tweet: tweet['user']['url']
                                  if tweet['user'] != None else '', tweets))  
    df['user_utc_offset'] = list(map(lambda tweet: tweet['user']['utc_offset']
                                  if tweet['user'] != None else '', tweets))  
    df['user_verified'] = list(map(lambda tweet: tweet['user']['verified']
                                  if tweet['user'] != None else '', tweets))  
    return df



