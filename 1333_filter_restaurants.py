class Solution:
    def filterRestaurants(self, restaurants: list[list[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> list[int]:
        return [i for i, _, veg, price, dist in sorted(restaurants, key=lambda r: (r[1], r[0]), reverse=True)
                if veg >= veganFriendly and price <= maxPrice and dist <= maxDistance]
