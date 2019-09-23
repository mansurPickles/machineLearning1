import matplotlib.pyplot as plt

def linearRegression():
    X = [45, 36, 37, 43, 38, 49, 39, 43, 44, 38, 42, 40]
    Y = [43, 35, 34, 41, 44, 44, 42, 46, 39, 39, 47, 39]

    #X = [1896, 1900, 1904, 1906, 1908, 1912, 1920, 1924, 1928, 1932, 1936, 1948, 1952, 1956, 1960, 1964,
    #     1968, 1972, 1976, 1980, 1984, 1988, 1992, 1996, 2000, 2004, 2008]

    #Y = [12, 11, 11, 11.20, 10.80, 10.80, 10.80, 10.60, 10.80, 10.30, 10.30, 10.30, 10.40, 10.50, 10.20, 10,
    #     9.95, 10.14, 10.06, 10.25, 9.99, 9.92, 9.96, 9.84, 9.87, 9.85, 9.69]


    X_squared = []
    XY = []

    size = len(X)

    #for X_squared
    for i in range(size):
        temp = pow(X[i],2)
        X_squared.append(temp)

    #for XY
    for i in range(size):
        temp = X[i] * Y[i]
        XY.append(temp)


    #get the averages

    x_average = average(X)
    y_average = average(Y)
    x_squared_average = average(X_squared)
    xy_average = average(XY)

    print(f'x_average {x_average}')
    print(f'y_average {y_average}')
    print(f'xy_average {xy_average}')
    print(f'x_squared_average {x_squared_average}')


    theta1 = (xy_average - (x_average * y_average)) / (x_squared_average - pow(x_average,2))
    print(f'theta1 {theta1}')

    theta0 = y_average - (theta1 * x_average)
    print(f'theta1 {theta0}')

    for i in range(size):

        h_theta_x = theta0 + (theta1 * X[i])
        print(h_theta_x)

    y_pred = []

    for i in range(size):
        h_theta_x = theta0 + (theta1 * X[i])
        y_pred.append(h_theta_x)

    plt.scatter(X,Y)
    plt.title('Assignment1')
    plt.xlabel('Interested in Class')
    plt.ylabel('Enrolled in Class')
    plt.plot(X, y_pred)

    print("X = 27")
    print(theta0 + (theta1 * 27))
    print("X = 150")
    print(theta0 + (theta1 * 150))


    plt.show()



def average(list):
    sum = 0
    for i in list:
        sum += i
    sum /= len(list)
    return sum



linearRegression()

