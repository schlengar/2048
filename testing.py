from random_approach import random_approach

sample = random_approach(10000)
samplePoints = sample[1]
sampleAmountOf2048 = sample[0]
sampleHighestBox = sample[2]

amountOfTestRuns = len(samplePoints)
averagePoints = float(sum(samplePoints)) / amountOfTestRuns
maximumPoints = max(samplePoints)
minimumPoints = min(samplePoints)


print("Performed %d runs." %(amountOfTestRuns))
print("With a maximum of %d, a minimum of %d, and an average of %d points." 
	%(maximumPoints, minimumPoints, averagePoints))
print("Among all these runs, the 2048 tile was reached %d times." %sampleAmountOf2048)
print("And the highest tile reached was %d." %sampleHighestBox)