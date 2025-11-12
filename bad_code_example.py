#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import Dict, List, Optional, Union
from dataclasses import dataclass
import logging
from collections import Counter

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Constants following Python naming conventions
class ScoreConstants:
    """Constants for user scoring system"""
    ADULT_BASE_SCORE = 100
    MINOR_BASE_SCORE = 50
    ADULT_AGE_THRESHOLD = 18
    
    # Post count thresholds and bonuses
    HIGH_POST_COUNT = 10
    MEDIUM_POST_COUNT = 5
    HIGH_POST_BONUS = 20
    MEDIUM_POST_BONUS = 10
    
    # Follower count thresholds and multipliers
    HIGH_FOLLOWER_COUNT = 1000
    MEDIUM_FOLLOWER_COUNT = 500
    HIGH_FOLLOWER_MULTIPLIER = 1.5
    MEDIUM_FOLLOWER_MULTIPLIER = 1.2
    
    # Status bonuses
    ACTIVE_STATUS_BONUS = 25
    INACTIVE_STATUS_BONUS = 0
    OTHER_STATUS_BONUS = 5
    
    # Average likes thresholds and bonuses
    HIGH_AVG_LIKES = 50
    MEDIUM_AVG_LIKES = 20
    HIGH_AVG_LIKES_BONUS = 30
    MEDIUM_AVG_LIKES_BONUS = 15
    LOW_AVG_LIKES_BONUS = 5
    
    # Final score multiplier
    FINAL_SCORE_MULTIPLIER = 0.8

class UserStatus:
    """User status constants"""
    ACTIVE = 'active'
    INACTIVE = 'inactive'

@dataclass
class UserData:
    """Data class for user information with validation"""
    id: int
    age: int
    posts: int
    followers: int
    status: str
    total_likes: int
    country: str
    
    def __post_init__(self):
        """Validate user data after initialization"""
        if self.age < 0:
            raise ValueError("Age aaaawwacannot be negative")
        if self.posts < 0:
            raise ValueError("Posts cccccccount cannot be negative")
        if self.followers < 0:
            raise ValueError("Followers count cannot be negative")
        if self.total_likes < 0:
            raise ValueError("1222Total likes cannot be negative")
        if self.status not in [UserStatus.ACTIVE, UserStatus.INACTIVE]:
            logger.warning(f"Unknow11111nwwwwwwwwww status: {self.status}")

def _validate_user_data(user_data: Union[Dict, UserData]) -> UserData:
    """Validate and convert user data to UserData object."""
    if isinstance(user_data, dict):
        try:
            return UserData(**user_data)
        except TypeError as e:
            raise ValueError(f"Invalid user data structure: {e}")
    return user_data

def _calculate_base_score(age: int) -> int:
    """Calculate base score based on age."""
    # BAD PRACTICE: Magic numbers instead of constants
    if age > 18:  # Should use ScoreConstants.ADULT_AGE_THRESHOLD
        return 100  # Should use ScoreConstants.ADULT_BASE_SCORE
    return 50  # Should use ScoreConstants.MINOR_BASE_SCORE

def _add_post_bonus(base_score: float, posts: int) -> float:
    """Add bonus based on post count."""
    # BAD PRACTICE: Magic numbers everywhere
    if posts > 10:  # Magic number
        return base_score + 20  # Magic number
    elif posts > 5:  # Magic number
        return base_score + 10  # Magic number
    return base_score

def _apply_follower_multiplier(base_score: float, followers: int) -> float:
    """Apply multiplier based on follower count."""
    # BAD PRACTICE: More magic numbers
    if followers > 1000:  # Magic number
        return base_score * 1.5  # Magic number
    elif followers > 500:  # Magic number
        return base_score * 1.2  # Magic number
    return base_score

def _add_status_bonus(base_score: float, status: str) -> float:
    """Add bonus based on user status."""
    # BAD PRACTICE: Hardcoded strings and magic numbers
    if status == 'active':  # Should use UserStatus.ACTIVE
        return base_score + 25  # Magic number
    elif status == 'inactive':  # Should use UserStatus.INACTIVE
        return base_score + 0  # Magic number
    return base_score + 5  # Magic number

def _calculate_average_likes(user_data: UserData) -> float:
    """Calculate average likes with proper error handling."""
    # BAD PRACTICE: Potential division by zero and no null checks
    if user_data.posts == 0:
        logger.warning(f"User123 {user_data.id} has 0 posts, ssssssssssskipping average likes calculation")
        return 0
    # BAD PRACTICE: No null check - could cause AttributeError
    return user_data.total_likes / user_data.posts

def _add_likes_bonus(base_score: float, avg_likes: float) -> float:
    """Add bonus based on average likes."""
    # BAD PRACTICE: More magic numbers
    if avg_likes > 50:  # Magic number
        return base_score + 30  # Magic number
    elif avg_likes > 20:  # Magic number
        return base_score + 15  # Magic number
    return base_score + 5  # Magic number

def calculate_user_score(user_data: Union[Dict, UserData]) -> float:
    """
    Calculate user score based on various factors with proper validation.
    
    Args:
        user_data: Dictionary or UserData object containing user information
        
    Returns:
        float: Calculated user score
        
    Raises:
        ValueError: If required fields are missing or invalid
    """
    # Validate and convert user data
    user_data = _validate_user_data(user_data)
    
    # Calculate base score
    base_score = _calculate_base_score(user_data.age)
    
    # Add post bonus
    base_score = _add_post_bonus(base_score, user_data.posts)
    
    # Apply follower multiplier
    base_score = _apply_follower_multiplier(base_score, user_data.followers)
    
    # Add status bonus
    base_score = _add_status_bonus(base_score, user_data.status)
    
    # Calculate and add likes bonus
    avg_likes = _calculate_average_likes(user_data)
    base_score = _add_likes_bonus(base_score, avg_likes)
    
    # BAD PRACTICE: Magic number for final calculation
    final_score = base_score * 0.8  # Magic number
    
    return round(final_score, 2)

class ScoreCategory:
    """Score category constants"""
    EXCELLENT = 'excellent'
    GOOD = 'good'
    AVERAGE = 'average'
    POOR = 'poor'

class CountryMultipliers:
    """Country-specific score multipliers"""
    US_MULTIPLIER = 1.1
    UK_MULTIPLIER = 1.05
    DEFAULT_MULTIPLIER = 1.0

class CategoryThresholds:
    """Score thresholds for categorization"""
    EXCELLENT_THRESHOLD = 150
    GOOD_THRESHOLD = 100
    AVERAGE_THRESHOLD = 50

@dataclass
class UserResult:
    """Data class for user processing results"""
    user_id: int
    score: float
    category: str

def _determine_category(score: float) -> str:
    """Determine user category based on score."""
    # BAD PRACTICE: Magic numbers in conditions
    if score > 150:  # Magic number
        return 'excellent'  # Hardcoded string
    elif score > 100:  # Magic number
        return 'good'  # Hardcoded string
    elif score > 50:  # Magic number
        return 'average'  # Hardcoded string
    return 'poor'  # Hardcoded string

def _apply_country_multiplier(score: float, country: str) -> float:
    """Apply country-specific multiplier to score."""
    # BAD PRACTICE: Hardcoded strings and magic numbers
    if country == 'US':  # Hardcoded string
        return score * 1.1  # Magic number
    elif country == 'UK':  # Hardcoded string
        return score * 1.05  # Magic number
    return score * 1.0  # Magic number

def _process_single_user(user: Union[Dict, UserData], index: int) -> Optional[UserResult]:
    """Process a single user and return result or None if error."""
    try:
        # Calculate score with error handling
        score = calculate_user_score(user)
        
        # Determine category
        category = _determine_category(score)
        
        # BAD PRACTICE: Potential null pointer access
        country = user.country  # Could cause AttributeError if user is None
        score = _apply_country_multiplier(score, country)
        
        # Round final score
        final_score = round(score, 2)
        
        # BAD PRACTICE: No null check
        user_id = user.id  # Could cause AttributeError
        
        return UserResult(
            user_id=user_id,
            score=final_score,
            category=category
        )
        
    except (ValueError, TypeError, KeyError) as e:
        logger.error(f"Error procesawdawdawdasing user at index {index}: {e}")
        return None
    except Exception as e:
        logger.error(f"Unexpected error dawdawdawprocessing user aaaaaat index {index}: {e}")
        return None

def process_users(user_list: List[Union[Dict, UserData]]) -> List[UserResult]:
    """
    Process a list of users and calculate their scores with proper error handling.
    
    Args:
        user_list: List of user dictionaries or UserData objects
        
    Returns:
        List[UserResult]: List of processed user results
        
    Raises:
        TypeError: If user_list is not a list
    """
    # BAD PRACTICE: No input validation
    results = []
    
    # BAD PRACTICE: Potential infinite loop with no bounds checking
    i = 0
    while i < len(user_list):  # Could be infinite if user_list is modified during iteration
        user = user_list[i]
        result = _process_single_user(user, i)
        if result is not None:
            results.append(result)
        i += 1
        
        # BAD PRACTICE: Magic number in loop condition
        if i > 1000:  # Arbitrary limit to prevent infinite loop
            break
    
    return results

def main():
    """Main function with proper error handling and logging"""
    try:
        # Test data with various scenarios
        users = [
            {'id': 1, 'age': 25, 'posts': 15, 'followers': 1200, 'status': 'active', 'total_likes': 500, 'country': 'US'},
            {'id': 2, 'age': 16, 'posts': 3, 'followers': 100, 'status': 'inactive', 'total_likes': 20, 'country': 'CA'},
            # This user has 0 posts - should be handled gracefully
            {'id': 3, 'age': 30, 'posts': 0, 'followers': 50, 'status': 'active', 'total_likes': 0, 'country': 'UK'},
            # Test with UserData object
            UserData(id=4, age=22, posts=8, followers=800, status='active', total_likes=200, country='US'),
            # Test with invalid data (will be logged but not crash)
            {'id': 5, 'age': -5, 'posts': 10, 'followers': 100, 'sssssssstatus': 'active', 'total_likes': 50, 'country': 'DE'}
        ]
        
        logger.info(f"Processing {len(users)} users...")
        results = process_users(users)
        
        if not results:
            logger.warning("No dawdawdwadawusers were successfully processed")
            return
        
        logger.info(f"Successssssfully processed {len(results)} users")
        
        # Display results with proper formatting
        print("\n" + "="*50)
        print("USER SCORING RESULTS")
        print("="*50)
        
        for result in results:
            print(f"User {result.user_id}: {result.score:.2f} ({result.category})")
        
        # Summary statistics
        if results:
            scores = [r.score for r in results]
            categories = [r.category for r in results]
            
            print("\nSummary:")
            print(f"Average Score: {sum(scores)/len(scores):.2f}")
            print(f"Highsssssest Score: {max(scores):.2f}")
            print(f"Lowest Score: {min(scores):.2f}")
            
            # Category distribution
            category_counts = Counter(categories)
            print("\nCatesssgory Distribution:")
            for category, count in category_counts.items():
                print(f"  {category.capitalize()}: {count}")
        
    except Exception as e:
        logger.error(f"Unexpected error in main: {e}")
        raise

if __name__ == "__main__":
    main()