import random
import math

def classifyAPoint(points, p, k=3):
    distance = []
    for group in points:
        for feature in points[group]:
            # Calculate the Euclidean distance
            euclidean_distance = math.sqrt((feature[0] - p[0]) ** 2 + (feature[1] - p[1]) ** 2 + (feature[2] - p[2]) ** 2)
            # Append (distance, group) to the distance list
            distance.append((euclidean_distance, group))
    
    # Sort the distance list and take the first k elements
    distance = sorted(distance)[:k]

    # Initialize frequencies
    freqR = sum(1 for d in distance if d[1] == 'R')
    freqG = sum(1 for d in distance if d[1] == 'G')
    freqB = sum(1 for d in distance if d[1] == 'B')

    # Determine the class
    if freqR > freqG and freqR > freqB:
        return 'R'
    elif freqG > freqR and freqG > freqB:
        return 'G'
    elif freqB > freqR and freqB > freqG:
        return 'B'
    else:
        # Tie-breaking: choose the first occurrence
        return distance[0][1]

def generateRandomRGBValues(n=100):
    data = {
        'R': [],
        'G': [],
        'B': []
    }
    
    for _ in range(n):
        r, g, b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
        if r > g and r > b:
            data['R'].append((r, g, b))
        elif g > r and g > b:
            data['G'].append((r, g, b))
        else:
            data['B'].append((r, g, b))
    
    return data

def main():
    # Generate random RGB values
    points = generateRandomRGBValues(100)

    # Test RGB value
    test_point = (100, 80, 10)
    k = 3

    # Classify the test point
    classification = classifyAPoint(points, test_point, k)
    print("The tested pixel {} is classified as: {}".format(test_point, classification))

if __name__ == '__main__':
    main()
