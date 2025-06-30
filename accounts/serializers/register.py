from rest_framework import serializers

from accounts.models.user import CustomUser

class RegisterSerializer(serializers.ModelSerializer):
    referral_code = serializers.CharField(write_only=True, required=False)

    def create(self, validated_data):
        referral_code = validated_data.pop("referral_code", None)
        user = CustomUser.objects.create_user(**validated_data)
        if referral_code:
            try:
                referrer = CustomUser.objects.get(referral_code=referral_code)
                user.referred_by = referrer
                user.save()
                referrer.loyalty_points += 20  # Award points to referrer
                referrer.save()
            except CustomUser.DoesNotExist:
                pass
        return user