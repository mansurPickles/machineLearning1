def linearRegression():
    X = [45, 36, 37, 43, 38, 49, 39, 43, 44, 38, 42, 40]
    Y = [43, 35, 34, 41, 44, 44, 42, 46, 39, 39, 47, 39]
    size = len(X)
    theta0 = 0
    theta1 = 0
    y_pred = 0


    learning_rate = .0001

    for i in range(10000000):
        theta0_y_average = 0
        theta1_y_average = 0

        for j in range(size):
            y_pred_temp = X[j]*theta1 + theta0
            y_pred_temp = y_pred_temp - Y[j]
            y_pred = y_pred_temp
            theta0_y_average += y_pred_temp
            theta1_y_average += (y_pred_temp * X[j])

        if(i % 50 == 0):
            print(f'cost theta0: {theta0_y_average / size}')
            print(f'cost theta1: {theta1_y_average / size}')


        theta0_y_average = theta0_y_average / size
        theta1_y_average = theta1_y_average / size
        #print(theta0_y_average)
        theta0 -= (learning_rate * theta0_y_average)
        theta1 -= (learning_rate * theta1_y_average)

    print(f'theta 0: {theta0}')
    print(f'theta 1: {theta1}')




linearRegression()