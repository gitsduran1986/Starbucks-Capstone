# -*- coding: utf-8 -*-
"""
Created on Wed May 20 14:09:48 2020

@author: duran
"""
def spending_in_window(offer_start,offer_end,person,transaction_df):
    """sums a customers spending during a window of an offer
    Inputs:
    offer start: when offer was sent
    offer end: offer start + duration of offer
    person: person offer was sent to
    transaction_df: data frame of all transaction labeled offer completed.   
    returns sum of spending within time window for a given customer.  
    """
    sum_df = transaction_df[(transaction_df['time'] >= offer_start) & (transaction_df['time'] <= offer_end) 
                   & (transaction_df['person'] == person)]['amount']
    if sum_df is None:
        return 0
    else:
        return np.sum(sum_df)
    
def check_viewed(offer_start,offer_end,person,offer_viewed_df):
    """searches transactions to see if they had an offer viewed event in the specified timespan
    for an offer's influence.  
    Inputs:
    offer start: when offer was sent
    offer end: offer start + duration of offer
    person: person offer was sent to
    offer_viewed_df: data frame of all transaction labeled offer_viewed.   
    returns 1 if the offer has been viewed, 0 otherwise.  
    """
    person_offer_df = offer_viewed_df[offer_viewed_df['person'] == person]
    column_index = person_offer_df.columns.get_loc('time')
    output = 0
    if person_offer_df is None:
        return output
    else:
        for i in range(0,len(person_offer_df)):
            if person_offer_df.iloc[i,column_index] >= offer_start and person_offer_df.iloc[i,column_index] <= offer_end:
                output = 1
                break
        return output
    
def check_completed(offer_start,offer_end,offer_id,person,offer_completed_df):
    """searches transactions to see if an offer was completed.  
    Inputs:
    offer start: when offer was sent
    offer end: offer start + duration of offer
    offer_id: offer id (portfolio)
    person: person offer was sent to
    offer_completed_df: data frame of all transaction labeled offer completed.   
    returns 1 if the offer has been completed, 0 otherwise.  
    """
    person_offer_df = offer_completed_df[(offer_completed_df['person'] == person) & (offer_completed_df['offer_id'] == offer_id)]
    column_index = person_offer_df.columns.get_loc('time')
    output = 0
    if person_offer_df is None:
        return output
    else:
        for i in range(0,len(person_offer_df)):
            if person_offer_df.iloc[i,column_index] >= offer_start and person_offer_df.iloc[i,column_index] <= offer_end:
                output = 1
                break
    return output


