from rest_framework import serializers
from .models import BetSlip

class BetSlipSerializer(serializers.ModelSerializer):
    class Meta:
        model = BetSlip
        # these will ultimately be the fields available on the intake form
        # this means no derived fields yet
        fields = (
            'bet_id_slug',
            'bet_date_time', # may not end up using this
            # 'bet_type' # derived from market_name
            'bet_amount',
            # 'n_bets' # probably won't be included at all tbh
            # 'n_legs' # must be derived from entries in web client
            # 'bet_settled' # derived from bet_result field
            'bet_selection',
            'market_name',
            'bet_american_odds', # must be derived from combination of leg odds
            'bet_result',
            # 'payout' # derived from result & potential_payout 
            'potential_payout', # must be derived from odds & bet_amount & leg odds in web client
            # 'leg_settled' # derived from leg_result field
            'leg_result',
            'leg_american_odds',
            # 'bet_settled_date', # may not use this either
            # 'bet_bonus_type', # pending bonus feature implementation
            # 'bet_bonus_amount', # pending bonus feature implementation
            # 'risk_free', # pending bonus feature implementation
            # 'bet_boosted_odds', # pending bonus feature implementation
            # 'bet_bonus_max_winnings_amount', # pending bonus feature implementation
            # 'bet_bonus_winning_amount', # pending bonus feature implementation
            # 'bet_boost_percentage', # pending bonus feature implementation
            # 'boosted_bet', # pending bonus feature implementation
            # 'early_win', # pending bonus feature implementation
            # 'primary', # must be derived when bets are entered in web client
            # 'user_id', # derived from login state
        )