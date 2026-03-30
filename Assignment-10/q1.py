import pandas as pd
import numpy as np


def assign_clusters(points, airports):
    distances=np.linalg.norm(points[:, np.newaxis]-airports, axis=2)
    return np.argmin(distances, axis=1)


def update_airports(points, labels, k, airports, lr=0.01):
    new_airports=airports.copy()

    for i in range(k):
        cluster_points=points[labels==i]

        if len(cluster_points)>0:
            grad=-2*np.sum(cluster_points-airports[i], axis=0)
            new_airports[i]=airports[i]-lr*grad

    return new_airports


def newton_update(points, labels, k):
    new_airports=[]

    for i in range(k):
        cluster_points=points[labels==i]

        if len(cluster_points)>0:
            # Newton step (closed-form solution)
            airport=cluster_points.mean(axis=0)
            new_airports.append(airport)
        else:
            new_airports.append(points[np.random.randint(len(points))])

    return np.array(new_airports)


def first_order(points, airports, k):
    for _ in range(100):
        labels=assign_clusters(points, airports)
        new_airports=update_airports(points, labels, k, airports)

        if np.allclose(airports, new_airports):
            break

        airports=new_airports
    return airports, labels


def second_order(points, airports, k):
    for _ in range(10):  # fewer iterations needed
        labels=assign_clusters(points, airports)
        new_airports=newton_update(points, labels, k)

        if np.allclose(airports, new_airports):
            break

        airports=new_airports
    return airports, labels


def compute_cost(points, airports, labels):
    cost=0

    for i in range(len(points)):
        c=airports[labels[i]]
        cost+=np.sum((points[i]-c)**2)

    return cost


def main():
    data=pd.read_csv("cities.csv")
    points=data[['x', 'y']].values
    k=3
    airports=points[np.random.choice(len(points), k, replace=False)]
    print("Starting airport locations:\n", airports)
    airports_first_order, labels_first_order=first_order(points, airports, k)
    print("=====First Order Derivatives=====")
    for i in range(3):
        airport=airports_first_order[i]
        print(f"Airport {i+1} at location: {airport}\n has following cities closest to it:-")
        print("City \t\t Distance")
        for city in points[labels_first_order==i]:
            print(f"{city}\t{np.sum((city-airport)**2)}")
    
    airports_second_order, labels_second_order=second_order(points, airports, k)
    print("\n\n=====Second Order Derivatives=====")
    for i in range(3):
        airport=airports_second_order[i]
        print(f"Airport {i+1} at location: {airport}\n has following cities closest to it:-")
        print("City \t\t Square of Distance")
        for city in points[labels_second_order==i]:
            print(f"{city}\t{np.sum((city-airport)**2)}")

    cost_first_order=compute_cost(points, airports_first_order, labels_first_order)

    cost_second_order=compute_cost(points, airports_second_order, labels_second_order)

    print("Gradient Descent Cost:", cost_first_order)
    print("Newton Method Cost:", cost_second_order)

if __name__=='__main__':
    main()