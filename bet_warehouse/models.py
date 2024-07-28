from django.db import models

# Create your models here.
class BetSlip(models.Model):
    bet_id_slug = models.SlugField(max_length=200, primary_key=True)
    bet_date_time = models.DateField(auto_now_add=True)
    bet_type = models.CharField(max_length=255) #The type of bet as categorized by Sportsbook
    bet_amount = models.FloatField()
    n_bets = models.IntegerField(blank=True,null=True)
    n_legs = models.IntegerField(default = 0)
    bet_settled = models.BooleanField(default=True)
    bet_selection = models.CharField() # What was bet on (ex: Denver Nuggets)
    market_name = models.CharField(max_length=255) #The market of the bet selection (ex: Spread)
    bet_american_odds = models.IntegerField(default=-110)
    bet_result = models.CharField(max_length=5, default = 'Won') # final result of entire bet
    payout = models.FloatField(default=0) # amount paid out for bet
    potential_payout = models.FloatField(default=0) # payout if bet was won
    leg_settled = models.BooleanField(default=True)
    leg_result = models.CharField(default='Won') # The result (Won/Lost/Draw/Void) of the leg
    leg_american_odds = models.IntegerField(default=-110) # american odds of that specific leg
    bet_settled_date = models.DateField(auto_now_add=True)
    bet_bonus_type = models.CharField(blank=True,null=True) # The type of bonus for the bet (ex: Early Win, Profit Boost, Odds Boost, etc.)
    bet_bonus_amount = models.FloatField(blank=True,null=True) # bonus amount for bet if applicable
    risk_free = models.BooleanField(default=False, blank=True,null=True)
    bet_boosted_odds = models.IntegerField(blank=True,null=True)
    bet_bonus_max_winning_amount = models.FloatField(blank=True,null=True)  # max winning amount of bed
    bet_bonus_winning_amount = models.FloatField(blank=True,null=True) # amount won for bet with bonus
    bet_boost_percentage = models.IntegerField(blank=True,null=True) # percentage boost on bet
    boosted_bet = models.BooleanField(default=False,blank=True,null=True) # if boost is applied
    early_win = models.BooleanField(default=False,blank=True,null=True)
    primary = models.BooleanField(default=False)
    # Assigns a single leg of a bet as Primary to allow for accurate
    # accounting. If you do not filter to Primary = True, then you will
    # duplicate metrics such as Bet Amount, Payout, Potential Payout, etc.
    # Any manual analysis will need to have this data filtered to
    # Primary = 1 in order to be accurate.
    user_id = models.CharField(max_length=255,default='000')

    class Meta:
        ordering = ('-bet_date_time',)

    def ___str___(self):
        return f"bet_{self.bet_id_slug}"
    
    def get_absolute_url(self):
        return f'/bet-slip-{self.bet_id_slug}/'
